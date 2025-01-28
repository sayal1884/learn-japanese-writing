from tkinter import *
from tkinter.ttk import Button, Progressbar, Style
from tkinter.messagebox import *
from tkinter.filedialog import *
import threading
import time, PIL
from PIL import Image, ImageTk

latinHira= {
    "a": "あ", "i": "い", "u": "う", "e": "え", "o": "お",
    "ka": "か", "ki": "き", "ku": "く", "ke": "け", "ko": "こ",
    "sa": "さ", "shi": "し", "su": "す", "se": "せ", "so": "そ",
    "ta": "た", "chi": "ち", "tsu": "つ", "tu": "つ", "te": "て", "to": "と",
    "na": "な", "ni": "に", "nu": "ぬ", "ne": "ね", "no": "の",
    "ha": "は", "hi": "ひ", "fu": "ふ","f": "ふ", "he": "へ", "ho": "ほ",
    "ma": "ま", "mi": "み", "mu": "む", "me": "め", "mo": "も",
    "ya": "や", "yu": "ゆ", "yo": "よ",
    "ra": "ら", "ri": "り", "ru": "る", "re": "れ", "ro": "ろ",
    "la": "ら", "li": "り", "lu": "る", "le": "れ", "lo": "ろ",
    "wa": "わ", "wo": "を",
    "ga": "が", "gi": "ぎ", "gu": "ぐ", "ge": "げ", "go": "ご",
    "za": "ざ", "zi": "じ", "zu": "ず", "ze": "ぜ", "zo": "ぞ",
    "da": "だ", "du": "づ", "de": "で", "do": "ど", "di": "じ",
    "ba": "ば", "bi": "び", "bu": "ぶ", "be": "べ", "bo": "ぼ",
    "pa": "ぱ", "pi": "ぴ", "pu": "ぷ", "pe": "ぺ", "po": "ぽ",
    "kya": "きゃ", "kyu": "きゅ", "kyo": "きょ",
    "sha": "しゃ", "shu": "しゅ", "sho": "しょ","shi": "しい",
    "cha": "ちゃ", "chu": "ちゅ", "cho": "ちょ","ti": "ちい",
    "nya": "にゃ", "nyu": "にゅ", "nyo": "にょ",
    "hya": "ひゃ", "hyu": "ひゅ", "hyo": "ひょ",
    "mya": "みゃ", "myu": "みゅ", "myo": "みょ",
    "rya": "りゃ", "ryu": "りゅ", "ryo": "りょ",
    "gya": "ぎゃ", "gyu": "ぎゅ", "gyo": "ぎょ",
    "ja": "じゃ", "ju": "じゅ", "jo": "じょ","ji": "ぢ",
    "bya": "びゃ", "byu": "びゅ", "byo": "びょ",
    "pya": "ぴゃ", "pyu": "ぴゅ", "pyo": "ぴょ"
}

def progression():
    global v
    progressVar.set(int(v*100/len(textVar)))
    if v <len(textVar):
        v+=10
        root.after(1, progression)

def convert():
    global textVar, v
    v = 1
    t2 = threading.Thread(target= conversion)
    t2.start()
    t1 = threading.Thread(target= progression)
    root.after(50, t1.start)
    
def conversion():
    global textVar, v, nihonVar, romanjiVar
    nihonText.config( state = 'normal')
    textVar = latinText.get('0.0', 'end')
    textVar = textVar.strip()
    textVar = textVar.lower()
    nihonVar = ''
    letters = 'azertyuiopqsdfghjklmwxcvbn'
    clist = ['eéèêë', 'aâäà', 'uùûü', 'iïî', 'oöô']
    llist = 'eauio'
    for i in range(len(llist)):
        for j in range(len(textVar)):
            if textVar[j] in clist[i]:
                textVar = textVar.replace(textVar[j], llist[i])
    
    consonn = 'zrtypqsdfghjklmwxcvbn'
    vowel = 'aeiou'
    i = 0
    textVar = textVar.replace('v','b')
    textVar = textVar.replace('x','z')
    textVar = textVar.replace("qu",'k')
    while i < len(textVar):
        if textVar[i] not in letters :
            nihonVar+= textVar[i]
            romanjiVar += textVar[i]
            i+=1
        elif textVar[i] in consonn:
            if textVar[i+1] in consonn:
                if textVar[i+1] == textVar[i]:
                    sc = textVar[i]+'u'
                    try:
                        nihonVar += latinHira[sc]
                        romanjiVar += sc
                    except:
                        nihonVar += textVar[i]+textVar[i]
                        romanjiVar += textVar[i]+textVar[i]
                    i+= 2
                elif textVar[i+1] != textVar[i]:
                    if textVar[i+2] in vowel and textVar[i+1] in ('h','y'):
                        sc = textVar[i]+textVar[i+2]
                        try:
                            nihonVar += latinHira[sc]
                            romanjiVar += sc
                            i +=3
                        except:
                            try:
                                nihonVar += latinHira[textVar[i]+'u']
                                romanjiVar += textVar[i]+'u'
                                i+= 1
                            except:
                                nihonVar += textVar[i]
                                romanjiVar += textVar[i]
                                i+=1
                    elif textVar[i+1]=='y':
                        try:
                            nihonVar += latinHira[textVar[i]+'i']
                            romanjiVar += textVar[i]+'i'
                            i +=2
                        except:
                            try:
                                nihonVar += latinHira[textVar[i]+'hi']
                                romanjiVar += textVar[i]+'hi'
                                i +=2
                            except:
                                nihonVar += latinHira[textVar[i]+'u']
                                romanjiVar += textVar[i]+'u'
                                i+=1
                    else:
                        try:
                            nihonVar += latinHira[textVar[i]+'u']
                            romanjiVar += textVar[i]+'u'
                            i+= 1
                        except:
                            nihonVar += textVar[i]
                            romanjiVar += textVar[i]
                            i+=1
                else:
                    sc = textVar[i]+'u'
                    try:
                        nihonVar += latinHira[sc]
                        romanjiVar += sc
                    except:
                        nihonVar += textVar[i]
                        romanjiVar += textVar[i]
                    i+= 1
            elif textVar[i+1] in vowel:
                sc = textVar[i]+textVar[i+1]
                try:
                    nihonVar += latinHira[sc]
                    romanjiVar += sc
                    i+= 2
                except:
                    nihonVar += textVar[i]
                    romanjiVar += textVar[i]
                    i+= 1
            else:
                sc = textVar[i]+'u'
                try:
                    nihonVar += latinHira[sc]
                    romanjiVar += sc
                except:
                    romanjiVar += textVar[i]
                    nihonVar += textVar[i]
                i+= 1
        elif textVar[i] in vowel:
            nihonVar += latinHira[textVar[i]]
            romanjiVar += textVar[i]
            i+= 1
        else:
            nihonVar += textVar[i]
            romanjiVar += textVar[i]
            i+= 1
        #time.sleep(0.00001)
    nihonText.insert('end', nihonVar)
    nihonText.config( state = 'disabled')
    pass

def importFile():
    file = askopenfilename(filetypes = [('text','.txt')])
    if file:
        resetText()
        nihonText.config( state = 'normal')
        with open(file, 'rb') as fiche :
            content = fiche.read()
        content = content.decode('utf8')
        latinText.insert('end', content)
        nihonText.config( state = 'disabled')

def resetText():
    nihonText.config( state = 'normal')
    latinText.delete('0.0', 'end')
    nihonText.delete('0.0', 'end')
    nihonText.config( state = 'disabled')
    progressVar.set(0)

def save():
    global nihonVar, romanjiVar
    file = asksaveasfilename(filetypes = [('text','.txt')])
    if file:
        with open(file, 'wb') as fiche:
            fiche.write(nihonVar.encode('utf8'))
        with open('r_'+file, 'wb') as fiche:
            fiche.write(romanjiVar.encode('utf8'))
            showinfo('alerte', 'fichier sauvegrader avec succes')

def checker():
    global nihonVar, romanjiVar
    nihonText.config( state = 'normal')
    if checkVar.get() ==0:
        nihonText.delete('0.0', 'end')
        nihonText.insert('end', nihonVar)
        check.config(text = 'hiragana viewed')
    else:
        nihonText.delete('0.0', 'end')
        nihonText.insert('end', romanjiVar)
        check.config(text = 'romanji viewed')
    nihonText.config( state = 'disabled')

root = Tk()
root.title('latin - hiragana Converter')
color, bgColor = '#ffffff', '#333355'
root['bg'] = '#222244'
root.iconbitmap('nihon.ico')
w , h = root.winfo_screenwidth(), root.winfo_screenheight()
textVar , progressVar, checkVar= '', IntVar(), IntVar()
root.maxsize(int(w*0.41), int(h*0.85))
nihonVar, romanjiVar = '', ''
tableImage,tablePhoto,tableImageLoad=[],[],['japan.png','open.png','erase.png','reload.png','save.png']

for i in range(len(tableImageLoad)):
    tableImage.append(PIL.Image.open(tableImageLoad[i]))
    if i ==0 :
        tableImage[-1]=tableImage[-1].resize((50,50),PIL.Image.LANCZOS)
    else:
        tableImage[-1]=tableImage[-1].resize((20,20),PIL.Image.LANCZOS)
    tablePhoto.append(ImageTk.PhotoImage(tableImage[-1]))


style = Style()
style.theme_use('xpnative')
available_themes = style.theme_names()
print(f"Thèmes disponibles : {available_themes}")
style.configure('TButton', font =('cambria',15,'bold','italic'), background ='#222244', foreground='#4444cc', relief = 'flat')
style.configure('TProgressbar',  background='#4444cc')
titleLab = Label(root, text = 'Apprendre le JAPONAIS  \n Latin - Hiragana Converter by Python Lite Fr',
                 font =('cambria',20,'bold','italic'), fg =color, bg=bgColor, image = tablePhoto[0], compound = 'left')
latinLab = Label(root, text = 'Latin text here', anchor ='w', font =('cambria',15,'bold','italic'), fg =color, bg=bgColor)
latinText = Text(root, width = int(w*0.05), height = int(h*0.018), bg = '#ffffff')

importButton = Button(root, text = 'import file', command = importFile, style = 'TButton', image = tablePhoto[1], compound = 'right')
eraseButton = Button(root, text = 'erase text', command = resetText , style = 'TButton', image = tablePhoto[2], compound = 'right')
convertButton = Button(root, text = 'convert ', command = convert , style = 'TButton', image = tablePhoto[3], compound = 'right')

nihonLab = Label(root, text = 'hiragana text here', anchor ='w', font =('cambria',15,'bold','italic'), fg =color, bg=bgColor)
nihonText = Text(root, width = int(w*0.05), height = int(h*0.018), state = 'disabled', fg = '#222288')
progress = Progressbar(root, orient="horizontal", length=100, 
mode="determinate", variable = progressVar, style = 'TProgressbar')
check = Checkbutton(root, variable = checkVar, text = 'hiragana', command = checker, font =('cambria',15,'bold','italic'), fg =color, bg=bgColor)
saveButton = Button(root, text = 'save conversion ', command = save , style = 'TButton', image = tablePhoto[4], compound = 'right')

titleLab.grid(column = 0, row = 0, columnspan =3 , sticky ='nswe' , padx = 5, pady = 1)
latinLab.grid(column = 0, row = 1, columnspan = 3, sticky = 'nswe', padx = 5, pady = 1)
latinText.grid(column = 0, row =2 , columnspan = 3, sticky = 'nswe', padx = 5, pady = 1)
importButton.grid(column =0 , row = 4, sticky = 'ns', padx = 1, pady = 5)
eraseButton.grid(column = 1, row = 4,  sticky = 'ns', padx = 1, pady = 5)
convertButton.grid(column =2 , row = 4, sticky = 'ns', padx = 1, pady = 5)
nihonLab.grid(column = 0, row = 5, columnspan = 3, sticky = 'nswe', padx = 5, pady = 1)
nihonText.grid(column = 0, row = 6, columnspan = 3, sticky = 'nswe', padx = 5, pady = 1)
progress.grid(column =0 , row = 7, sticky = 'nswe', padx = 1, pady = 5)
check.grid(column =1 , row = 7, sticky = 'ns', padx = 1, pady = 5)
saveButton.grid(column =2 , row = 7, sticky = 'ns', padx = 1, pady = 5)

root.mainloop()
