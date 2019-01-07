import click
from clients import command as clients_commands

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}


cli.addCommand(clients_commands.all)
