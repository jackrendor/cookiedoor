# cookiedoor
## Introduction
Cookie door is a php backdoor that allows you to execute remote shell command on the webserver.
Commands are sent via cookie.

## How to use
You can place the `payload.php` script code inside another existing script to hide it or just upload it creating a new file.

## Configure
The handler works with python3, so you need to install dependecies.
```sh
sudo apt install python3
sudo pip3 install requests
```

## Usage
Just run the script and pass to it the url target.
### Example:
```sh
./cookiedoor http://127.0.0.1:8080/payload.php
```

