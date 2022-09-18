from dataclasses import replace
from ppadb.client import Client as AdbClient
import re

client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()
device = devices[0]

app_vpn = ["wireguard", "openvpn"]
app_camara = ["cam"]

app_list = app_vpn + app_camara

stats_origin = device.shell("dumpsys procstats --hours 3")
stats_n = stats_origin.split('\n')

stats_list = []
stats_output = []

i = 0

while i < len(app_list):
    for stats_w in stats_n:
        if app_list[i] in stats_w:
            stats_list.append(stats_w)
    i += 1

i = 0
j = 0

search_app = re.findall("[a-z]+[.]+[a-z]+[.]+[a-z]+", str(stats_list))

shell_output = device.shell("pm list packages -f "+search_app[i])
label_strip = shell_output.strip("package:")
label_sub = str(re.sub("=[a-z]+[.]+[a-z]+[.]+[a-z]+", "", label_strip))

aapt_origin = device.shell("aapt dump badging "+label_sub)
aapt_n = aapt_origin.split("\n")

print(aapt_origin)
