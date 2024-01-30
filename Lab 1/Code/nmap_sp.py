import subprocess
import argparse
import time

def nmap(f, ip_addr):
    command = f'nmap -sn {ip_addr}'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    result = process.communicate()

    with open(f,'w') as file:
        for line in result[0].splitlines():
            if 'Nmap scan report for' in line:
                ip = line.split()[-1]
                file.write(ip +'\n')
                print(ip+'\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ip_address/range')
    parser.add_argument('--ip', type=str, default=None, help='Provide the IP address with /subnet mask if you need to check for a range')
    args = parser.parse_args()
    ip_addr = args.ip
    nmap("nmap_ip_list_1.txt", ip_addr)
    time.sleep(600)
    nmap("nmap_ip_list_2.txt", ip_addr)



