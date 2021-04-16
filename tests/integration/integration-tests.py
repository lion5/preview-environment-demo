import requests
import sys

EXPECTED_RESPONSE = "Hello World!"


def check_response(url):
    response = requests.get(url)

    return response.status_code == 200 and response.text == EXPECTED_RESPONSE


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Required parameter url missing.")
        sys.exit(1)

    if not check_response(sys.argv[1]):
        print("Checks failed.")
        sys.exit(1)
    else:
        print("Checks passed.")
