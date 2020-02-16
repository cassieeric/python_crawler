from scapy.all import *
def packetHandler(p):
    #p.show()
    if p.haslayer(Dot11Beacon):
        Pmac=p.addr2
        name=p.info
        if Pmac=='b0:eb:57:d7:a3:45':
            print(Pmac,name)
packets=sniff(iface='wlan0mon',prn=packetHandler)