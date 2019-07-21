from invoke import Collection, task

from pathlib import Path

BASE_PATH = Path.cwd()
OUTPUT_PATH = BASE_PATH / "output"
CONF_FILE = BASE_PATH / "pelicanconf.py"
PUBLISH_CONF_FILE = BASE_PATH / "publishconf.py"


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
def fix(ctx):
    """Execute black"""
    ctx.run("black -l 80 .")


ns = Collection()
ns.add_task(clean)
ns.add_task(preview)
ns.add_task(pub)
ns.add_task(fix)
