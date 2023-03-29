Title: Pycharm에 pylint 추가
Date: 2018-09-24 00:49:24
Category: Software 
Tags: pycharm, pylint, python, lint
Slug: pycharme_pylint_cu-ga
Summary: Pycharm 에 pylint를 외부 툴로 등록하는 방법

나는 블로그를 사용할때 Python 스크립트를 사용해서 작업을 하고 있다. 그러다보니 매번 파일에 추가되는 내용이나 달라지는 것들이 있으면 수정을 하는데...

지금까지는 lint 작업은 하지않고서 pycharm에서 지적하는 부분만 가지고 작업을 하였다만... 이제 lint를 적용해서 작업을 공통으로 사용할 수 있게 해놔야지...

pylint만 있는건 아니지만, pep8이나 다른것들을 정리하려면... 너무 많은 것을 등록해야된... 논외로..

[How to run Pylint with PyCharm - stackoverflow](https://stackoverflow.com/questions/38134086/how-to-run-pylint-with-pycharm)

위의 글을 읽어보면 자세히 되어있다.

여기서 나와 다른 점에 대해서 기록하고 넘어가기로 한다.

나는 global로 pylint를 설치하지 않았다. 귀찮기도하고 많은 버전을 섞어쓰는 환경이다보니... `pipenv` 를 사용하고 있는데 이것에 대한 내용은 없다. global 하게 패키지까는 것도 부담스럽고...

다음 사진과 같이 나는 내용을 수정해서 사용한다.

![My_settings]({static}/img/2018-09-24_pycharm_export_tool_setting.png)

