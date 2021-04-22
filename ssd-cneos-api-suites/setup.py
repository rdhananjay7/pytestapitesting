from setuptools import setup, find_packages

setup(name='sdbdapitesting',
      version='1.0',
      description="Practice API testing",
      author='Dhananjay Argade',
      author_email='rdhananjay7@yahoo.co.in',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          "pytest==6.2.3",
          "pytest-html-reporter==0.2.5",
          "requests==2.25.1",
          "requests-oauthlib==1.3.0"
      ]
      )
