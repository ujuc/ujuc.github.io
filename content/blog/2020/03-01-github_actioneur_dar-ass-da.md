Title: github actions를 달았다
Date: 2020-03-01 10:07:50
Modified: 2020-03-01 10:07:50
Category: Develop
Tags: github actions
Slug: github-actionsreul-dal-ass-da
Summary: 블로그 퍼플리싱을 자동으로 하기위해 Github Actions 추가!

블로그 페이지 생성을 자동으로 하고 싶었다. 그런데 아무리 해도 안되더라.
포기하고 있었는데.

[fastpages](https://github.com/fastai/fastpages) 라는 Jupyter notebooks을 생성하면 Github 블로그로 출력해주는 서비스를 보고 Github Actions를 이용해서 진행하고 있는 것을 발견!

그 Actions는 [peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages)!!

아싸 이제 붙여야지...

기존에 gh-pages로 퍼블리싱을 진행하고 있었기에 cli 명령어에 `build`라는 명령어를 추가하고 작업을 진행하였다.

```yaml
name: github pages

on:
  push:
    branches: develop

jobs:
  deploy:
    runs-on: ubuntu-18.04
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: Checkout submodules
        shell: bash
        run: |
          auth_header="$(git config --local --get http.https://github.com/.extraheader)"
          git submodule sync --recursive
          git -c "http.extraheader=$auth_header" -c protocol.version=2 submodule update --init --force --recursive --depth=1

      - uses: actions/setup-python@v1
        with:
          python-version: 3.8

      - name: Setup poetry
        uses: Gr1N/setup-poetry@v1
        with:
          poetry-version: 1.0.3

      - name: Install python pacakge
        run: poetry install

      - name: Build posts
        run: poetry run cli build

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          personal_token: ${{ secrets.PERSONAL_TOKEN }}
          publish_branch: master
          publish_dir: ./output
```

추가하고 테스트 커밋으로 퍼블리싱되는 것을 확인하였다.

오늘의 삽질은 끝...

PS. Poetry 를 사용하기 위한 actions가 여러개 있는데. [Gr1N/Seup Poetry](https://github.com/marketplace/actions/setup-poetry) 를 사용한 것은 별표 많이 받은 Actions가 너무 느려서 였다.
명령어 많이 쓰지도 않는데 빌드하는데 1분이상 자기가 잡아먹고 있는건 아니지않는가...
