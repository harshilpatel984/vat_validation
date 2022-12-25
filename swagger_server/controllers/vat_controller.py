import connexion
import six
import requests


from ..log import log
from swagger_server import util
from flask import jsonify


def vat_vat_number_get(vat_number):  # noqa: E501
    """validate vat number

     # noqa: E501

    :param vat_number: vat number which needs to be validate
    :type vat_number: str

    :rtype: None
    """
    log.info("Vat Number:{}".format(vat_number))
    url = "https://api.vatcomply.com/vat?vat_number={0}".format(vat_number)
    payload = {}
    headers = {}
    print(url)
    response = requests.request("GET", url,
                                headers=headers, data=payload)
    log.info("API Response Code:{}".format(response.status_code))
    log.info("API Response:{}".format(response.text))
    return jsonify(response.json()), response.status_code
