# ujuc.github.io

- 기술 블로그

## 환경 설정

```sh
git submodule update --init --recursive
pre-commit install

# submodule branch 설정
cd clean
git checkout master
```

## Pelican 명령어

### 글 생성

```sh
uv run cli post <TITLE>
```

### preview

```sh
uv run cli preview
```
