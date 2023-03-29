Title: git-vendor
Date: 2016-02-20 21:02
Category: Develop
Tags: git, git-vendor, git-subtree, dependencies
Slug: git-vender
Summary: git-vendor. git 확장이며 git-subtree를 이용하여 vendor 소스를 관리할 수 있도록 도와준다.

brew 업그레이드하다가 `git-vender`라는 확장 프로그램이 보였다. 이건 뭐하는 넘인지 궁금해서 정리한다.

`git-vender`는 git 명령어를 이용하여 vendor 소스를 관리할 수 있도록 도와주는 확장이다. `git-subtree`를 이용해서 소스를 체크 아웃하고 업데이트된 내용들을 관리할 수 있도록 해준다.

`git-vendor`는 golang에서 vendor 종속성을 관리하는 패턴에 따라서 작업을 진행한다고 한다.

* 연관되는 소스들은 `vendor/` 디렉토리에 저장된다.
* 프로젝트에대한 전체 위치로 폴더가 생성되게 된다.

### 기본 명령어

* `git vendor add [--prefix <dir>] <name> <repository> [<ref>]` : 새로운 vendor 연관 소스 추가
* `git vendor list [<name>]` : 현재 레포에 있는 vendor 연관 소스 보기.
* `git vendor update <name> [<ref>]` : vendor 연관 소스 업데이트.

설치는 알아서...

### 예제

Readme에 있는 예제를 가져왔다. 만들어보는 것보다 낫다 판단해서. 아직 `git-subtree`를 모르겠는데 뭐...

    :::shell
    $ # Chekout github.com/brettlangdon/forge@v0.1.6 를 가져온다.
    $ git vendor add forge https://github.com/brettlangdon/forge v0.1.6
    + git subtree add --prefix vendor/github.com/brettlangdon/forge --message 'Add "forge" from "https://github.com/brettlangdon/	forge@v0.1.6"

    git-vendor-name: forge
    git-vendor-dir: vendor/github.com/brettlangdon/forge
    git-vendor-repository: https://github.com/brettlangdon/forge
    git-vendor-ref: v0.1.6
    ' https://github.com/brettlangdon/forge v0.1.6 --squash
    git fetch https://github.com/brettlangdon/forge v0.1.6
    warning: no common commits
    remote: Counting objects: 405, done.
    remote: Total 405 (delta 0), reused 0 (delta 0), pack-reused 404
    Receiving objects: 100% (405/405), 68.31 KiB | 0 bytes/s, done.
    Resolving deltas: 100% (227/227), done.
    From https://github.com/brettlangdon/forge
     * tag               v0.1.6     -> FETCH_HEAD
    Added dir 'vendor/github.com/brettlangdon/forge'

    $ # 목록으로보면..
    $ git vendor list
    forge@v0.1.6:
        name:   forge
        dir:    vendor/github.com/brettlangdon/forge
        repo:   https://github.com/brettlangdon/forge
        ref:    v0.1.6
        commit: 3335840c5f0ad9e821006588f1b16a3385d9c318

    $ # 업데이트를 하면
    $ git vendor update forge v0.1.7
    From https://github.com/brettlangdon/forge
    	* tag               v0.1.7     -> FETCH_HEAD
    Merge made by the 'recursive' strategy.
     vendor/github.com/brettlangdon/forge/forge_test.go | 2 ++
     vendor/github.com/brettlangdon/forge/scanner.go    | 4 ++++
     vendor/github.com/brettlangdon/forge/test.cfg      | 1 +
     3 files changed, 7 insertions(+)

    $ # 확인하면..
    $ git vendor list
    forge@v0.1.7:
        name:   forge
        dir:    vendor/github.com/brettlangdon/forge
        repo:   https://github.com/brettlangdon/forge
        ref:    v0.1.7
        commit: 071c5f108e0af39bf67a87fc766ea9bfb72b9ee7


## 관련 페이지
* [Github](https://github.com/brettlangdon/git-vendor)
* [Manpage](https://brettlangdon.github.io/git-vendor/)
