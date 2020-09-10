import click

from src._01 import weather 
from src._02 import weathers 
from src._03 import forecast 
from src._04 import dailyforecast 



@click.group()
def cli():
    pass

cli.add_command(weather)
cli.add_command(weathers)
cli.add_command(forecast)
cli.add_command(dailyforecast)






if __name__ == "__main__":
    cli()