Title: 맥에서 gpg 키 서명 실패
Date: 2020-02-19 05:38:42
Modified: 2023-01-18 19:22:00
Category: Operation
Tags: gpg, key, gnupg, pinentry
Slug: macos-e-seo-gpg-ki-seo-myeong-sil-pae
Summary: commit 할때마다 gpg키로 서명하게 해놨는데 안된다. 고치자!

2023.01.18 설정값이 변경된 것들이 있어서 회사 컴퓨터를 새롭게 받아 설치한 기념으로 업데이트 한다. (Thanks to. [@roeniss](https://github.com/roeniss))

---

열심히 공부하고 커밋하려는 순간...

```shell
> git commit
error: gpg tailed to sign the data
fatal: failed to write commit object
```

gpg키로 commit을 할때마다 비밀번호를 물어야되는데...
우리 macOS에서는 비밀번호를 처음에 묻고 keychain에 저장을 해놓으시고 커밋할때마다 자동으로 입력한다.

그게 문제가 되었다. 오랜만에 재시작을 하면서 섹션 만료가 되었고, 바꼈으면 물어야지...
조용히 있어서 문제가 되었다.

이럴때 [Stack Overflow/ git - gpg onto mac osx: error: failed to sign the data][1]에서는 [pinentry][2]를 추가 설치해서 비밀번호를 얻어서 하라고 되어있다.

MacOS의 경우, `pinentry` 가 `pinentry-mac`으로 패키징되어있다. 그래서 다음과같이 설치한다.

```shell
brew install pinentry-mac

echo 'pinentry-program ${which pinentry}' >> ~/.gnupg/gpg-agent.conf
echo 'export GPG_TTY=$(tty) >> ~/.zshrc
```

작동하는지 테스트

```shell
> echo "test" | gpg --clearsign
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

test
-----BEGIN PGP SIGNATURE-----
```

그리고 블로그 쓸려고 확인중 이 문제를 겪었을때 대응 할 수 있다는 다른 방법!

#### 1. Keychain Access에서 수정

macOS에서 `Keychain Access`로 접근 Passwords 카테고리에서 gpg키에 대한 비밀번호를 찾고, `Access Control`에서 **Confirm before allowing access > Ask for Keychain password** 를 체크 하도록 하자.
이것도 매번 물어볼꺼다 저장이 안되어있는데 물어야지...

#### 2. 처음 입력할때

gpg키를 맨처음 입력할때 잘보도록하자 거기에 비밀번호 저장할래가 있을꺼다. 그걸 해지한다.
그러면 매번 git commit할때마다 물을꺼다.
그러면 서명이 가능해지겠지...

[1]: https://stackoverflow.com/questions/41502146/git-gpg-onto-mac-osx-error-gpg-failed-to-sign-the-data/41506446
[2]: https://www.gnupg.org/related_software/pinentry/index.en.html
