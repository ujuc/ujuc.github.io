Title: git switch, restore 훑어보기
Date: 2020-07-04 08:54:35
Modified: 2020-07-05 12:21
Category: Develop
Tags: git, command, restore, switch
Slug: git-switch-n-restore-hurt-eo-bo-gi
Summary: git 2.23.0 이상에서 추가된 명령어인 switch, restore에 대해서 정리한다.

[TOC]

---

# 들어가자

**Note: THIS COMMAND IS EXPERIMENTAL. THE BEHAVIOR MAY CHANGE.**

git 2.23.0 이후로 `switch`와 `restore` 실험 명령어가 추가 되었다. 그래서 `switch` 명령을 사용하고는 있지만, 어떻게 써야되는지에 대해서 고민을 해보지 않았던것...

요즘에는 [git commit message template](/2020/02/02/git_commit_message_template_man-deur-gi)를 만들어두고 쓰고 있기에 git cli를 많이 쓰게 되었다. git template을 보여주는건 git 명령을 통해서 실행되는 vim, VSCode가 아니면 보여주지도 않더라. 그러다보니 힘들게 사용중이다.

---

# `git switch`

- 특정 branch로 변경(switching)한다.
- 딴 의미 없다. 말그대로 switching 한다는 것.
- `branch` 명령이나 `checkout` 명령을 이용해서 작업하던 것 중 branch를 관리하는 것에 대한 내용을
 하나의 명령으로 따로 빼서 구성하도록 변경되었다.
- 참고: [git-scm: git-switch](https://git-scm.com/docs/git-switch)

## 개요

```text
git switch [<option>] [--no-guess] <branch>
git switch [<option>] --detach [<start-point>]
git switch [<option>] (-c|-C) <new-brach> [<start-point>]
git switch [<option>] --orphan <new-branch>
```

## 옵션별 설명

### `<start-point>`

- Branch를 딸 특정위치를 나타낸다.
- 기본은 `HEAD`니 딱히 고민할 이유는 없을듯.

### `(-c|--create) <new-branch>`

- 새로운 branch를 `<start-point>`에서 생성을 한다.
- 같은 명령어: `git branch <new-branch>`

### `(-C|--force-create) <new-branch>`

- 있어도 그냥 새롭게 만든다.
- 같은 명령어: `git branch -f <new-branch>`

### `(-d|--detach)`

- 뭘 빼버린다는걸까?
- 쓸일 없을꺼같으니 같은데...
- `git checkout --detach [<branch>]`[[1]](https://git-scm.com/docs/git-checkout#Documentation/git-checkout.txt-emgitcheckoutem--detachltbranchgt)를 보도록 하자.

### `--guess`, `--no-guess`

- 원격 레포에 동일한 이름이 있는 경우, 원걱 branch에서 해당 branch로 매칭한다.
- 기본 값은 `--guess`, 아마 쓸때는 `--no-guess`를 이용할듯.

### `(-f|--force)`, `--discard-changes`

- 자세한 설명은 생략한다.

### `(-m|--merge)`

- 이 옵션을 사용하면 변화분이 있더라도 three-way 머지를 진행하고 branch를 딴다.
- 충돌나는 부분이 존재하면 해당 내용은 `git add`, `git rm`을 이용해서 해당 내용을 정리한뒤 진행하면된다.

### `--conflict=<style>`

- 충돌이 발생했을때 어떤 방법으로 진행할지에 대해서 정의한다.

### `(-q|--quiet)`

- 출력끔

### `--progress`, `--no-progress`

- 터미널이 연결되던 말던 stderr 메시지를 전달한다.
- `--no-progress`는 `-q`와 같다.

### `(-t|--track)`

- 원격 branch에서 새로운 branch를 딴다.
- 이때는 `origin`, `remote/origin`, `refs/remote/origin`와 같이 `/`를 추가하여 만들어주면 새로운 브런치를 딸 수 있다.
- 원격에서 새롭게 따는게 아니라면 `-c` 옵션을 같이 사용해야된다.
- `git branch --tracker`[[2]](https://git-scm.com/docs/git-branch#Documentation/git-branch.txt--t) 에 자세히 적혀있단다.

### `--no-track`

- "upstream" 구성을 하지 않는다.
- `branch.autoSetupMerge` 옵션을 `true`로 설정하는 것과 동일한 효과.

### `--orphan <new-branch>`

- 새로운 `orphan` branch를 생성한다.
- 모든 추적하던 파일은 삭제된다.

### `--ignore-other-worktrees`

- `git switch` 명령은 참조하는 위치가 다른 working tree에서 사용중이면 브런치를 따지 못한다.
- 이 옵션으로 연결된 working tree를 계속 만들 수 있다.

### `--recurse-submodules`, `--no-recurse-submodules`

- `superproject`에 활성화된 submodule 내용을 업데이트하여 반영한다.
- `git submodule` 명령과 같이 서브 모듈 `HEAD`를 표기한다.

# `git restore`

- Working tree 파일을 되돌린다.
- 생각보다 옵션이 많다...

## 개요

```text
git restore [<option>] [--source=<tree>] [--staged] [--worktree] [--] <pathspec>...
git restore [<option>] [--source=<tree>] [--staged] [--worktree] --pathspec-from-file=<file> [--pathspec-file-nul]
git restore (-p|--patch) [<option>] [--source=<tree>] [--staged] [--worktree] [--] [<pathspec>...]
```

## 옵션별 설명

### `-s <tree>`, `--source=<tree>`

- 입력된 work tree의 내용으로 되돌린다.
- `--staged` 옵션 사용때 지정하지 이 옵션을 지정하지 않으면, `HEAD`에서 자동으로 되돌려진다.

### `(-p|--patch)`

- 대화 모드로 파일 변화 분을 되돌린다.

### `(-W|--worktree)`, `(-S|--staged)`

- 되돌리는 위치를 지정한다.
- 옵션이 아무것도 없으면 work tree로 되돌려지며, `--staged`를 지정하면 index만 복원됨.
- 옵션을 둘다 사용하면 둘다 되돌려진다.

### `(-q|--quiet)`

- 메시지 끔.

### `--progress`, `--no-progress`

- stderr로 메시지를 출력한다.
- `--no-progress` 옵션은 `-q`와 같다.

### `--ours`, `--theirs`

- 머지가 되지 않은 위치의 2번째(`ours`), 3번째(`theirs`) 위치의 값으로 되돌림
- 뭔말이지...

### `(-m|--merge)`

- Working tree에서 인덱스로 되돌릴때, 충돌이 발생하면 해당 내용을 머지 커밋으로 만든다.

### `--conflict=<style>`

- `--merge` 옵션 과 비슷하나 상위 계념이다.
- 충돌이 났을대 어떻게 할지에 대해서 정의한다.
- `merge.conflictStyle` 옵션을 덮어쓴다.
- `merge`(기본값), `diff3`으로 지정할 수 있다.

### `--ignore-unmerged`

- 변경 사항이 있어 충돌이 발생했을때, 머지를 진행한다.
- 머지되지 않은건 그대로 둔다.

### `--ignore-skip-worktree-bits`

- 희소 체크아웃 모드(sparse checkout mode)에서 기본값은 `<pathspec>`과 `$GIT_DIR/info/sparse-checkout`에서의 희소 패턴(sparse pattern)에 맞는 항목만 업데이트한다.
- 하지만 이 옵션을 붙이면 희소 패턴(sparse pattern) 값은 무시하고 `<pathspec>`에 존재하는 파일을 무조건 되돌리게 된다.

### `--recurse-submodules`, `--no-recurse-submodules`

- `superproject`에 저장된 커밋으로 sub module이 되돌려진다.

### `--overlay`, `--no-overlay`

- 기본 값은 `--no-overlay`.
- 되돌릴때 수정된 파일을 삭제하지 않는다.

### `--pathspec-from-file=<file>`

- 옵션 내용들을 파일로 입력받는다.
- `-`로 입력되면 stdin으로 받은 값을 옵션으로 받아들인다.
- `LF`, `CR/LF` 로 항목을 구분한다.
- `git-config`[[3]](https://git-scm.com/docs/git-config)에서 `core.quotePath` 항목 값이다.

### `--pathspec-file-nul`

- `NUL` 문자로만 구분을 진행한다.
- 이 옵션은 `--pathspec-from-file` 옵션과 같이 작동한다. 혼자서는 아무것도 안됨

### `--`

- 이후 인수를 옵션으로 읽지 않는다.

### `<pathspec>...`

- [git glossary](https://git-scm.com/docs/gitglossary#Documentation/gitglossary.txt-aiddefpathspecapathspec) 항목으로 대신한다.
