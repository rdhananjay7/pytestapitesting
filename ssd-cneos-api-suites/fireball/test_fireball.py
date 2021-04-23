import logging as logger
from pytest import mark
import requests
import fireball_query_params


class FireballTests:
    # class variables
    PATH = "fireball.api"
    VERSION = "1.0"
    SUCCESS = 200

    @mark.fireball
    def test_fireball(self, app_config):
        """Test the fireball GET api for fetching most recent20 records"""

        logger.info("Test for checking if Fireball API service is up and running")
        response = requests.get(app_config.base_url + self.PATH, params=fireball_query_params.get_fireball_health_check)

        logger.info("Validating the response to check if status code == 200")
        assert response.status_code == self.SUCCESS

    @mark.fireball
    def test_sbdb_version(self, app_config):
        """Test the Fireball API Version"""

        logger.info("Test for checking if Fireball API version {}".format(self.VERSION))
        response = requests.get(app_config.base_url + self.PATH, params=fireball_query_params.get_fireball_health_check)

        json_data = response.json()
        logger.info("Validating the response to check if Version == {}".format(self.VERSION))

        assert json_data["signature"]["version"] == self.VERSION
