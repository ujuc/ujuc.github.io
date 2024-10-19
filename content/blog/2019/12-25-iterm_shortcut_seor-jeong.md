Title: iTerm shortcut 설정
Date: 2019-12-25 13:06:25
Modified: 2020-01-10 07:38:00
Category: Operation
Tags: iterm, shortcut
Slug: iterm_shortcut_seor-jeong
Summary: iTerm를 사용하다보면 커멘드라인 맨앞으로간다거나 중간중간 건너 띄워서 가야할때, 사용하는 단축키를 정리한다.

## 01/10 추가

[@channprj](https://github.com/channprj) 님께서 댓글로 Hex code로 하지 않아도 된다는 소식을 알려주셨다.

1. iTerm2 -> Preferences
2. Profile > Keys
3. Presets... > Natual Text Editing

<img src="{static}/img/2020-01-10_iterm2.png" width="30%">

---

매번 찾았는데... 이제는 기억을 못해서 써두려고 한다.

원래 글은 [(stackoverflow) iTerm 2: How to set keyboard shorcuts to jump to beginning/end of line?](https://stackoverflow.com/questions/6205157/iterm-2-how-to-set-keyboard-shortcuts-to-jump-to-beginning-end-of-line)

지금 글쓰는 오늘 날짜로 8년도 더된 글이다

이정도면 기본으로 넣어줄 만한데... 암튼...

개인적으로 설정해서 사용하는 답변은 [두번째](https://stackoverflow.com/questions/6205157/iterm-2-how-to-set-keyboard-shortcuts-to-jump-to-beginning-end-of-line/22312856#22312856)

---

1. iTerm2 -> Preferences
2. "Key" 탭설정
3. 다음 단축키들을 입력한다.

## 왼쪽으로 워드 단위 이동

* 키보드 입력: `option` + `<-`
* Action : Send Hex Code
* Code: `0x1b 0x62`

## 오른쪽으로 워드 단위 이동

* 키보드 입력: `option` + `->`
* Action: Send Hex Code
* Code: `0x1b 0x66`

**위의 두 설정을 하게되면 다음 작업을 꼭 해줘야 된다.**

1. "Profiles" 열고
2. "Keys" 선택
3. `option` + `<-`, `option` + `->` 항목을 삭제한다.

## 맨 첫번째로 이동

* 키보드 입력: `cmd` + `<-`
* Action: Send Hex Code
* Code: `0x01`

## 맨끝으로 이동

* 키보드 입력: `cmd` + `->`
* Action: Send Hex Code
* Code: `0x05`

