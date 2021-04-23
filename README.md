# Containerized test execution of API automation 

🚀 A repository for API testing using pytest framework

This repository contains an end-to-end automation framework for the containerized test execution of API automation using PyTest.

### Objective

The solution is designed to address the following objectives;

1.	To implement the generic API automation framework that can be reused for any type of API automation.
2.	To implement the containerized test execution that download and runnable with minimal efforts required to set up and execute.

### Pre-requisites

1. You need to have docker installed on your machine
2. OS: MacOS or Linux

## Steps to execute

### Checkout a GIT repository

In order to run a containerised test execution on your local machine, you need to download/clone this Git repository onto your local machine.

```bash
git clone rdhananjay7/pytestapitesting
```

Move to the project home directory

```
$ cd /Users/rdhananjay7/python-projects/api-testing
$ ls -ltr
total 312
-rwxr-xr-x   1 rdhananjay7  staff     305 Apr 22 01:52 pytest.ini
-rw-r--r--   1 rdhananjay7  staff     344 Apr 22 19:44 requirements.txt
drwxr-xr-x   3 rdhananjay7  staff      96 Apr 23 01:12 logs
drwxr-xr-x   5 rdhananjay7  staff     160 Apr 23 01:15 venv
-rw-r--r--   1 rdhananjay7  staff     163 Apr 23 01:35 Dockerfile
drwxr-xr-x  15 rdhananjay7  staff     480 Apr 23 15:35 archive
drwxr-xr-x   5 rdhananjay7  staff     160 Apr 23 16:26 bin
drwxr-xr-x  10 rdhananjay7  staff     320 Apr 23 16:28 ssd-cneos-api-suites
drwxr-xr-x   3 rdhananjay7  staff      96 Apr 23 16:33 report
-rw-r--r--   1 rdhananjay7  staff     841 Apr 23 17:08 output.json
-rw-r--r--   1 rdhananjay7  staff  137284 Apr 23 17:08 pytest_html_report.html
-rw-r--r--   1 rdhananjay7  staff    1824 Apr 23 17:51 README.md

```

### Build a Docker image

```bash
docker build -t sbdbapitests .
```

### Execute tests inside a Container

```bash
./bin/run_docker.sh
```

### Test Report 

Test Reports are available on host machine under /reports directory

```
$ pwd
/Users/rdhananjay7/python-projects/api-testing
$ cd report
$ ls -ltr
total 0
drwxr-xr-x  4 rdhananjay7  staff  128 Apr 23 16:33 report.2021.04.23-16.33.30
drwxr-xr-x  4 rdhananjay7  staff  128 Apr 23 17:55 report.2021.04.23-17.55.44
$ 
```

## Approach: 

In this approach;

1. We build a docker image, run a container on the fly and then run the tests in this container 
2. Build a docker image that has the latest python version
3. Copy or mount the test code onto this container
4. Install the requirements
5. Run a runner script that exports the required environment variables (credentials etc.) and then runs the tests inside a container
6. Report is saved to the mounted directory.
7. Running container is removed

### Framework Components:

1.	Logging
2.	Reporting
3.	Runner Scripts, to run the tests and to clean up the logs
4.	Command line support for parameterizing the run
5.	Properties file to set up the environment variables that can be sourced while running a runner script
