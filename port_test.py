from dataclasses import replace
from ppadb.client import Client as AdbClient
import re

client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()
device = devices[0]

text = device.shell("netstat -tul")
strings = text.split('\n')

port_list = []
port_output = []

for word in strings:
    if "LISTEN" in word:
        port_list.append(word)

port_listen = re.findall(":[0-9]+", str(port_list))

for i in port_listen:
    temp = i.replace(':', '')
    port_output.append(temp)

print(port_output)
