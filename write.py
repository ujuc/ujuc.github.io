#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Oirign : http://nafiulis.me/making-a-static-blog-with-pelican.html
# edit: ujuc

import sys
from datetime import datetime

TEMPLATE = """
{title}
{hashes}

:date: {year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}
:modified:
:category:
:tags:
:slug: {slug}
:summary:


"""

file_path = "content/blog"


def make_entry(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    file_create = "{0}/{1}-{2:0>2}-{3:0>2}-{4}.rst".format( file_path,
        today.year, today.month, today.day, slug)
    t = TEMPLATE.strip().format(
        title=title,
        hashes='#' * len(title),
        year=today.year,
        month=today.month,
        day=today.day,
        hour=today.hour,
        minute=today.minute,
        slug=slug)
    with open(file_create, 'w') as w:
        w.write(t)
    print("File created -> " + file_create)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        make_entry(sys.argv[1])
    else:
        print("No title given")
