Title: Task 실행 라이브러리 - Invoke
Date: 2019-07-21 16:20:49
Category: Develop
Tags: invoke, devops, paramiko, command, cli, task
Slug: task_sir-haeng_ra-i-beu-reo-ri_-_invoke
Summary: Task 실행 라이브러리인 `Invoke`를 확인한다.

Pelican 에서 Makefile를 이용해서 빌드하고 있었는데.
4.0.0 버전으로 올라오면서 `Invoke` 라이브러리를 사용하게 되었음을 확인.
그러니 사용해봐야징...

[Home](https://www.pyinvoke.org/)

## What is Invoke?

Python (2.7, 3.4+) 태스크 실행 툴이자 라이브러리

- `[tasks.py](http://tasks.py)` 파일에 태스크를 명시하여 진행
    - 물론 `tasks/*.py` 형식으로 만들어서 정의할 수도 있다.
- GNU Make 처럼, 명령을 나열할 수 있다.

        $ invoke clean build

- REPL 쪽에서 사용이 가능하다.
- Unix CLI 와 같이 flag-based style 명령어를 만들 수 있다.
    - `--ab` , `-d` 이런거

## 사용?

- `tasks.py` - [ujuc.github.io - tasks.py](https://github.com/ujuc/ujuc.github.io/blob/develop/tasks.py)

```python
from invoke import Collection, task

from pathlib import Path

BASE_PATH = Path.cwd()
OUTPUT_PATH = BASE_PATH / "output"
CONF_FILE = BASE_PATH / "pelicanconf.py"
PUBLISH_CONF_FILE = BASE_PATH / "publishconf.py"


@task()
def preview(ctx):
    """Start preview web page server"""
    ctx.run(f"pelican -s {CONF_FILE}")
    ctx.run(f"pelican -l")


@task()
def clean(ctx):
    """Clean up this dir"""
    ctx.run(f"rm -rf {OUTPUT_PATH} {BASE_PATH}/__pycache__ {BASE_PATH}/cache")


@task(post=[clean])
def pub(ctx):
    """Publish to github main page"""
    ctx.run(f"pelican -s {PUBLISH_CONF_FILE}")
    ctx.run(f"ghp-import -m 'Generate Pelican site' -b master {OUTPUT_PATH}")
    ctx.run(f"git push origin master")


@task()
def fix(ctx):
    """Execute black"""
    ctx.run("black -l 80 .")


ns = Collection()
ns.add_task(clean)
ns.add_task(preview)
ns.add_task(pub)
ns.add_task(fix)
```

### 실행

- 목록은 이렇게

```shell
$ inv --list

Available tasks:

  clean     Clean up this dir
  fix       Execute black
  preview   Start preview web page server
  pub       Publish to github main page
```

- help는 이렇게

```shell
$ inv pub -h

Usage: inv[oke] [--core-opts] pub [other tasks here ...]

Docstring:
  Publish to github main page

Options:
  none
```

---

자세한건 [Docs](http://docs.pyinvoke.org/en/stable) 에서 읽어가면서 확인
