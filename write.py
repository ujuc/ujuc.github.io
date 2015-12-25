#!/usr/bin/env python3
# coding: utf-8
# Oirign : http://nafiulis.me/making-a-static-blog-with-pelican.html
# edit: ujuc
"""write

Usage:
    write new [-m | --markdown] [-p | --page] <title>
    write edit <title>
    write backup <title> <date>

-d --date       datetime change

"""

from datetime import datetime
from docopt import docopt

RST_TEMPLATE = ('{title}\n'
                '{hashes}\n'
                '\n'
                '{date}\n'
                ':category: \n'
                ':tags: \n'
                ':slug: {slug}\n'
                ':summary: \n'
                '{modified}\n'
                '\n')

MD_TEMPLATE = ('Title: {title}\n'
               'Date: {date}\n'
               'Category: \n'
               'Tags: \n'
               'Slug: {slug}\n'
               'Summary: \n')

post_path = "content/blog"
page_path = "content/pages"


def make_entry(title, path, template):
    today = datetime.today()
    # GTODO : 한국어를 영어로 변환하는 것이 필요
    slug = title.lower().strip().replace(' ', '-')
    date = ":date: {year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}"\
        .format(year=today.year, month=today.month, day=today.day,
                hour=today.hour, minute=today.minute)

    if template == 'rst':
        file_create = \
            "{0}/{1}-{2:0>2}-{3:0>2}-{4}.rst".format(path,
                                                     today.year,
                                                     today.month,
                                                     today.day, slug)
        article = RST_TEMPLATE.strip().format(
                title=title,
                hashes='#' * len(title) * 2,
                slug=slug,
                date=date,
                modified="")
    elif template == 'md':
        file_create = \
            "{0}/{1}-{2:0>2}-{3:0>2}-{4}.md".format(path,
                                                    today.year,
                                                    today.month,
                                                    today.day, slug)
        article = MD_TEMPLATE.strip().format(
                title=title,
                slug=slug,
                date=date)

    with open(file_create, 'w') as w:
        w.write(article)
    print("File created -> " + file_create)


def edit_entry(title):
    """
    title을 가져오는데, file_path는 동일하고 앞에 일자-제목이 붙으니 그것까지 가져와서 변경해야되는
    점이있음.
    :param title:
    :return:
    """
    pass


if __name__ == '__main__':
    opt = docopt(__doc__, version='write 0.1')

    if opt['new']:
        if opt["-p"] or opt["--page"]:
            make_entry(opt["<title>"], page_path)
        elif opt["-m"] or opt["--markdown"]:
            make_entry(opt["<title>"], post_path, 'md')
        else:
            make_entry(opt["<title>"], post_path, 'rst')
    elif opt['edit']:
        print("edit")
    elif opt["backup"]:
        print("backup")
    else:
        print(opt)
