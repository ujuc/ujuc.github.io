Title: git 기본 editor를 VS Code로 변경하기
Date: 2020-06-11 20:27:58
Modified: 2020-06-11 20:27:58
Category: Develop
Tags: git, git editor, vscode, code
Slug: git-gi-bon-editorreur-vs-codero-byeon-gyeong-ha-gi
Summary: Git 커밋을 할때 VIM말고 다른 에디터도 사용할 수 있게 설정하자.

git 처음 설치해서 commit을 하게되면 nano라는 에디터를 만날 수 있다. 이거 잘 쓰는 사람을 본적이 없다.

나오는 방법을 나도 까먹는데...;;

nano가 싫어 vim으로 변경해두길 어언.... 몇년... 이제 그것도 귀찮아져서 VS Code로 변경하려고 한다.

명령은 간단하다.

```shell
git config --global core.editor "code --wait"
```

하게되면 git commit 입력창이 VS code 창으로 뜬다.

![git commit 창 vs code]({static}/img/2020-06-11_git-commit-at-vs-code.png)

이제 Tower 구독 결제가 되어있는지 한번 확인하고 없에야지..

---

**번외**

```shell
git difftool
```

위 명령을 실행하게되면 git diff 를 vimdiff를 이용하여 보여준다.

이것도 아래 명령으로 변경이 가능하다.

```shell
git config --global diff.tool diff-code
git config --global difftool.diff-code.cmd 'code --wait --diff $LOCAL $REMOTE'
```

`tool` 이름이 잘못되면 잘 안나올 수 있으니 편한걸로 바꾸도록 하자.

---

#### 참고

- [VS Code as Git editor](https://code.visualstudio.com/docs/editor/versioncontrol#_vs-code-as-git-editor)
