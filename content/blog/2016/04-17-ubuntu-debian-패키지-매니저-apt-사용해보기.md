Title: Ubuntu-Debian 패키지 매니저 apt 사용해보기
Date: 2016-04-17 12:23
Category: Develop
Tags: ubuntu, debian, apt, system, 
Slug: ubuntu-debian-패키지-매니저-apt-사용해보기
Summary: 하위 명령어 `apt-get`, `apt-cache`를 사용하지 않고 패키지 매너저 `apt`를 사용하는 방법.

기본적으로 `apt` 패키지가 설치되어있었지만... 사용하지 않았었다. 여기저기서 `apt-get` 같은 명령어를 알려줬기에... 그리고 얼마안되기도 했고, 그 간단한 사용법에 대해서 남겨두려고 한다.

참고는 [15 Examples of How to Use New Advanced Package Tool (APT) in Ubuntu/Debian](http://www.tecmint.com/apt-advanced-package-command-examples-in-ubuntu/) 을 사용함. 기본적으로 되는 [Ubuntu man](http://manpages.ubuntu.com/manpages/xenial/man8/apt.8.html) 페이지는 끼고 살자...

## 1. 패키지 설치

	:::shell
	sudo apt install glances

항상 사용하던건 `apt-get` 명령어로 설치를 하는거였는데 4글자 줄엇다!
`sudo aptitude install` 로도 가능하다만... 이렇게 하는 사람들 잘못봤다.

## 2. 패키지가 설치된 위치 확인

	:::shell
	sudo apt content glances

대응되는 명령어는 `dpkg -L`.

## 3. 패키지 디펜던시 확인

	:::shell
	sudo apt depends glances

대응되는 명령어가 `apt-get check`, `dpkg -C`.

## 4. 패키지 찾기

	:::shell
	sudo apt search openstack

대응되는 명령어는 `apt-cache search`.

## 5. 패키지 정보 확인

	:::shell
	sudo apt show firefox

대응되는 명령어 `apt-cache show`, `dpkg -p`

## 6. 깨진 디펜던시가 있는지 확인

	:::shell
	sudo apt check firefox

이거와 대응되는게 있는지 잘모르겠다.

## 7. 제공된 패키지에서 빠진 패키지에 대한 목록 보여주기

	:::shell
	sudo apt recommends apache2

## 8. 패키지 버전 체크

	:::shell
	sudo apt version firefox

## 9. 시스템 패키지 업데이트

	:::shell
	sudo apt update

대응되는건 `apt-get update`.

## 10. 시스템 업그레이드

	:::shell
	sudo apt upgrade

대응되는건 `apt-get upgrade`.

## 11. 커널 버전까지 시스템 업그레이드

	:::shell
	sudo apt full-upgrade

대응되는건 `apt-get dist-upgrade`.

## 12. 사용하지 않는 페키지 삭제

	:::shell
	sudo apt autoremove

대응되는건 `apt-get autoremove`.

## 13. 다운로드된 페키지에서 오래된 저장소 삭제

	:::shell
	sudo apt autoclean
	sudo apt clean

대응되는건 `apt-get clean`, `apt-get autoclean`.

## 14. 패키지 구성파일까지 삭제

	:::shell
	sudo apt purge glance

대응되는건 `apt-purge`.

## 15. deb 패키지 설치 (작동이 안된다... -160502)

	:::shell
	sudo apt deb atom-amd64.deb

대응되는건 `dpkg` 에서 찾으면될듯..

## 16. 사용법은

	:::shell
	apt help

`apt` 사용법을 찾아서 작업하면 될것으로 보여짐.

## 맺음

동일한 명령어가 여러가지 존재하고 사용하는 방법에 따라 달라지는 것으로 보여지는데...
패키지 메니저가 `dpkg`, `aptitude`, `apt`로 나눠져있으니 편한걸로.. 그리고 설치되어있는걸로 사용하면될 듯.
