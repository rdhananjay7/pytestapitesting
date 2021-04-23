import logging as logger
from pytest import mark
import requests
import sbdb_query_params


class SBDBTests:
    # class variables
    PATH = "cad.api"

    @mark.sbdb
    def test_sbdb(self, app_config):
        """Test the SBDB Close GET api"""

        logger.info("Hitting an SBDB Close api for get response")
        response = requests.get(app_config.base_url + self.PATH, params=sbdb_query_params.get_sbdb)

        logger.info("Validating the response to check if status code == 200")
        assert response.status_code == 200
