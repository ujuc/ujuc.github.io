Title: Tig Manual
Date: 2016-02-10 02:08
Modified: 2019-03-23 16:50
Category: 번역
Tags: tig, translate
Slug: tig-manual
Summary: Tig 메뉴얼 번역 축약본

Git을 사용하기 위한 프로그램들이 많다. 그중에서도 번역하려고 하는 것은 Tig. 터미널 환경에 맞게 구성이되어 있으며, Git CLI와 같이 사용하면 왠만한 GUI 프로그램 못지않은 사용성을 보여주고 있다. 단지... 명령어가 많아질 뿐이다...

[Tig Homepage](https://github.com/jonas/tig)

![Tig snap]({static}/img/2016-02-10_tig_snap.png)

실행시키면 위와 같은 모습을 보여주게된다. 간단한 설명은 여기까지하고 메뉴얼이나 보자. 다수의 의역이 포함되어있다. 안할려고 했으나 하루죙일 하다보니... 그리고 한국어로 곧장 옮기니 이상한 부분이 있어...

-----

[The Tig Manual](http://jonas.nitro.dk/tig/manual.html)

이 문서는 Tig에 대한 메뉴얼이며, Tig는 Git에 대한 ncurses 기반의 텍스트 모드 인터페이스로 작성되었습니다. Tig는 Git 저장소의 변화를 확인하고 추가적으로 다양한 Git 명령에 대한 출력 내용을 확인할 수 있는 pager로 사용할 수 있습니다. Pager로 사용할 경우, stdin에서 입력을 표시하고, 생상을 추가할 수 있습니다.

저장소 확인용으로 사용할 경우, Tig는 기초적인 Git 명령을 사용하여 요약된 커밋 로그, 로그 메시지에서의 커밋 내용, diffstat, diff 와 같은 다양한 뷰를 이용하여 사용자에게 보여줍니다.

[TOC]

## 1. Calling Conventions (호출 규칙)

### Pager Mode (Pager 모드)

Stdin 파이프를 사용할 경우, 모든 로그나 diff 옵션은 무시되고 pager 뷰는 stdin으로 들어온 데이터를 로딩하여 확인할 수 있습니다. Pager 모드는 다양한 Git 명령에 대한 출력값을 색상을 추가하여 확인할 수 있도록 도와줍니다.

예로 `git-show(1)` 명령에 대한 출력을 색상을 추가한 버전으로 보고 싶다면:

	:::shell
	$ git show | tig

* `git-show`

![git-show]({static}/img/2016-02-10_tig_1-1.png)

* `git-show | tig`

![git-show|tig]({static}/img/2016-02-10_tig_1-2.png)

### Git Command Options (Git 명령어 옵션)

명령 줄에서 모든 Git 명령어 옵션은 주어진 명령에 전달되고 셸에 모두 전달되기 전에 인용 셸을 통과할 것입니다.

> 주의: 메인 뷰에 대한 옵션을 지정하는 경우엔, 메인 뷰에서 사용하는 형식으로 자동 설정되는 `--pretty` 옵션을 사용할 수 없습니다.

커밋과 author, 커미터 정보를 모두 보여주는 방법에 대한 예:

	:::shell
	$ tig show --pretty=fuller

Git 명령에 대해 지원되는 변경 옵션 지원에 대한 소개는 [지정 리버전](#5-revision-specification) 섹션을 참조하세요. 특정 Git 명령 옵션에 대한 자세한 설명은 해당 명령의 맨 페이지를 참조하세요.

## 2. The Viewer (뷰어)

디스플레이는 하나 이상의 뷰와 스크린으로 구성되어있으며, 맨 마지막 라인은 상태 윈도우로 사용됩니다. 기본 값은 한번에 하나의 뷰만을 보여줍니다. 하지만 메인과 로그 뷰로 나눠서 커밋 diff를 확인할 수 있습니다.

현재 라인이 커밋 라인일때, 로그 뷰에서 엔터키를 누르게되면 다음과 같은 명령이 실행되는 것과 같습니다:

	:::shell
	commit 4d55caff4cc89335192f3e566004b4ceef572521

뷰를 나눠서 볼 수 있는데, 로그 뷰는 윈도우 상단에, diff 뷰는 윈도우 하단에 위치시킬 수 있습니다. 탭을 눌러 두 뷰사이를 왔다갔다 할 수 있습니다. 로그 뷰만 보려면 `l`를 누르면 됩니다.

### Views (뷰)

저장소에서 여러가지 `views`를 볼 수 있습니다. 각 뷰는 확장 명령, `git log`, `git diff`, `git show`로부터 나오는 출력 값에 기반하여 보여줍니다.

메인 뷰
:    기본 뷰이며, 리버전의 선택된 목록에서 각 커밋을 요약하여 보여줍니다. 요약한 내용에서는 author 날짜, author, 로그 메시지 첫 줄을 포함하고 있습니다. 추가적으로 태그와 같은 저장소 참조 표시도 같이 표시됩니다.

로그 뷰 
:    전체 로그 메시지와 diffstat에대한 리버전 로그를 보여주는 다양한 뷰를 제공합니다.

Diff 뷰
:    현재 작업 트리에 대한 diff, 즉, 마지막 커밋이후 변화분, 로그 메시지, diffstat, diff에 대한 커밋 diff 완료 내용을 나타냅니다.

트리 뷰 
:    디렉토리 목록을 트리로 표현하여 현재 리버전에대한 하위 디렉토리로 내려가며 확인하거나 올라오며 확인할 수 있으며 파일의 blob에 대해서도 확인이 가능합니다.

Blob 뷰
:    파일 내용이나 파일 이름에 대한 관련 데이터의 "blob"을 보여줍니다.

Blame 뷰
:    파일 내용의 주석이나 커밋에 대한 blam을 보여줍니다.

Refs 뷰
:    저장소에서 브런치, 리모트, 태그를 보여줍니다.

Status 뷰
:    작업 트리내의 파일 상태나 staged/unstaged 변화분 확인과 추적되지 않는 파일의 추가를 좀 더 쉽게 보여줍니다.

Stage 뷰
:    stage된 변화분, unstage된 파일의 추적분, 추적되지 않는 파일의 내용에 대한 diff를 보여줍니다.

Stash 뷰
:    저장소의 Stash 목록을 보여줍니다.

Grep 뷰
:    검색 패턴과 동일한 내용으로 모든 라인과 파일 목록을 보여줍니다.

Pager 뷰
:    Stdin으로 입력과 내부 프롬프트에서 입력된 Git 명령어로부터 출력 모두를 보여주는데 사용됩니다.

도움말 뷰
:    키 바인딩에 대한 간단한 참조를 보여줍니다.

### Browsing State and User-defined Commands (상태 확인과 사용자 정의 명령어)

뷰어는 head와 커밋 ID 모두를 추적하고, 현재 상태를 보여줍니다. 커밋 ID는 커서 라인에 따라가며 다른 커밋을 선택할때마다 강조표시가 변경됩니다. 커밋 ID가 변경되면, diff 뷰에선 열때마다 재로드됩니다. Head ID는 지나온 로그를 보면서 리버전된 것이 나타내는 메인과 로그 뷰를 확인할때 사용됩니다.

Tig에서 명령을 사용하거나 제공하는 명령을 구성할 수 있습니다. [환경 변수](#3-environment-variables)의 일부와 [외부 명령](#external-commands)을 사용할 수 있습니다. 사용자 정의 명령의 경우 다음 변수들을 이용하여 현재 브라우징 상태에 대한 참조 인자로 사용할 수 있습니다.

| 변수 값 | 설명 |
| :-- | :-- |
| `%(head)` | 현재 보여지는 `haed` ID. 기본값은 `HEAD` |
| `%(commit)` | 현재 선택된 커밋 ID |
| `%(blob)` | 현재 선택된 blob ID |
| `%(branch)` | 현재 선택된 브런치 이름 |
| `%(stash)` | 현재 선택된 stash 이름 |
| `%(directory)` | 현재 트리 뷰에서 보여지는 위치, 루트 디렉토리일 경우, 빈칸으로 표시 |
| `%(file)` | 현재 선택된 파일 |
| `%(lineno)` | 현재 선택된 라인 번호. 기본 값은 `0` |
| `%(ref)` | 참조에서 재공되는 blame 또는 정의되지 않았을 경우, `HEAD` |
| `%(revargs)` | 명령 라인에서 리버전 인수 값 |
| `%(fileargs)` | 명령 라인에서 파일 인수 값 |
| `%(cmdlineargs)` | 명령 라인에서 다른 옵션 인자 값 |
| `%(diffargs)` | `diff-options`나 diff 뷰에 대한 `TIG_DIFF_OPTS`에서 사용되는 옵션 |
| `%(logargs)` | Blame 뷰에 대한 `blame-options`에서 사용된 옵션 |
| `%(mainargs)` | 로그 뷰에 대한 `log-options`에서 사용된 옵션 |
| `%(prompt)` | 인자 값에 대한 프롬프트 |

사용자 정의 명령어 예제들:

* 마지막 커밋에 대해 amend 적용:

		:::shell
		bind generic + !git commit --amend

* 크립 보드에서 커밋 ID 복사:
	
		:::shell
		bind generic 9 !@sh -c "echo -n %(commit) | xclip -selection c"

* 리뷰 즁 현재 커밋에서 사용된 노트 추가/수정:
	
		:::shell
		bind generic T !git notes edit %(commit)

* Git 대화형으로 파일 내용에 세밀한 staging 추가 입력:
		
		:::shell
		bind generic I !git add -i %(file)

* 선택된 브런치의 최상위에서 현재 브런치로 리배이스:
		
		:::shell
		bind refs 3 !git rebase -i %(branch)

### Title Windows (제목 윈도우)

각 뷰는 뷰 이름에 대한 제목 윈도우를 가집니다. 가능하다면 현재 커밋 ID로도 나태낼 수 있으며, 뷰에서는 다음과 같이 위치됩니다:

	:::shell
	[main] c622eefaa485995320bc743431bae0d497b1d875 - commit 1 of 61 (1%)

기본 값으로 현재 뷰의 제목은 굵은 폰트를 사용하여 강조됩니다. 긴 로딩이 있는 뷰의 경우(3초 이상), 로딩이 시작된 시간으로 부터의 시간이 추가되어 보여집니다:

	:::shell
	[main] 77d9e40fbcea3238015aea403e06f61542df9a31 - commit 1 of 779 (0%) 5s

## 3. Environment Variables (환경 변수)

Git 인터페이스에 관련된 몇가지 옵션을 환경 옵션을 통해 구성할 수 있습니다.

### Configuration Files (구성 파일)

시작시 Tig는 시스템 전체 구성 파일(기본 값 `{sysconfigdir}/tigrc`)을 읽은 다음 사용자 구성 파일(기본 값 `~/.tigrc`)을 읽습니다. 이 파일 중 하나의 경로를 다음과 같은 환경 변수를 이용하여 재정의 할 수 있습니다:

`TIGRC_USER`
:    사용자 구성 파일 위치

`TIGRC_SYSTEM`
:    시스템 전체 구성 파일 위치

### Repository References (저장소 참조)

태그와 브런치 head가 참조하는 커밋은  `[`과 `]`에 둘러쌓여 참조 이름으로 표시됩니다:

	:::shell
	2006-03-26 19:42 Petr Baudis         | [cogito-0.17.1] Cogito 0.17.1

브런치가 보여지는 것을 제한하길 원한다면, 보여질 브런치의 이름이 `master`이거나 `feature/` 로 접두어로 시작하는 경우엔 다음과 같이 변수를 설정할 수 있습니다:

	:::shell
	$ TIG_LS_REMOTE="git ls-remote . master feature/*" tig

또는 여러분의 환경에서 영구적으로 변수를 설하여 사용할 수 있습니다.

`TIG_LS_REMOTE`
:    모든 저장소에 대한 참조를 검색하는 명령을 설정합니다. 명령을 사용하게 되면 `git-ls-remote(1)` 과같은 포맷으로 데이터를 출력할 수 있습니다. 기본 값은 다음과 같습니다:

		:::shell
		git ls-remote .

### Diff options (Diff 옵션)

Diff 뷰에 대해 diff를 어떻게 표시할 것인가에 대한 내용으로 수정이 가능합니다. 예를 들어 커멧과 author 날짜를 상대 날짜와 같이 보길 원한다면:

	:::shell
	$ TIG_DIFF_OPTS="--relative-date" tig

또는 여러분의 환경에서 영구적으로 변수를 설정하여 사용할 수 있습니다.

## 4. Default Keybindings (기본 키 바인딩)

기본 키 바인딩에 대해서는 아래와 같습니다.

### View Switching (뷰 전환)

* `m` | 메인 뷰로 전환

![tig main view]({static}/img/2016-02-10_tig_2-1_main.png)

* `d` | diff 뷰로 전환

![tig diff view]({static}/img/2016-02-10_tig_2-2_diff.png)

* `l` | 로그 뷰로 전환

![tig log view]({static}/img/2016-02-10_tig_2-3_log.png)

* `p` | pager 뷰로 전환

![tig parger view]({static}/img/2016-02-10_tig_2-4_pager.png)

* `t` | 디렉토리 트리 뷰로 전환

![tig tree view]({static}/img/2016-02-10_tig_2-5_tree.png)

* `f` | 파일 blob 뷰로 전환

![tig file blob view]({static}/img/2016-02-10_tig_2-6_file.png)

* `g` | grep 뷰로 전환

![tig grep view]({static}/img/2016-02-10_tig_2-7_grep.png)

* `b` | blame 뷰로 전환

![tig blame view]({static}/img/2016-02-10_tig_2-8_blame.png)

* `r` | refs 뷰로 전환

![tig refs view]({static}/img/2016-02-10_tig_2-9_refs.png)

* `y` | stash 뷰로 전환

![tig stash view]({static}/img/2016-02-10_tig_2-10_stash.png)

* `h` | 도움말 뷰로 전환

![tig help view]({static}/img/2016-02-10_tig_2-11_help.png)

* `s` | status 뷰로 전환

![tig status view]({static}/img/2016-02-10_tig_2-12_status.png)

* `c` | stage 뷰로 전환

![tig stage view]({static}/img/2016-02-10_tig_2-13_stage.png)

### View Manipulation (뷰 조작)

| 키 | 동작 |
| :-- | :-- |
| `q` | 뷰를 닫는다. 여러뷰가 열려있다면, 뷰 스택 안에서 이전 뷰로 되돌아가게 된다. 마지막 뷰라면, Tig에서 나오게 됨. `Q`를 이용하면 모든 뷰를 닫는다. |
| Enter | 이 키는 현재보고 있는 뷰에서 "상황에 맞게(context sensitive)" 동작합니다. 커밋줄에서의 로그 뷰나 메인 뷰일땐 뷰를 분활하여 커밋 diff를 보여줍니다. diff 뷰에서는 간단하게 한줄을 내리는데 사용됩니다. |
| Tab | 다음 뷰로 전환 |
| `R` | 현재 뷰를 리로드하거나 새로고침 |
| `O` | 현재 뷰를 화면에 꽉차도록 |
| Up | "상황에 맞게(context sensitive)" 작동하며, 한 줄 위로 이동합니다. 그러나 메인 뷰에서(split이나 전체 화면에서) diff 뷰를 열경우, 메인 뷰에서는 이전 커밋으로 커서를 변경하고 해당 diff 뷰를 보여주게 됩니다. |
| Down | *Up*과 동일하며 단지 아래로 내려갑니다. |
| `,` | 상위로 이동합니다. 트리 뷰에서는 상위 디렉토리로 이동하게 됩니다. blame 뷰에서는 상위 커밋에 대한 blame가 표시됩니다. 머지의 경우, 상위가 쿼리됩니다. |

### View Specific Actions (뷰 지정 동작)

| 키 | 동작 |
| :-- | :-- |
| `u` | 파일 상태를 업데이트 합니다. Status 뷰에서는 다음 커밋에 대해 추가하지 않은 파일이나 stage 변경 파일에 대해서 추가할 수 있습니다.(`git-add <filename>`과 동일한 작업입니다.) Stage 뷰에서는 diff 청크 라인에서는 다음 커밋에 대한 청크만 stage 합니다. diff에 표시되는 모든 변화가 diff 청크 라인에서 stage 되지는 않습니다. |
| `M` | `git-mergetool(1)`을 실행하여 머지되지 않은 파일을 해결합니다. 주의, 원하는 머지 도구를 사용하기 위해 초기 구성이 필요할 수 있습니다. 올바르게 작동하는지 확인하세요. `git-mergetool(1)`의 맨페이지를 확인하세요. |
| `!` | Unstage된 변경을 파일에서 체크아웃합니다. 마지막 커밋한 콘텐츠가 포함된 파일을 재설정합니다. |
| `1` | Stage 싱글 diff 라인 |
| `@` | Stage 뷰에서 다음 청크로 이동 |
| `]` | diff 콘텍스트 확장 |
| `[` | diff 콘텍스트 축소 |

### Cursor Navigation (커서 네비게이션)

| 키 | 동작 |
| :-- | :-- |
| `k` | 커서 한 라인 위로 이동 |
| `j` | 커서 한라인 아래로 이동 |
| PgUp, `-`, `a` | 커서 한 페이지 위로 이동 |
| PgDown, Space | 커서 한 페이지 아래로 이동 |
| End | 마지막 라인으로 점프 |
| Home | 첫 라인으로 점프 |

### Scrolling (스크롤링)

| 키 | 동작 |
| :-- | :-- |
| Insert | 뷰 한 라인 위로 스크롤 |
| Delete | 뷰 한 라인 아래로 스크롤 |
| ScrBack | 뷰 한 페이지 위로 스크롤 |
| ScrFwd | 뷰 한 페이지 아래로 스크롤 |
| Left | 뷰 한 컬럼 왼쪽으로 스크롤 |
| Right | 뷰 한 컬럼 오른쪽으로 스크롤 |
| `|` | 뷰 첫 칼럼으로 스크롤 |

### Searching (검색)

| 키 | 동작 |
| :-- | :-- |
| `/` | 뷰에서 검색. 열려진 프롬프트에서 정규식을 사용해서 찾을 수 있음. |
| `?` | 뷰에서 뒤에서부터 검색. 이것도 정규식 사용 가능. |
| `n` | 현재 검색 정규식과 동일한 다음 검색 |
| `N` | 현재 검색 정규식과 동일한 이전 검색 |

### Misc

| 키 | 동작 |
| :-- | :-- |
| `Q` | 나가기 |
| `<C-L>` | 스크린 새로고침 |
| `z` | 모든 백그라운드 로딩 정지. 리버전 로그의 제한 없이 긴 히스토리를 가진 저장소에서 Tig를 사용할때 필요할 수 있습니다. |
| `v` | 버전 확인 |
| `o` | 옵션 메뉴 열기 |
| `#` | 라인 번호 on/off |
| `D` | 날짜 표시 on/off/short/relative/local |
| `A` | Author 표기 on/off/abbreviated/email/email 사용자 이름 |
| `G` | 리버전 그래프 시각화 on/off |
| `~` | 라인 그래프 모드 on/off |
| `F` | 참조 표시 on/off (태그, 브런치 이름) |
| `W` | diff에 대한 공백 무시 on/off |
| `X` | 커밋 ID 표시 on/off |
| `%` | 모든 diff 대신에 현재 선택한 파일에 대한 diff를 참조하기 위한 파일 필터링 on/off |
| `$` | 커밋 제목 넘어감에 대한 강조표시 on/off |
| `:` | 프롬프트 열기. 특정 명령어를 실행할 수 있도록 허용 |
| `e` | 에디터에서 파일 열기 |

### Prompt (프롬프트)

| 키 | 동작 |
| :-- | :-- |
| `:<number>` | 특정 라인 번호로 점프. 예 `:80` |
| `:<sha>` | 특정 커밋으로 점프. 예 `:2f12bcc` |
| `:<x>` | 일치하는 키 바인딩 실행. 예 `:q` |
| `:!<command>` | Pager 내에서 시스템 명령어 실행. 예 `:!git log -p` |
| `:<action>` | Tig 명령 실행. 예 `:edit` |
| `:save-display <file>` | `<file>`에서 현재 화면 저장 |
| `:save-options <file>` | `<file>`에서 현재 옵션 저장 |
| `:script <file>` | `<file>`로부터 명령어 실행 |
| `:exec <flags><args...>` | `<flags>`에 정의된 확장 사용자 정의 명령 옵션과 `<args>` 사용하여 명령 실행 |

### External Commands (외부 명령어)

사용자에 따라 외부 명령어가 더 필요한 경우, 쉽게 스크립트다 프로그램을 사용할 수 있는 방법을 제공합니다. 현재 커밋 ID로 키를 연결하고 현재 보여지는 상태에서 정보를 사용할 수 있습니다. Tig에서 기본 등록되어있는 확장 명령어:

| Keymap | 키 | 동작 |
| :-- | :-- | :-- |
| main | `C` | `git cherry-pick %(commit)` |
| status | `C` | `git commit` |
| generic | `C` | `git gc` |

## 5. Revision Specification (리버전 사항)

이 세션에서는 리버전을 표시하거나 볼 수 있는 내용을 제한할 수 있도록 설정하는 방법에 대해서 설명합니다. Tig에서는 구문 분석을 하지 않습니다. 리버전 옵션에 대한 자세한 설명은 Git 메뉴얼 페이지에서 확인하십시오. 연관된 맨페이지는 `git-log(1)`을 기준으로 `git-diff(1)`과 `git-rev-list(1)`입니다.

설정 가능한 옵션을 사용하여 Git과 상호 작용을 이 세션에서 설명합니다. 예를 들어 [diff 옵션](#diff-options-diff)에 대한 세션에서 설명된 환경 변수를 사용하여 구성할 수 있습니다.

### Limit by Path Name (패치 이름 제한)

특정 파일 (또는 여러 파일) 변경에 대해서만 확인하고 싶다면 다음과 같이 목록으로 나타냅니다:

	:::shell
	$ tig Makefile README

Tig의 하위 명령 또는 태그 이름과 같은 저장소 참조에서 발생할 수 있는 모호성을 방지하기 위해 Git 옵션의 경우 `--`를 사용하여 구분해야됩니다. `states`라는 이름을 가진 파일이 있다면, `status` 하위 명령과 충돌을 일으킬꺼니 다음과 같이 사용해야합니다:

	:::shell
	$ tig -- status

### Limit by Date or Number (날짜나 숫자 제한)

Git과의 상호작용 속도를 올리기 위해 로그와 메인 뷰에서 보여지는 커밋의 수를 제한할 수 있습니다. 예를 들어, 날짜로 제한을 걸 경우엔 `--since=1.month`, 커밋 수로 제한을 걸 경우엔 `-n400`와 같이 사용합니다.

만약 두 날짜 사이에 발생한 변경분에 대해서 확인하고 싶다면:

	:::shell
	$ tig --after="May 5th" --before="2006-05-16 15:44"

> 주의, 공간을 포함하는 날짜를 사용하지 않는다면 `.`를 이용하여 나타낼 수 있습니다. 예, `--after=May.5th`

### Limiting by Commit Ranges (커밋 범위 제한)

대안으로 "`tag-1.0`과 `tag-2.0` 사이의 모든 커밋"과 같은 특정 범위로 제안할 수 있습니다. 예를 들면:

	:::shell
	$ tig tag-1.0..tag-2.0

원격 브런치로 푸시되지 않은 커밋의 검색 제한은 다음과 같은 방법으로 가능합니다. `origin`을 업스트림 원격 브런치고 가정하고 사용한다면:

	:::shell
	$ tig origin..HEAD

원격 브런치에서 푸시된 내용들을 나열 합니다. 선택적으로 `HEAD`는 생략될 수 있습니다.

### Limiting by Reachability (도달 가능 제한)

Git 인터프리트에서는 "tag-1.0...tag-2.0"을 사용하는 경우, "`tag-1.0`를 제외하고 `tag-2.0`까지의 모든 커밋"으로 지정할 수 없습니다. 도달 가능한 참조는 물음의 브런치의 원형 (또는 히스토리의 일부분)의 커밋 또는 테그된 리버전일 수 있습니다.

이 방법으로 다음 미리 커밋을 지정하려는 경우:

	:::shell
	$ tig tag-2.0 ^tag-1.0

부정 연산자로 `^`를 생각할 수 있습니다. 이 대체 문법을 사용하면 위의 여려 브런치의 cut off를 지정하여 커밋 브런치를 없애버릴 수 있습니다.

### Combining Revisions Specification (변경 사항 연결)

리버전 옵션은 다음과 같이 연결하여 사용할 수 있습니다. "`Documentation/` 디렉토리에 있는 파일의 변경 사항들을 마지막달 20개 커밋까지 보여다오."를 다음과 같이 나타낼 수 있습니다:

	:::shell
	$ tig --since=1.month -n20 -- Documentation/

### Examining All Repository References (모든 저장소 참조 검사)

일부 경우엔 저장소에 대한 모든 참조를 걸쳐서 변화를 조회하는 것이 편할 수 있습니다. 다음 예제는 "이 저장소의 개발 라인에서 지난주내 특정파일이 변경되었는지"에 대해 묻는 것입니다. 다음 명령으로 가능합니다:

	:::shell
	$ tig --all --since=1.week -- Makefile

## 6. More Information (정보를 더 원하시면)

Tig [홈페이지](http://jonas.nitro.dk/tig)나 [메인 Git 저장소](https://github.com/jonas/tig)를 방문하여 새로운 릴리즈 내용, 버그 리포트 내용, 기능 요청에 대한 정보를 얻어가시길 바랍니다.

## 7. Copyright (저작권)

Copyright (c) 2006-2014 Jonas Fonseca <jonas.fonseca@gmail.com>

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

## 8. See Also (더보기)

맨 페이지:

* [tig(1)](http://jonas.nitro.dk/tig/tig.1.html)
* [tigrc(5)](http://jonas.nitro.dk/tig/tigrc.5.html)
