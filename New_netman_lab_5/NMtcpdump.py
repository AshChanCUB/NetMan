from scapy.all import *
from threading import Thread as Th


def extractIpv6(pfile):
    scapy_cap = rdpcap(pfile)
    ipv6_set = set()
    for packet in scapy_cap:
        if ICMPv6EchoRequest in packet:
            ipv6_set.add(packet[IPv6].src)         
    return ipv6_set


def euiDecoder(hexa):

        mac_list = list()
        client_list = list()
        for h in hexa:
            print("IPv6 address using EUI-64 = " + h, end="\n\n")
            #extract first hextet and removing FF, FE
            temp_ls = h.split(":")[-4:]
            temp_join= "".join(temp_ls)
            ls = [temp_join[i:i+2] for i in range(0, len(temp_join), 2)]
            print(f"Before removing FF, FE = {ls}")
            ls.pop(3)
            ls.pop(3)
            print(f"After removing FF, FE = {ls}")
            temp = ls[0]
            print("Old hex value - first hextet = " + temp)
            
            #convert to binary
            b = bin(int(temp, 16))[2:].zfill(8)
            print("Binary (Before) = "+b)

            #figuring out the 7th element and changing it
            print("binary value to change = "+b[6])
            if b[6] == "0":
                b = b[:6]+"1"+b[7:] 
            else:
                b = b[:6]+"0"+b[7:]    
            print("Binary (After) = "+b)
            
            #converting back to decimal
            fin_hex = hex(int(b, 2))[2:]
            ls[0] = fin_hex
            print(f"New hex value - first hextet = {fin_hex}", end="\n\n")
            mac_addr= ":".join(ls)
            mac_list.append(mac_addr)
            
            #creating client ID
            ls.insert(0, "01")
            cl = "".join(ls).ljust(14, '0')

            chunk = [cl[i:i+4] for i in range(0,len(cl),4)]
            client_id = ":".join(chunk)
            client_list.append(client_id)
            print("Mac Address of the device interface = "+mac_addr)
            print("Client ID of the interface = "+client_id, end="\n\n\n\n")
            
        return(mac_list, client_list)


if __name__ == "__main__": 
    hexa = extractIpv6('/home/student/Desktop/netman/lab5/code/tap0_new.pcap')
    mac_addr_list, client_id_list = euiDecoder(hexa)

        