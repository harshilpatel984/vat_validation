#!/usr/bin/env python3
import connexion
from swagger_server import encoder
from .log import log


def main():
    log.info("#################################################")
    log.info("############## API Server Started ###############")
    log.info("#################################################")
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'VAT Validattion'}, pythonic_params=True)
    app.run(port=8080, debug=False)


if __name__ == '__main__':
    main()
