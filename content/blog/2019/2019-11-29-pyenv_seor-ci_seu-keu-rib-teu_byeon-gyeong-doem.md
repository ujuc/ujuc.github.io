Title: pyenv 설치 스크립트 변경됨
Date: 2019-11-29 15:44:29
Category: Operation
Tags: python, pyenv, python version management, version management
Slug: pyenv_seor-ci_seu-keu-rib-teu_byeon-gyeong-doem
Summary: pyenv 설치 방법이 변경되어 간략하게 남겨둔다.

dotrc를 작성할때 만들었던 스크립트에서는 다음의 URL로 Pyenv를 설치했다.

```shell
$ brew install pyenv

$ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

이번 수정하면서, 확인하니 이분들이 `pyenv.run` 도메인을 구매하셨나보다. 스크립트가 변경되었다.

```shell
$ curl https://pyenv.run | bash
```

