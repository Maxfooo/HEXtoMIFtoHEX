'''
Created on Jan 24, 2016

@author: Max Ruiz
'''
from tkinter import *
from FileIO import *

class HexUI(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.title('Hex Parameters')
        self.pack()

        self.parameters = ['depth','width','address_radix','data_radix', 0]

        self.fileIO = FileIO()

        self.mainFrame()

    def mainFrame(self):

        depthFrame = Frame(self)
        depthValue = StringVar()
        depthLabel = Label(depthFrame, text = 'Mem Depth')
        depthLabel.pack(side = 'left')
        self.depthEntry = Entry(depthFrame, textvariable = depthValue)
        self.depthEntry.pack(side = 'left')
        depthFrame.pack()

        widthFrame = Frame(self)
        widthValue = StringVar()
        widthLabel = Label(widthFrame, text = 'Mem width')
        widthLabel.pack(side = 'left')
        self.widthEntry = Entry(widthFrame, textvariable = widthValue)
        self.widthEntry.pack(side = 'left')
        widthFrame.pack()

        addRadFrame = Frame(self)
        addRadValue = StringVar()
        addRadLabel = Label(addRadFrame, text = 'Mem addRad')
        addRadLabel.pack(side = 'left')
        self.addRadEntry = Entry(addRadFrame, textvariable = addRadValue)
        self.addRadEntry.pack(side = 'left')
        addRadFrame.pack()

        datRadFrame = Frame(self)
        datRadValue = StringVar()
        datRadLabel = Label(datRadFrame, text = 'Mem datRad')
        datRadLabel.pack(side = 'left')
        self.datRadEntry = Entry(datRadFrame, textvariable = datRadValue)
        self.datRadEntry.pack(side = 'left')
        datRadFrame.pack()

        zeroFillFrame = Frame(self)
        zeroFillValue = IntVar()
        self.zeroFillCB = Checkbutton(zeroFillFrame, text='Fill/pad extra zeros?', variable=zeroFillValue, \
                                 onvalue = 1, offvalue = 0)
        self.zeroFillCB.pack(side = 'left')
        zeroFillFrame.pack()

        setParamButton = Button(self, text = 'Set Parameters', command = self.getFieldEntries)
        setParamButton.pack()

    def getFieldEntries(self):
        try:
            self.parameters[0] = int(self.depthEntry.get())
            self.parameters[1] = int(self.widthEntry.get())
            self.parameters[2] = self.addRadEntry.get()
            self.parameters[3] = self.datRadEntry.get()
            self.parameters[4] = self.zeroFillCB.get()
            self.quit()
        except:
            self.fileIO.errorPopup('Depth and Width should be integers!')

    def getParameters(self):
        return self.parameters

        '''
        depth
        width
        address_radix
        data_radix
        '''
