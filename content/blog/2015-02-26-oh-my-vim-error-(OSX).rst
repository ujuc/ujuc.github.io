oh-my-vim 설치후 오류 (OSX)
============================

:date: 2015-02-26
:modified: 2015-04-01 21:14
:category: Develop
:tags: vim, setting
:slug: oh-my-vim-error-osx
:summary: oh-my-vim 설치하고나면 오류가 난다. 그것때문에 작성한글이다. 혹시나
          동일한 것이 있으면 수정합세...

oh-my-vim_ 으로 vim 플러그인 설정에 관련된 기본 프로그램을 바꿨다 (이것저것
변경하고 있긴하다만...). 달라진게 없다. 좀 더 화려해지고 플러그인들로 인해서
IDE급으로 에디터가 변경됐을 뿐이다. 단지 80라인 와랩이 필요했을뿐인데...

.. _oh-my-vim: https://github.com/liangxianzhe/oh-my-vim

암튼 그렇게 쓰다보니 실행할때마다 에러가 뜬다.

::

    neocomplete does work this version of Vim.
    It requires "if_lua" enabled Vim(7.3.885 or above).

혹시나 해서 검색을 해봤다. 매번 실행할 때마다 엔터 3번은 너무 오래걸려서...

`neocomplete.vim - Vim version and lua`_ 에서는 실행후 `:version` 으로 `lua` 가
`-` 인지 `+` 인지 확인을 하라고 말을 한다.

.. _neocomplete.vim - Vim version and lua:
   https://github.com/Shougo/neocomplete.vim/issues/237

여기서는 `-lua` 면 `lua` 사용 옵션이 빠져있는 것이 되기에 vim 설치시 그에 대한
옵션을 설정해줘야된다는 말을...

OSX 사용자들에게만 나온는 것같은데... Linux에 대한 오류가 없는 걸보면...

암튼 그것을 수정하는 방법은 `brew` 로 설치할때 옵션을 걸어주고 설치하면 된다.
물론 설치했다면, 다시 설치하면된다. 난 삭제하고 다시 설치... (적다보니... 자동화
스크립트에 작성해둔거 변경을 해줘야겠다...)

.. code:: bash

   $ brew install vim --with-cscope --with-lua --override-system-vim

설치해주면된다. 그러면 자연스럽게 넘어가고 에러는 밑으로 나올꺼니 엔터칠 일이
줄었다.!!!
