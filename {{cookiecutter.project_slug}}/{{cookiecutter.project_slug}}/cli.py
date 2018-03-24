# -*- coding: utf-8 -*-

'''
cli
---

console script for {{cookiecutter.project_slug}}.
'''


import click
import sys


@click.command()
def main(args=None):
    '''
    {{cookiecutter.project_slug}} command line interface
    '''

    click.echo("update {{cookiecutter.project_slug}}.cli.main")
    return 0


def entry_point():
    '''
    required to make setuptools and click play nicely (context object)
    '''

    return sys.exit(main())  # add obj={} to create in context


if __name__ == "__main__":
    entry_point()
