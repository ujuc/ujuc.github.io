#!/usr/bin/env python3
# coding: utf-8
# Origin : http://nafiulis.me/making-a-static-blog-with-pelican.html
# edit: ujuc
"""write

Usage:
    write new [-r | --rst] <title>
    write page [-r | --rst] <title>
    write edit <title>
    write backup <title> <date>

-d --date       datetime change

"""

import os

import kroman
import pendulum
from docopt import docopt

POST_PATH = "content/blog"
PAGE_PATH = "content/pages"


def make_entry(title, path, template):
    """
    블로그 포스트를 생성한다.

    :param title:
    :param path:
    :param template:
    :return:
    """
    today = pendulum.now()

    slug = kroman.parse(title).lower().strip().replace(' ', '_')
    date = today.to_date_string()
    post_date = today.to_datetime_string()
    file_name = f'{path}/{date}-{slug}'

    article = ()

    if template == 'rst':
        file_name = f'{file_name}.rst'
        hashes = '#' * len(title) * 2

        article = (
            f'{title}\n'
            f'{hashes}\n\n'
            f':date: {post_date}\n'
            f':category: \n'
            f':tags: \n'
            f':slug: {slug}\n\n'
        )
    elif template == 'md':
        file_name = f'{file_name}.md'

        article = (
            f'Title: {title}\n'
            f'Date: {post_date}\n'
            f'Category: \n'
            f'Tags: \n'
            f'Slug: {slug}\n'
            f'Summary: \n\n'
        )

    if not os.path.isdir(path):
        os.mkdir(path)

    with open(file_name, 'w') as article_file:
        article_file.write(article)

    print(f'File created -> {file_name}')


def edit_entry():
    """
    title 을 가져오는데, file_path 는 동일하고 앞에 일자-제목이 붙으니
    그것까지 가져와서 변경해야되는 점이있음.
    :return:
    """
    pass


if __name__ == '__main__':
    OPT = docopt(__doc__, version='write 1.1')

    if OPT['new']:
        if OPT["-r"] or OPT["--rst"]:
            make_entry(OPT["<title>"], POST_PATH, 'rst')
        else:
            make_entry(OPT["<title>"], POST_PATH, 'md')
    elif OPT['page']:
        if OPT["-r"] or OPT["--rst"]:
            make_entry(OPT["<title>"], PAGE_PATH, 'rst')
        else:
            make_entry(OPT["<title>"], PAGE_PATH, 'md')
    elif OPT['edit']:
        print("edit")
    elif OPT["backup"]:
        print("backup")
    else:
        print(OPT)
