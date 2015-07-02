#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Oirign : http://nafiulis.me/making-a-static-blog-with-pelican.html
# edit: ujuc
'''write

Usage:
    write new [-p | --page] <title>
    write edit <title>
    write backup <title> <date>

-d --date       datetime change

'''



import sys
from docopt import docopt
from datetime import datetime

TEMPLATE = """
{title}
{hashes}

{date}
:category:
:tags:
:slug: {slug}
:summary:
{modified}

"""

post_path = "content/blog"
page_path = "content/pages"

def make_entry(title, path):
    today = datetime.today()
    # GTODO : 한국어를 영어로 변환하는 것이 필요
    slug = title.lower().strip().replace(' ', '-')
    file_create = "{0}/{1}-{2:0>2}-{3:0>2}-{4}.rst".format(path,
                                                           today.year,
                                                           today.month,
                                                           today.day, slug)
    date = ":date: {year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}"\
        .format(year=today.year, month=today.month, day=today.day,
                hour=today.hour, minute=today.minute)
    t = TEMPLATE.strip().format(
        title=title,
        hashes='#' * len(title) * 2,
        slug=slug,
        date=date,
        modified="")
    with open(file_create, 'w') as w:
        w.write(t)
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
    print(opt)

    if opt['new']:
        print("{0}, {1}, {2}, {3}".
              format(opt["new"], opt["-p"], opt["--page"], opt["<title>"]))
        if opt["-p"] or opt["--page"]:
            make_entry(opt["<title>"], page_path)
            print("page")
        make_entry(opt["<title>"], post_path)
    elif opt['edit']:
        print("edit")
    elif opt["backup"]:
        print("backup")
    else:
        print(opt)
    # if len(sys.argv) > 1:
    #     make_entry(sys.argv[1])
    # else:
    #     print("No title given")
