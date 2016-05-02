Title: Select text of vim with set mouse=a enabled
Date: 2016-05-02 23:27
Category: Software
Tags: vim, mouse, copy
Slug: select-text-of-vim-with-set-mouse=a-enabled
Summary: Vim사용에 있어서 마우스로 블록을 선택할 수 있도록 하였다. 그랬더니 다른 부분에서 
제대로된 선택을 할 수 없어 해당 내용을 찾아보았다.

조금 쉽게 사용하려고 vim에 `mouse=a` 설정을 하였다. 그것이 원흉이 었지만. 결국 찾았다!

[Copy text out of vim with set mouse=a enabled](http://stackoverflow.com/questions/4608161/copy-text-out-of-vim-with-set-mouse-a-enabled)

리눅스에서는 `shift`를 누르고 선택하는것이고, Mac에서는 `alt/option`을 누르고 선택하면 된다.

설정하나때문에 많은 삽질을 하는 사람들에게 남겨둠..
그런데 설정은 tmux에서도 사용이가능하다.
