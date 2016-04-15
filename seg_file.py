'''
Code for segmenting trails between given coordinates
Place the code where the input folder resides or give the path
'''

import os
import math
def readFile(filename,header,seperator=","):

    output=[]
    fopen=open(filename)
    
    if header:
        fopen.readline()
    while True:
        line=fopen.readline()
        if line and len(line)>1:    #len(line)>1 : to avoid empty last line
            output.append(line.strip().split(seperator))
        else:
            fopen.close()
            break
        #print line
    return output

def dist(pt1_Lat,pt1_Lon,pt2_Lat,pt2_Lon):
    R = 6372800; #meter
    phi1 = math.radians(pt1_Lat)
    phi2 = math.radians(pt2_Lat)
    del_phi=math.radians((pt2_Lat-pt1_Lat))
    del_lambda = math.radians((pt2_Lon-pt1_Lon))
    a = (math.sin(del_phi/2) ** 2) + math.cos(phi1) * math.cos(phi2) * (math.sin(del_lambda/2) **2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d 

def main():
    file_name=raw_input("Enter the file name: ")
    #outputFolder=folder+"_Segmented"
    seg=readFile('file.txt',True)
    print seg
    first=[seg[0][1],seg[0][2]]           #Give starting Coordinate
    last=[seg[1][1],seg[1][2]]      #Give end Coordinate
    print first,last
    f1=open("out"+file_name,'w')
    data=readFile(file_name,True)
    flag=False
    for i,row in enumerate(data):
        d=dist(float(data[i][0]),float(data[i][1]),float(first[0]),float(first[1]))
        d1=dist(float(data[i][0]),float(data[i][1]),float(last[0]),float(last[1]))
        ##print d
        #print (str(data[i][0]),str(data[i][1]),float(first[0]),float(first[1]))
        if d<30 :
            flag=True
            f1.write(data[i][0]+','+data[i][1]+','+data[i][2]+'\n')
        elif d1<30:
            flag=False
            f1.write(data[i][0]+','+data[i][1]+','+data[i][2]+'\n')
        if flag:
            f1.write(data[i][0]+','+data[i][1]+','+data[i][2]+'\n')                
if __name__=='__main__':
    main()
        
    
    
