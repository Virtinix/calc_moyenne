# imports
from tkinter import *
from turtle import bgcolor, right

# app instance
app = Tk()

# app config
app.title("Calcul moyenne")
app.config(background="#2C795D")
app.geometry("1080x720")
app.minsize(600, 450)

# frame du milieu
frame = Frame(app, background="#2C795D")
frame.pack(expand=YES)

# widjets:

# label pour donner des instructions pour l'utilisation de l'app
lb = Label(frame, text="Entrer la note et son coefficient :\n\n",
           font=(("Helvetica"), 30), fg="white", bg="#2C795D")

# première partie de la note (numérateur)
note1 = Entry(frame, font=(("Courrier"), 15),
              fg="white", bg="#2C795D", width=5)

# deuxième partie de la note (dénominateur)
note2 = Entry(frame, font=(("Courrier"), 15),
              fg="white", bg="#2C795D", width=5)

# ligne de fraction
canvas = Canvas(frame, background="#2C795D", width=400,
                height=100, bd=0, highlightthickness=0)

ligne1 = canvas.create_line(1000000, 0, 0, 50, width=6, fill='black')

# canva pour faire un espace
space_canva = Canvas(frame, background="#2C795D",
                     height=100, bd=0, highlightthickness=0)

# label info coef
lb_coef = Label(frame, text="Coefficient :\n",
                font=(("Helvetica"), 20), fg="white", bg="#2C795D")

# coef
coef = Entry(frame, font=(("Courrier"), 15), fg="white", bg="#2C795D", width=7)

# positionnement
lb.pack()
note1.pack()
canvas.pack()
note2.pack()
space_canva.pack()
lb_coef.pack()
coef.pack()

# lists recupération des notes
note1_list = []
note2_list = []
coef_list = []


def suivant_btn_press():
    # récupération des notes
    note1_list.append(note1.get())
    note2_list.append(note2.get())
    coef_list.append(coef.get())

    # Suppr des notes
    note1.delete(0, END)
    note2.delete(0, END)
    coef.delete(0, END)


def end_note():
    # suppr de touts les éléments
    lb.pack_forget()
    note1.pack_forget()
    canvas.pack_forget()
    note2.pack_forget()
    space_canva.pack_forget()
    lb_coef.pack_forget()
    coef.pack_forget()
    next_note_btn.pack_forget()
    end_note_btn.pack_forget()

    # récup la dernière note
    note1_list.append(note1.get())
    note2_list.append(note2.get())
    coef_list.append(coef.get())

    # varibales
    note_nbr = -1
    coef_nbr = -1
    note_on_20 = []

    # calcul de la moyenne
    for i in range(len(coef_list)):
        note_nbr += 1
        coef_nbr += 1
        note_on_20.append(float(
            note1_list[note_nbr]) * 20 / float(note2_list[note_nbr]) * float(coef_list[coef_nbr]))

    total_coef = sum(list(map(int, coef_list)))
    # moyenne finale
    moyenne = sum(note_on_20) / total_coef

    # affichage : resultat final de la moyenne
    lb_final_result = Label(frame, font=(("Helvetica"), 30), fg="white",
                            bg="#2C795D", text="La moyenne finale des notes entrées est :\n\n")
    lb_final_result.pack()

    # affichage de la moyenne finale
    lb_moyenne = Label(frame, font=(("Helvetica"), 40),
                       fg="white", bg="#2C795D", text=moyenne)
    lb_moyenne.pack()


# bouton note suivante
next_note_btn = Button(app, text="Note suivante", fg="white",
                       bg="#2C795D", font=(("Helvetica"), 25), command=suivant_btn_press)

end_note_btn = Button(app, text="Fin", fg="white",
                      bg="#2C795D", font=(("Helvetica"), 25), command=end_note)

# position des boutons
next_note_btn.pack(side=RIGHT, padx=40, pady=40)
end_note_btn.pack(side=RIGHT)

# affichage de la fenêtre
app.mainloop()
