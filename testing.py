'''
Created on Jan 21, 2016

@author: Max Ruiz
'''

import re
import FileIO

hexFormat = {'length' : 2, 'address' : 4, 'type' : 2, 'checksum' : 2}

hexContent = ''':030000000200916A
:03000B001151325E
:10004B00114E32115D22117B22C2A1C2A2D2A1D2CA
:10005B00A222C2A0C2A2E580F8E590540FF9D2A06B
:10006B00D2A222C2A7C2A3C2A6D2A3D2A7D2A62231
:10007B00118CEBF5802401FBECF5902402FC116E46
:10008B0022C2A5D2A52275A88275B8027589027500
:10009B008810758A50758C5075A0FF7580AA759065
:0B00AB00AA7BAA7CAAC2A4118C80FED4
:00000001FF'''


hex_format_expression = r':(\w{2})(\w{4})(\w{2})(\w*)(\w{2})'

print(hex_format_expression)

hexFields = re.findall(hex_format_expression,hexContent)

print(hexFields)

base = 16
width = 8
data_digits = base / width


hexLen = []
hexAddr =[]
hexType = []
hexData =[]
hexCS = []
for records in hexFields:
    hexLen.append(records[0])
    hexAddr.append(records[1])
    hexType.append(records[2])
    if hexType[-1] == '01':
        hexData.append(['00'])
    else:
        hexData.append(re.findall(r'\w{%d}' %data_digits,records[3]))
    hexCS.append(records[4])

print(hexData)

for i in range(len(hexLen)):
    tempAddress = []
    for j in range(int(hexLen[i],base)):
        tempAddress.append(int(hexAddr[i],base)+j)
    for k in range(len(tempAddress)):
        print(str(hex(tempAddress[k])).replace('0x','') + '\t:\t' + str(hexData[i][k]) + ';')
