from netmiko import ConnectHandler
from threading import Thread
from napalm import get_network_driver

def netmikoConn(ip, usr, pwd):
    conn = ConnectHandler(device_type="cisco_ios", host=ip, username=usr, password=pwd)
    return(conn)

def napalmConn(ip, usr, pwd):
    driver = get_network_driver('ios')
    device = driver(hostname=ip, username=usr, password=pwd)
    return(device)

def thrdNetmiko(ip, usr, pwd):   
    
    threads = []
    thread = Thread(target=netmikoConn, args=(ip, usr, pwd,))
    thread.start()
    threads.append(thread)

    # Waiting for all threads to complete
    for thread in threads:
        thread.join()

def thrdNapalm(ip, usr, pwd):   
    
    threads = []
    thread = Thread(target=napalmConn, args=(ip, usr, pwd,))
    thread.start()
    threads.append(thread)

    # Waiting for all threads to complete
    for thread in threads:
        thread.join()
