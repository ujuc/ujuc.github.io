Title: Python setup.py unilnstall 방법
Date: 2013-11-22 11:22:23
Modified: 2018-03-11 11:22:23
Category: Develop
Tags: python, setup.py, setup, tool
Slug: python_setup.py_unilnstall_bang-beob
Summary: setup.py를 이용하여 uninstall 하는 방법에 대해서 간략 정리.

[Python setup.py uninstall](http://stackoverflow.com/questions/1550226/python-setup-py-uninstall)

삭제하는 방법은 모든걸 지워 버려야된다는 것.

우선 `setup.py`로 설치하는 경로를 파일로 받는다.

```
$ python setup.,py install --record files.txt
```

그러고 난 뒤 그 내용에 있는 것들을 모두 다 지워주면 되는데. 이때, 폴더 내부만 삭제할뿐 생성된 파일이 삭제되지 않으니 유의해서 삭제할 수 있도록 조정해주면 된다.

```
$ cat files.txt | xargs rm -rf
```
