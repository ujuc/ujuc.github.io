Title: 맥에서 GPG키를 이용하여 Commit 해보기
Date: 2018-10-26 23:24:58
Category: Develop
Tags: gpg key, keybase.io, keybase
Slug: maeg-e-seo_gpgki-reur_i-yong-ha-yeo_commit_hae-bo-gi
Summary: GPG 키를 이용해서 내 커밋이 정말 내가 올린 것이라 말하고 싶었다.

[keybase.io](https://keybase.io/) 계정이 있다는 가정하에서 하니, 가입을 하자.

### 필요한 것들

```bash
$ brew install gpg
$ brew cask install keybase
$ brew cask install gpg-suite
```

### GPG 키 생성

```bash
$ keybase pgp gen --multi
```

### Git 구성에 추가

```bash
$ gpg --list-secret-keys --keyid-format LONG
/Users/{username}/.gnupg/pubring.kbx
------------------------------
sec   rsa4096/{keyid} 2018-10-18 [SC] [expires: 20xx-10-01]
      ?????
uid                 [ unknown] Sungjin Kang <example@example.com>
ssb   rsa4096/{keyid} 2018-10-18 [E] [expires: 20xx-10-01]

$ git config --global user.signingkey {keyid}
$ git config --global commit.gpgsign true
```

### Github 에 Public GPG 키 등록

[https://github.com/settings/keys](https://github.com/settings/keys) 에 접속하여 **New GPG key** 메뉴 선택

아래 명령어로 GPG키 복사하여 붙여넣기

```bash
$ keybase pgp export -q {keyid} | pbcopy
```

### Git GUI 툴에서 커밋이 가능하게 옵션 추가

```bash
$ echo no-tty >> ~/.gnupg/gpg.conf
$ git config --global gpg.program ${which gpg}
```

### 회사 컴퓨터에도 가능하게 해두자

위에서 말한 프로그램을 설치한 뒤 다음 명령을 이용해서 key를 저장한다. 하나의 키를 가지고 있을 경우에만 다음 명령이 먹힌다. 두개이상이면 다른 모습이 보인다고...

```bash
$ keybase pgp export
-----BEGIN PGP PUBLIC KEY BLOCK-----

# Public key export
$ keybase pgp export | gpg --import
# Private key export
$ keybase pgp export --secret | gpg --allow-secret-key-import --import
```

### 참고 사이트

- [Set up Keybase.io, GPG & Git to sign commits on GitHub](https://github.com/pstadler/keybase-gpg-github)
- [Signed git commits with Tower](https://aaronparecki.com/2016/07/29/10/git-tower)
- [simnalamburt/keybase-github.md](https://www.notion.so/ujuc/GPG-commit-11c88ce0b00f4dc79713b4ce09f62714)