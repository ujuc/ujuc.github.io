import re

from pathlib import Path
from subprocess import run as sub_run

import pendulum

from cleo.application import Application
from cleo.commands.command import Command
from cleo.helpers import argument


BASE_PATH = Path.cwd()
CONTENT_PATH = BASE_PATH / "content"
OUTPUT_PATH = BASE_PATH / "output"
CONF_FILE = BASE_PATH / "pelicanconf.py"
PUBLISH_CONF_FILE = BASE_PATH / "publishconf.py"


class PostCmd(Command):
    name = "post"
    description = "Make post template"
    arguments = [argument("title", "Post title")]

    def handle(self) -> int:
        title = self.argument("title")
        today = pendulum.now()

        slug = re.sub("[^\w\s가-힣]", "", title).lower().replace(" ", "-")
        date = f"{today.month}-{today.day}"
        post_date = today.to_datetime_string()

        file_name = f"{date}-{slug}.md"

        article = (
            f"Title: {title}\n"
            f"Date: {post_date}\n"
            f"Modified: {post_date}\n"
            "Category: \n"
            "Tags: \n"
            f"Slug: {slug}\n"
            "Summary: \n\n"
        )

        blog_path = CONTENT_PATH / "blog" / f"{today.year}"
        if not blog_path.is_dir():
            blog_path.mkdir(parents=True)

        post_path = blog_path / file_name

        with post_path.open("w") as post_file:
            post_file.write(article)

        self.line(f"Post crate -> {post_path}")

        return 0


class PreviewCmd(Command):
    name = "preview"
    description = "Start preview page server"

    def handle(self) -> int:
        return sub_run(
            "pelican --autoreload --listen", shell=True, check=True
        ).returncode


class CleanCmd(Command):
    name = "clean"
    description = "Clean up cache dir"

    def handle(self) -> int:
        return sub_run(
            f"rm -rf {OUTPUT_PATH} {BASE_PATH}/__pycache__ {BASE_PATH}/cache",
            shell=True,
            check=True,
        ).returncode


class BuildCmd(Command):
    """
    Build Blog Post
    """

    name = "build"
    description = "Build Blog Post"

    def handle(self) -> int:
        return sub_run(
            f"pelican -s {PUBLISH_CONF_FILE}", shell=True, check=True
        ).returncode


def run():
    app = Application("cli", "2.0")

    app.add(PostCmd())
    app.add(PreviewCmd())
    app.add(CleanCmd())
    app.add(BuildCmd())

    app.run()
