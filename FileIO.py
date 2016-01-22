'''
Created on Jan 21, 2016

@author: Max Ruiz
'''
import tkinter
from tkinter import filedialog
from tkinter import messagebox

def filePrompt(command = 'open', msg = ''):
    root = tkinter.Tk()
    root.withdraw()
    if(command == 'open'):
        messagebox.showinfo('Open File','Please select a file to open!\n{}'.format(msg))
    elif(command == 'save'):
        messagebox.showinfo('Save File','Please select a file to save to!\n{}'.format(msg))
    elif(command == 'file'):
        messagebox.showinfo('File Location','Please locate a file!\n{}'.format(msg))
    elif(command == 'folder'):
        messagebox.showinfo('Folder Location','Please locate a folder!\n{}'.format(msg))


def openFile(exten='.hex', ftypes=[('all files', '.*')], idir='C:\\',
             ifilen='myhexfile.hex', title='Open File'):
    root = tkinter.Tk()
    file_opt = options = {}
    options['defaultextension'] = exten
    options['filetypes'] = ftypes
    options['initialdir'] = idir
    options['initialfile'] = ifilen
    options['parent'] = root
    options['title'] = title
    root.withdraw()
    return filedialog.askopenfile(mode='r', **file_opt)

def saveFile(exten='.hex', ftypes=[('all files', '.*')], idir='C:\\',
             ifilen='myhexfile.hex', title='Open File'):
    root = tkinter.Tk()
    file_opt = options = {}
    options['defaultextension'] = exten
    options['filetypes'] = ftypes
    options['initialdir'] = idir
    options['initialfile'] = ifilen
    options['parent'] = root
    options['title'] = title
    root.withdraw()
    return filedialog.asksaveasfile(mode='w', **file_opt)

def getFileLocation():
    exten='.*'
    ftypes=[('all files', '.*')]
    idir='C:\\',
    title='Get File Location'

    root = tkinter.Tk()
    file_opt = options = {}
    options['defaultextension'] = exten
    options['filetypes'] = ftypes
    options['initialdir'] = idir
    options['parent'] = root
    options['title'] = title
    root.withdraw()

    return filedialog.askopenfilename(**file_opt)

def getFolderLocation():
    root = tkinter.Tk()
    file_opt = options = {}
    options['parent'] = root
    root.withdraw()
    return filedialog.askdirectory(parent=root, title='Path to Copy to', \
                                     initialdir='.')
