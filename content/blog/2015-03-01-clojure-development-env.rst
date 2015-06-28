Clojure 개발 환경 구축
=======================

:date: 2015-03-01
:modified: 2015-04-01 21:30
:category: Develop
:tags: clojure, 개발 환경, lein
:slug: clojure-development-env
:summary: Clojure 개발 환경 구축... `#이상한 모임`_ 에서 웹 작업을 진행하는데
          있어서... 내가 불편하여...

.. _#이상한 모임: https://www.facebook.com/weweirdmeetup


1. 개요
--------

Clojure를 공부하려하는데... 이것 저것 작업을 하려하니 짧은 기억력으로는 계속
봐야되는지라. 이렇게 작성을 해놔야 나중에 볼 듯하고, 또 어딘가에 넣어둔다고해도
찾을때는 잘 못찾는 지라...

1. 전재
~~~~~~~

OSX를 기반으로 한다. ``brew`` 를 패키지로 모두 작성된다. 만약 Linux에서
작업하게되면 관련해서 문서는 추가로 작성할 예정임. 문제는 언제될지 모르겠다.

2. 설치할 것들
---------------

1. JDK 설치
~~~~~~~~~~~~

* 검색해서 JDK를 다운받으면 된다.
* Apple에서 기본적으로 주는걸 써도 될 듯.
* 8으로 설치했는데 작업하는데는 아무런 이상없다.
* 그래서 그냥 쓴다.
* 그리고 ``brew-cask`` 에 JDK가 있다는...

2. Leiningen 설치
------------------

* ``brew install leiningen`` 으로 설치.
* 딱히 설정할 것 없음.

3. lein 사용
------------

* 이거 쓸려고 넘많이 적었다...

.. code:: bash

    $ lein
	Leiningen is a tool for working with Clojure projects.

	Several tasks are available:
	change              Rewrite project.clj by applying a function.
	check               Check syntax and warn on reflection.
	classpath           Print the classpath of the current project.
	clean               Remove all files from project's target-path.
	compile             Compile Clojure source into .class files.
	deploy              Build and deploy jar to remote repository.
	deps                Download all dependencies.
	do                  Higher-order task to perform other tasks in succession.
	help                Display a list of tasks or help for a given task.
	install             Install the current project to the local repository.
	jar                 Package up all the project's files into a jar file.
	javac               Compile Java source files.
	new                 Generate project scaffolding based on a template.
	plugin              DEPRECATED. Please use the :user profile instead.
	pom                 Write a pom.xml file to disk for Maven interoperability.
	release             Perform :release-tasks.
	repl                Start a repl session either with the current project or standalone.
	retest              Run only the test namespaces which failed last time around.
	run                 Run a -main function with optional command-line arguments.
	search              Search remote maven repositories for matching jars.
	show-profiles       List all available profiles or display one if given an argument.
	test                Run the project's tests.
	trampoline          Run a task without nesting the project's JVM inside Leiningen's.
	uberjar             Package up the project files and dependencies into a jar file.
	update-in           Perform arbitrary transformations on your project map.
	upgrade             Upgrade Leiningen to specified version or latest stable.
	vcs                 Interact with the version control system.
	version             Print version for Leiningen and the current JVM.
	with-profile        Apply the given task with the profile(s) specified.

	Run `lein help $TASK` for details.

	Global Options:
	  -o             Run a task offline.
	  -U             Run a task after forcing update of snapshots.
	  -h, --help     Print this help or help for a specific task.
	  -v, --version  Print Leiningen's version.

	See also: readme, faq, tutorial, news, sample, profiles, deploying, gpg,
	mixed-source, templates, and copying.
    

1. project 생성
~~~~~~~~~~~~~~~

.. code:: bash

   lein new myproject

* ``project.clj`` 에 프로젝트에 관련된 내용들을 작성한다.
  
  - 필요한 것들이 있다면 여기다가 차곡차곡 넣어준다.
  - 그리고 이곳에 ``main`` 으로 사용할 코드의 위치를 작성해 줘야된다.

    + 키워드는 ``:main`` 이다.


2. 의존하는 라이브러리 다운로드
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   lein deps

위에서 작성해준 패키지들을 받아와서 실행해준다. 그러니 왠만해서는 설치하고 하자.

3. 코드 작성
~~~~~~~~~~~~

``src/myproject/core.clj`` 가 있다. 이곳에다가 코드를 작성해주면 된다.


4. 실행
~~~~~~~~

.. code:: bash

   lein run

쉽게 실행해서 나오는 것을 볼 수 있다. 뭐 간단하네...


5. 패키징
~~~~~~~~~

역시 Java라고 해야될까... jar 로 만들어두면 멀티 플랫폼에서도 작동이 가능하다는 
것이지. 그리고 그것을 묶어서 보여준다. 나중에가서 설정을 좀 해줘야되는 부분이 
발생하겠지만, 지금은 그렇게까지는 나올 필요가 없으니...

.. code:: bash

   lein uberjar


6. 라이브러리 검색
~~~~~~~~~~~~~~~~~~

필요한 라이브러리들을 검색 하는건데... 검색하는게 더 빠를듯... 너무 많이
나온다. 그리고 가끔 인덱스를 업데이트를 해주긴 해야되는데... 오래걸려... 
너무 오래...

.. code:: bash

  lein search ring


불편하게... 페이지별로 나오니. 이름은 정확히 입력하자. 그리고 동일한 페키지
이름으로 버전들이 쭉~~ 나오니 그것도하나 염두해둘 것... 버전 정보는 명령어를
하나더 쳐서 확인하게 해야지... 저렇게 다 보여줄 필요가 있나...


7. 패치 설정
~~~~~~~~~~~~

자동으로 잡아준다. 그래도 추가해야된다면 ``proejct.clj`` 에 키워드
``:extra-classpath-dirs`` 를 사용하여 리스트 형식으로 추가해주면 된다.


8. 인터프리터 실행
~~~~~~~~~~~~~~~~~~

인터프리터를 실행해서 작성한 내요이 맞는지 확인이 가능하다.

.. code:: bash

   lein repl


참고 사이트!
-------------

`Clojure 강좌 - 김영태`_
    emacs로 되어있는 부부만 제외했...

.. _Clojure 강좌 - 김영태: http://english4u.kr/clojure-memo/index.html 
