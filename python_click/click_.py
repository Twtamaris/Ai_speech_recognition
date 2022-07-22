import click
import json
import pprint

@click.group('example')
@click.pass_context
@click.argument('json')

def example(ctx, json):
    """Wiil you marry me?"""
    
@example.command('love')
def typer():
    """Returns type of context object"""

def main():
    example(prog_name='i love you')

if __name__ == '__main__':
    main()