Title: Python pre-commit 설정하기
Date: 2025-07-28 08:49
Modified: 2025-07-28 08:49
Category: Develop
Tags: Python, Git, pre-commit, Git hooks
Slug: python-precommit-설정하기
Summary: 블로그를 만들고 처음으로 git hook을 설정해다.

다른 파이썬 프로젝트를 보다가 [ruff-pre-commit][1]이 설정되었는 것을 확인해서 적용해보기로 하고, 블로그에 작업을 시작.

# pre-commit

파이썬 라이브러리인 [pre-commit][2]. ~~12년된 프로젝트인데 왜 설정안했나? 나야?~~

나는 uv를 사용하니까 다음으로 설치.

```bash
uv add --dev pre-commit
```

`dev` 그룹으로 넣은건 커밋할때 빼고는 동작하지 않아도 되는걸 굳이 캐싱까지하는 CI에 넣어야하나 싶어서 이기도함.
그냥 글만 쓰게 되는 환경을 구성하게되면, 수정을 해보는걸로...

# 설정

pre-commit에서 사용하는 설정은 `.pre-commit-config.yaml` 파일에 나열 해주면된다.

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.12.5
    hooks:
      - id: ruff-check
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: check-merge-conflict
      - id: check-toml
      - id: check-yaml
      - id: detect-private-key
      - id: end-of-file-fixer
      - id: mixed-line-ending
      - id: pretty-format-json
        args: [--autofix]
      - id: trailing-whitespace
```

## pre-commit-config.yaml 파일 구조

내용을 다적을려고 했는데, 어떤 방법으로 보여주는게 좋을지 생각나지 않아 URL로 대체한다.

[여길 참고하자!](https://pre-commit.com/#adding-pre-commit-plugins-to-your-project)

# pre-commit plugins

- [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
- [ruff-pre-commit](https://github.com/charliermarsh/ruff-pre-commit)

# pre-commit cli

```bash
# 설정 내역 반영
pre-commit install

# 제거!
pre-commit uninstall
```

# 끝

뭔가 더 적을까했으나, 뭔가 더 적을 만한게... 없다.
한번만 설정해두면, 왠만해서는 변경할 일이 없으니, 한번 잘 작성해두고 두고두고 버전업만 하면서 사용하도록하자.
그리고 `pre-commit`과 비슷한 동작을 하는 것들이 언어별로 있으니 Python이 아닌 다른 언어를 사용한다면, 언어에 맞는 것을 사용하기 바란다. 레포에 두가지이상 언어가 섞이면 어지럽다.

[1]: https://github.com/charliermarsh/ruff-pre-commit
[2]: https://pre-commit.com/
