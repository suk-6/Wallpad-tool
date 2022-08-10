from ppadb.client import Client as AdbClient
import asyncio

client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()
device = devices[0]

class adb_tool:
    def t_netstat(self):
        r_netstat = device.shell("netstat -tul")
        return "사용 중인 포트를 점검합니다.\n"+r_netstat

tool = adb_tool()