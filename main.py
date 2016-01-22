'''
Created on Jan 21, 2016

@author: Max Ruiz
'''
import re
from FileIO import *
from HEXClass import *

filePrompt('open', 'Looking for a .hex file!')
hex_file = openFile()


filePrompt('save' 'Looking for a .mif file.')
mif_file = saveFile()

hclass = HEXClass(hex_file, mif_file)

hex_file.close()

if __name__ == '__main__':
    hclass.convertHEXtoMIF()
