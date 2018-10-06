Title: PHP Package Manager : phpenv
Date: 2018-10-06 09:29:19
Category: Develop
Tags: php, phpenv, env
Slug: php_package_manager_:_phpenv
Summary: PHP 패키지 매니저, phpenv를 확인해본다. 설치 실패기다.

## 들어가는 말

PHP로 개발을 해야되는 일이 생겼다. 버전을 7.x대로 써야되는데... 7.2는 아닌거같으니... 뭔가 버전을 따로 구성해서 진행하고 싶다.!

## PHP Package Manager

[github.com/phpenv/phpemv](https://github.com/phpenv/phpenv)

버전 관리를 위한 부분.
사용법은 `rbenv`, `pyenv` 와 동일하다. (그렇다보니 shell script로만 작성이되어있다.)

### 설치

#### [Github Checkout](https://github.com/phpenv/phpenv#installation)

```
$ git clone git://github.com/phpenv/phpenv.git ~/.phpenv
$ echo 'export PATH="$HOME/.phpenv/bin:$PATH"' >> ~/.bash_profile
$ echo 'eval "$(phpenv init -)"' >> ~/.bash_profile
$ exec $SHELL -l
```

#### [phpenv-installer](https://github.com/phpenv/phpenv-installer)


```
curl -L https://raw.githubusercontent.com/phpenv/phpenv-installer/master/bin/phpenv-installer | bash
```

이걸 설치하면 `php-build/php-build`, `madumlao/phpenv-aliases`, `ngyuki/phpenv-composer`가 자동으로 설치된다.

### PHP 설치

```
$ phpenv install --list
$ phpenv install {php_version}
```

### PHP 설치시 에러

* Mac os error [해결 문서](https://qiita.com/maosanhioro/items/82698a8bdf6b7694ad36)

```
-----------------
|  BUILD ERROR  |
-----------------

Here are the last 10 lines from the log:

-----------------------------------------
configure: WARNING: This bison version is not supported for regeneration of the Zend/PHP parsers (found: 2.3, min: 204, excluded: ).
configure: WARNING: You will need re2c 0.13.4 or later if you want to regenerate PHP parsers.
configure: error: Cannot find OpenSSL's <evp.h>
-----------------------------------------
```

* 추가 설치 패키지
  
```
$ brew install bison@2.7
$ brew link bison@2.7 --force

$ brew install re2c

$ brew install openssl libxml2
$ brew link --force openssl && brew link --force libxml2

$ brew install mcrypt
```

* `libz` error

```
configure: error: Cannot find libz
```

```
xcode-select --install
```

모하비에서는 안된다.

## 나오는 말

`phpenv`로는 설치가 안되서... `brew`로 그냥 설치...
`brew` 로 7.2 버전이랑 7.1 버전을 설치해두고 PhpStorm 에서 둘다 잡아두면 두개다 쓸수있지뭐... 마이너까지만 신경쓰면되니.
