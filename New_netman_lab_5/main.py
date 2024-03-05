import subprocess


if __name__ == "__main__":

    print("------------------------------ [Objective 2 - TCP DUMP] ------------------------------")
    subprocess.run(['python3', 'NMtcpdump.py'])
    print("------------------------------ [Objective 2 - DHCP SERVER] ------------------------------")
    subprocess.run(['python3', 'NMdhcpserver.py'])
    print("------------------------------ [Objective 3 - SNMP] ------------------------------")
    subprocess.run(['python3', 'NMsnmp.py'])
    print("------------------------------ [Objective 4 - GITHUB] ------------------------------")
    subprocess.run(['python3', 'NMgithub.py'])