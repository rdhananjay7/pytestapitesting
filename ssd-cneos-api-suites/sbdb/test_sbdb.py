import json
import logging as logger
from pytest import mark
import requests
import sbdb_query_params
import urllib.request, time


class SBDBTests:
    # class variables
    PATH = "cad.api"
    VERSION = "1.3"
    SUCCESS = 200

    @mark.sbdb
    def test_sbdb(self, app_config):
        """Test the SBDB Close GET api service"""

        logger.info("Test for checking if SBDB API service is up and running")
        response = requests.get(app_config.base_url + self.PATH, params=sbdb_query_params.get_sbdb_health_check)

        logger.info("Validating the response to check if status code  is {}".format(self.SUCCESS))
        assert response.status_code == self.SUCCESS

    @mark.sbdb
    def test_sbdb_version(self, app_config):
        """Test the SBDB Close API Version"""

        logger.info("Test for checking if SBDB API version {}".format(self.VERSION))
        response = requests.get(app_config.base_url + self.PATH, params=sbdb_query_params.get_sbdb_health_check)

        json_data = response.json()
        logger.info("Validating the response to check if Version == {}".format(self.VERSION))

        assert json_data["signature"]["version"] == self.VERSION
