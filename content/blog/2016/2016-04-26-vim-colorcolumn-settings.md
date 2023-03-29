Title: Vim ColorColumn Settings
Date: 2016-04-26 22:04
Category: Develop
Tags: vim, vimrc, colorcolumn, cc
Slug: vim-colorcolumn-settings
Summary: vim에서 코드의 길이를 줄을 그어 쉽게 확인하자.

나같은 경우엔, `git commit` 명령어를 실행하면 기본 에디터로 `vim`으로 구성해뒀다.
그러다보니 가끔 길이를 확인해서 커밋을 해야되는 경우가 발생하는데...

그나마 기본적으로 설정해놓은 80줄은 쉽게 찾으나... 커밋 제목인 50자, 커밋 메시지
제한인 72자를 확인하는게 쉽지가 않아서 줄을 그어놓고 사용하기위해 설정을 한다.

    :::
    set cc=51,73,81,121
    highlight ColorColumn ctermbg=17 guibg=navyblue

위와 같이 설정하면 아래와 같이 줄이 그어져있는 모습을 볼 수 있다.

![vim_ex]({static}/img/2016-04-26_vim.png)

이건 덤...

vim에서 사용하는 색이름과 설정값에 대해서 확인할 수 있다.

[Xterm256 color names for console Vim](http://vim.wikia.com/wiki/Xterm256_color_names_for_console_Vim)
