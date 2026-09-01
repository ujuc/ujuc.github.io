import subprocess
import sys
import unittest
from importlib.metadata import version
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

import pendulum
from cleo.testers.command_tester import CommandTester

from cli import main

RUN_CLI = "from cli.main import run; run()"


def run_cli(path: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-c", RUN_CLI, *args],
        cwd=path,
        capture_output=True,
        check=False,
        text=True,
    )


class CliTest(unittest.TestCase):
    def test_clean_removes_generated_directories(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            generated_paths = [root / "output", root / "__pycache__", root / "cache"]
            for path in generated_paths:
                path.mkdir()
                (path / "generated").touch()

            with (
                patch.object(main, "BASE_PATH", root),
                patch.object(main, "OUTPUT_PATH", root / "output"),
            ):
                result = CommandTester(main.CleanCmd()).execute()

            self.assertEqual(result, 0)
            self.assertTrue(all(not path.exists() for path in generated_paths))

    def test_post_does_not_overwrite_existing_file(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            first = run_cli(root, "post", "기존 글")
            self.assertEqual(first.returncode, 0, first.stderr)

            post_path = next(root.glob("content/blog/*/*.md"))
            post_path.write_text("existing content", encoding="utf-8")

            second = run_cli(root, "post", "기존 글")

            self.assertNotEqual(second.returncode, 0)
            self.assertEqual(post_path.read_text(encoding="utf-8"), "existing content")

    def test_post_uses_seoul_timezone(self) -> None:
        machine_now = pendulum.datetime(2025, 12, 31, 15, 30, tz="UTC")
        seoul_now = pendulum.datetime(2026, 1, 1, 0, 30, tz="Asia/Seoul")

        with TemporaryDirectory() as directory:
            root = Path(directory)
            with (
                patch.object(main, "CONTENT_PATH", root / "content"),
                patch.object(
                    main.pendulum,
                    "now",
                    side_effect=lambda timezone=None: (
                        seoul_now if timezone == "Asia/Seoul" else machine_now
                    ),
                ),
            ):
                result = CommandTester(main.PostCmd()).execute('"서울 시간"')

            self.assertEqual(result, 0)
            post_path = root / "content/blog/2026/1-1-서울-시간.md"
            self.assertTrue(post_path.is_file())
            self.assertIn(
                "Date: 2026-01-01 00:30", post_path.read_text(encoding="utf-8")
            )

    def test_cli_version_matches_package_version(self) -> None:
        with TemporaryDirectory() as directory:
            result = run_cli(Path(directory), "--version")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(version("ujuc.github.io"), result.stdout)


if __name__ == "__main__":
    unittest.main()
