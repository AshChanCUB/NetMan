import subprocess
import argparse
import re

def getOID(headerValue, OIDList,version, ip_addr):
  print('SNMP v'+ version)
  for header, oid in zip(headerValue, OIDList):
    if version == '1':
      command = f'snmpget -v {version} -c public {ip_addr} {oid}'

    elif version == '2c':
      command = f'snmpget -v {version} -c public {ip_addr} {oid}'

    elif version == '3':
      command = f'snmpget -v {version} -u ash -l authPriv -a md5 -A ash_auth -x aes128 -X ash_encrypt {ip_addr} {oid}'
    
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    result = process.communicate()
    act_str = result[0]
    req_str=act_str.split(': ')[-1]
    req=re.search(r'[^\n]+(?=\s)',req_str)
    out=req.group(0).replace('"','')
    print(f"{header}: {out}")

  
def printValues(headerValue,OIDList,version,ip_addr):
  print('SNMP v'+ version)
  print('ip: '+ip_addr)
  for header, oid in zip(headerValue, OIDList):
    print(f"{header}: {oid}")



if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='SNMP version number')
  parser.add_argument('--ver', type=str, default=None, help='Provide the SNMP version')
  parser.add_argument('--ip', type=str, default=None, help='Provide the IP address')
  args = parser.parse_args()
  version = args.ver
  ip_addr = args.ip

  with open('oid.txt') as o:
    OIDList = [line.strip() for line in o]
  
  with open('headers.txt') as h:
    headerValue = [line.strip() for line in h]

  getOID(headerValue,OIDList,version,ip_addr)
 # printValues(headerValue,OIDList,version,ip_addr)

