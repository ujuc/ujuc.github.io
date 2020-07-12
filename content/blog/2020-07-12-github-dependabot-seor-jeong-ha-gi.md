Title: Github dependabot 설정하기
Date: 2020-07-12 10:46:57
Modified: 2020-07-12 10:46:57
Category: Develop
Tags: github, dependabot, dependencies packages, package manager
Slug: github-dependabot-seor-jeong-ha-gi
Summary: Github Dependabot 설정을 해보자.

블로그 확인 중 Github Dependabot을 설정할 수 있는 기능이 있어서 적용.

블로그는 간단해서 의존성을 관리할 필요가... 없지만 블로그는 테스트 용이니까... 이것을 붙여봤다.
자세한 사용법은 링크 타고 설명페이지에서 확인하도록... 저거까지하기엔 많아...

---

[TOC]

## 설정 파일

`./.github/dependabo.yml` 으로 설정 파일을 구성한다. Github Actions랑 같은 위치.
그냥 여기다가 다 넣을 작정인듯.

## 구성 옵션

## [`package-ecosystem`](https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates#package-ecosystem)

- **필수 항목!**
- 패키지 메니저에 대한 내용을 정의 한다.
- 사용 가능한 패키지 메니저
    - `bundler`
    - `cargo`
    - `composer`
    - `docker`
    - `elm` (??)
    - `gitsubmodule`
    - `github-actions`
    - `gomode`
    - `gradle`
    - `maven`
    - `mix` (??)
    - `npm`
    - `unget`
    - `pip`
    - `terraform`
- ecosystem별로 하나의 리스트로 사용하여 작업한다.

### [`drectory`](https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates#directory)

- **필수 항목**
- 패키지 설정파일의 위치를 패키지 메니저마다 지정해줘야된다.
- Github Actions는 `/`로 하면 알아서 `.github/workflows`에 있는 파일을 가져다가 쓴다.

### `Schedule`

#### [`interval`](https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates#scheduleinterval)

- **필수 항목**
- 얼마마다 확인할 것인지에 대해서 정의하는 위치.
- 항목은 `daily`, `weekly`, `monthly`가 있다.
    - `daily`는 월~금요일에만 실행한다. (주말은 왜 쉬는거지...?)
    - `weekly`는 기본은 월요일에만 실행한다. 밑에서 설명할 `day` 항목으로 변경 가능.
    - `monthly`는 매달 한번 1일에 실행한다.

#### [`day`](https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates#scheduleday)

- 주마다 업데이트할 스케출을 적어준다.
- 기본값은 `monday 05:00 UTC` 이다.
- 항목
    - `monday`
    - `tuesday`
    - `wednesday`
    - `thursday`
    - `friday`
    - `saturday`
    - `sunday`

#### [`timezone`](https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates#scheduletimezone)

- UTC가 기본인데 이걸 바꾸고 싶으면 작성한다.
- Timezone은 풀네임 `Asia/Seoul`으로 해준다. [다른 타임존](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
- (?) 여기다가 한국시간을 박아두면 `13:00 KST`로 도는건가..음..?

### [`allow`](https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates#scheduleinterval)

- 기본적으로 모든 의존성을 확안하여 PR을 넣게 되는데, 업데이트 하고 싶은 의존성만 허용할 수 있는 옵션이다.
- 항목
    - `dependency-name`: 명시한 이름을 가진 패키지만 업데이트 한다. `*`를 이용하여 여러개의 패키지를 지정할 수 있다. (정규식의 `*` 사용법과 동일)
    - `dependency-type`: 음.. 타입....음..

| Type | Support ecosystem | Allow updates |
| ---- | ----------------- | ------------- |
| `direct` | 전부 | 명시된 모든 의존성 |
| `indirect` | `bundler`, `pip`, `composer`, `cargo` | 하위 의존성까지 전부 |
| `all` | 전부 | 명시된 모든 의존성. `bundle`, `pip`, `composer`, `cargo` 는 하위 의존성까지 전부 |
| `production` | `bundler`, `composer`, `mix`, `maven`, `npm`, `pip` | **Product** 환경에서 사용하는 패키지만 |
| `development` | `bundler`, `composer`, `mix`, `maven`, `npm`, `pip` | **Developmen** 환경에서 사용하는 패키지만 |

### [`assignees`](https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates#assignees)

- Github Dependabot의 PR에 대한 담당자 지정.
- 음...

### [`commit-message`](https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates#commit-message)

- Github Dependabot이 커밋할때 어떤걸 붙일 건지에 대한 설정
- 항목
    - `prefix`: 앞에 붙일 단어
    - `prefix-development`: 개발 환경용 앞에 붙일 단어
        - 지원하는데는 당연히 `bundler`, `composer`, `mix`, `maven`, `npm`, `pip`
    - `include: "scope"`: 업데이트된 의존성 목록을 점두사 뒤에 넣어준다.
- **NOTE**: `target-branch`를 사용해서 특정 브런치를 지정하지 않으면, 보안 업데이트 PR에도 영향을 끼칠 수 있음.

### [`ignore`](https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates#ignore)

- `@dependabot ignore`를 이용해서 `ignore` 된게 있는지 확인하라고 하는데...
    - `@dependabot`은 어디서... 사용하나...?
- 암튼 뭔가를 하기 싫을때 하는거
- 항목
    - `dependency-name`: 의존성 패키지 이름
    - `versions`: 제외할 버전이나 버전 범위를 지정한다. 패키지 메니저마다 사용하는 패턴을 이용해서 작성하자.
- **NOTE**: `target-branch`를 사용해서 특정 브런치를 지정하지 않으면, 보안 업데이트 PR에도 영향을 끼칠 수 있음.

### [`labels`](https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates#labels)

- PR시 명시된 `label`을 붙여 요청하게 된다.
- 기본값은 `dependencies`.

### [`milestone`](https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates#milestone)

- 특정 milestone을 지정하여 해당 항목에 넣을 수 있다.
- **NOTE**: `target-branch`를 사용해서 특정 브런치를 지정하지 않으면, 보안 업데이트 PR에도 영향을 끼칠 수 있음.

### [`pull-request-branch-name.separator`](https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates#pull-request-branch-nameseparator)

- PR마다 브런치를 만드는데, 이때 브런치 이름 구분자 명시용
- 기본은 `/`

### [`rebase-strategy`](https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates#rebase-strategy)

- 브런치 충돌났을때, 자동으로 PR을 리베이스하는데 이걸 끄고 싶을때 설정하면됨.
- `disabled`: 충돌 해결은 사용자가.
- `auto`: 기본값

### [`reviewers`](https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates#reviewers)

- PR시 리뷰를 요청할 사람 지정. 팀도 가능함.
- **NOTE**: `target-branch`를 사용해서 특정 브런치를 지정하지 않으면, 보안 업데이트 PR에도 영향을 끼칠 수 있음.

### [`target-branch`](https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates#target-branch)

- 기본으로 확인하는 브런치는 레포에 설정된 기본 브런치로 진행한다.
- 이걸 사용하면 명시된 브런치에서 의존성을 검사한다.
- 보안 PR에 영향갈 수 있단다.

### [`versioning-strategy`](https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates#versioning-strategy)

- Github Dependabot에서 의존성 업데이트를 진행하면서 명시하는 방법은 두가지 방법이 있다.
    - App: 요구 버전이 업데이트 (`npm`, `pip`, `composer`)
    - Library: 버전 범위 업데이트 (`bundler`, `cargo`)
- 이 사항을 변경하기 위해서 사용.
- **NOTE**: `target-branch`를 사용해서 특정 브런치를 지정하지 않으면, 보안 업데이트 PR에도 영향을 끼칠 수 있음.
- 사용 가능한 업데이트 옵션

| Option | Support echosystem | Action |
| ------ | ------------------ | ------ |
| `lockfile-only` | `bundler`, `cargo`, `composer`, `mix`, `npm`, `pip` | `lockfile` 업데이트에 대한 것만 PR한다. |
| `auto` | `bundler`, `cargo`, `composer`, `mix`, `npm`, `pip` | 디폴트로 진행한다. |
| `widen` | `composer`, `npm` | 가능하면 새 버전이랑 이전 버전을 모두 사용할 수 있도록 설정한다. |
| `increase` | `bundler`, `composer`, `npm` | 롤링 업데이트!!!!!!! |
| `increase-if-necessary` | `bundler`, `comopser`, `npm` | 꼭 필요할때만 업데이트 |

---

참고: [Configuration options for dependency updates](https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates)
