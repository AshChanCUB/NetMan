import subprocess
from threading import Thread



def normalRun(file):
    subprocess.run(['python3', file])

if __name__ == "__main__":

    threads = [Thread(target=normalRun, args=('NMtcpdump.py',)),
               Thread(target=normalRun, args=('NMdhcpserver.py',)),
               Thread(target=normalRun, args=('scapyLoad.py',), kwargs={'shell' :True}),
               Thread(target=normalRun, args=('NMsnmp.py',)),
               Thread(target=normalRun, args=('NMtcpdump.py.py',))]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()