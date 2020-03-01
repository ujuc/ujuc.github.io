from pathlib import Path

import kroman
import pendulum
from invoke import Collection, Program, task

BASE_PATH = Path.cwd()
CONTENT_PATH = BASE_PATH / 'content'
OUTPUT_PATH = BASE_PATH / "output"
CONF_FILE = BASE_PATH / "pelicanconf.py"
PUBLISH_CONF_FILE = BASE_PATH / "publishconf.py"

@task(
    help={
        'title': 'Post title',
        'rst': 'Post format. if false, make markdown format'
    }
)
def post(ctx, title, rst=False):
    """Make post template"""
    today = pendulum.now()

    slug = kroman.parse(title).lower().strip().replace(' ', '_')
    date = today.to_date_string()
    post_date = today.to_datetime_string()
    file_title = f'{date}-{slug}'

    file_name = f'{file_title}.md'

    article = (
        f'Title: {title}\n'
        f'Date: {post_date}\n'
        f'Modified: {post_date}\n'
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
def build(ctx):
    """Build Blog Post"""
    ctx.run(f"pelican -s {PUBLISH_CONF_FILE}")


def run():
    program = Program(version='1.0.0')
    program.namespace = Collection()
    program.namespace.add_task(post)
    program.namespace.add_task(preview)
    program.namespace.add_task(pub)
    program.namespace.add_task(clean)
    program.namespace.add_task(build)
    program.run()
