import xmlrpc.client


class SW():
    url = 'http://localhost:8069'
    username = 'b@b.b'
    password = 'admin'
    db = 'Admin'

    def __init__(self, url, username, password, db):
        common = xmlrpc.client.ServerProxy(
            f'{url}/xmlrpc/2/common')
        self.uid = common.authenticate(
            db, username, password, {})
        self.models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')


def main():
    url = 'http://localhost:8069'
    username = 'b@b.b'
    password = 'admin'
    db = 'Admin'
    SW(url, username, password, db)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
