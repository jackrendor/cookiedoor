# cookiedoor
## Introduction
Cookie door is a php backdoor that allows you to execute remote shell command on the webserver.
Commands are sent via cookie.

## How to use
You can place the `payload.php` script code inside another existing script to hide it or just upload it creating a new file.

## How does it work?
The webshell checks for 2 cookie valuse:
- `d` (delimeter) that contains a random string, used to delimeter the content of output.
- `c` (command) that contains the command to be executed by the webshell.

Values will be encoded and decoded in the following way: `base64 -> bzip -> base64`.

The "delimeter" values are used (by the client/handler) to know where to search the output of the command.

If you place the script inside an existing page, it will look up for the delimetes and returns what's between them. Easy. 

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

