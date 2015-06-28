OpenStack rootwrap
===================

:date: 2015-03-04
:modified: 2015-04-02 21:18
:category: Develop
:tags: openstack, oslo, 오픈스택
:slug: openstack-rootwrap
:summary: OpenStack의 Oslo에는 root권한을 얻긱위한 rootwrap이라는 라이브러리가
          존재한다.

OpenStack 프로젝트들에서 사용되는 것들 중... **root** 와 관련된 작업을
진행해야하는 경우가 있다. 그럴때 사용하려고 만들어둔 rootwrap_

.. _rootwrap: https://wiki.openstack.org/wiki/Rootwrap


Wiki에서는 이 블로그_ 에 작성된 문제를 해결하기 위해서 만들어졌다고 한다.

.. _블로그:
   https://fnords.wordpress.com/2011/11/23/improving-nova-privilege-escalation-model-part-1/


짧은 내기억으로는 간단한 팡리로만 존재했던 것같은데. (아닐 가능성 100%라논
소리...), 지금은 oslo 패키지로 관리되고 있다. `github repo`_

.. _github repo: https://github.com/openstack/oslo.rootwrap


사용자용
~~~~~~~~

``nova.conf`` 에 다음 문구 추가하도록...

::

    rootwrap_config=/etc/nova/rootwrap.conf


배포용 패키지를 만드는 사람용
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Suduers 설정
````````````

``sudoers`` 에 다음 문구를 추가하도록...

::

    nova ALL = (root) NOPASSWD: /usr/bin/nova-rootwrap /etc/nova/rootwrap.conf *


필터 위치 설정 
```````````````

``rootwrap`` 으로 ``Nova-provided`` 필터 파일을 로드하고, ``rootwrap.d`` 로 확장
사용자의 필터 파일을 로드하도록 설정해 줄것.

::

    [DEFAULT]
    filters_path=/etc/nova/rootwrap.d,/usr/share/nova/rootwrap


필터 정의  
``````````

각 노드마다 설치를... 해줘야된다고.


플러그인 작성자용
~~~~~~~~~~~~~~~~~~

새로운 ``run-as-root`` 명령을 추가
`````````````````````````````````````````

root로 동작시킬 것이 있을 경우.

* ``nova.utils.execute(run_as_root=True)`` 를 사용할 것.
* 관련 필터 내용은 ``/etc/nova/rootwrap.d/foobar.filters`` 에 추가해둘 것.


프로젝트 개발자용 
~~~~~~~~~~~~~~~~~~

새로운 ``run-as-root`` 명령을 추가
`````````````````````````````````````````

* ``nova.utils.execute(run_as_root=True)`` 를 사용할 것.
* Nova 코드에서 ``/etc/nova/rootwrap.d/{filter_name}.ilters`` 파일에 관련된 내용을
  추가해줄 것.
  
  - 예로 Compute 노드에서 작동하는 소스라면
    ``/etc/nova/rootwrap.d/compute.filters`` 에다가 추가하도록.


상위 필터 타입 추가
~~~~~~~~~~~~~~~~~~~~

* 기본 필터 타입은 ``CommandFilter`` 임.
* 새로운 타입을 만들거나 지금 존재하는 타입을 확인하고 싶다면 filters.py_ 를
  보면 된다. - `Available Filter Classes`_ 가 아닌걸로도 볼 수 있다.

.. _filters.py:
  https://github.com/openstack/oslo.rootwrap/blob/master/oslo_rootwrap/filters.py
.. _Available Filter Classes:
   https://wiki.openstack.org/wiki/Rootwrap#Available_Filter_classes
