Title: Yet Another Cron (yacron)
Date: 2017-07-21 13:17:58
Category: Operation
Tags: cron, yaml, scadule, docker, python
Slug: yet_another_cron_(yacron)
Summary: Docker에서 쓰기 편하게 작성한 crontab 이란다.

* [Github](https://github.com/gjcarneiro/yacron)

해당 프로젝트는 지금은 alpha 버전이라고 한다. 제대로된 기능들이 들어가기 시작하면 좋아질듯. 그리고 그때쯤되면 간단한 소개가 아닌 사용법에 대해서 작성해둬야겠다.

우선은 Readme 파일 번역 수준

## 기능

가장 중요하다. 기능!

* "Crontab" 을 YAML로 작성이 가능하다.
  - 솔직히 YAML이 편한지는 모르겠다.
* cron job이 실패에 대한 부분을 제어할 수 있게 되어있다.
  - 실패시 해당 값을 재시도 할 수 있다.
* 유연하게 구성 가능
* Docker, Kubernetes, 12 factor environments에 맞게 디자인이 되었다며...

## 설치

* python >= 3.5
* pip install yacron

## 사용

```bash
yacron -c my-crontab.yaml
```

`-c`를 사용해서 구성파일이 있는 곳을 가리킨다.

### 기본 구성

* 매 5분마다 `echo "foobar"`를 실행하는 job.

```yaml
jobs:
  - name: test-01
    command: echo "foobar"
    shell: /bin/bash
    schedule: "*/5 * * * *"
```

* 특정일 (2017/7/19)에만 5분마다 `echo "foobar"`를 실행하는 job.

```yaml
jobs:
  - name: test-01
    command: echo "foobar"
    schedule:
      minute: "*/5"
      dayOfMonth: 19
      month: 7
      year: 2017
      dayOfWeek: "*"
```

* 특정 환경변수 값 설정

```yaml
jobs:
  - name: test-01
    command: echo "foobar"
    shell: /bin/bash
    schedule: "*/5 * * * *"
    environment:
      - key: PATH
        value: /bin:/usr/bin
```

### 기본 값 지정

```yaml
defaults:
    environment:
      - key: PATH
        value: /bin:/usr/bin
    shell: /bin/bash
jobs:
  - name: test-01
    command: echo "foobar"  # run /bin/bash
    schedule: "*/5 * * * *"
  - name: test-02
    command: echo "zbr"  # run /bin/sh
    shell: /bin/sh
    schedule: "*/5 * * * *"
```

### 리포트

* job 이 실패했을때 알려준다. Sentry는 나중에 추가될 꺼임.

```yaml
- name: test-01
  command: |
    echo "hello" 1>&2
    sleep 1
    exit 10
  schedule:
    minute: "*/2"
  captureStderr: true
  onFailure:
    report:
      sentry:
        dsn:
          value: example
      mail:
        from: example@foo.com
        to: example@bar.com
        smtp_host: 127.0.0.1
```

`onFailure` 부분이 job 실패시 작어하는 부분임.
`captureStderr: true` 부분은 stderr로 출력되는 데이터를 잡겠다는거 반대로는 `captureStdout: true` 가 있다.

* job 이 성공했을 경우, 알림은 `onSuccess` 옵션을 추가한다.

```yaml
- name: test-01
  command: echo "hello world"
  schedule:
    minute: "*/2"
  captureStdout: true
  onSuccess:
    report:
      mail:
        from: example@foo.com
        to: example@bar.com
        smtp_host: 127.0.0.1
```

### failure 제어

* 실패 조건
  * `producesStdout`
    - default: `false`
    - stdout 출력이 있을 경우
  * `producesStderr`
    - default: `true`
    - stderr 출력이 있을 경우
  * `nonzeroReturn`
    - default: `true`
    - 반환값이 0이 아닌경우

```yaml
failsWhen:
  producesStdout: false
  producesStderr: true
  nonzeroReturn: true
```

* `retry`

`onFailure` 안에다가 추가한다. 그리고 job 재시도도 완전히 실패했다면, `onPermanentFailure` 옵션을 사용하여 리포트를 받는다.

```yaml
- name: test-01
  command: |
    echo "hello" 1>&2
    sleep 1
    exit 10
  schedule:
    minute: "*/10"
  captureStderr: true
  onFailure:
    report:
      mail:
        from: a@foo.com
        to: a@bar.com
        smtp_host: 127.0.0.1
    retry:
      maximumRetries: 10
      initialDelay: 1
      maximumDelay: 30
      backoffMultiplier: 2
  onPermanentFailure:
    report:
      mail:
        from: a@foo.com
        to: a@bar.com
        smtp_host: 127.0.0.1
```

