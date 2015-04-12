Uubntu에서 Nabi 툴바를 tray에 넣기
#####################################

:date: 2014-11-09 00:44
:modified: 2015-04-12 14:12
:category: software
:tags: linux, ubuntu, nabi, setting
:slug: nabi-toolbar-in-tray-on-ubuntu
:summary: Ubuntu에서 nabi를 입력기로 사용한다. 그런데 언제부터인가. tray로
		  들어가지 않는 문제가 발생했다. 거의 업데이트가 안되고 있어서
		  그런것같기도 하지만, 그것에 대한 내용이다.


오랜만에 Ubuntu를 설치하고 `ibus` 가 조금 불편할뻔하다가... 
쓰던거 쓰자해서 `nabi` 를 설치했는데.. 이놈의 tray에 들어갈려고 하지 않는다.

그래서 조금 검색을 했더니...
`gsettings get com.canonical.Unity.Panel systray-whitelist` 라는 걸로 추가를
해줘야한다고 하는데... 이넘은 14.10에는 없다. 조금더 찾아보니, 13.04부터는 아예
빠져있었다.

다시 검색어를 `systray-whitelist` 로 검색중 **Web UPD8** 에 올라온 글을 확인.

`How to whitelist systray apps in ubuntu 14.04 or 14.10(W/unity)`_

.. _How to whitelist systray apps in ubuntu 14.04 or 14.10(W/unity):
   http://www.webupd8.org/2013/05/how-to-get-systray-whitelist-back-in.html

* 나같은 겨웅에는  14.10을 설치했으니.

.. code:: bash

   sudo apt-add-repository ppa:guran/systray-utopic
   sudo apt-get update; sudo apt-get upgrade

그리고 `Alt + F2` 를 눌러 `unity` 를 찾아 클릭해주면 알아서 unity가 재시작되면서
nabi가 트레이에 들어가게 된다.

* 덧. 아래에보면 관련 ppa를 삭제하는 방법이 나오는데 따로 패키지를 설치할
  필요없이 아래의 명령어로 삭제가 가능하다.

.. code:: bash

   sudo apt-add-repository -r ppa:guran/systray-utopic
   sudo apt-get update; sudo apt-get autoremove

