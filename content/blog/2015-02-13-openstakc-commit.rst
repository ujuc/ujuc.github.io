OpenStack Commit
================

:date:      2015-02-13
:modified:  2015-03-31 22:29
:category:  Develop
:tags:      OpenStack, commit
:slug:      openstack-commit
:summary:   OpenStack 커밋에 대한 내용. 이번에 커멋히면서 정리한 글.

기본적인 흐름은 `Developer's Guide`_ 를 보고서 따라하면 쉽게 작업을 할 수 있다.
그런데.... 왜이리 어려운거지....

.. _Developer's Guide: http://docs.openstack.org/infra/manual/developers.html

.. |code review| image:: http://docs.openstack.org/infra/manual/_images/code_review.png

신경 써야될 곳은 파란색으로 되어있는 곳만 신경 쓰면되는 그런... 어렵지 않을
것같아 시작...


준비 해야될 것
-----------------

#. Launchpad_ 계정

   * 버그리포팅을 위해서는 Launchpad 계정이 있어야한다.
   * 그리고 왠만한 OpenID를 이걸로 다 할 수 있다.

#. `OpenStack Review`_ 가입

   * 리뷰를 무조건 타야된다...
   * 그러니 만들어야....
   * 그리고 ssh key등록을 해두는게...
   * 그리고 메일링은 꺼두는게... 너무 많이와...

.. _Launchpad: https://launchpad.net/+login
.. _OpenStack Review: https://review.openstack.org


Individual Contributor License Agreement 결재
-------------------------------------------------------

#. `Individual Contributor License Agreement`_ 간단하게 작성하고..

#. 회사 대신 기여하거나 단체로 한다면 `Corporate Contributor License Agreement`_
   도 한장... 작성하고 보니 난 이걸 왜했지...

.. _Individual Contributor License Agreement: https://review.openstack.org/#/settings/agreements
.. _Corporate Contributor License Agreement:  https://secure.echosign.com/public/hostedForm?formid=56JUVGT95E78X5


`git-review` 설치
-------------------

* 맥은 그냥 `brew` 로 통일시켜서 설치하는게 편한듯...
* 문서상으로는 `pip` 로 설치하라고 했지만...
* 설치하고 제대로 됐는지 확인을 하기위해서는

  - 하나를 클론하고
  - `git review -s` 를 해서 `review.openstack.org` 에 제대로 접속했는지를 체크를
    해준다.
  - 이때 `gitreview.username` 을 `.gitconfig` 파일에 작성해두지 않았다면
    설정하라고 뜸.


작업 플로워
-----------

버그일 경우
~~~~~~~~~~~

* 우선 `bugs.launchpad.net/<projectname>` 으로 접속하여 버그 리포팅.

  - 이때 4가지로 테스크가 나뉘는데,

    #. 새로운 버그 확인: "New"로 표기된 버그를 "Confirmed"로 변경 가능한 상태.
       거의 초기를 말한다고 보면됨.
    #. 버그 수정 : 버그를 할당하고, "In Progress"로 등록.
    #. 리뷰중 : "Incomplete"로 표기되고 리뷰가 진행되는 상태를 말함. 최대
       4주까지 걸린다고 함.
    #. 버그가 또다시 발견된 경우 : 그렇다고함... (뭐라말하기가... 그냥 나같은
       경우엔 리오픈으로 적고 프로세스 해버림...)

* 커밋할때 버그 진행상태를 남겨둘 수 있음. 자세한건 `Including external
  references`_ 를 보면됨.

.. _Including external references:
   https://wiki.openstack.org/wiki/GitCommitMessages#Including_external_references


청사진으로 새로운 기능을 붙일 경우
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* 이건 그냥 `Blueprints - wiki`_ 를 보자.
* 관심 없고, 내가 딱히 추가할 내용도 별로 없어서... 우선은.. 빈칸...

.. _Blueprints - wiki: https://wiki.openstack.org/wiki/Blueprints


변경을 시작해볼까~~~
~~~~~~~~~~~~~~~~~~~~

* 첫 클론을 떠온거라면 상관없지만... 뜬지 꽤됐으면 업스트림이랑 코드를 맞춰줘야
  된다.

  - 안하면 일 두번하는 생긴다... OTL
  - 내가 이글을 쓰고 있는 이유기도 하다...

.. code:: bash

   $ git remote update
   $ git checkout master
   $ git pull --ff-only origin master

* 그리고 브런치를 따는데, Blueprint는 `bp/<blueprint_name>`, Bug는
  `bug/<bug-number>` 로 따주면된다.

.. code:: bash

   git checkout -b TOPIC-BRANCH


변경 사항 커밋
~~~~~~~~~~~~~~

* 제목은 50자 이내로 작성하고, 한줄 띄우고 내용을 작성해줘야된다. 
* 자세한 내용은 `Git commit messages`_ 참고.
  
.. _Git commit messages: https://wiki.openstack.org/wiki/GitCommitMessages

.. code:: text
   
   summary

   brrrrrrbrrrrrra
   
   <if blueprint>
   Implements: blueprint <blueprint_name>
   <if bug>
   Closes-Bug: #<bug_number>

* `Change-id` 는 `git review` 로 올린뒤에 알아서 붙여주는거라 따로 적을 필요는
  없다.
* 리뷰에 반려가되어서 다시 커밋을 해야되는 경우에는 `git commit --amend`
  오셤으로 해주면된다. 짧게 쓰면 `git commit -a`.

리뷰 등록 
~~~~~~~~~

* `git reivew` 로 하면 `review.openstack.org` 에 올라가 있는 것을 확인할 수
  있다.


변경사항이 있을때 
~~~~~~~~~~~~~~~~~

* 커밋 메시지에 `Change-Id` 가없을때는 붙여넣기 해준 다음 `--amend` 로 커밋.


나머지 자세한 것들은 `Developer's Guide`_ 를 확인하도록하자. 이것도 뭐... 내가
까먹으니까 작성한 것이기도하지만...
