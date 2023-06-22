import time
from subprocess import check_output
from xml.etree.ElementTree import fromstring
from ipaddress import IPv4Interface, IPv6Interface
import socket
import os


def getNics():
    cmd = 'wmic.exe nicconfig where "IPEnabled  = True" get ipaddress,MACAddress,IPSubnet,DNSHostName,Caption,DefaultIPGateway /format:rawxml'
    xml_text = check_output(cmd, creationflags=8)
    xml_root = fromstring(xml_text)

    nics = []
    keyslookup = {
        'DNSHostName': 'hostname',
        'IPAddress': 'ip',
        'IPSubnet': '_mask',
        'Caption': 'hardware',
        'MACAddress': 'mac',
        'DefaultIPGateway': 'gateway',
    }

    for nic in xml_root.findall("./RESULTS/CIM/INSTANCE"):
        # parse and store nic info
        n = {
            'hostname': '',
            'ip': [],
            '_mask': [],
            'hardware': '',
            'mac': '',
            'gateway': [],
        }
        for prop in nic:
            name = keyslookup[prop.attrib['NAME']]
            if prop.tag == 'PROPERTY':
                if len(prop):
                    for v in prop:
                        n[name] = v.text
            elif prop.tag == 'PROPERTY.ARRAY':
                for v in prop.findall("./VALUE.ARRAY/VALUE"):
                    n[name].append(v.text)
        nics.append(n)

        # creates python ipaddress objects from ips and masks
        for i in range(len(n['ip'])):
            arg = '%s/%s' % (n['ip'][i], n['_mask'][i])
            if ':' in n['ip'][i]:
                n['ip'][i] = IPv6Interface(arg)
            else:
                n['ip'][i] = IPv4Interface(arg)
        del n['_mask']

    return nics


def getIP():
    import subprocess
    # file and directory listing
    returned_text = subprocess.check_output("ipconfig/all", shell=True, universal_newlines=True)
    # print("dir command to list file and directory")
    return(returned_text)

def yourIP():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return(IPAddr)
def lanIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
def resIP():
    os.system('ipconfig/release')
    time.sleep(5)
    os.system('ipconfig/renew')




# a = ""
# nics = getNics()
# for nic in nics:
#     for k, v in nic.items():
#          a = a + '<p><a style=\"color: Blue\"> %s :</a> <a> %s</a></p> ' % (k, v)
#             a = a + "<p style=\"color: Blue; font-size:10pt; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> %s : %s </p>" % (k, v)+"\n"
# self.uic.textEdit.setText("Windows IP Configuration\nHost Name . . . . . . . . . . . . : CanhPro\nPrimary Dns Suffix  . . . . . . . :\nNode Type . . . . . . . . . . . . : Hybrid\nIP Routing Enabled. . . . . . . . : No\nWINS Proxy Enabled. . . . . . . . : No\n\nEthernet adapter Radmin VPN:\n\nConnection-specific DNS Suffix  . :\nDescription . . . . . . . . . . . : Famatech RadminVPN Ethernet Adapter\nPhysical Address. . . . . . . . . : 02-50-35-C7-A2-2F\nDHCP Enabled. . . . . . . . . . . : No\nAutoconfiguration Enabled . . . . : Yes\nIPv6 Address. . . . . . . . . . . : fdfd::1ad9:feb0(Preferred)\nLink-local IPv6 Address . . . . . : fe80::808f:b84a:fbba:5928%11(Preferred)\nIPv4 Address. . . . . . . . . . . : 26.217.254.176(Preferred)\nSubnet Mask . . . . . . . . . . . : 255.0.0.0\nDefault Gateway . . . . . . . . . : 26.0.0.1\nDHCPv6 IAID . . . . . . . . . . . : 822235189\nDHCPv6 Client DUID. . . . . . . . : 00-01-00-01-27-A3-56-F1-98-40-BB-01-2B-25\nDNS Servers . . . . . . . . . . . : fec0:0:0:ffff::1%1\n\tfec0:0:0:ffff::2%1\n\tfec0:0:0:ffff::3%1\n\nNetBIOS over Tcpip. . . . . . . . : Enabled\n\nEthernet adapter Ethernet:\nMedia State . . . . . . . . . . . : Media disconnected\nConnection-specific DNS Suffix  . :\nDescription . . . . . . . . . . . : Realtek PCIe FE Family Controller\nPhysical Address. . . . . . . . . : 98-40-BB-01-2B-25\nDHCP Enabled. . . . . . . . . . . : Yes\nAutoconfiguration Enabled . . . . : Yes\n\nEthernet adapter VirtualBox Host-Only Network:\n\nConnection-specific DNS Suffix  . :\nDescription . . . . . . . . . . . : VirtualBox Host-Only Ethernet Adapter\nPhysical Address. . . . . . . . . : 0A-00-27-00-00-05\nDHCP Enabled. . . . . . . . . . . : No\nAutoconfiguration Enabled . . . . : Yes\nLink-local IPv6 Address . . . . . : fe80::15ec:b87a:9ff9:578b%5(Preferred)\nIPv4 Address. . . . . . . . . . . : 192.168.56.1(Preferred)\nSubnet Mask . . . . . . . . . . . : 255.255.255.0\nDefault Gateway . . . . . . . . . :\nDHCPv6 IAID . . . . . . . . . . . : 688521255\nDHCPv6 Client DUID. . . . . . . . : 00-01-00-01-27-A3-56-F1-98-40-BB-01-2B-25\nDNS Servers . . . . . . . . . . . : fec0:0:0:ffff::1%1\n\tfec0:0:0:ffff::2%1\n\tfec0:0:0:ffff::3%1\nNetBIOS over Tcpip. . . . . . . . : Enabled\n\nEthernet adapter VirtualBox Host-Only Network #2:\n\nConnection-specific DNS Suffix  . :\nDescription . . . . . . . . . . . : VirtualBox Host-Only Ethernet Adapter #2\nPhysical Address. . . . . . . . . : 0A-00-27-00-00-07\nDHCP Enabled. . . . . . . . . . . : No\nAutoconfiguration Enabled . . . . : Yes\nLink-local IPv6 Address . . . . . : fe80::8020:3611:a612:a97%7(Preferred)\nIPv4 Address. . . . . . . . . . . : 192.168.22.2(Preferred)\nSubnet Mask . . . . . . . . . . . : 255.255.255.0\nDefault Gateway . . . . . . . . . :\nDHCPv6 IAID . . . . . . . . . . . : 822738983\nDHCPv6 Client DUID. . . . . . . . : 00-01-00-01-27-A3-56-F1-98-40-BB-01-2B-25\nDNS Servers . . . . . . . . . . . : fec0:0:0:ffff::1%1\n\tfec0:0:0:ffff::2%1\n\tfec0:0:0:ffff::3%1\nNetBIOS over Tcpip. . . . . . . . : Enabled\n\nWireless LAN adapter Local Area Connection* 10:\n\nMedia State . . . . . . . . . . . : Media disconnected\nConnection-specific DNS Suffix  . :\nDescription . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter\nPhysical Address. . . . . . . . . : E4-02-9B-6C-D0-6E\nDHCP Enabled. . . . . . . . . . . : Yes\nAutoconfiguration Enabled . . . . : Yes\n\nWireless LAN adapter Local Area Connection* 11:\n\nMedia State . . . . . . . . . . . : Media disconnected\nConnection-specific DNS Suffix  . :\nDescription . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter #3\nPhysical Address. . . . . . . . . : E6-02-9B-6C-D0-6D\nDHCP Enabled. . . . . . . . . . . : Yes\nAutoconfiguration Enabled . . . . : Yes\n\nEthernet adapter VMware Network Adapter VMnet1:\n\nConnection-specific DNS Suffix  . :\nDescription . . . . . . . . . . . : VMware Virtual Ethernet Adapter for VMnet1\nPhysical Address. . . . . . . . . : 00-50-56-C0-00-01\nDHCP Enabled. . . . . . . . . . . : Yes\nAutoconfiguration Enabled . . . . : Yes\nLink-local IPv6 Address . . . . . : fe80::30af:ef61:1df:d140%9(Preferred)\nIPv4 Address. . . . . . . . . . . : 192.168.80.1(Preferred)\nSubnet Mask . . . . . . . . . . . : 255.255.255.0\nLease Obtained. . . . . . . . . . : 09 Tháng Chín 2021 23:44:11\nLease Expires . . . . . . . . . . : 10 Tháng Chín 2021 01:14:00\nDefault Gateway . . . . . . . . . :\nDHCP Server . . . . . . . . . . . : 192.168.80.254\nDHCPv6 IAID . . . . . . . . . . . : 989876310\nDHCPv6 Client DUID. . . . . . . . : 00-01-00-01-27-A3-56-F1-98-40-BB-01-2B-25\nDNS Servers . . . . . . . . . . . : fec0:0:0:ffff::1%1\n\tfec0:0:0:ffff::2%1\n\tfec0:0:0:ffff::3%1\nNetBIOS over Tcpip. . . . . . . . : Enabled\n\nEthernet adapter VMware Network Adapter VMnet8:\n\nConnection-specific DNS Suffix  . :\nDescription . . . . . . . . . . . : VMware Virtual Ethernet Adapter for VMnet8\nPhysical Address. . . . . . . . . : 00-50-56-C0-00-08\nDHCP Enabled. . . . . . . . . . . : Yes\nAutoconfiguration Enabled . . . . : Yes\nLink-local IPv6 Address . . . . . : fe80::9424:ae33:84bb:ad45%15(Preferred)\nIPv4 Address. . . . . . . . . . . : 192.168.23.1(Preferred)\nSubnet Mask . . . . . . . . . . . : 255.255.255.0\nLease Obtained. . . . . . . . . . : 09 Tháng Chín 2021 23:44:00\nLease Expires . . . . . . . . . . : 10 Tháng Chín 2021 01:13:59\nDefault Gateway . . . . . . . . . :\nDHCP Server . . . . . . . . . . . : 192.168.23.254\nDHCPv6 IAID . . . . . . . . . . . : 1006653526\nDHCPv6 Client DUID. . . . . . . . : 00-01-00-01-27-A3-56-F1-98-40-BB-01-2B-25\nDNS Servers . . . . . . . . . . . : \fec0:0:0:ffff::1%1\n\tfec0:0:0:ffff::2%1\n\tfec0:0:0:ffff::3%1\nPrimary WINS Server . . . . . . . : 192.168.23.2\nNetBIOS over Tcpip. . . . . . . . : Enabled\n\nWireless LAN adapter Wi-Fi:\n\nConnection-specific DNS Suffix  . :\nDescription . . . . . . . . . . . : Intel(R) Dual Band Wireless-AC 3160\nPhysical Address. . . . . . . . . : E4-02-9B-6C-D0-6D\nDHCP Enabled. . . . . . . . . . . : Yes\nAutoconfiguration Enabled . . . . : Yes\nLink-local IPv6 Address . . . . . : fe80::c1d0:2649:1f3:ae5f%17(Preferred)\nIPv4 Address. . . . . . . . . . . : 192.168.1.178(Preferred)\nSubnet Mask . . . . . . . . . . . : 255.255.255.0\nLease Obtained. . . . . . . . . . : 09 Tháng Chín 2021 19:19:33\nLease Expires . . . . . . . . . . : 10 Tháng Chín 2021 03:34:15\nDefault Gateway . . . . . . . . . : 192.168.1.1\nDHCP Server . . . . . . . . . . . : 192.168.1.1\nDHCPv6 IAID . . . . . . . . . . . : 602145435\nDHCPv6 Client DUID. . . . . . . . : 00-01-00-01-27-A3-56-F1-98-40-BB-01-2B-25\nDNS Servers . . . . . . . . . . . : 192.168.1.1\nNetBIOS over Tcpip. . . . . . . . : Enabled\n\nTunnel adapter Teredo Tunneling Pseudo-Interface:\n\nConnection-specific DNS Suffix  . :\nDescription . . . . . . . . . . . : Microsoft Teredo Tunneling Adapter\nPhysical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0\nDHCP Enabled. . . . . . . . . . . : No\nAutoconfiguration Enabled . . . . : Yes\nIPv6 Address. . . . . . . . . . . : 2001:0:2851:fcb0:146c:31:8b98:24cf(Preferred)\nLink-local IPv6 Address . . . . . : fe80::146c:31:8b98:24cf%19(Preferred)\nDefault Gateway . . . . . . . . . :\nDHCPv6 IAID . . . . . . . . . . . : 234881024\nDHCPv6 Client DUID. . . . . . . . : 00-01-00-01-27-A3-56-F1-98-40-BB-01-2B-25\nNetBIOS over Tcpip. . . . . . . . : Disabled")
