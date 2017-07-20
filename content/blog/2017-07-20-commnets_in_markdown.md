Title: Commnets in Markdown
Date: 2017-07-20 16:33:15
Category: Chat
Tags: markdown, comment, 문법
Slug: commnets_in_markdown
Summary: Markdown에서는 comment는 어떻게 해야되지...

JSON API 스팩 문서를 다시 번역하면서 꽤나 긴 markdown 문서를 작성해야되는 경우가 발생했다. 그러다보니... 코멘트로 나눔이 필요한 경우가 발생!

구글에서 간단하게 검색하니 [Comments in Markdown - Stackoverflow](https://stackoverflow.com/questions/4823468/comments-in-markdown) 라는 글이 하나 발견...

코멘트 남기는 방법은 다음처럼 구성하면 된다.

```
[comment]: # (This is a comment.)
[//]: # (This is a comment.)
```

개인적 취향은 두번째가 좋아보인다. 그리고 긴 코멘트가 필요하다면... HTML 코멘트 태그를 사용해도 좋을듯.

```
<!---
This is comment.
--->
```

오늘은 여기까지...

