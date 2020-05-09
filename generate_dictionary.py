import click
import io

from jinja2 import Environment


@click.command()
@click.argument("nouns", type=click.File(mode="r"), default="nouns.txt")
@click.argument("adjectives", type=click.File(mode="r"), default="adjectives.txt")
@click.argument("verbs", type=click.File(mode="r"), default="verbs.txt")
@click.option("--remove-list", is_flag=True, help="Remove leading numbers")
def generate(
    nouns: io.TextIOBase,
    adjectives: io.TextIOBase,
    verbs: io.TextIOBase,
    remove_list: bool,
):
    template = Environment().from_string(dictionary_template)

    def _process(things):
        words = (w.split(" ", 1)[1] if remove_list else w for w in things if w.strip())
        return [f'    "{n.strip().lower()}",' for n in words]

    items = [
        ("nouns", _process(nouns)),
        ("adjectives", _process(adjectives)),
        ("verbs", _process(verbs)),
    ]

    click.echo(template.render(items=items).strip())
    for name, value in items:
        click.echo(f"{len(value)} {name}", err=True)


dictionary_template = """
{% for name, value in items %}
{{ name }} = (
{{ value|join("\n") }}
)
{% endfor %}
"""

if __name__ == "__main__":
    generate()
