import json
import urllib3

http = urllib3.PoolManager()


def get_external_ip():
    request = http.request('GET', 'http://ip.jsontest.com')

    assert request.status < 300, "Could not retrieve external IP address"

    result = json.loads(request.data)
    ip = result["ip"]

    return ip


def main():
    ip = get_external_ip()
    print("Your external IP address is {}".format(ip))


if __name__ == "__main__":
    main()
