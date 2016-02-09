timesheet.js??
==============

:date: 2015-03-02
:modified: 2015-04-01 22:21
:category: Develop
:tags: javascript, js
:slug: timesheet-js
:summary: timesheet.js라는 연대표를 그려주는 JS 라이브러리

놀다 보니 이것저것 보는 것들도 많다. 그런것들이라도 간단히 적어둬야지... 

노트에다가 작성을 해놓고 넣어두는 것도 한 방법이지만, 봤을때 좋은거라 생각한다면
그것으로 작업이 가능하지 않을까 하여...

timesheet.js
-------------

* 홈페이지: `sbstjn/timesheet.js`_
* 손을 좀 대서 자세하게 보이거나 이것저것 손을 볼 수 있을 것같은데...

.. |time sheet| image:: https://raw.githubusercontent.com/sbstjn/timesheet.js/master/screen.png
.. _sbstjn/timesheet.js: https://github.com/sbstjn/timesheet.js

예제
-----

HTML 태그를 쓸수 없다는게 rst의 단점...

그래서 예제_ 는 링크로.... OTL

.. _예제: http://jsfiddle.net/fujstt3s/1/


특이점
------

* 소스파일로 되어있는기.. haml_ 로 되어있고, sass_ 는 첨가.
  
  - sass는 CSS를 더 변수, 함수, 확장 / 상속 등의 기능을 추가해서 쉽게 만들고,
    쉽게 유지보수 할 수 있도록 되어있다고 한다. 여러 종류가 있다고... [1]_
  - haml은 HTML abstraction markup language라고 하는걸 줄였다고, 작성을 해놨네.
    HTML 태그를 작성하기 더 쉽게 되어있긴한데... 태그를 변수로 주는게 특이하다.

* 조금이나 더 짧게 쓰고 조금이나마 더 버전 관리가 쉽게 하도록 하는걸 보면, 점점
  더 바닥을 아는 사람들이 없어져가고, 그것들을 알 수 있는 방법들도
  없어져가는건 안좋은 점 중 하나다.

.. _haml: http://haml.info/
.. _sass: http://sass-lang.com/                   
.. [1] http://windtale.net/blog/why-i-choose-sass/
