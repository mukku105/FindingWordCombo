
"""
Created on Sat Jan 25 00:11:17 2020

@author: MukSam_Limboo
"""

from nltk.corpus import wordnet
import re
import tkinter as tk

#-------------------- Tkinter Window Initialization -------------------------
window = tk.Tk()
window.geometry("450x324")
window.title("Find all the words consisting of specific letters")

lFrame = tk.Frame(window).pack(side = "left")
rFrame = tk.Frame(window).pack(side = "right")

#---------------------------------------------------------------------
def compRepeat(strComb, strWord):
    strComboCh = list(dict.fromkeys(list(strComb)))
    
    for c in strComboCh:
        if strWord.count(c) > strComb.count(c):
            return False
        
    return True   
    
def getWords():
    str = textSearch.get()
    sLen = searchLen.get()
    if sLen:
        sLen = int(sLen)
    else:
        sLen = 0
        
    listWords = []

    compRegx = re.compile('^[{}]+$'.format(str))
        
    for w in wordnet.words():
        match = compRegx.search(w)
        if match and compRepeat(str, w):
            if sLen == 0:
                listWords.append(match.group())
            elif len(match.group()) == sLen:
                listWords.append(match.group())
    
    listBox1.delete(0, listBox1.size())
    
    i=1
    for w in listWords:
        listBox1.insert(i, "->  {}".format(w))
        i +=1
    listBox1.pack()

    
#------------------ Tkinter GUI ------------------------
scrollBar = tk.Scrollbar(window)
scrollBar.pack(side = "right", fill='y')
listBox1 = tk.Listbox(lFrame, height = 14, width= 25,  yscrollcommand = scrollBar.set, bg="aqua")
listBox1.pack(side = "left", fill="both")
scrollBar.config(command = listBox1.yview)

tk.Label(rFrame, text="Enter Constituent words: ", pady=6).pack(side="top")
textSearch = tk.Entry(rFrame)
textSearch.pack(side="top")

tk.Label(rFrame, text="Enter word size(leave it blank if all): ", pady=6).pack(side="top")
searchLen = tk.Entry(rFrame)
searchLen.pack(side="top")

tk.Button(window, text="Search", width=25, bg="#91ead9",command=lambda: getWords()).pack(side="bottom")
window.mainloop()
