Title: `_vim_files: function definition files net found` on zsh
Date: 2016-01-16 22:53
Category: Develop
Tags: dev, zsh, vim
Slug: vim_files:-function-definition-files-net-found-on-zsh
Summary: zsh이 올라가고 난뒤에 vim도 같이 올라갔더니 에러를 뿝네...

아... 오랜만에 vim으로 작업을 하려고 탭을 두번 클릭했더니 아래와 같은 에러가 뜬다. 이넘을 어떻게 해야되지.

![error!]({static}/img/2016-01-16_error.png)

### 원인
`zcompdump` 때문이라고 하고, 이건 매번 문제가 있나보다.ㅡ.ㅡ;;

[github/robbyrusell/oh-my-zsh/issues/518](https://github.com/robbyrussell/oh-my-zsh/issues/518)

### 해결방법

`rm ~/.zcompdump`를 삭제하면 된다고...
그리고 꼭 하고 난뒤에 `exec zsh`를 하도록 하자.
