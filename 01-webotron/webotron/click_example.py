import click

@click.group()
def cli():
    "Example Code for Click"
    pass

@cli.command('initdb')
def initdb():
    "Initialize Database"
    click.echo("Initialization Done")

@cli.command('dropdb')
def dropdb():
    "Dropping Database"
    click.echo("Dropped Database")


if __name__ == '__main__':
    cli()
