'''
Created on Jan 21, 2016

@author: Max Ruiz
'''
import re

class HEXClass(object):
    '''
    Intel hex
    http://www.keil.com/support/docs/1584/
    :LLAAAATT[DD...]CC
    '''


    def __init__(self, hexFile, mifFile):
        self.hexFile = hexFile
        self.mifFile = mifFile
        self.hexContent = None
        self.hexLen = []
        self.hexAddr = []
        self.hexType = []
        self.hexData = []
        self.hexCS = []
        self.hexTypeEOF = '01'
        self.hexFileSettings()
        self.readHEXFile()

    def hexFileSettings(self, base=16, depth=16, width=8, address_radix='HEX', data_radix='HEX'):
        self.base = base
        self.depth = depth
        self.width = width
        self.address_radix = address_radix
        self.data_radix = data_radix
        self.data_digits = base / width

    def convertHEXtoMIF(self):
        self.sortHEXContents()
        self.writeMIFFile()

    def readHEXFile(self):
        self.hexContent = self.hexFile.read()

    def sortHEXContents(self):
        hex_format_expression = r':(\w{2})(\w{4})(\w{2})(\w*)(\w{2})'
        hexFields = re.findall(hex_format_expression,self.hexContent)

        for records in hexFields:
            self.hexLen.append(records[0])
            self.hexAddr.append(records[1])
            self.hexType.append(records[2])
            if self.hexType[-1] == self.hexTypeEOF:
                self.hexData.append(['00'])
            else:
                self.hexData.append(re.findall(r'\w{%d}' %self.data_digits,records[3]))
            self.hexCS.append(records[4])

    def writeMIFFile(self):
        self.mifFile.write('DEPTH = {};\nWIDTH = {};\n'.format(self.depth,self.width) +
                           'ADDRESS_RADIX = {};\n'.format(self.address_radix) +
                           'DATA_RADIX = {};\n'.format(self.data_radix) +
                           'CONTENT\nBEGIN\n')

        for i in range(len(self.hexLen)):
            tempAddress = []
            for j in range(int(self.hexLen[i],self.base)):
                tempAddress.append(int(self.hexAddr[i],self.base)+j)
            for k in range(len(tempAddress)):
                self.mifFile.write(str(hex(tempAddress[k])).replace('0x','') +
                                   '\t:\t' + str(self.hexData[i][k]) + ';\n')
        self.mifFile.write('END;')













