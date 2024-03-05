import pandas as pd
from sshConnection import netmikoConn 
from sshConnection import napalmConn
from sshConnection import thrdNapalm
from NMtcpdump import extractIpv6
from NMtcpdump import euiDecoder
import time
from threading import Thread as Th
from importFiles import getSshinfo
from importFiles import getPcap


def parseSsh(ssh_data,target,csv_file):

    fetch_ip = input("Enter the device to SSH: ")
    spec = ssh_data.loc[ssh_data["Router"]== fetch_ip.upper()]
    ip = spec['IP'].iloc[0]

    
    if pd.isna(ip) and target != "NA":
        print("Entered elif")
        ssh_data.at[spec.index[0], 'IP'] = target
        ssh_data.to_csv(csv_file, index=False)

    """elif pd.isna(ip):
        print("Entered if")
        ssh_data.at[spec.index[0], 'IP'] = input("No IP address found for the device, Enter the IP address to update csv: ")
        ssh_data.to_csv(csv_file, index=False)"""

    ip = spec['IP'].iloc[0]
    usr = spec['Username'].iloc[0]
    pwd = spec['Password'].iloc[0]

    return(ip, usr, pwd)


def findR5(conn):
    output = conn.send_command('sh ipv6 neighbors | sec 2508:9835')
    a = output.split("\n")
    b=set()
    for i in a:
        if "2508:9835" in i.split(" ")[0]:
            b.add(i.split(" ")[0])
    return b
    

"""def verifyMac(ssh_data, ip_ls, mac_ls):
    for spec in ssh_data:
    device = thrdNapalm()
    interfaces = device.get_interfaces()
    print(interfaces['FastEthernet0/0']['mac_address'])"""


def dhcpServer(conn, cl_ls):

    conf_list = ["ip dhcp excluded-address 25.25.25.25",
                 "ip dhcp excluded-address 25.25.25.2",
                 "ip dhcp excluded-address 25.25.25.3",
                 "ip dhcp pool r2_static_ipv4",
                 "host 25.25.25.2 255.255.255.0",
                 f"client-identifier {cl_ls[0]}",
                 "ip dhcp pool lab5_ipv4",
                 "network 25.25.25.0 255.255.255.0",
                 "ip dhcp pool r3_static_ipv4",
                 "host 25.25.25.3 255.255.255.0",
                 f"client-identifier {cl_ls[1]}",
                 "interface fa0/0",
                 "ip addr 25.25.25.25 255.255.255.0",
                 "no shut",
                 ]
    conn.send_config_set(conf_list)
    time.sleep(30)
    output = conn.send_command('sh ip dhcp binding | sec include 25.25.25')
    print(output)


if __name__ == "__main__": 


    #fetching input files
    pcap_file = getPcap()
    ssh_data , csv_file= getSshinfo()

    #SSH into R4 to find R5 IP
    ip, usr, pwd = parseSsh(ssh_data, "NA", csv_file)
    conn_r4 = netmikoConn(ip, usr, pwd)
    ipv6_extract = extractIpv6(pcap_file)
    b = findR5(conn_r4)

    lower_ipv6_extract = {ip.lower() for ip in ipv6_extract}
    lower_b = {ip.lower() for ip in b}
    c = lower_b-lower_ipv6_extract
    r5_ip = list(c)[0]
    print(f"IP address of R5: {r5_ip}")

    #SSH into R5 and configure DHCPv4 for R2 and R3
    i, u, p = parseSsh(ssh_data, r5_ip, csv_file)
    print("Configuring DHCPv4 in R5")
    conn_r5 = netmikoConn(i, u, p)
    mac_addr_list, client_id_list = euiDecoder(ipv6_extract)
    dhcpServer(conn_r5, client_id_list)