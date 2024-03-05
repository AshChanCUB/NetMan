import subprocess


if __name__ == "__main__":


    subprocess.run(['python3', 'NMtcpdump.py'])
    subprocess.run(['python3', 'NMdhcpserver.py'])
    subprocess.run(['python3', 'NMsnmp.py'])
    subprocess.run(['python3', 'NMgithub.py'])