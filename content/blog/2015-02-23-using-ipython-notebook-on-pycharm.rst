Pycharm에서 iPython notebook 사용
=================================

:date: 2015-02-23
:modified: 2015-04-01 21:07
:category: Develop
:tags: Pycharm, iPython, notebook
:slug: using-ipython-notebook-on-pycharm
:summary: Pycharm이 4.0으로 판올림되면서 iPython notebook을 사용할 수 있도록
          되었다. 아직 불편한감이 없지않아 있음.

Pycharm iPython notebook 지원은 4.0에서부터 지원하기 시작했다. 아직 버전업이
안됐으니 작년인듯...

iPython을 설치하고 Pycharm에서 설치하려고 봤더니 제대로 돌아가질 않는다.
그렇다고 오류가 보이지도 않아서 직접 터미널에서 쳤더니...

**패키지가 없어서 안된다!!!** 라는 비명을 볼 수 있었다.

설치해줘야되는 패키지는 ``pyzmq``, ``tornado``, (``certifi`` 는 ``torando`` 설치시 같이
설치가되니 넘어간다.). 편한 방법으로 설치해주고 작동시키면 돌아가는 것을 확인할
수 있다만...

Pycharm의 iPython notebook 입력기 UI가 너무 안좋다. 그냥 서버를 띄우고 Web에서
작동하는 것이 입력하기도 쉽고 값들을 확인하면서 작성하기가 더 쉽게 되어있으니
사용자가 알아서... 나는 안쓸꺼임...

아마 업데이트 하면... 괜찮아질꺼야... 그럴꺼야...
