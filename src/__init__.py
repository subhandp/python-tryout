import click

from src._01 import weather 


@click.group()
def cli():
    pass

cli.add_command(weather)
# cli.add_command(uppercase)
# cli.add_command(capitalize)


if __name__ == "__main__":
    cli()