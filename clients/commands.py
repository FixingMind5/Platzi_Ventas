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
@click.argument('cid',
                type=str)
@click.pass_context
def update(ctx, cid):
    """Updates client"""
    client_service = ClientService(ctx.obj['clients_table'])

    client_list = client_service.listClients()

    client = [client for client in client_list if client['uid'] == cid]

    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.updateC(client)

        click.echo("READY!!!")
    else:
        click.echo("Client {} not found".format(client))


def _update_client_flow(client):
    click.echo('Leave it empty if you dont want to modify it')

    client.name = click.prompt("New name", type=str, default=client.name)
    client.company = click.prompt("New company", type=str, default=client.company)
    client.email = click.prompt("New email", type=str, default=client.email)
    client.position = click.prompt("New position", type=str, default=client.position)

    return client


@clients.command()
@click.argument('cid',
                type=str)
@click.pass_context
def delete(ctx, cid):
    """Deletes client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.listClients()
    dClient = [dClient for dClient in client_list if dClient['uid'] == cid]

    if dClient:
        client_service.deleteClient(dClient)
        click.echo('Client already deleted')
    else:
        click.echo("Client did't exists")


all = clients
