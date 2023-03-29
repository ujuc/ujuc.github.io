Title: 파이썬으로 내가 쓸 셸 만들기
Date: 2016-07-08 00:29
Category: Develop
Tags: python, shell, yosh, Your Own SHell
Slug: pa-i-sseon-eu-ro_nae-ga_sseur_syer_man-deur-gi
Summary: python `cmd` 라이브러리를 가지고서 셸을 만들어서 작업을 할까라는 생각을 가지고 있었는데... 다른 방법이지만 그것을 실제로 진행한 내용이 있어서 정리용.

매주 python관련 뉴스들이 오는데 이번에는 흥미로운 것이 있어서 이렇게 남긴다.

* [Create Your Own Shell in Python: Part 1](https://hackercollider.com/articles/2016/07/05/create-your-own-shell-in-python-part-1/)
* [Create Your Own Shell in Python: Part 2](https://hackercollider.com/articles/2016/07/06/create-your-own-shell-in-python-part-2/)
* [supasate/yosh](https://github.com/supasate/yosh)

`yosh` 프로젝트로 간단히 Python을 이용해서 셸을 구성할 수 있도록 도와준다. 그리고 이것을 이용해서 조금이나마 편하게 사용할 수 있음을 이야기해주고도 있다.
다른 것보다는 손쉽게 내가 원하는 셸을 만들어서 사용할 수 있다는 점과 내가 2014년에 PyconKR에서 봤던 것들로 구성만 하고 있엇던 [`cmd`][1] 라이브러리가 아닌 [`shlex`][2] 라이브러리를 사용해서 셸에서 입력하는 것과 유사하게 만들어주는 것으로 보인다.

첫번째로 부럽다. 생각만했지 실행으로 옮기지는 못했다. 내가 사용하는 셸 프로그램들을 묶어서 내가 원하는 생각대로 실행할 수 있도록 하는 것. 쉽지 않다고 생각만 했지. 언젠가 하려고만 했지. 이렇게까지 만들 수 있으리라 생각하지 못했다.

한번 도전해봐야겠다. 처음 생각했던 [`cmd`][1] 라이브러리로 기본 라이브러리 구성을 남겨두고, 작업을 진행할 수 있도록.

[1]: https://docs.python.org/3.5/library/cmd.html
[2]: https://docs.python.org/3.5/library/shlex.html
