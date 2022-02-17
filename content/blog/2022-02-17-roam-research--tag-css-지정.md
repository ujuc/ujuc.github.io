Title: Roam Research - Tag CSS 지정
Date: 2022-02-17 21:22:11
Modified: 2022-02-17 21:22:11
Category: Develop
Tags: roam research, css, note
Slug: roam-research--tag-css-지정
Summary: Roam Research 에서 tag 지정할때 눈에 좀 띄게하고 싶었다.

그냥 본론으로 들어가자.
Roam Research에서는 사용자 CSS를 지원한다. 참 간단하게. 이렇게 간단해도 되나 싶은...

1. `[[roam/css]]` 페이지를 생성한다.
      - 앞으로 모든 CSS 파일을 수정하는건 여기서 한다.
2. `/code block`을 선택한다.
3. 언어 선택을 `css`로 변경해준다.
4. `[data-tag="{TAG_NAME}"]` CSS를 먹일 태그를 지정해준다.
      - 앞뒤로 뭔가를 붙일려면 `[data-tag={TAG_NAME}"]::before`, `[data-tag="{TAG_NAME}"]::after` 를 이용해서 앞뒤에 특정 내용을 붙일 수 있다.

### 예제

![생각 tag 나가기]({static}/img/2022-02-17-roam_tag.png)

```css
[data-tag="생각"] {
  color: #1A87C0;
  font-weight: bold;
}

[data-tag="생각"]::after {
  content: "\f090";
  font-family: FontAwesome;
  padding: 0px 2px 0px 4px;
}
```
