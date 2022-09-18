from dataclasses import replace
from ppadb.client import Client as AdbClient
import re

client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()
device = devices[0]

device.shell('logcat -c')
text = device.shell('logcat -d | grep "IPWebcam"')
strings = text.split('\n')

if len(text) > 0:
    print("실시간 카메라 사용 감지")
else:
    print("실시간 카메라 중이 아님")

cam_client = []

for word in strings:
    if "Mozilla" in word:
        cam_client.append(word)
