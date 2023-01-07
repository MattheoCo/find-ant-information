import tkinter as tk
import sqlite3
conn = sqlite3.connect('mirme.db')
c = conn.cursor()
c.execute('''CREATE TABLE if not exists mirme
            (sp TEXT, nom PRIMARY KEY, fondation TEXT, foreuse TEXT, nourriture TEXT, temp TEXT, humi TEXT, diap TEXT, temp_diap TEXT)''')

class Create_sp:
    def __init__(self, sp, nom, fondation, foreuse, nourriture, temp, humi, diap, temp_diap):
        self.sp = sp
        self.nom = nom
        self.fondation = fondation
        self.foreuse = foreuse
        self.nourriture = nourriture
        self.temp = temp
        self.humi = humi
        self.diap = diap
        self.temp_diap = temp_diap
        self.v=[(self.sp, self.nom, self.fondation, self.foreuse, self.nourriture, self.temp, self.humi, self.diap, self.temp_diap)]
        c.executemany("INSERT INTO mirme VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", self.v)
    
def affiche_info_sp(espece, nom):
    esp = str(espece)
    n = str(nom)
    c.execute("SELECT * FROM mirme WHERE sp = ? AND nom = ?", (esp, n))
    lst_tuples = c.fetchall()
    print(lst_tuples)
    for resultat in lst_tuples:  # chaque résultat est un tuple
        sp = resultat[0]
        nom  = resultat[1]
        fondation = resultat[2]
        foreuse = resultat[3]
        nourriture = resultat[4]
        temp = resultat[5]
        humi = resultat[6]
        diap = resultat[7]
        temp_diap = resultat[8]
        label11.configure(text=sp)
        label12.configure(text=nom)
        label13.configure(text=fondation)
        label14.configure(text=foreuse)
        label15.configure(text=nourriture)
        label16.configure(text=temp)
        label17.configure(text=humi)
        label18.configure(text=diap)
        label19.configure(text=temp_diap)

def main():
    espece = value.get()
    nom = valuee.get
    affiche_info_sp(espece, nom)


f1 = Create_sp("lasius", "niger", "claustrale", "NON", "omnivore", "20 à 26°", "40 à 70%", "obligatoire", "5 à 10°")
f2 = Create_sp("lasius", "flavus", "claustrale", "NON", "omnivore", "24 à 26°", "80 à 100%", "obligatoire", "6 à 15°")
f3 = Create_sp("lasius", "emarginatus", "claustrale", "NON", "omnivore", "20 à 28°", "15 à 40%", "obligatoire", "5 à 10°")


fenetre = tk.Tk()
#===================================
#           On assigne les paramètre de la fenètre
#===================================
fenetre.iconbitmap('icone.ico')
fenetre.title('Dico des fourmis')
fenetre.configure(bg='#988080')

#explication de la fenètre
expliquation = tk.Label(fenetre, text="Cette fenêtre permets d'obtenir les informations voulue pour une espèce de fourmis.", bg='#988080')
expliquation.grid(row =1, column=0, columnspan = 9)

fonction = tk.Label(fenetre, text="Plus précisement elle vous donnera en fonction de nom et de l'espèce :", bg='#988080')
fonction.grid(row=2, column=0, columnspan = 9)

fonction = tk.Label(fenetre, text="type de fondation, si elle est foreuse, quelle nourriture, quelle température obtimal, quelle humidité, si besoins de diapause, quelle température de diapause", bg='#988080')
fonction.grid(row=3, column=0, columnspan = 9)

fonction = tk.Label(fenetre, text="Ne mettre aucune majuscule", bg='#988080')
fonction.grid(row=4, column=0, columnspan = 9)

fonction = tk.Label(fenetre, text="", bg='#988080')
fonction.grid(row=6, column=0, columnspan = 9)

value = tk.StringVar() 
value.set("Quelle est l'espèce ?")
entree = tk.Entry(fenetre, textvariable=value, width=30)
entree.grid(row=5, column=0, columnspan = 4)

valuee = tk.StringVar() 
valuee.set("Quelle est son nom ?")
entree = tk.Entry(fenetre, textvariable=valuee, width=30)
entree.grid(row=5, column=6, columnspan = 4)

#===================================
#           CREATION DES FRAMES
#===================================
# frame 1
Frame1 = tk.Frame(fenetre, borderwidth=2)
Frame1.grid(row = 7, column=0)

# frame 2
Frame2 = tk.Frame(fenetre, borderwidth=2)
Frame2.grid(row = 7, column=1)

# frame 3
Frame3 = tk.Frame(fenetre, borderwidth=2)
Frame3.grid(row = 7, column=2)

# frame 4
Frame4 = tk.Frame(fenetre, borderwidth=2)
Frame4.grid(row = 7, column=3)

# frame 5
Frame5 = tk.Frame(fenetre, borderwidth=2)
Frame5.grid(row = 7, column=4)

# frame 6
Frame6 = tk.Frame(fenetre, borderwidth=2)
Frame6.grid(row = 7, column=5)

# frame 7
Frame7 = tk.Frame(fenetre, borderwidth=2)
Frame7.grid(row = 7, column=6)

# frame 8
Frame8 = tk.Frame(fenetre, borderwidth=2)
Frame8.grid(row = 7, column=7)

# frame 9
Frame9 = tk.Frame(fenetre, borderwidth=2)
Frame9.grid(row = 7, column=8)
#===================================
#           CREATION DES FRAMES
#===================================

#===================================
#                 ZONE REPONSES
#===================================
# frame 1
Frame11 = tk.Frame(fenetre, borderwidth=2)
Frame11.grid(row = 8, column=0)

# frame 2
Frame12 = tk.Frame(fenetre, borderwidth=2)
Frame12.grid(row = 8, column=1)

# frame 3
Frame13 = tk.Frame(fenetre, borderwidth=2)
Frame13.grid(row = 8, column=2)

# frame 4
Frame14 = tk.Frame(fenetre, borderwidth=2)
Frame14.grid(row = 8, column=3)

# frame 5
Frame15 = tk.Frame(fenetre, borderwidth=2)
Frame15.grid(row = 8, column=4)

# frame 6
Frame16 = tk.Frame(fenetre, borderwidth=2)
Frame16.grid(row = 8, column=5)

# frame 7
Frame17 = tk.Frame(fenetre, borderwidth=2)
Frame17.grid(row = 8, column=6)

# frame 8
Frame18 = tk.Frame(fenetre, borderwidth=2)
Frame18.grid(row = 8, column=7)

# frame 9
Frame19 = tk.Frame(fenetre, borderwidth=2)
Frame19.grid(row = 8, column=8)
#===================================
#                 ZONE REPONSES
#===================================

#===================================
#ATTRIBUTION DES DONNES AUX FRAMES
#===================================
label1 = tk.Label(Frame1, text="espèce")
label1.grid()
label2 = tk.Label(Frame2, text="nom")
label2.grid()
label3 = tk.Label(Frame3, text="type de fondation")
label3.grid()
label4 = tk.Label(Frame4, text="foreuse ?")
label4.grid()
label5 = tk.Label(Frame5, text="alimentation ?")
label5.grid()
label6 = tk.Label(Frame6, text="température")
label6.grid()
label7 = tk.Label(Frame7, text="humidité")
label7.grid()
label8 = tk.Label(Frame8, text="diapause ?")
label8.grid()
label9 = tk.Label(Frame9, text="température de diapause")
label9.grid()

label11 = tk.Label(Frame1, text="'affichage ici'")
label11.grid()
label12 = tk.Label(Frame2, text="'affichage ici'")
label12.grid()
label13 = tk.Label(Frame3, text="'affichage ici'")
label13.grid()
label14 = tk.Label(Frame4, text="'affichage ici'")
label14.grid()
label15 = tk.Label(Frame5, text="'affichage ici'")
label15.grid()
label16 = tk.Label(Frame6, text="'affichage ici'")
label16.grid()
label17 = tk.Label(Frame7, text="'affichage ici'")
label17.grid()
label18 = tk.Label(Frame8, text="'affichage ici'")
label18.grid()
label19 = tk.Label(Frame9, text="'affichage ici'")
label19.grid()
#===================================
#ATTRIBUTION DES DONNES AUX FRAMES
#===================================

tk.Button(text="Lancer la recherche", bg='#988080', command=main).grid(row=8, column=0, columnspan = 9)


#===================================
#           On ferme la fenètre
#===================================
fenetre.mainloop()

