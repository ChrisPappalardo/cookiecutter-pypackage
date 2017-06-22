# -*- coding: utf-8 -*-

'''
cli
---

console script for {{cookiecutter.project_slug}}.
'''

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import sys
{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.command()
def main(args=None):
    '''
    {{cookiecutter.project_slug}} command line interface
    '''

    click.echo("update {{cookiecutter.project_slug}}.cli.main")
    return 0
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
def main():
    '''
    {{cookiecutter.project_slug}} command line interface.
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print('Arguments: ' + str(args._))
    print('Replace this message by putting your code into '
          '{{cookiecutter.project_slug}}.cli.main')
    return 0
{%- endif %}

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
