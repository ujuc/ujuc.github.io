Title: ReadtheDocs 로 퍼블리싱되는 문서에 한국어 지원하기
Date: 2020-01-31 10:07:44
Modified: 2020-02-02 17:31
Category: Develop
Tags: documents, po, readthedocs
Slug: readthedocs-ro-peo-beur-ri-sing-doe-neun-mun-seo-e-han-gug-eo-ji-weon-ha-gi
Summary: Airship 프로젝트 문서 번역을 하려는데... ReadtheDocs에서 제공하고 있었다. 여기서 한국어로 지원할 수 있도록 수정해주자.

[Airship](https://www.airshipit.org/) 프로젝트는 나중에 설명하도록 하자. (블로그 자주 써야지...)

번역을 하려던 문서는 [Airship Treasuremap](https://airship-treasuremap.readthedocs.io/en/latest/)이었는데, 잘못보고 다른 저장소를 사용하게 되어 중간에 작업했던거 남겨두고 진행하려고 한다.

지금의 내용은 [Manage Translations](https://docs.readthedocs.io/en/stable/guides/manage-translations.html) 를 보고 따라하면 되는 부분이다.

## 번역 파일 생성

- **NOTE**: `conf.py` 파일이 있는 `docs` 폴더나 도큐먼트 폴더에서 실행을 해야한다.

```shell
sphinx-build -b gettext . _build/gettext
```

위 명령을 실행하면 `pot` 파일을 `_build/gettext` 에 생긴것을 확인할 수 있다.

## 번역할 텍스트 만들기

`pot` 파일은 `po` 템플릿이라 곧장 번역을 할 수 없다.
그러니 `po`파일을 다시 만들어야한다.

먼저 `sphinx-intl` 패키지를 설치하여 다음 명령어를 실행한다.

```shell
sphinx-intl update -p _build/gettext -l ko
```

`locale/ko/LC_MESSAGES/**.po` 파일이 생성된다.

나머지는 알아서... po 파일을 가지고서 다른 서비스에 올려서 번역을 하거나 하면된다.

## 선택한 언어로 문서 만들기

```shell
sphinx-build -b html -D language=ko . _build/html/ko
```

로 하면된다고 한다. 아직이 부분을 해보지는 않아서 해보고 업뎃하는걸로...
