# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestVatController(BaseTestCase):
    """VatController integration test stubs"""

    def test_vat_vat_number_get(self):
        """Test case for vat_vat_number_get

        validate vat number
        """
        response = self.client.open(
            '/vat/{vat_number}'.format(vat_number='vat_number_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
