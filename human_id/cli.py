import click
from human_id import generate_id


@click.command()
@click.option("--words", type=int, default=4)
@click.option("--sep", default="-")
@click.option("--seed")
@click.option("--count", type=int, default=1)
def main(words, sep, seed, count):
    for i in range(count):
        click.echo(generate_id(separator=sep, seed=seed, word_count=words))
