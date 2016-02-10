Title: Tig Manual
Date: 2016-02-10 02:08
Category: Development
Tags: tig
Slug: tig-manual
Summary: Tig 메뉴얼 번역 축약본

Git을 사용하기 위한 프로그램들이 많다. 그중에서도 번역하려고 하는 것은 Tig. 터미널 환경에 맞게 구성이되어 있으며, Git CLI와 같이 사용하면 왠만한 GUI 프로그램 못지않은 사용성을 보여주고 있다. 단지... 명령어가 많아질 뿐이다...

[Tig Homepage](https://github.com/jonas/tig)

![Tig snap]({filename}/img/2016-02-10_tig_snap.png)

실행시키면 위와 같은 모습을 보여주게된다. 간단한 설명은 여기까지하고 메뉴얼이나 보자.

-----

[The Tig Manual](http://jonas.nitro.dk/tig/manual.html)

이 문서는 Tig에 대한 메뉴얼이며, Tig는 Git에 대한 ncurses 기반의 텍스트 모드 인터페이스로 작성되었습니다. Tig는 Git 저장소의 변화를 확인하고 추가적으로 다양한 Git 명령에 대한 출력 내용을 확인할 수 있는 pager로 사용할 수 있습니다. Pager로 사용할 경우, stdin에서 입력을 표시하고, 생상을 추가할 수 있습니다.

저장소 확인용으로 사용할 경우, Tig는 기초적인 Git 명령을 사용하여 요약된 커밋 로그, 로그 메시지에서의 커밋 내용, diffstat, diff 와 같은 다양한 뷰를 이용하여 사용자에게 보여줍니다.

[TOC]

## 1. 호출 규칙

### Pager 모드

Stdin 파이프를 사용할 경우, 모든 로그나 diff 옵션은 무시되고 pager 뷰는 stdin으로 들어온 데이터를 로딩하여 확인할 수 있습니다. Pager 모드는 다양한 Git 명령에 대한 출력값을 색상을 추가하여 확인할 수 있도록 도와줍니다.

예로 git-show(1) 명령에 대한 출력을 색상을 추가한 버전으로 보고 싶다면:

	:::shell
	$ git show | tig

* `git-show`
![git-show]({filename}/img/2016-02-10_tig_1-1.png)

* `git-show | tig`
![git-show|tig]({filename}/img/2016-02-10_tig_1-2.png)

### Git 명령어 옵션

명령 줄에서 모든 Git 명령어 옵션은 주어진 명령에 전달되고 셸에 모두 전달되기 전에 인용 셸을 통과할 것입니다.

> 주의: 메인 뷰에 대한 옵션을 지정하는 경우엔, 메인 뷰에서 사용하는 형식으로 자동 설정되는 `--pretty` 옵션을 사용할 수 없습니다.

커밋과 author, 커미터 정보를 모두 보여주는 방법에 대한 예:

	:::shell
	$ tig show --pretty=fuller

Git 명령에 대해 지원되는 변경 옵션 지원에 대한 소개는 [지정 변경](#5) 섹션을 참조하세요. 특정 Git 명령 옵션에 대한 자세한 설명은 해당 명령의 맨 페이지를 참조하세요.

## 2. 뷰어
### 뷰
### 상태 확인과 사용자 정의 명령어
### 제목 윈도우
## 3. 환경 변수
### 구성 파일
### 저장소 참조
### Diff 옵션
## 4. 기본 키설정
### 뷰 전환
### 뷰 조작
### 뷰 지정 동작
### 커서 네비게이션
### 스크롤링
### 검색
### Misc
### 프롬프트
### 확장 명령어
## 5. 변경 사항
### 패치 이름 제한
### 날짜나 숫자 제한
### 도달 가능 제한
### 변경 사항 연결
### 모든 저장소 참조 검사

## 6. 정보를 더 원하시면

Tig [홈페이지](http://jonas.nitro.dk/tig)나 [메인 Git 저장소](https://github.com/jonas/tig)를 방문하여 새로운 릴리즈 내용, 버그 리포트 내용, 기능 요청에 대한 정보를 얻어가시길 바랍니다.

## 7. 저작권

Copyright (c) 2006-2014 Jonas Fonseca <jonas.fonseca@gmail.com>

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

## 8. 더보기

맨 페이지:
	* [tig(1)](http://jonas.nitro.dk/tig/tig.1.html)
	* [tigrc(5)](http://jonas.nitro.dk/tig/tigrc.5.html)