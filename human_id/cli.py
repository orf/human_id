import click
from human_id import generate_id


@click.command()
@click.option("--words", type=int, default=4, help="Number of words")
@click.option("--sep", default="-", help="Separator")
@click.option("--seed", help="Seed to use")
@click.option("--count", type=int, default=1, help="Number of IDs to generate")
def main(words, sep, seed, count):
    """
    Generate human readable IDs
    """
    for i in range(count):
        click.echo(generate_id(separator=sep, seed=seed, word_count=words))
