Title: 특정 CSS selector를 잡기위해 정규식 사용하기
Date: 2023-01-01 22:38:23
Modified: 2023-01-01 22:38:23
Category: TIL
Tags: css, selector, regex
Slug: 특정-css-selector를-잡기위해-정규식-사용하기
Summary: Roam Research에서 tag에 특정 값을 넣는데 필요한 설정을 찾다가 발견한 css 규식이형 사용법

Roam Research에서 css를 튜닝할 수 있도록 열어두고 있다.

그냥 tag가 `@home/경조사` 와 같이 단계를 만들어나가고 있는데... 튜닝을 하고 싶다는거지...
그래서 규식이형이 가능한지 찾다가 [Css with regex for id](https://stackoverflow.com/questions/42497352/css-with-regex-for-id) 라는 글을 발견.

사용법은 간단하다.

`id^=s`를 하게되면 `id`가 `s`로 시작하는 것을. `id$=0`을 하게되면 `id`가 `0`으로 끝나는 것을 찾아서 적용해준다.

`*`도 사용가능 하다고... [Empowering your CSS Identifiers with RegEx patterns](https://www.linkedin.com/pulse/empowering-your-css-identifiers-regex-patterns-sandeep-chandra-sekhar)

