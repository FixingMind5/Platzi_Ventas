import click
from clients.services import ClientService
from clients.models import Client

@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.option('-n', '--name',
              type=str,
              prompt=True,
              help='The client name')
@click.option('-c', '--company',
              type=str,
              prompt=True,
              help='The client company')
@click.option('-e', '--email',
              type=str,
              prompt=True,
              help='the client e-mail')
@click.option('-p', '--position',
              type=str,
              prompt=True,
              help='The client position')
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a new client"""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """list all clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    clients_list = client_service.listClients()

    click.echo('# ID  |  NAME |  COMPANY  |  EMAIL  |  POSITION')
    click.echo('*' * 100)

    for client in clients_list:
        click.echo("{uid}  |  {name}  |  {company}  |  {email}  |  {position}".format(
        uid=client['uid'],
        name=client['name'],
        company=client['company'],
        email=client['email'],
        position=client['position']
        ))


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


all = clients
