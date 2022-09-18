from time import sleep
from ppadb.client import Client as AdbClient
import re
from dataclasses import replace

client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()
device = devices[0]


class adb_tool:
    def t_netstat(self):
        port_origin = device.shell("netstat -tul")
        port_n = port_origin.split('\n')

        port_list = []
        port_output = []

        for port_w in port_n:
            if "LISTEN" in port_w:
                port_list.append(port_w)

        port_listen = re.findall(":[0-9]+", str(port_list))

        for i in port_listen:
            temp = i.replace(':', '')
            port_output.append(temp)

        r_netstat = str(port_output)+"\n"
        return "사용 중인 포트를 점검합니다. \n현재 개방 중인 포트: "+r_netstat

    def t_dumpsys_memory(self):
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

        search_app = re.findall("[a-z]+[.]+[a-z]+[.]+[a-z]+", str(stats_list))

        # shell_output = device.shell("pm list packages -f "+search_app[i])
        # label_strip = shell_output.strip("package:")
        # label_sub = str(re.sub("=[a-z]+[.]+[a-z]+[.]+[a-z]+", "", label_strip))

        i = 0

        while i < len(search_app):
            if search_app[i] == "com.wireguard.android":
                search_app[i] = "WireGuard VPN"
            if search_app[i] == "com.pas.webcam":
                search_app[i] = "IP Webcam"
            i += 1

        r_dumpsys_memory = str(search_app)+"\n"
        return "최근 3시간 동안 실행된 앱을 점검합니다. \n비정상적인 앱 리스트: "+r_dumpsys_memory

    def t_camara(self):
        device.shell('logcat -c')
        sleep(1)
        adb_out = device.shell('logcat -d | grep "IPWebcam"')
        adb_str = adb_out.split('\n')

        cam_client = []

        if len(adb_out) > 0:
            for client_line in adb_str:
                if "Mozilla" in client_line:
                    cam_client.append(client_line)
            return ("실시간 카메라 사용 검사 중... \n검사 결과: 실시간 카메라 사용 감지! \n접속 클라이언트: \n"+str(cam_client[0]))
        else:
            return ("실시간 카메라 사용 검사 중... \n검사 결과: 실시간 카메라 중이 아님")


tool = adb_tool()
