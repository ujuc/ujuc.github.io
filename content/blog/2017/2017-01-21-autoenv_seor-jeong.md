Title: autoenv 설정
Date: 2017-01-21 16:40:06
Category: Develop
Tags: autoenv, env, setup
Slug: autoenv_seor-jeong
Summary: 컴퓨터를 밀었다. env 구성을 해야되는데 `autoenv` 를 사용하면 해당 프로젝트로 들어가면 자동으로 해준다기에 설정을 했다.

## `authenv` 설치

* 프로젝트 url: [kennethreitz/autoenv](https://github.com/kennethreitz/autoenv)

나는 맥에서 설치하는 `brew install autoenv` 로 설치한다. 딴걸로 써볼려고도 했었는데... `brew` 하나로 구성해서 관리하는게 더 좋다.
셸에도 넣어주자. `zsh` 를 사용하니 `~/.zshrc` 에 `source $(brew --prefix autoenv)/activate.sh` 를 넣어두게 되면 쉽다.

## 설정
블로그를 `pelican` 으로 구성해서 작성하다보니 `pyenv`, `venv` 설정해서 패키지 설치 파일이 필요해서 구성했다.

```
# ujuc.github.io

source ../env/blog/bin/activate
```

다 좋은데 다른 폴더로 가거나 다른 프로젝트로 갔을때... 문제가 생길 수 있어서 끄는 방법을 찾았다. 상위 폴더에 다음 `.evn`를 만들어서 넣어주면 된다. 개발하면서 자주가는 곳에다가는 꼭 박아두자. ([원문](https://github.com/kennethreitz/autoenv/issues/30#issuecomment-26832177))

```
# .env

if [ -n "$VIRTUAL_ENV" ] ; then
    deactivate
fi
```
