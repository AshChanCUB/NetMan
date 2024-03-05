import pandas as pd

def getSshinfo():

    while True:
        try:
            csv_file = '/home/student/Desktop/netman/lab5/code/sshInfo.csv' #input('Enter the path for the sshInfo.conf file: ')
            ssh_data = pd.read_csv(csv_file) #'/home/student/Desktop/netman/lab5/code/sshInfo.csv' 
            break
        except FileNotFoundError as e:
            #print(e)
            print("File not found or invalid path")
            print("Re-enter a valid path")
    return(ssh_data, csv_file)

def getPcap():
 
    while True:
        try:
            pcap_file = '/home/student/Desktop/netman/lab5/code/tap0_new.pcap' #input('Enter the path for the pcap file: ')
            break
        except FileNotFoundError as e:
            #print(e)
            print("File not found or invalid path")
            print("Re-enter a valid path")
    return(pcap_file)
