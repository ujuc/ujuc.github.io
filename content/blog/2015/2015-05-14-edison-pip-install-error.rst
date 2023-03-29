Edison pip install error
################################################

:date: 2015-05-14 01:39
:category: Develop
:tags: edison, pypi, pip, python, error
:slug: edison-pip-install-error
:summary: Edison으로 파이썬을 작업하기위해 패키지를 설치하려보면... 이넘이 안된
          다. 그것에 대한 내용이다.

pip를 설치하고 패키지를 확인하려고하면 다음과 같은 에러가 발생한다.

.. code:: bash
   
   # pip install flask
   Traceback (most recent call las):
   File "/usr/bin/pip", line 5, in <module>
   from pkg_resources import load_entry_point
   ImportError:No module named pkg_resources
   

발생하는건 ``setuptools`` 패키지가 설치되지 않아서 문제가...

.. code:: bash
   
   # wget --no-check-certificate \
     https://pypi.python.org/packages/source/s/setuptools/setuptools-15.2.tar.gz#md5=a9028a9794fc7ae02320d32e2d7e12ee
   # tar zxf setuptools-15.2.tar.gz
   # python setuptools-15.2/ez_setup.py
   


* ``pip install --upgrade pip`` 로 제대로 설치된건지 확인하자.
    + 기본 설치되는 pip 버전이 낮으니.. 업글해줘야되기도 해서..
