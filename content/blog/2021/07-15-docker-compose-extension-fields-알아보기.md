Title: docker-compose Extension fields 알아보기
Date: 2021-07-15 15:53:42
Modified: 2021-07-15 15:53:42
Category: Develop
Tags: docker, compose, config file
Slug: docker-compose-extension-fields-알아보기
Summary: docker-compose 파일에서 새로운 문구를 발견했다. 정리나 하자.

Airflow를 볼까해서 docker-compose 파일을 받아서 봤는데... 뭔가 새로운 문구가 발견되었다.
다음과같은 부분임.

```yaml
version: '3'
x-airflow-common:
  &airflow-common
  image: ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.1.2}
  environment:
    &airflow-common-env
    AIRFLOW__CORE__EXECUTOR: CeleryExecutor
    AIRFLOW__CORE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
    AIRFLOW__CELERY__RESULT_BACKEND: db+postgresql://airflow:airflow@postgres/airflow
    AIRFLOW__CELERY__BROKER_URL: redis://:@redis:6379/0
    AIRFLOW__CORE__FERNET_KEY: ''
    AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION: 'true'
    AIRFLOW__CORE__LOAD_EXAMPLES: 'true'
    AIRFLOW__API__AUTH_BACKEND: 'airflow.api.auth.backend.basic_auth'
    _PIP_ADDITIONAL_REQUIREMENTS: ${_PIP_ADDITIONAL_REQUIREMENTS:-}
  volumes:
    - ./dags:/opt/airflow/dags
    - ./logs:/opt/airflow/logs
    - ./plugins:/opt/airflow/plugins
  user: "${AIRFLOW_UID:-50000}:${AIRFLOW_GID:-50000}"
  depends_on:
    redis:
      condition: service_healthy
    postgres:
      condition: service_healthy

services:
...
  airflow-init:
    <<: *airflow-common
    command: version
    environment:
      <<: *airflow-common-env
      _AIRFLOW_DB_UPGRADE: 'true'
      _AIRFLOW_WWW_USER_CREATE: 'true'
      _AIRFLOW_WWW_USER_USERNAME: ${_AIRFLOW_WWW_USER_USERNAME:-airflow}
      _AIRFLOW_WWW_USER_PASSWORD: ${_AIRFLOW_WWW_USER_PASSWORD:-airflow}

...
```
보면 알겠지만 분명 version 3버전인데 `&`, `*` 를 이용해서 이미지와 환경설정 구문을 반복해서 사용할 수 있도록 구성해놓은 것으로 판단되고 있다.
그래서 문서를 찾다보니 맨밑에... `Extension fields` 라고 되어있는 부분이 존재한다. 문서를 끝까지 안봐서 몰랐던듯.

뭔가 써봤으면 알것는데. 이번기회에 정리하고 사용해봐야할듯. 메뉴얼 문서 번역이 될듯함.

추가로 YAML 스팩을 봐야할듯. YAML 스팩에 있는 내용을 그대로 사용할 수 있다고 해놓은걸보니... YAML에 대한 내용을 제대로 안다면 쉽게 구성할 수 있을 것으로 보여진다.

---

## Extension fields

- [공식 문서](https://docs.docker.com/compose/compose-file/compose-file-v3/#extension-fields)

> 버전 3.4에 추가됨

확장 필드를 사용해 구성 조각을 재 사용할 수 있습니다. 이 부분은 compose 파일에서 루트 위치에 존재하고 키이름에 접두사로 `x-`를 사용하여 표시합니다.

> Note: 포멧 버전 3.7과 2.4에서는 `service`, `volume`, `network`, `config`, `secret` 정의시 사용이 가능합니다.

다음과 같이 YAML anchor 기능을 통해서 리소스 정의에 삽입이 가능합니다.

```yaml
version: "3.9"
x-logging:
  &default-logging
  options:
    max-size: '12m'
    max-file: '5'
  driver: json-file

services:
  web:
    image: myapp/web:latest
    logging: *default-logging
  db:
    image: mysql:latest
    logging: *default-logging
```

YAML 머지 형식을 이용하여 원하는 값을 추가할 수 있습니다.

```yaml
version: "3.9"
x-volumes:
  &default-volume
  driver: foobar-storage

services:
  web:
    image: myapp/web:latest
    volumes: ["vol1", "vol2", "vol3"]
volumes:
  vol1: *default-volume
  vol2:
    << : *default-volume
    name: volume02
  vol3:
    << : *default-volume
    driver: default
    name: volume-local
```
