import logging as logger
from pytest import mark
import requests
import fireball_query_params


class FireballTests:

    # class variables
    PATH = "fireball.api"

    @mark.fireball
    def test_fireball(self, app_config):
        """Test the fireball GET api for fetching most recent20 records"""

        logger.info("Hitting an Fireball api for fetching the most recent 20 records")
        response = requests.get(app_config.base_url + self.PATH, params=fireball_query_params.latest_twenty_records)

        logger.info("Validating the response to check if status code == 200")
        assert response.status_code == 200
