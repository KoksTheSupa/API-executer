from dataclasses import dataclass
import xmlrpc.client

from script.log import logger


@dataclass
class AccInfo:
    odoo_url: str = 'http://localhost:8069'
    username: str = 'b@b.b'
    password: str = 'admin'
    db: str = 'Admin'


class OdooClient:
    def __init__(self, info: AccInfo):
        self._info = info
        common = xmlrpc.client.ServerProxy(
            f'{self._info.odoo_url}/xmlrpc/2/common')
        self.uid = common.authenticate(
            self._info.db, self._info.username, self._info.password, {})
        self.models = xmlrpc.client.ServerProxy(
            f'{self._info.odoo_url}/xmlrpc/2/object')

    def get_odoo_id(self, model_name, args_name):
        """Get record id on odoo model"""
        odoo_id = self.models.execute_kw(self._info.db, self.uid,
                                         self._info.password, model_name,
                                         'search', [
                                             [['name', '=', [args_name]]]],
                                         {'limit': 1})
        return odoo_id

    def create_odoo_model(self, model_name, args):
        """Create record on odoo"""
        ids = self.models.execute_kw(
            self._info.db, self.uid, self._info.password, model_name, 'create', [args])
        logger.info(f"In {model_name} was created odoo id: {ids}")
        print(f"Created record in {model_name} ended successful")


odoo_client = OdooClient(AccInfo())
