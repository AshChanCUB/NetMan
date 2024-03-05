from easysnmp import Session
from threading import Thread
import json
import matplotlib.pyplot as plt
import time


def plotGraph(key, value):

    sesh = Session(hostname=value, community='netman', version=2)
    time_intr = []
    cpu = []

    for i in range(1,25):
        cpu_stat = sesh.get('1.3.6.1.4.1.9.9.109.1.1.1.1.6.1').value
        time_intr.append(i*5)
        cpu.append(int(cpu_stat)+1)
        time.sleep(5) 
    
    plt.plot(time_intr, cpu, color="orange")
    plt.xlabel('Time')
    plt.ylabel('Percentage utilization')
    plt.xticks(time_intr)
    plt.ylim(0, 100)
    plt.savefig(f'CPU_Utilization_{key}.jpg', format='jpg')
    plt.show()



def updateDict(key, value, routerInfo):
    
    routerInfo[key] = {'addresses': {}}
    sesh = Session(hostname=value, community='netman', version=2)
    index = sesh.walk('1.3.6.1.2.1.4.20.1.2')
    ipv6_list = sesh.walk('iso.3.6.1.2.1.4.34.1.3.2')
   
    for ind in index:
        #print(f'{ind.oid} = {ind.value}')
        spl = ind.oid.split('.')
        ipv4 = '.'.join(spl[-4:])
        #print(ip_addr)
        interface = sesh.get(f'1.3.6.1.2.1.2.2.1.2.{ind.value}')
        #print(interface.value)
        mask = sesh.get(f'1.3.6.1.2.1.4.20.1.3.{ipv4}')
        #print(mask.value, end="\n\n")
        routerInfo[key]['addresses'][interface.value] = {'v4':f'{ipv4} / {mask.value}'}


    for ip in ipv6_list:

        interface= sesh.get(f'iso.3.6.1.2.1.2.2.1.2.{ip.value}')
        spl = ip.oid.split(".")
        ipv6 = spl[-16:]

        hex_parts = [f"{int(part):02x}" for part in ipv6]

        hex_str = ''.join(hex_parts)

        ipv6_blocks = [hex_str[i:i+4] for i in range(0, len(hex_str), 4)]
        ipv6 = ":".join(ipv6_blocks)
        routerInfo[key]['addresses'][interface.value].update({'v6':f'{ipv6} / 64'})


        int_stat = sesh.get(f'1.3.6.1.2.1.2.2.1.8.{ip.value}')
        if int_stat.value == "1":
            routerInfo[key]['addresses'][interface.value].update({'Status': 'UP'})
        
        for i in {1, 2, 8}:
            st = sesh.get(f'iso.3.6.1.2.1.2.2.1.8.{i}')
            inter = sesh.get(f'iso.3.6.1.2.1.2.2.1.2.{i}')
            if (st.value == "2"):
                routerInfo[key]['addresses'].update({inter.value:{'Status': 'DOWN'}})
        
    #print(f"Dictionary Updated with {key}'s information")
             
if __name__ == "__main__":

    routers = {}
    routerInfo = {}
    n = int(input("How many routers to configure? "))

    for i in range(n):
        r_h = str(input("Enter the Router hostname:"))
        r_ip = input("Enter the Router loopback ip address:")
        routers.update({r_h:r_ip})

    threads = []
    for key, value in routers.items():
        thread = Thread(target=updateDict, args=(key, value, routerInfo,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

    txt_file = json.dumps(routerInfo, indent=4)
    with open('router_data.txt', 'w') as file:
        file.write(txt_file)
        

    plotGraph('R1', '1.1.1.1')
