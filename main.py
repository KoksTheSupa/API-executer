from script.client import AccInfo, OdooClient
from script.model import OdooPlanet, OdooPartner
from script.utils import YAMLReader


def main():
    while True:
        configure_path = YAMLReader().check_path()
        if configure_path:
            break
    account_info = YAMLReader().read_yaml(configure_path).get("ODOO")
    account = AccInfo(account_info.get("odoo_url"), account_info.get(
        "username"), account_info.get("password"), account_info.get("db"))
    url_info = YAMLReader().read_yaml('configure.yaml').get("URL")
    partner_url = url_info.get('PARTNER')
    planet_url = url_info.get('PLANET')
    image_url = url_info.get('IMAGE')
    odoo_client = OdooClient(account)

    planet_args = OdooPlanet('res.planet', planet_url).get_args()
    odoo_client.create_odoo_model(
        "res.planet", planet_args)

    partner_args = OdooPartner('res.partner', partner_url).get_args(image_url)
    odoo_client.create_odoo_model(
        "res.partner", partner_args)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
