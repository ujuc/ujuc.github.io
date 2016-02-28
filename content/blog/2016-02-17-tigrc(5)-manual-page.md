Title: tigrc(5) Manual Page
Date: 2016-02-17 21:42
Category: Develop
Tags: tig, tigrc, git, ncurses
Slug: tigrc(5)-manual-page
Summary: tigrc 파일에 대한 내용이다.
Status: draft

## Name

tigrc - Tig 구성 파일

## SYNOPSIS

> set variable = value
> bind keymap key action
> color area fgcolor bgcolor [attributes]
> source path

## DESCRIPTION

`~/.tigrc` 파일에 옵션을 넣어 영구적으로 설정할 수 있습니다. 파일은 *commands* 나열로 구성됩니다. 파일의 각 행은 명령 하나입니다. 각 라인 끝에 백슬래시(`\`)를 넣어 여러줄로 구성할 수 있습니다.

해쉬 마크(`#`)는 *주석(commant)* 문자로 사용합니다. 주석 문자 이후로오는 모든 문자는 무시됩니다. 주석 문자를 이용해 초기 파일에 주석을 달 수 있습니다.

이부 옵션은 옵션 메뉴를 통해서 작동중 조작 할 수 있습니다. 추가적으로 `:toggle` 프롬프트 명령을 이용하여 옵션을 변경하거나 프롬프트 구성 명령을 입력할 수 있습니다.

## Git configuration

`~/.tigrc`를 사용하거나, Git 구성 파일에 Tig 옵션을 설정하여 사용할 수 있습니다. 이 내용들은 Tig가 시작하면서 읽어 사용합니다. 다음 예제와 같이 기본 구문 강조, 바인딩, 색들을 설정할 수 있습니다.

	:::text
	[tig] show-changes = true
	[tig "color"] cursor = yellow red bold
	[tig "bind"] generic = P parent

Tig-specific 옵션을 추가하여 Git 옵션에 따라 Git 구성에서 읽어옵니다:

`coror.*`
:    다양한 UI 타입에대한 색. `git-color` 설정을 통해 구성할 수 있습니다.
`core.abbrev`
:    커밋 ID의 넓이(width). `id-width` 옵션을 확인합니다.
`core.worktree
:    편집기 명령. GIT_EDITER 설정을 덮어쓸수 있습니다.
`gui.encoding`
:    파일 내용을 보여주는데 사용되는 인코딩.
`i18n.commitencoding`
:    커밋에서 사용하는 인코딩. 기본값은 UTF-8

## Set command

일부 선택할 수 있는 값들은 set 명령어를 통해서 구성할 수 있습니다. 구문은 다음과 같다는:

> set variables = value

예제:

	:::text
	set commit-order = topo         # Order commits topologically
	set git-colors = no             # Do not read Git's color settings.
	set horizontal-scroll = 33%     # Scroll 33% of the view width
	set blame-options = -C -C -C    # Blame lines from other files

	# Wrap branch names with () and tags with <>
	set reference-format = (branch) <tag>

	# Configure blame view columns using command spanning multiple lines.
	set blame-view = \
	        date:default \
	        author:abbreviated \
	        file-name:auto \
	        id:yes,color \
	        line-number:yes,interval=5 text

Git 구성 파일에서:

	:::text
	[tig]
        line-graphics = no      # Disable graphics characters
        tab-size = 8            # Number of spaces per tab

변수 형식은 bool, int, string, mixed.

bool 변수 값
:    "1", "true", "yes" 값은 ture 값로 설정됩니다. 다른 값들은 false 값으로 설정됩니다.
int 변수 값
:    양의 정수
string 변수 값
:    문자열. 추가적으로 `'`나 `"` 값으로 경계를 나타낼 수 있습니다.
mixed 변수 값
:    이 값은 여러 타입을 같이 사용합니다. 유요한 값은 다음 설명에서 확인합니다.

### 변수

다음 변수를 이용하여 설정할 수 있습니다.

`diff-options`(string)
:    diff 뷰에서 사용하며, diff 옵션에 대한 공간을 나눠 보여줍니다. `git-show(1)`은 포멧팅을 사용하고 항상 `--patch-with-stat`을 통과합니다. 이 옵션은 ([tig(1)](http://jonas.nitro.dk/tig/tig.1.html)에 포함되어 있는) `TIG_DIFF_OPTS` 환경 변수에 지정된 값을 덮어쓰지만, 커멘드 라인에서 호출된 diff 플래그로 덮어쓰일 수 있습니다.
`blame-options`(string)

### 뷰 설정

## 바인드 명령어
### 외부 사용자 정의 명령어
#### Browsing 상태 변수
#### 고급 셸같은 명령어
### 내부 사용자 정의 명령어
### 동작 이름
#### 뷰 전환
#### 뷰 조작
#### 커서 네비게이션
#### 스크롤링
#### 검색
#### Misc
## 색 명령어
### UI 색

강조 표시시되거나 기본 터미널 색상 사용을 지정하지 않은 텍스트와 색상의 속성은 **기본** 색상 옵션을 제어하여 설정할 수 있습니다.

Table 1. 일반

| default | 기본 터미널 색상을 덮어씁니다. |
| cursor | 커서 라인 |
| status | 상태 윈도우에서 보여주는 정보 메시지 |
| title-focus | 현재 뷰에대한 제목 윈도우 |
| title-blur | 어떤 배경 뷰에대한 제목 윈도우 |
| delimiter | 구문 문자는 짤린 라인을 보여줍니다 |
| header | 뷰 헤더 라인. 상태 뷰에서 `status.header`를 이용하여 staged, unstaged, untracked 의 색을 변경하여 사용합니다. 도움말 뷰에서 `help.header` 키맵 섹션의 색을 변경하는데 사용합니다. |
| line-number | 라인 넘버 |
| id | 커밋 ID |
| date | 작성 일자 |
| author | 커밋 작성자 |
| mode | 권한과 유형을 유지하는 파일 모드 |
| overflow | 텍스트 넘침 |
| directory | 디렉토리 이름 |
| file | 파일 이름 |
| file-size | 파일 크기 |

### 구문 강조

Diff을마크업
:    diff 시작, 청크, 라인 추가, 삭제를 합니다.

**diff-header, diff-chunk, diff-add, diff-add2, diff-del, diff-del2**

향상된 Git diff 마크업
:    Git diff 매커니즘에대한 확장 diff 정보를 출력합니다. 모드 변경, 이름 변경 확인, 유사성에 대해 확인합니다.

**diff-oldmode, diff-newmode, diff-copy-from, diff-copy-to, diff-similarity, diff-index**

Pretty print commit headers
:    커밋 diff와 리버전 로그는 `--pretty=raw`로 설정하지 않으면, pretty printed 해더 포멧을 설정합니다. 여기에는 머지 정보, 커밋 ID, 커밋 저자, 커밋 날짜 등의 라인이 포함됩니다.

**pp-refs, pp-reflog, pp-reflogmsg, pp-merge**

Raw commit headers
:    `--pretty=raw`값을 사용하는 것과 동일합니다. 그러나 *commit*은 어디서든 꽤 괜찮게 나옵니다.

**commit, parent, tree, author, committer**

커밋 메시지
:    `Signed-off-by`, `Acked-by`, `Reviewed-by`, `Tested-by` 라인에 색을 더합니다. 미리 정의된 너비를 넘어간 커밋 제목 문자를 강조 표시할 수 있습니다.

Tree 마크업
:    Tree 뷰에대한 정보에 색을 더합니다.

**tree-dir, tree-file**

## 소스 명령

소스 명령은 추가 설정 파일을 불러올 수 있도록 합니다. 소스로 구성된 파일은 해당 자리에 포함되고 소스 명령과 만났을때 해당 파일을 읽어오게 됩니다. 현재 구성 파일에 있는 명령 이후에 해당 명령을 먼저 실행합니다. 구문은 다음과 같습니다:

> source path

예제:

    :::text
    source ~/.tig/colorscheme.tigrc
    source ~/.tig/keybindings.tigrc

## COPYRIGHT

Copyright (c) 2006-2014 Jonas Fonseca <jonas.fonseca@gmail.com>

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

## SEE ALSO

[tig(1)](http://jonas.nitro.dk/tig/tig.1.html), [the Tig manual](/2016/02/10/tig-manual/), [git(7)](https://www.kernel.org/pub/software/scm/git/docs/gittutorial.html), [git-config(1)](https://www.kernel.org/pub/software/scm/git/docs/git-config.html)