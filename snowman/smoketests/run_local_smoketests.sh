echo "Running Local Snowman Smoketests"

export SNOWMAN_URL="http://localhost:8080";python -m unittest -v $SMOKETESTS/tests/smoke_tests.py