echo "Running Local Snowman Smoketests"

export SNOWMAN_URL="http://localhost:8080";python3 -m unittest -v $SMOKETESTS/tests/smoke_tests.py