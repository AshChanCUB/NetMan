from scapy.all import *
import smtplib

fromaddr = 'schedule.genius.planner@gmail.com'
toaddrs  = 'ash250898@gmail.com'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(fromaddr,'hwco nbke iblr zgxn')

pcap=rdpcap('test.pcap')

for packet in pcap:
    if packet.haslayer(SNMP) and packet.haslayer(UDP) and packet[UDP].dport == 162:
        temp = packet.show(dump=True)
        msg = 'Subject: Found a SNMP-Trap\r\n\r\n'+ temp
        server.sendmail(fromaddr, toaddrs, msg)

server.quit()

