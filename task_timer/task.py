import click
@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hi(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")


@click.command()
def initdb():
    click.echo('Initialized the database')

@click.command()
def dropdb():
    click.echo('Dropped the database')

