Title: Rust 개발 환경 구성
Date: 2019-08-06 08:58:16
Category: Develop
Tags: rust, rustup, develop, env
Slug: rust_gae-bar_hwan-gyeong_gu-seong
Summary: Rust 개발을 해볼까나~

그냥 공부할 목적으로 Rust를 하기로 하였다.
요즘에 참 잘 나간다고도 했고...

## Rustup으로 Rust 설치

처음에는 rustup을 이용해서 설치한게 아니라 brow를 이용해서 설치를 했었다.
coc.nvim에서 rust 플러그인을 쓸려고하니... 안된다고 해서 설치.

```shell
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

명령어를 확인했는데 이거 괜찮은 툴이다.
나중에 따로 정리해야지.

## Vim 환경

### coc.nvim 플러그인 설치

원래 목적인 coc.nvim 플러그인을 설치하자.
vim에서 명령을 날린다.

```
:CocInstall coc-rls
```

환경 끝.

## IDEA

### CLion

1. CLion을 설치한다.
2. Rust 플러그인을 설치한다.
3. Rust를 가지고서 개발한다.

환경 끝.

