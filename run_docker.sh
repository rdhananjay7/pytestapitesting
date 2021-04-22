
set -x

docker run --name testapis \
-it -v $(pwd)/report:/apitests/report sbdbapitests \
py.test --html-report=/apitests/report/report.html

docker rm testapis