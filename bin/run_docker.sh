#!/bin/bash

set -x

# We can source the env.sh file here in case we want to set the environment variables

current_time=$(date "+%Y.%m.%d-%H.%M.%S")
report_file_name="report".$current_time

echo "Test report can be found under: " "$report_file_name"

docker run --name testapis \
-it -v $(pwd)/report:/apitests/report sbdbapitests \
py.test --html-report=/apitests/report/"$report_file_name"

docker rm testapis