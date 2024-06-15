"""Docstring"""
import typer
from typing_extensions import Annotated

from {{ python_package_name }}.common.utils import get_logger

logger = get_logger(__name__)
cli = typer.Typer(add_completion=False)


@cli.command(help="{{ project_description }}")
def hello_world(
    name: Annotated[str, typer.Option(help="Your name.")] = "World",
) -> str:
    """Hello."""
    logger.info(f"Hello, {name}")
    return f"Hello, {name}"


if __name__ == "__main__":
    cli()
