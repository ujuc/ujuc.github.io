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
    today = pendulum.now()

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
