Edison 초기 설정
###################

:date: 2015-05-13 22:46
:category: Develop
:tags: edison, 개발, embedded, 임베디드, intel, iot
:slug: edison-초기-설정
:summary: Edison을 사용하는데 있어서 초기에 설정하는 부분으로 구성을 한다.


Yocta Project Update
====================

* 무엇이든 처음 설정할때는 기본 OS먼저 업데이트를 해줘야된다. 최신 Yocta Project
  파일을 받아서 설치해준다.
* 최신이 아니라면 몇몇 기능이 제대로 되지 않아 다시 설치해줘야될 수 도 있으니 꼭
  하도록하자.
* 컴파일을 진행해도 된다만, 시간이 많거나, 꼭 필요한 패키지가 없거나, 기본적으로
  설정을 변경해주어야 할때빼고는 하지말자.
* `Yocta 컴파일 이미지 다운로드`_

.. _Yocta 컴파일 이미지 다운로드:
   http://www.intel.com/support/edison/sb/CS-035180.htm


`플래싱 순서`_
-----------------

.. |USB 연결| image::
    https://lh3.googleusercontent.com/tSEF4jbQq5fN_VuqzLndcXa6YfOWRh9iWj7pjuSBU-T148EgyENW6moTDRdOJ8oo3EV8RyM5FludcqenhTzxjNDcMNDx-QRJlCE-0uF0-Q5k2jv099_-6v7C8xJ92P-2u3aoX9M

#. 위의 사진대로 USB를 연결해주고 (2번에 연결)
#. Edison 외장디스크가 깨끗한지 확인한다.
   * 만약 이전의 이미지 내용이 있다면, ``rm -rf Edison/\.*`` 를 이용하여 모든 내용을 삭제한 다음 받은 이미지를 올리면 된다.
   * Edison 파티션의 정보를 확인하여 포멧이 FAT16이라면 디스크 유틸에서 포맷하여 FAT32로 변경해주도록.
#. 다운 받은걸 복사하자.
#. 시리얼 통신으로 Edison에 접근한다.
   * ``screen /dev/cu.usbserial-A**** 115200 -L``
   * ``subserial`` 로 접근을 하면되는데 A뒤의 이름은 변경될 수 있어 작성하지 않았다.
#. 아무런 내용이 안나온다면 들어간 것이니, 엔터 두번.
#. 로그인후 `reboot ota` 명령어로 재시작.
   * `ota` 로 할 경우, 부팅때 Edison 외장하드에 넣어둔 부팅 이미지들로 새롭게 씌우고 관련 내용들을 업데이트하여 사용할 수 있도록 되어있다.
#. 자세한 내용은 제목에 연결된 링크로 가서 확인하고 작업을 진행한다.

.. _플래싱 순서:
   https://software.intel.com/en-us/articles/intel-edison-flashing-firmware-on-os-x-wired


Edison 구성
============

* 기본 구성을 하는데 필요한 명령어는 ``configure_edison`` 으로 작업을 구성하도록
  한다.
* 전체 설정을 다 변경하고 싶으면 ``configure_edison --setup`` 이다.


Hostname
------------

.. code:: bash

   # configure_edison --name


* 다음에 나오는 것들에따라서 입력해주면 된다.


Wifi
-----

.. code:: bash

   # configure_edison --wifi


* 근처에 있는 Wifi들이 다 잡힐 것이나 만약 아무것도 안보인다면 firmware를 업그레
  이드 한 뒤에 다시 명령어를 입력하여 확인하도록하자.
* 버전업이 안되어있는 경우, 잡지 못하더라.
* 설정이 완료되고 나면 URL을 보여주니 그것을 이용하여 접근하면 된다.


SSH 설정
---------

* Screen으로 시리얼 접근하는 것은 사용하기가 불편하다.
* 비밀번호를 설정해주게되면 SSH로 접근이 가능하게 되니 그부분을 추가하여 작업을
  진행하도록 한다.

.. code:: bash

   # configure_edison --password



Package 관리자
===================

* Edison은 opkg(OpenPackaGe Managemet)라는 비교적 가벼운 패키지 관리자를 사용한
  다고 한다. 몇몇 설정이 그렇게 되어있었다. (Yocta Projectdp서 사용하는데,
  OpenWRT에서 사용하고 있다.)


패키지 관리자 설치 및 설정
---------------------------------

* `Intel page`_

.. _Intel page:
   https://software.intel.com/en-us/articles/managing-devkit-libraries-intel-edison-or-intel-galileo-board

.. code:: bash

   # echo "src intel-iotdk http://iotdk.intel.com/repos/1.1/intelgalactic" > \
       /etc/opkg/intel-iotdk.conf# opkg update; opkg upgrade
   # opkg update; opkg upgrade


* 이렇게하면 기본적인 것들은 추가가 된다만 패키지가 많지는 않다.
* 더 많은 패키지를 사용하려면 레포지토리를 추가해줘야 된다.

.. code:: bash

   # vi /etc/opkg/base-feeds.conf

   src/gz all http://repo.opkg.net/edison/repo/all
   src/gz edison http://repo.opkg.net/edison/repo/edison
   src/gz core2-32 http://repo.opkg.net/edison/repo/core2-32

   # opkg update
