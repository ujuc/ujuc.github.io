Title: direnv
Date: 2017-02-08 20:44:05
Category: Develop
Tags: env, shell, environment
Slug: direnv
Summary: 이것 참... 결국 env 종류를 다 돌고 있다.

이번에 소개할 direnv 는 이상한 모임에서 autoenv 를 올리고 난뒤 [@raccoony](http://raccoonyy.github.io/)님께서 알려주셨다. 오홍 신기한거 많다.

### [direnv](https://direnv.net/)

홈페이지는 제목을 누르면 연결이되고 깃허브 주소는 [direnv/direnv](https://github.com/direnv/direnv) 이다. 신기한건 go로 작성이 되었네... 마지막 커밋이 이글 쓰는 날 기준으로 10일전!

다른 env 프로그램들과 비슷하게 이건 셸에서 사용하는 환경변수를 변경할 수 있도록 도와준다.
코드에는 넣지 못하는 환경변수들을 셸에 `.bashrc` 나 `.profile` 에 모든 곳에서 사용하는 경우가 생기는데, 이걸 쓰면 프로젝트마다 다른 내용을 생성하여 보안을 높힐 수 있는 기회가 된다. (모든 보안은 사람이 행하는 보안을 제외하고... 직접 OS에 들어와서 까는건 어쩔 수 없잖아...)

#### 설치

##### 빠지지 않는 메뉴얼 설치!

```
$ git clone https://github.com/direnv/direnv
$ cd direnv
$ make install
# or symlink ./direnv into the $PATH
```

##### brew

```
$ brew install direnv
```

 * 리눅스 패키지도 있다고 하니 사용하는 것에 있는지 검색해보고 설치하도록 하자.
 
#### 사용

우선 사용한 셸 구성 파일에 다음 내용들을 넣어준다.

* `~/.bashrc`

```
eval "$(direnv hook bash)"
```

* `~/.zshrc`

```
eval "$(direnv hook zsh)"
```

* `~/.config/fish/config.fish`

```
eval (direnv hook fish)
```

* `~/.cshrc`

```
eval `direnv hook tcsh`
```

다음으로는 다음과 같이 설정해주면 된다.

```
$ cd playground
$ echo export FOO=foo > .envrc
direnv: error .envrc is blocked. Run `direnv allow` to approve its content.
$ direnv allow
direnv: loading .envrc
direnv: export +FOO -PS2
$ cd ..
direnv: unloading
$ cd playground
direnv: loading .envrc
direnv: export +FOO -PS2
$ echo ${FOO}
foo
```

사용법은 간단하다.

그런데 이걸 쓰는 이유는 코드에 자동으로 생성하는 비번이나 아니면 Auth token 등을 넣으실껀데...
절대로 git 에는 올리지 말길... 꼭 `.gitignore` 설정해서 사용하도록 하자.

더 자세한건 홈페이지에서!!
그런데 이거 참 좋당.
이제 어디서 쓰써볼까나...
