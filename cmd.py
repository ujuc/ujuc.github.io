#!/usr/bin/env python3
import subprocess
from pathlib import Path

import click
import kroman
import pendulum

BASE_PATH = Path.cwd()
CONTENT_PATH = BASE_PATH / "content"
OUTPUT_PATH = BASE_PATH / "output"
CONF_FILE = BASE_PATH / "pelicanconf.py"
PUBLISH_CONF_FILE = BASE_PATH / "publishconf.py"


@click.group()
def cli():
    """Pelican Helper"""
    pass


@cli.group()
def new():
    """Make new post or page."""
    pass


@new.command()
@click.option("-r", "--rst", is_flag=True, help="Post format reStructuredText")
@click.argument("title")
def post(title, rst):
    """Make new post."""
    today = pendulum.now()

    slug = kroman.parse(title).lower().strip().replace(" ", "_")
    date = today.to_date_string()
    post_date = today.to_datetime_string()
    file_title = f"{date}-{slug}"

    if rst:
        file_name = f"{file_title}.rst"
        hashes = "#" * len(title) * 2

        article = (
            f"{title}\n"
            f"{hashes}\n\n"
            f":date: {post_date}\n"
            f":category: \n"
            f":tags: \n"
            f":slug: {slug}\n"
            f":summary: \n"
        )
    else:
        file_name = f"{file_title}.md"

        article = (
            f"Title: {title}\n"
            f"Date: {post_date}\n"
            f"Category: \n"
            f"Tags: \n"
            f"Slug: {slug}\n"
            f"Summary: \n\n"
        )

    blog_path = CONTENT_PATH / "blog"
    if not blog_path.is_dir():
        blog_path.mkdir(parents=True)

    post_path = blog_path / file_name
    with post_path.open("w") as post_file:
        post_file.write(article)

    print(f"File created -> {post_path}")


@new.command()
def page():
    """Make new page."""
    print("Page command feature~~~~~~~~~~. Next year?")


def serve():
    subprocess.run(["pelican", "-l"])


@cli.command()
def preview():
    """Preview web page using Pelican server"""
    subprocess.run(
        ["pelican", CONTENT_PATH, "-o", OUTPUT_PATH, "-s", CONF_FILE]
    )
    serve()


@cli.command()
def pub():
    subprocess.run(
        ["pelican", CONTENT_PATH, "-o", OUTPUT_PATH, "-s", PUBLISH_CONF_FILE]
    )
    subprocess.run(
        [
            "ghp-import",
            "-m",
            "Generate Pelican site",
            "-b",
            "master",
            OUTPUT_PATH,
        ]
    )
    subprocess.run(["git", "push", "origin", "master"])


@cli.command()
def clean():
    subprocess.run(
        [
            "rm",
            "-rf",
            OUTPUT_PATH,
            BASE_PATH / "__pycache__",
            BASE_PATH / "cache",
        ]
    )


if __name__ == "__main__":
    cli()
