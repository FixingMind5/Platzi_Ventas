import click


@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a new client"""
    pass


@clients.command()
@click.pass_context
def list(ctx):
    """list all clients"""
    pass


@clients.command()
@click.pass_context
def update(ctx, cid):
    """Updates client"""
    pass


@clients.command()
@click.pass_context
def delete(ctx, cid):
    """Deletes client"""
    pass


all = clients()
