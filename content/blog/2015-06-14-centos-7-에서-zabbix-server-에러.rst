CentOS 7 에서 zabbix-server 에러
############################################

:date: 2015-06-14 22:30
:category: Develop
:tags: zabbix, centos
:slug: centos-7-에서-zabbix-server-에러
:summary: 숙제를 늦게하고 있는데 잘안되서 찾다보니...

2주전에 받은 숙제인데, 회사일이 바빠서 못하고 있다가 조금 시간이 있어서 설정하고 있는데.

CentOS 7에다가 Zabbix를 올리고있다. VM에서 4시간동안 서비스가 제대로 안돌아서, 내 설정이 잘못되었나 하여, 설치하는 메뉴얼도 바꿔서 확인을 했는데도 안되길레 혹시나 로그에는 있나하여 들어갔더니 `journal` 로 보여지는 것 말고도 `/var/log/zabbix` 가 보여서 확인했더니..

.. code::

    using configuration file: /etc/zabbix/zabbix_server.conf
    current database version (mandatory/optional): 02040000/02040000
    required mandatory version: 02040000
    listener failed: zbx_tcp_listen() fatal error: unable to serve on any address [[-]:10051]
    Got signal [signal:11(SIGSEGV),reason:1,refaddr:0x18]. Crashing ...

음? 서버를 못찾는다고..?? 뭔 말이지. 그래서 그냥 통짜로 복사 붙여넣기. 구글에서 말하는 것들이 많은데 그 중에서 일본사람이 작성한 글. `CentOS7.1 で zabbix-serverの起動が失敗する話とその解決方法`_ 에서는 CV#-2014-0092는... gnutls에 패치가되었는데.. CVE-2014-8564는 적용이 안되서 그부분에 대한 내용을 추가하던지 수정을 해야된다고 한다.

.. _CentOS7.1 で zabbix-serverの起動が失敗する話とその解決方法: http://qiita.com/_BSmile_/items/61932e45de5330190027

자세한건 구글 번역기로 사이트를 돌려서 보도록하자. 그렇다보니 여기서 추천하는 방법은 `trousers` 를 업데이트 하는 방법을 추천하고 있다.

.. code::

    $ sudo rpm -Uvh https://kojipkgs.fedoraproject.org/packages/trousers/0.3.11.2/3.fc20/x86_64/trousers-0.3.11.2-3.fc20.x86_64.rpm
    Retrieving https://kojipkgs.fedoraproject.org/packages/trousers/0.3.11.2/3.fc20/x86_64/trousers-0.3.11.2-3.fc20.x86_64.rpm
    Preparing...                          ################################# [100%]
    Updating / installing...
    1:trousers-0.3.11.2-3.fc20         ################################# [ 50%]
    Cleaning up / removing...
    2:trousers-0.3.11.2-3.el7          ################################# [100%

    $ sodu systemctl start zabbix-server

작동되는 것을 확인할 수 있다.

이 글은 **CentOS 7.1.1503** 버전, **Zabbix 2.4.5** 버전에서 확인되었고 테스트되었다. 이후 버전에서는 관련 버그가 잡히길.
