from tkinter import *

app = Tk()
app.title('Calculateur Moyenne')
app.geometry("10000x10000")
app.minsize(500, 300)
app.config(background='#DF6F1C')

frame = Frame(app, bg='#DF6F1C')
frame.pack(expand=YES)

#Fonctions :

def func_1():
    #Suppr n°1
    entry_note1_part1.pack_forget()
    entry_note1_part2.pack_forget()
    entry_coef1.pack_forget()
    btn_1.pack_forget()
    #ajout n°2
    entry_note2_part1.pack()
    entry_note2_part2.pack()
    entry_coef2.pack()
    btn_2.pack()
    
#Savoir si oui ou non on veut continuer
def yes_or_no_1():
    #Suppr n°2
    entry_note2_part1.pack_forget()
    entry_note2_part2.pack_forget()
    entry_coef2.pack_forget()
    btn_2.pack_forget()
    #ajout oui/non 1
    lb_1['text'] = 'Veuillez indiquer si oui ou non vous voulez continuer :\n'
    btn_yes_1.pack()
    btn_no_1.pack()
    
#si on appuie sur le bouton 'oui'
def yes_1():
    #suppr oui/non
    btn_yes_1.pack_forget()
    btn_no_1.pack_forget()
    # ajout n°3
    lb_1['text'] = 'Entrer la première et deuxième partie de la première note et le coefficient de cette note ici :\n'
    entry_note3_part1.pack()
    entry_note3_part2.pack()
    entry_coef3.pack()
    btn_3.pack()
    

#si on appuie sur le bouton 'non'
def no_1():
    note1_part1 = float(entry_note1_part1.get())
    note1_part2 = float(entry_note1_part2.get())
    coef1 = float(entry_coef1.get())
    note2_part1 = float(entry_note2_part1.get())
    note2_part2 = float(entry_note2_part2.get())
    coef2 = float(entry_coef2.get())
    #mettre la note sur 20
    note_20_1 = note1_part1 * 20 / note1_part2
    note_20_2 = note2_part1 * 20 / note2_part2
    #calculer la moyenne
    global moyenne_1
    moyenne_1 =  (note_20_1 * coef1 + note_20_2 * coef2) / (coef1 + coef2)
    #modif et suppr
    lb_1['text'] = 'La moyenne de ces notes est :\n'
    lb_1['font'] = ('Helvetica', 26)
    btn_yes_1.pack_forget()
    btn_no_1.pack_forget()
    #Créer un nouveau label avec la moyenne
    vb_1 = DoubleVar()
    vb_1.set(moyenne_1)
    lb_moyenne_1 = Label(frame, font=("helvetica", 23), textvariable=vb_1, bg='#DF6F1C', fg='white')
    lb_moyenne_1.pack()
    
def yes_or_no_2():
    #Suppr n°2
    entry_note3_part1.pack_forget()
    entry_note3_part2.pack_forget()
    entry_coef3.pack_forget()
    btn_3.pack_forget()
    #ajout oui/non 1
    lb_1['text'] = 'Veuillez indiquer si oui ou non vous voulez continuer :\n'
    btn_yes_2.pack()
    btn_no_2.pack()
    
def no_2():
    note1_part1 = float(entry_note1_part1.get())
    note1_part2 = float(entry_note1_part2.get())
    coef1 = float(entry_coef1.get())
    note2_part1 = float(entry_note2_part1.get())
    note2_part2 = float(entry_note2_part2.get())
    coef2 = float(entry_coef2.get())
    note3_part1 = float(entry_note3_part1.get())
    note3_part2 = float(entry_note3_part2.get())
    coef3 = float(entry_coef3.get())
    #mettre la note sur 20
    note_20_1 = note1_part1 * 20 / note1_part2
    note_20_2 = note2_part1 * 20 / note2_part2
    note_20_3 = note3_part1 * 20 / note3_part2
    #calculer la moyenne
    global moyenne_2
    moyenne_2 =  (note_20_1 * coef1 + note_20_2 * coef2 + note_20_3 * coef3) / (coef1 + coef2 + coef3)
    #modif et suppr
    lb_1['text'] = 'La moyenne de ces notes est :\n'
    lb_1['font'] = ('Helvetica', 26)
    btn_yes_2.pack_forget()
    btn_no_2.pack_forget()
    #Créer un nouveau label avec la moyenne
    vb_2 = DoubleVar()
    vb_2.set(moyenne_2)
    lb_moyenne_2 = Label(frame, font=("helvetica", 23), textvariable=vb_2, bg='#DF6F1C', fg='white')
    lb_moyenne_2.pack()
    
def yes_2():
    #suppr
    lb_1['text'] = 'Entrer la première et deuxième partie de la note et le coefficient de cette note ici :\n'
    btn_no_2.pack_forget()
    btn_yes_2.pack_forget()
    #ajout note 4
    entry_note4_part1.pack()
    entry_note4_part2.pack()
    entry_coef4.pack()
    btn_4.pack()

def yes_or_no_3():
    #Suppr
    entry_note4_part1.pack_forget()
    entry_note4_part2.pack_forget()
    entry_coef4.pack_forget()
    btn_4.pack_forget()
    #ajout oui/non 3
    lb_1['text'] = 'Veuillez indiquer si oui ou non vous voulez continuer :\n'
    btn_yes_3.pack()
    btn_no_3.pack()
    
def no_3():
    note1_part1 = float(entry_note1_part1.get())
    note1_part2 = float(entry_note1_part2.get())
    coef1 = float(entry_coef1.get())
    note2_part1 = float(entry_note2_part1.get())
    note2_part2 = float(entry_note2_part2.get())
    coef2 = float(entry_coef2.get())
    note3_part1 = float(entry_note3_part1.get())
    note3_part2 = float(entry_note3_part2.get())
    coef3 = float(entry_coef3.get())
    note4_part1 = float(entry_note4_part1.get())
    note4_part2 = float(entry_note4_part2.get())
    coef4 = float(entry_coef4.get())
    #mettre la note sur 20
    note_20_1 = note1_part1 * 20 / note1_part2
    note_20_2 = note2_part1 * 20 / note2_part2
    note_20_3 = note3_part1 * 20 / note3_part2
    note_20_4 = note4_part1 * 20 / note4_part2
    #calculer la moyenne
    global moyenne_3
    moyenne_3 =  (note_20_1 * coef1 + note_20_2 * coef2 + note_20_3 * coef3 + note_20_4 * coef4) / (coef1 + coef2 + coef3 + coef4)
    #modif et suppr
    lb_1['text'] = 'La moyenne de ces notes est :\n'
    lb_1['font'] = ('Helvetica', 26)
    btn_yes_3.pack_forget()
    btn_no_3.pack_forget()
    #Créer un nouveau label avec la moyenne
    vb_3 = DoubleVar()
    vb_3.set(moyenne_3)
    lb_moyenne_3 = Label(frame, font=("helvetica", 23), textvariable=vb_3, bg='#DF6F1C', fg='white')
    lb_moyenne_3.pack()

def yes_3():
    #suppr oui/non 3
    btn_yes_3.pack_forget()
    btn_no_3.pack_forget()
    #ajout note 5
    lb_1['text'] = 'Entrer la première et deuxième partie de la note et le coefficient de cette note ici :\n'
    entry_note5_part1.pack()
    entry_note5_part2.pack()
    entry_coef5.pack()
    btn_5.pack()

def yes_or_no_4():
    #Suppr
    entry_note5_part1.pack_forget()
    entry_note5_part2.pack_forget()
    entry_coef5.pack_forget()
    btn_5.pack_forget()
    #ajout oui/non 3
    lb_1['text'] = 'Veuillez indiquer si oui ou non vous voulez continuer :\n'
    btn_yes_4.pack()
    btn_no_4.pack()
    
def no_4():
    note1_part1 = float(entry_note1_part1.get())
    note1_part2 = float(entry_note1_part2.get())
    coef1 = float(entry_coef1.get())
    note2_part1 = float(entry_note2_part1.get())
    note2_part2 = float(entry_note2_part2.get())
    coef2 = float(entry_coef2.get())
    note3_part1 = float(entry_note3_part1.get())
    note3_part2 = float(entry_note3_part2.get())
    coef3 = float(entry_coef3.get())
    note4_part1 = float(entry_note4_part1.get())
    note4_part2 = float(entry_note4_part2.get())
    coef4 = float(entry_coef4.get())
    note5_part1 = float(entry_note5_part1.get())
    note5_part2 = float(entry_note5_part2.get())
    coef5 = float(entry_coef5.get())
    #mettre la note sur 20
    note_20_1 = note1_part1 * 20 / note1_part2
    note_20_2 = note2_part1 * 20 / note2_part2
    note_20_3 = note3_part1 * 20 / note3_part2
    note_20_4 = note4_part1 * 20 / note4_part2
    note_20_5 = note5_part1 * 20 / note5_part2
    #calculer la moyenne
    global moyenne_4
    moyenne_4 =  (note_20_1 * coef1 + note_20_2 * coef2 + note_20_3 * coef3 + note_20_4 * coef4 + note_20_5 * coef5) / (coef1 + coef2 + coef3 + coef4 + coef5)
    #modif et suppr
    lb_1['text'] = 'La moyenne de ces notes est :\n'
    lb_1['font'] = ('Helvetica', 26)
    btn_yes_4.pack_forget()
    btn_no_4.pack_forget()
    #Créer un nouveau label avec la moyenne
    vb_4 = DoubleVar()
    vb_4.set(moyenne_4)
    lb_moyenne_4 = Label(frame, font=("helvetica", 23), textvariable=vb_4, bg='#DF6F1C', fg='white')
    lb_moyenne_4.pack()

def yes_4():
    #suppr oui/non 3
    btn_yes_4.pack_forget()
    btn_no_4.pack_forget()
    #ajout n°6
    lb_1['text'] = 'Entrer la première et deuxième partie de la note et le coefficient de cette note ici :\n'
    entry_note6_part1.pack()
    entry_note6_part2.pack()
    entry_coef6.pack()
    btn_6.pack()
    
def end():
    note1_part1 = float(entry_note1_part1.get())
    note1_part2 = float(entry_note1_part2.get())
    coef1 = float(entry_coef1.get())
    note2_part1 = float(entry_note2_part1.get())
    note2_part2 = float(entry_note2_part2.get())
    coef2 = float(entry_coef2.get())
    note3_part1 = float(entry_note3_part1.get())
    note3_part2 = float(entry_note3_part2.get())
    coef3 = float(entry_coef3.get())
    note4_part1 = float(entry_note4_part1.get())
    note4_part2 = float(entry_note4_part2.get())
    coef4 = float(entry_coef4.get())
    note5_part1 = float(entry_note5_part1.get())
    note5_part2 = float(entry_note5_part2.get())
    coef5 = float(entry_coef5.get())
    note6_part1 = float(entry_note6_part1.get())
    note6_part2 = float(entry_note6_part2.get())
    coef6 = float(entry_coef6.get())
    #mettre la note sur 20
    note_20_1 = note1_part1 * 20 / note1_part2
    note_20_2 = note2_part1 * 20 / note2_part2
    note_20_3 = note3_part1 * 20 / note3_part2
    note_20_4 = note4_part1 * 20 / note4_part2
    note_20_5 = note5_part1 * 20 / note5_part2
    note_20_6 = note6_part1 * 20 / note6_part2
    #calculer la moyenne
    global moyenne_5
    moyenne_5 =  (note_20_1 * coef1 + note_20_2 * coef2 + note_20_3 * coef3 + note_20_4 * coef4 + note_20_5 * coef5 + note_20_6 * coef6) / (coef1 + coef2 + coef3 + coef4 + coef5 + coef6)
    #modif et suppr
    lb_1['text'] = 'La moyenne de ces notes est :\n'
    lb_1['font'] = ('Helvetica', 26)
    entry_note6_part1.pack_forget()
    entry_note6_part2.pack_forget()
    entry_coef6.pack_forget()
    btn_6.pack_forget()
    #Créer un nouveau label avec la moyenne
    vb_5 = DoubleVar()
    vb_5.set(moyenne_5)
    lb_moyenne_5 = Label(frame, font=("helvetica", 23), textvariable=vb_5, bg='#DF6F1C', fg='white')
    lb_moyenne_5.pack()
    
        
lb_1 = Label(frame, text='Entrer la première et deuxième partie de la note et le coefficient de cette note ici :\n', font=('Helvetica', 20), bg='#DF6F1C', fg='white')
lb_1.pack()

#Note 1 partie 1, 2, coef1 et bouton 1 :
entry_note1_part1 = Entry(frame, fg='white', bg='#DF6F1C', font=('Helvetica', 23))
entry_note1_part1.pack()

entry_note1_part2 = Entry(frame, fg='white', bg='#DF6F1C', font=('Helvetica', 23))
entry_note1_part2.pack()

entry_coef1 = Entry(frame, fg='white', bg='#DF6F1C', font=('Helvetica', 23))
entry_coef1.pack()

btn_1 = Button(frame, fg='white', bg='#DF6F1C', font=('Hecvetica', 22), text='Suivant', command=func_1)
btn_1.pack()

#Note 2 partie 1, 2, coef2 et bouton 2 :
entry_note2_part1 = Entry(frame, fg='white', bg='#DF6F1C', font=('Helvetica', 23))
entry_note2_part1.pack_forget()

entry_note2_part2 = Entry(frame, fg='white', bg='#DF6F1C', font=('Helvetica', 23))
entry_note2_part2.pack_forget()

entry_coef2 = Entry(frame, fg='white', bg='#DF6F1C', font=('Helvetica', 23))
entry_coef2.pack_forget()

btn_2 = Button(frame, fg='white', bg='#DF6F1C', font=('Hecvetica', 22), text='Suivant', command=yes_or_no_1)
btn_2.pack_forget()

#oui/non 1
btn_yes_1 = Button(frame, fg='white', bg='#DF6F1C', font=('Hecvetica', 22), text='Oui', command=yes_1)
btn_yes_1.pack_forget()

btn_no_1 = Button(frame, fg='white', bg='#DF6F1C', font=('Hecvetica', 22), text='Non', command=no_1)
btn_no_1.pack_forget()

#Note 3 partie 1, 2, coef3 et bouton 3 :
entry_note3_part1 = Entry(frame, fg='white', bg='#DF6F1C', font=('Helvetica', 23))
entry_note3_part1.pack_forget()

entry_note3_part2 = Entry(frame, fg='white', bg='#DF6F1C', font=('Helvetica', 23))
entry_note3_part2.pack_forget()

entry_coef3 = Entry(frame, fg='white', bg='#DF6F1C', font=('Helvetica', 23))
entry_coef3.pack_forget()

btn_3 = Button(frame, fg='white', bg='#DF6F1C', font=('Hecvetica', 22), text='Suivant', command=yes_or_no_2)
btn_3.pack_forget()

#Note 4 partie 1, 2, coef4 et bouton 4 :
entry_note4_part1 = Entry(frame, fg='white', bg='#DF6F1C', font=('Helvetica', 23))
entry_note4_part1.pack_forget()

entry_note4_part2 = Entry(frame, fg='white', bg='#DF6F1C', font=('Helvetica', 23))
entry_note4_part2.pack_forget()

entry_coef4 = Entry(frame, fg='white', bg='#DF6F1C', font=('Helvetica', 23))
entry_coef4.pack_forget()

btn_4 = Button(frame, fg='white', bg='#DF6F1C', font=('Hecvetica', 22), text='Suivant', command=yes_or_no_3)
btn_4.pack_forget()

#Note 5
entry_note5_part1 = Entry(frame, fg='white', bg='#DF6F1C', font=('Helvetica', 23))
entry_note5_part1.pack_forget()

entry_note5_part2 = Entry(frame, fg='white', bg='#DF6F1C', font=('Helvetica', 23))
entry_note5_part2.pack_forget()

entry_coef5 = Entry(frame, fg='white', bg='#DF6F1C', font=('Helvetica', 23))
entry_coef5.pack_forget()

btn_5 = Button(frame, fg='white', bg='#DF6F1C', font=('Hecvetica', 22), text='Suivant', command=yes_or_no_4)
btn_5.pack_forget()

#Note 6
entry_note6_part1 = Entry(frame, fg='white', bg='#DF6F1C', font=('Helvetica', 23))
entry_note6_part1.pack_forget()

entry_note6_part2 = Entry(frame, fg='white', bg='#DF6F1C', font=('Helvetica', 23))
entry_note6_part2.pack_forget()

entry_coef6 = Entry(frame, fg='white', bg='#DF6F1C', font=('Helvetica', 23))
entry_coef6.pack_forget()

btn_6 = Button(frame, fg='white', bg='#DF6F1C', font=('Hecvetica', 22), text='Afficher le résultat', command=end)
btn_6.pack_forget()

#yes/no 2
btn_yes_2 = Button(frame, fg='white', bg='#DF6F1C', font=('Hecvetica', 22), text='Oui', command=yes_2)
btn_yes_2.pack_forget()

btn_no_2 = Button(frame, fg='white', bg='#DF6F1C', font=('Hecvetica', 22), text='Non', command=no_2)
btn_no_2.pack_forget()

#yes/no 3
btn_yes_3 = Button(frame, fg='white', bg='#DF6F1C', font=('Hecvetica', 22), text='Oui', command=yes_3)
btn_yes_3.pack_forget()

btn_no_3 = Button(frame, fg='white', bg='#DF6F1C', font=('Hecvetica', 22), text='Non', command=no_3)
btn_no_3.pack_forget()

#yes/no 4
btn_yes_4 = Button(frame, fg='white', bg='#DF6F1C', font=('Hecvetica', 22), text='Oui', command=yes_4)
btn_yes_4.pack_forget()

btn_no_4 = Button(frame, fg='white', bg='#DF6F1C', font=('Hecvetica', 22), text='Non', command=no_4)
btn_no_4.pack_forget()

app.mainloop()