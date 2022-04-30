import typer
from typing import Optional
from beerlog.core import add_beer_to_database, get_beers_from_database
from rich.table import Table
from rich.console import Console
from rich import print

main = typer.Typer(help="Beer Management Application")

console = Console()


@main.command()
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """
    Adds a new beer to database
    """
    if add_beer_to_database(name, style, flavor, image, cost):
        print("Beer added to database")
    else:
        print("Cannot add beer")


@main.command("list")
def list_beers(style: Optional[str] = None):
    """
    List beers in database
    """
    beers = get_beers_from_database(style)
    table = Table(
        title="Beerlog :beer_mug:" if not style else f"Beerlog {style}"
    )
    headers = [
        "id",
        "name",
        "style",
        "flavor",
        "image",
        "cost",
        "rate",
        "date",
    ]
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        beer.date = beer.date.strftime("%Y-%m-%d")
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)
