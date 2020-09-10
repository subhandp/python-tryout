import click

# from src._01 import lowercase,uppercase,capitalize 


@click.group()
def cli():
    pass

# cli.add_command(lowercase)
# cli.add_command(uppercase)
# cli.add_command(capitalize)




if __name__ == "__main__":
    cli()