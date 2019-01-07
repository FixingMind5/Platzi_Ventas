from clients.models import Client

import csv

class ClientService:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self, client):
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.toDict())

    def listClients(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())

            return list(reader)

    def updateC(self, updatedClient):
        clients = self.listClients()

        updatedClients = []

        for client in clients:
            if client['uid'] == updatedClient.uid:
                updatedClients.append(updateClient.toDict())
            else:
                updatedClients.append(client)

        self._saveToDisk(updatedClients)

    def _saveToDisk(clients):
        tmpTable = self.table_name + '.tmp'
        with open(tmpTable) as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            write.writerows(clients)

            os.remove(self.table_name)
            os.remove(tmpTable, self.table_name)
