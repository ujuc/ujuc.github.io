Title: Custom Virtual Environment Location on piping
Date: 2018-04-21 13:01:22
Category: Develop
Tags: pip, pipenv, env, python
Slug: custom_virtual_environment_location_on_piping
Summary: pipevn를 사용하는데... env가 안보인다. 보이는 곳으로 옮기자!

`pipenv`를 사용하면 `.env` 파일까지 생성해주고 그것을 사용할 수 있도록 해준다.
그런데... 이거 참... 저 깊숙한곳에 만들어주니... Pycharm에서 `env`를 쓰려고 찾기시작하니 귀찮다. 그리고 그냥 지워버리면 그 밑에있는건...

물론 확인할 수 있는 방법이 없는건아니다. `pipenv shell`로 하면 `.env` 파일이 존재하는 곳을 찾아서 실행시켜주기도 하는데...
내마음에 안드니...

`pipenv` 에서 사용하는 `.env`를 내가 원하는 위치에 옮겨보자.

### `WORKON_HOME`

저 깊이 들어가는 `.env` 폴더를 내가 원하는 위치로 옮겨준다.

    export WORKON_HOME=~/.venvs

### `PIPENV_VENV_IN_PROJECT`

프로젝트를 진행하고있는 곳에 `.env` 파일을 만들어준다.
이럴때는 `.gitignore`에서 `.env/` 파일을 예외로 해주어야된다. 해주는게 좋을꺼다.

    export PIPENV_VENV_IN_PROJECT=true

#### 참고

[pipenv - Custom Virtual Environment Location](https://docs.pipenv.org/advanced/#custom-virtual-environment-location)