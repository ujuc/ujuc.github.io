Vim mouse mode
############################

:date: 2015-07-25 13:22
:modified: 2015-08-15 16:00
:category: Develop
:tags: vim, vi, vimrc, mouse, 기본 설정
:slug: vim-mouse-mode
:summary: .vimrc 설정을 하는데 사용했던 "mouse" 명령어에 대한 내용.


나도 vimrc_ 설정을 따로 만들었다만, 그것들을 전부 다른 애들이 설정해놓은 것들에서 수정해서 만든거라. 자세히 매뉴얼을 읽어보고 만들지는 않았다.

그런데 얼마전부터 NeoVim_ 매뉴얼을 번역하면서 기능들을 보고 있는데, 사용하고 있는 것들에대해서 나올때마다 작성을 해놔야지... 안그러면 또 안찾아볼 가능성이 높으니...

마우스와 관련된 옵션은 ``mouse``, ``mousefocus``, ``moushide``, ``mousemodel``, ``mouseshape``, ``mousetime``

옵션 설명(이라쓰고 번역...)
---------------------------------------

mouse_
~~~~~~~~

string (기본값 "a")

마우스를 사용할 수 있도록 설정한다. 터미널에서는 100%. GUI에서 작동하는 것에 대해서 알고 싶으면, | gui-mouse_ | 를 확인하도록.

모드에서 사용하려면 다음 옵션을 달아준다:

* `n <http://neovim.io/doc/user/pattern.html#n>`_: `Normal <http://neovim.io/doc/user/intro.html#Normal>`_ 모드
* `v <http://neovim.io/doc/user/visual.html#v>`_: `Visual <http://neovim.io/doc/user/visual.html#Visual>`_ 모드
* `i <http://neovim.io/doc/user/insert.html#i>`_: `Insert <http://neovim.io/doc/user/insert.html#Insert>`_ 모등
* `c <http://neovim.io/doc/user/change.html#c>`_: `Command-line <http://neovim.io/doc/user/cmdline.html#Command-line>`_ 모드
* `h <http://neovim.io/doc/user/motion.html#h>`_: 도움말 파일에서 수정할때, 모든 모드
* a: 모든 모드
* r: | `hint-enter <http://neovim.io/doc/user/message.html#hit-enter>`_ | 와 | `more-prompt <http://neovim.io/doc/user/message.html#more-prompt>`_ | 프롬프트에서

일반적으로 모든 모드에서 사용하길 원한다면 ``:set mouse=a`` 로 구성해두면 된다.
마우스 모드가 제대로 작동하지 않을땐, `GUI <http://neovim.io/doc/user/gui.html#GUI>`_ modeless 섹션에서 마우스를 사용하고 있어서 빠진게 아닌지 확인을... 아마 텍스트 커서도 안움직인다고...

`mouse-using <http://neovim.io/doc/user/term.html#mouse-using>`_ , `clipboard <http://neovim.io/doc/user/options.html#'clipboard'>`_ 를 보세요.

노트 : X-server로 접근한 터미널에서 마우스를 사용할 땐, 복사, 붙여넣기를 사용할땐 "* `register <http://neovim.io/doc/user/sponsor.html#register>`_ 를 사용하게 됩니다. 마우스 버튼을 ``xterm``  에서 사용하려면, `shift <http://neovim.io/doc/user/intro.html#shift>`_ 를 누르고 사용하면 됩니다. 자세한건 `clipboard <http://neovim.io/doc/user/options.html#'clipboard'>`_ 옵션에서 확인하세요.

mousefocus_
~~~~~~~~~~~~~

'mousef'  boolean (기본은 off) - {GUI 에서만 작동}

`window <http://neovim.io/doc/user/windows.html#window>`_ 에서 마우스 포인터를 자동으로 활성화 시킬 수 있습니다. 윈도우 레이아웃이나 다른 방법으로 윈도우 초점을 변경(`changing <http://neovim.io/doc/user/change.html#changing>`_) 하려한다면, 마우스 포인터는 윈도우에서 이동하게된다는데...
딱히 GUI로 할일은 없음...

mousehide_
~~~~~~~~~~~~

'mh'  boolean (기본은 on) - {GUI에서만 작동}

입력할때 마우스 포인터를 감추고, 마우스가 움직이면 그때사 보여줌.

mousemodel_
~~~~~~~~~~~~

'mousem'  string (기본은 "extend", `Win32 <http://neovim.io/doc/user/os_win32.html#Win32>`_ 에서는 "popup")

마우스를 사용하는 모델을 설정한다. 마우스 오른쪽 키를 눌렸을때 뭘할지에 대해서 설정하는 것.

* extend: 마우스 오른쪽 키를 누르면 섹션이 확장됩니다. ``xterm`` 에서의 내용과 동일하게 동작함.
* popup: 마우스 오른쪽 키를 누르면 팝업 메뉴가 뜸. 마우스 왼쪽키를 누르고 있으면, 섹션을 확장 합니다. MS Windows의 작업과 동일함.
* popup_setpos: "popup"과 유사. 커서가 마우스 클릭된 곳으로 움직임. 자세한건 한번 읽어보는 걸로.

설정별 마우스 동작

+------------------+---------------------+---------------------------+
| mouse            | extend              | popup(_setpost)           |
+==================+=====================+===========================+
|왼쪽 클릭         | 커서 위치           | 커서 위치                 |
+------------------+---------------------+---------------------------+
|왼쪽 끌기         | 섹션 시작           | 섹션 시작                 |
+------------------+---------------------+---------------------------+
|시프트 - 왼쪽     | `word`_ 검색        | 섹션 확장                 |
+------------------+---------------------+---------------------------+
|오른쪽 클릭       | 섹션 확장           | popup 메뉴 (커서 위치)    |
+------------------+---------------------+---------------------------+
|오른쪽 끌기       | 섹션 확장           |                           |
+------------------+---------------------+---------------------------+
|가운데 키         | 붙이기              | 붙이기                    |
+------------------+---------------------+---------------------------+

"popup" 모델에서는 pop-up 메뉴를 구성할 수 있음. | `popup-menu <http://neovim.io/doc/user/gui.html#popup-menu>`_ | 에서 확인할 것.

마우스 버튼 맵핑을 바꿀려면 | `gui-mouse-mapping <http://neovim.io/doc/user/gui.html#gui-mouse-mapping>`_ | 확인. modeless 섹션에서는 작동 안함.

'mousemodel_' 옵션은 `:behave <http://neovim.io/doc/user/gui.html#:behave>`_ 명령어로 설정할 수 있음.

mouseshape_
~~~~~~~~~~~~~

'mouses'  string (기본은 "i:beam,r:beam,s:updown,sd:corss,m:no,ml:up-arrow,v:rightup-arrow") - {| `+mouseshape <http://neovim.io/doc/user/various.html#+mouseshape>`_ | 기능이 켜진채로 컴파일이 되었을 경우, 사용 가능}

다른 모드에서 마우스 포인터가 작동하는 것에대한 것들을 VIM에게 알려주는 옵션(?).

적용할 수 있는 모드 목록:
  일반 윈도우:
    `n <http://neovim.io/doc/user/pattern.html#n>`_
      `Normal <http://neovim.io/doc/user/intro.html#Normal>`_ 모드
    `v <http://neovim.io/doc/user/visual.html#v>`_
      `Visual <http://neovim.io/doc/user/visual.html#Visual>`_ 모드
    ve
      '`selection <http://neovim.io/doc/user/options.html#'selection'>`_' "`exclusive <http://neovim.io/doc/user/motion.html#exclusive>`_"가 포함된 `Visual <http://neovim.io/doc/user/visual.html#Visual>`_ 모드 (특정짓지 않은 거라면, `as <http://neovim.io/doc/user/motion.html#as>`_ '`v <http://neovim.io/doc/user/visual.html#v>`_'와 동일)
    `o <http://neovim.io/doc/user/insert.html#o>`_
      `Operator-pending <http://neovim.io/doc/user/intro.html#Operator-pending>`_ 모드
    `i <http://neovim.io/doc/user/insert.html#i>`_
      `Insert <http://neovim.io/doc/user/insert.html#Insert>`_ 모드
    `r <http://neovim.io/doc/user/change.html#r>`_
      `Replace <http://neovim.io/doc/user/insert.html#Replace>`_ 모드
  나머지:
    `c <http://neovim.io/doc/user/change.html#c>`_
      커멘드 라인에서 추가
    ci
      커멘드 라인에서 삽입(`inserting <http://neovim.io/doc/user/insert.html#inserting>`_)
    cr
      커멘드 라인에서 변경(`replacing <http://neovim.io/doc/user/change.html#replacing>`_)
    `m <http://neovim.io/doc/user/motion.html#m>`_
      'HIT ENTER'나 'More' 프롬프트에서
    ml
      idem, 마지막 줄에 커서일 경우
    `e <http://neovim.io/doc/user/motion.html#e>`_
      어떤 모드든, 포인터에 마지막 `window <http://neovim.io/doc/user/windows.html#window>`_
    `s <http://neovim.io/doc/user/change.html#s>`_
      어떤 모드든, 상태 라인 위에 포인터
    sd
      어떤 모드든, 상태 라인으로 드래그
    vs
      어떤 모드든, 수직 분할 라인에 포인터
    vd
      어떤 모드든, 수직 분할 라인으로 드래그
    a
      어디든...

마우스 모양(shape)는 다음 모양으로 보여짐

+-------+---------------+--------------------------------------------------------------+
| avail | 이름          | 뭐냐면...                                                    |
+=======+===============+==============================================================+
| w_ x_ | arrow         | 기본(Normal_) 마우스 포인터                                  |
+-------+---------------+--------------------------------------------------------------+
| w_ x_ | blank         | 모든 곳에서 포인터가 아닌경우 (사용시 주의!)                 |
+-------+---------------+--------------------------------------------------------------+
| w_ x_ | beam          | I-빔                                                         |
+-------+---------------+--------------------------------------------------------------+
| w_ x_ | updown        | 상하 크기 조절 화살표                                        |
+-------+---------------+--------------------------------------------------------------+
| w_ x_ | leftright     | 좌우 크기 조절 화살표                                        |
+-------+---------------+--------------------------------------------------------------+
| w_ x_ | busy          | 시스템에서 사용하는 busy 포인터                              |
+-------+---------------+--------------------------------------------------------------+
| w_ x_ | no            | 시스템에서 사용하는 'no input' 포인터                        |
+-------+---------------+--------------------------------------------------------------+
| x_    | udsizing      | 상하 크기 재조절을 가르킴                                    |
+-------+---------------+--------------------------------------------------------------+
| x_    | lrsizing      | 좌우 크기 재조절를 가르킴                                    |
+-------+---------------+--------------------------------------------------------------+
| x_    | crosshair     | 큰 '+'                                                       |
+-------+---------------+--------------------------------------------------------------+
| x_    | hand1         | 검은색 손                                                    |
+-------+---------------+--------------------------------------------------------------+
| x_    | hand2         | 흰색 손                                                      |
+-------+---------------+--------------------------------------------------------------+
| x_    | pencil        | 뭘 쓰고 싶을때                                               |
+-------+---------------+--------------------------------------------------------------+
| x_    | question      | 큰 '?'                                                       |
+-------+---------------+--------------------------------------------------------------+
| x_    | rightup-arrow | 오른쪽 위를 가르키는 화살표                                  |
+-------+---------------+--------------------------------------------------------------+
| w_ x_ | up-arrow      | 위를 가르키는 화살표                                         |
+-------+---------------+--------------------------------------------------------------+
| x_    | <number>      | 모든 X11 포인트 숫자 (``X11/cursorfont.h`` 에서 확인 가능)   |
+-------+---------------+--------------------------------------------------------------+

.. _w: http://neovim.io/doc/user/motion.html#w
.. _x: http://neovim.io/doc/user/change.html#x
.. _Normal: http://neovim.io/doc/user/intro.html#Normal

"avail" 칼럼의 내용에서 'w_' 의 경우 `Win32 <http://neovim.io/doc/user/os_win32.html#Win32>`_ 에서 사용하는 것이고, 'x_' 는 X11에서 사용하는 것에 대한 것임.
Any modes not specified or shapes not available use the normal mouse pointer. - 영어의 짧음으로 뭔말인지 모르겠다.

예로 ``:set mouseshape=s:udsizing,m:mo`` 요로케 작성가능. 이렇게 해놓으면, (클릭이후 마우스가 이상태에서 효과가 없으면,)상태 바에 마오스를 올리면 크기 조절 화살표로 변경되고, 화면에서 `hit-enter <http://neovim.io/doc/user/message.html#hit-enter>`_ 프롬프트일때 no input을 가르키게됩니다.


mousetime_
~~~~~~~~~~~~

'mouset'  number (기본 500)

GUI, MS-DOS, Win32, Unix의 ``xterm`` 에서만 사용 가능. 다중 클릭으로 인식할 수 있는 두 번째 클릭에 대한 msec의 최대 값을 정의함.


.. _vimrc: http://github.com/ujuc/dotrc
.. _NeoVim: http://neovim.io
.. _mouse: http://neovim.io/doc/user/options.html#'mouse'
.. _gui-mouse: http://neovim.io/doc/user/gui.html#gui-mouse
.. _mousefocus: http://neovim.io/doc/user/options.html#'mousefocus'
.. _mousehide: http://neovim.io/doc/user/options.html#'mousehide'
.. _word: http://neovim.io/doc/user/motion.html#word
.. _mousemodel: http://neovim.io/doc/user/options.html#'mousemodel'
.. _mouseshape: http://neovim.io/doc/user/options.html#'mouseshape'
.. _mousetime: http://neovim.io/doc/user/options.html#'mousetime'
