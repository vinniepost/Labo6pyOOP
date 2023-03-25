# PingDing

PingDing is a simple Python command-line tool for pinging servers and generating an HTML report of their status. The tool can also be used to manage a list of servers to ping.
## Requirements

    Python 3.x
    ping3 module (pip3 install ping3)
    keyboard module (pip3 install keyboard)
    jinja2 module (pip3 install jinja2)

## Usage

To run PingDing, open a terminal or command prompt and navigate to the directory containing the pingding.py file. Then, run one of the following commands:

    To ping all servers in the server list and generate an HTML report: python3 pingding.py check
    To enter management mode, which allows you to add, remove, or view servers in the server list: python3 pingding.py management
    To ping a specific server by name or IP address: python3 pingding.py [server name or IP]

## Management mode

In management mode, you can perform the following actions:

    Add a new server to the server list: python3 pingding.py management 1
    Remove an existing server from the server list: python3 pingding.py management 2
    View the current server list: python3 pingding.py management 3

## Adding a new server

To add a new server to the server list, use the following command:

python3 pingding.py management 1 [server name] [server IP address or hostname]

If you don't provide the server name and IP address as arguments, the tool will prompt you to enter them.
Removing a server

### To remove an existing server from the server list, use the following command:

python3 pingding.py management 2 [server name]

If you don't provide the server name as an argument, the tool will prompt you to enter it.
## Viewing the server list

### To view the current server list, use the following command:

python3 pingding.py management 3

## Acknowledgments

PingDing uses the following open-source libraries:

    ping3: https://pypi.org/project/ping3/
    keyboard: https://pypi.org/project/keyboard/
    jinja2: https://pypi.org/project/Jinja2/
