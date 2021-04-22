import requests


class Config:

    def __init__(self, env, auth):
        self.base_url = {
            'master': "https://ssd-api.jpl.nasa.gov/"
        }[env]

        # Logic to initialize session id, xsrf_token etc. goes here,
        # that can be reused across the test execution.

        # e.g. username and passwords can be initialized for various authentications
        # based on the command line options received

        self.username = {
            'basic': "ssd-cneos-api-suites",
            'ldap': "admin",
            'ntlm': "nt_admin"
        }[auth]

        self.password = {
            'basic': "ssd-cneos-api-suites",
            'ldap': "admin",
            'ntlm': "nt_admin"
        }[auth]

    def get_session_id(self, base_url, username, password):
        # a helper method to generate a session id
        pass

    def get_session(self, url, username, password):
        # a helper method to initialize a session by passing command line options
        pass

    def get_xsrf_token(self, base_url, username, password, session_id):
        # a helper function to retrieve an xsrf token
        pass
