import subprocess
import csv
import pandas
import re

with open('Packets.txt', 'w',newline="") as f:
#     writer=csv.writer(f)
    
    subprocess.run(['netstat','-s'], stdout=f)
from pathlib import Path
countriesStr=Path('Packets.txt').read_text()  
connections=open('packets.txt','w')
connections.write(countriesStr)

locations = set([])
Only_size=[]
with open('packets.txt', 'r') as f_input:
    unknown = 0
    # Pass 1, build a set of locations
    for line in f_input:
        line = line.strip(' : \n')
        if ':' in line:
            loc = line.rsplit(":" ,1)[1].strip()
            locations.add(loc)

    # Pass 2, try and find location in line
    f_input.seek(0)

    for line in f_input:
        line = line.strip('\n')
        if ':' in line:
            uni, loc = line.rsplit(":" ,1)
            loc = loc.strip()
        else:
            uni = line
            loc_matches = set(re.findall(r"\b(\w+)\b", line)).intersection(locations)

            if loc_matches:
                loc = list(loc_matches)[0]
            else:
                loc=0
                unknown += 1

        uni = uni.strip()

        print ("Task:", uni)
        print ("Size", loc)
        Only_size.append(loc)

    print( "Unknown locations:", unknown)
    print(Only_size)
from pathlib import Path
countriesStr=Path('Packets.txt').read_text()  
connections=open('packets.txt','w')
connections.write(countriesStr)

locations = set([])
Only_size=[]
TaskP=[]
with open('packets.txt', 'r') as f_input:
    unknown = 0
    # Pass 1, build a set of locations
    for line in f_input:
        line = line.rstrip('\n')
        if ':' in line:
            loc = line.rsplit(":" ,1)[1].strip()
            locations.add(loc)

    # Pass 2, try and find location in line
    f_input.seek(0)

    for line in f_input:
        line = line.strip('\n')
        if ':' in line:
            uni, loc = line.rsplit(":" ,1)
            loc = loc.strip()
        else:
            uni = line
            loc_matches = set(re.findall(r"\b(\w+)\b", line)).intersection(locations)

            if loc_matches:
                loc = list(loc_matches)[0]
            else:
                loc=0
                unknown += 1

        uni = uni.strip()

        print ("Task:", uni)
        print ("Size", loc)
        Only_size.append(loc)
        TaskP.append(uni)
    print( "Unknown size:", unknown) 
# while("" in Only_size) :
#         Only_size.remove("")
#       Only_size.remove(0)
#         Only_size.remove( 0)
        
print(len(Only_size))
print(TaskP)

#     subprocess.run(['last'], stdout=f)
    
# types = [ ("Ip:", int) ]

# rowlist = []

#Accessing a text file - www.101computing.net/mp3-playlist/

# file = open("Packets.csv","r")

# #Repeat for each song in the text file
# for line in file:
  
#   #Let's split the line into an array called "fields" using the ";" as a separator:
#   fields = line.split(";")
  
#   #and let's extract the data:
#   Ip = fields[0]
#   Packets = fields[1]
  
  
#   #Print the song
#   print(Ip)

# #It is good practice to close the file at the end to free up resources   
# file.close()
i=0
with open('throughput.csv','w',newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Task","Size"])
    while i<len(TaskP):
        writer.writerow([TaskP[i],Only_size[i]])
        i+=1
import re
from datetime import datetime
from datetime import date
from getmac import get_mac_address as gma
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()
with open('throughput.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    rows = list(csv_reader)
    i=23
    j=3
    r=34
    R=43
    J=59
    Pckdet=[]
    while j<10:
        Pckdet.append(rows[j])#Extracting required rows
        j+=1
    while i<33:
        Pckdet.append(rows[i])#Extracting required rows
        
        i+=1
    while r<=39:
        Pckdet.append(rows[r])#Extracting required rows
        
        r+=1    
    while R<=50:
        Pckdet.append(rows[R])#Extracting required rows
        
        R+=1  
    while J<=61:
        Pckdet.append(rows[J])#Extracting required rows
        J+=1    
    print(len(Pckdet))
    REQ=[]
    k=0
    for k in range(len(Pckdet)):#Extracting required rows[][]
        REQ.append(Pckdet[k][0])
    #print(REQ)
    z=0
    numbers=[]
    tasks=[]
    while z<len(Pckdet):
        
        temp = re.findall(r'\d+', REQ[z])
        res = list(map(int, temp))
        res1 = " ".join(re.findall("[a-zA-Z]+", REQ[z]))  
        numbers.append(res)
        tasks.append(res1)
        z+=1
    #print(tasks,numbers)
    #Extracting required rows
    result = [(item1, s) for item1, item2 in zip(tasks, numbers) for s in item2]
#     for item1, item2 in zip(tasks, numbers):
#         for s in item2:
#             result.append((item1, s))
        
    print(result[0][0],result[0][1])
    Tasks=["Date","Time","Hostname","Ipaddress","MAC"]
    import socket
    hostname=socket.gethostname()
    ip=socket.gethostbyname(hostname)
    Host=str(hostname)
    Ip=str(ip)

    Sizes=[today,current_time,Host,Ip,gma()]
    
    g=0
    for g in range(len(result)):
        Sizes.append(result[g][1])
        Tasks.append(result[g][0])
    print(Tasks)    
    with open('Throough.csv','w',newline="") as file:
            writer=csv.writer(file)
            writer.writerow(Tasks)
            writer.writerow(Sizes)
         

#             writer.writerows([result[i][0],])        
