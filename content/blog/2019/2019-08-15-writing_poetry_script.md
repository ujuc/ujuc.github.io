Title: Writing poetry script
Date: 2019-08-15 08:51:09
Modified: 2019-08-19 20:52:00
Category: Develop
Tags: poetry, script, invoke
Slug: writing_poetry_script
Summary: `poetry`를 사용하면서 사용하고 싶었던 `[tool.poetry.scripts]` 사용법을 남긴다.

1. 이 문서에서 `invoke` 라이브러리를 사용한다.
2. 실제 코드는 [https://github.com/ujuc/ujuc.github.io](https://github.com/ujuc/ujuc.github.io) 에서 확인이 가능하다.


## 명령어 작성

블로그 새 글을 만들 수 있는 명령어를 작성한다.

`cli.py`

```python
from pathlib import Path

import kroman
import pendulum
from invoke import Collection, task

BASE_PATH = Path.cwd()
CONTENT_PATH = BASE_PATH / 'content'


@task(
    help={
        'title': 'Post title',
        'rst': 'Post format. if false, make markdown format'
    }
)
def post(ctx, title, rst=False):
    """Make post template"""
    today = pendulum.new()

    slug = kroman.parse(title).lower().strip().replace(' ', '_')
    date = today.to_date_string()
    post_date = today.to_datetime_string()
    file_title = f'{date}-{slug}'

    file_name = f'{file_title}.md'

    article = (
        f'Title: {title}\n'
        f'Date: {post_date}\n'
        'Category: \n'
        'Tags: \n'
        f'Slug: {slug}\n'
        'Summary: \n\n'
    )

    if rst:
        file_name = f'{file_title}.rst'
        hashes = '#' * len(title) * 2

        article = (
            f'{title}\n'
            f'{hashes}\n'
            f':date: {post_date}\n'
            ':category: \n'
            ':tags: \n'
            f':slug: {slug}\n'
            ':summary: \n\n'
        )

    blog_path = CONTENT_PATH / 'blog'
    if not blog_path.is_dir():
        blog_path.mkdir(parents=True)

    post_path = blog_path / file_name

    with post_path.open('w') as post_file:
        post_file.write(article)

    print(f'File created -> {post_path}')


ns = Collection()
ns.add_task(post)
```

task를 등록해 주고 명령을 확인하면 다음 같이 보인다.

```shell
$ inv --list

Available tasks:

  clean      Clean up this dir
  fix        Execute black
  preview    Start preview web page server
  pub        Publish to github main page
  cli.post   Make post template
```

명령어를 실행해 보자.
```shell
$ inv --help cli.post
Usage: inv[oke] [--core-opts] cli.post [--options] [other tasks here ...]

Docstring:
  Make post template

Options:
  -r, --rst                   Post format. if false, make markdown format
  -t STRING, --title=STRING   Post title

# Test create post
$ inv cli.post -t "포스트 테스트"
File created -> /Users/ujuc/repos/ujuc.github.io/content/blog/2019-08-14-po-seu-teu_te-seu-teu.md

# Cat post file
$ cat content/blog/2019-08-14-po-seu-teu_te-seu-teu.md
Title: 포스트 테스트
Date: 2019-08-14 23:49:02
Category: 
Tags: 
Slug: po-seu-teu_te-seu-teu
Summary:

```    

여기까지 [code commit](https://github.com/ujuc/ujuc.github.io/commit/8e4fa75978c249192c203658dace4949a7956936).

---

이제 만들어지는 걸 확인했으니... `poetry run cli`  명령을 이용해서도 만들 수 있게 코드를 수정하자.

`cli/main.py`

- Package로 추가해야 되어 `cli` 폴더를 만들었다.
- [Poetry run: ModuleOrPackageNotFound with implicit namespace packages (PEP420)](https://github.com/sdispater/poetry/issues/577)

```python
# Import Program class
from invoke import Collection, Program, task

...

def run():
    program = Program(version='1.0.0')
    program.namespace = Collection()
    program.namespace.add_task(post)

    program.run()
```

`pyproject.toml`
```toml
[tool.poetry]
...

packages = [
    { include='cli', from='.' }
]

...

[tool.poetry.scripts]
cli = 'cli.main:run'

...
```

이제 실행해 보자.
```shell
$ poetry run cli --list
Subcommands:

  post   Make post template

# Test create post
$ poetry run cli post -t "포스트 테스트"
File created -> /Users/ujuc/repos/ujuc.github.io/content/blog/2019-08-15-po-seu-teu_te-seu-teu.md
```

잘된다.

여기까지 [code commit](https://github.com/ujuc/ujuc.github.io/commit/ded484d94cec63e684d1f8fab2ea0b8006ceab63).

---

이렇게 하면 간단한 cli 툴을 실행할 수 있다.

문제는 build를 하게되면 해당 명령 셋이 등록이 되니... build용이 아닌 상태로 사용하자.

build일때는 고민을...

[poetry 레포](https://github.com/sdispater/poetry/blob/master/pyproject.toml#L69)를 보면 해당 `pyproject.toml`에 실행하는 코드가 들어가있는 것을 확인할 수 있다.


---

ps. 파일 단위로도 가능하다.

`tasks.py`

```
위에꺼 갔다 쓰자.. 귀찮다...
```

`pyproject.toml`

```
[tool.poetry.scripts]
cli = "tasks:run"
```

---

이제 나머지 명령어 옮기러가야겠다.
