import re
import shutil
import subprocess
import sys
from importlib.metadata import version
from pathlib import Path
from typing import ClassVar

import pendulum
from cleo.application import Application
from cleo.commands.command import Command
from cleo.helpers import argument
from cleo.io.inputs.argument import Argument

BASE_PATH = Path.cwd()
CONTENT_PATH = BASE_PATH / "content"
OUTPUT_PATH = BASE_PATH / "output"
PUBLISH_CONF_FILE = BASE_PATH / "publishconf.py"


class PostCmd(Command):
    name = "post"
    description = "Make post template"
    arguments: ClassVar[list[Argument]] = [argument("title", "Post title")]

    def handle(self) -> int:
        title = self.argument("title")
        today = pendulum.now("Asia/Seoul")

        slug = (
            re.sub(r"[^\w\s가-힣]", "", title, flags=re.UNICODE)
            .lower()
            .replace(" ", "-")
        )
        date = f"{today.month}-{today.day}"
        post_date = today.format("YYYY-MM-DD HH:mm")

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
        blog_path.mkdir(parents=True, exist_ok=True)

        post_path = blog_path / file_name

        with post_path.open("x", encoding="utf-8") as post_file:
            post_file.write(article)

        self.line(f"Post created -> {post_path}")

        return 0


class PreviewCmd(Command):
    name = "preview"
    description = "Start preview page server"

    def handle(self) -> int:
        return subprocess.run(
            [sys.executable, "-m", "pelican", "--autoreload", "--listen"],
            check=True,
        ).returncode


class CleanCmd(Command):
    name = "clean"
    description = "Clean up cache dir"

    def handle(self) -> int:
        for path in (OUTPUT_PATH, BASE_PATH / "__pycache__", BASE_PATH / "cache"):
            if path.exists():
                shutil.rmtree(path)

        return 0


class BuildCmd(Command):
    """
    Build Blog Post
    """

    name = "build"
    description = "Build Blog Post"

    def handle(self) -> int:
        return subprocess.run(
            [sys.executable, "-m", "pelican", "-s", PUBLISH_CONF_FILE],
            check=True,
        ).returncode


def run() -> int:
    app = Application("cli", version("ujuc.github.io"))

    app.add(PostCmd())
    app.add(PreviewCmd())
    app.add(CleanCmd())
    app.add(BuildCmd())

    return app.run()
