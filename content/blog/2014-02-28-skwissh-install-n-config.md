Title: [Monitoring] SkwiSSH 설치 및 구성
Date: 2014-02-28 21:46
Modified: 2016-03-03 22:08
Category: Operation
Tags: python, monitoring, ssh, django
Slug: skwissh-install-n-config
Summary: Django App으로 ssh를 이용하여 서버 모니터링이 가능하다. 개발이 멈춘지 너무 오래됐다.

[SkwiSSH][skwissh]
=====

오늘 Facebook에 공유가된 Monitoring Tool. Django에서 App으로 돌릴 수 있고, 참 깔ㄹ끔하기에 회사에서 서버 볼 때 사용할까하여 구성해봤다.

코드로는 Django v1.5와  v1.5.1을 지원한다고 작성해놨는데 `setup.py`를 사용하여 구성하게 되면 Django v1.6을 설치하라며 에러문구가 발생한다.

그리고 외부 서버를 추가하기 위해서 `server_ip:22`를 입력해줘야지 외부 서버에 ssh로 접근하여 값들을 읽어오게 된다.

아직은 부족한 점이 많다.

* Sensor(명령어를 날려서 값을 받아오는 worker를 의미한다.) 추가하고 변경하려면 변경사항이 적용이 안되는 현상.
* Sensor들의 정렬을 임의로 할 수 없다는 것. (오름차순으로 구성되어있다.)
* 기본 명령어 날리는게 1분간격으로 수정할만한 탭이 안보인다.
* 기본 DB로 SQLite3 파일을 사용하는데 점점 커지는 모습을 확인 할 수 있다.
* bash를 사용할 줄 안다면 정말 쉽게 사용이 가능하다.
	* 명령을 SSH로 날리기에 그쪽 서버 콘솔로 리턴값을 넘길 수 있는 프로그램이라면 어떻게든 사용하면된다.

이 글에서는 Sensor에 명령어와 파셔 세팅은 작성하지 않았다.

## 기본 구성

* OS: Ubuntu 12.04.4 server
* Install Package

```bash
$ sudo apt-get install python-pip
```

### 패키지 설치

#### Django 설치

```bash
$ sudo pip isntall Django
```

#### Django-skwissh 설치

```bash
$ sudo apt-get install buid-essential python-dev
$ git clone https://github.com/rsaikali/django-skwissh.git
$ cd django-skwissh
$ sudo python setup.py install
```

### Django 설정

``` bash
$ django-admin.py startproject mysite
$ cd mysite
$ vi mysql/settings.py

INSTALL_APPS = (
	"kronos",
	"skwissh",
)

$ vi mysite/urls.py

# Skwissh
url("skwissh", include("skwissh.urls")),
```

* 데이터 베이스 설정

```bash
$ python manage.p syncdb
```

* Skwissh 테스트 설치
* 이작업을 하면 crontab에 테스크가 등록된다.

```bash
$ python manage.py installtask
# crontab에 등록되었는지 확인
$ crontab -l
```

* Django 서버 작동
```bash
$ python mange.py runserver 0.0.0.0:8000
```

## 참고 페이지
* [Github][skwissh]
* [Gitpage](http://rsaikali.github.io/django-skwissh/)

[skwissh]: https://github.com/rsaikali/django-skwissh
