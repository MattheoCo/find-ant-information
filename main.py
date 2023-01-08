import tkinter as tk
import sqlite3
conn = sqlite3.connect('mirme.db')
c = conn.cursor()
c.execute('''CREATE TABLE if not exists mirme
            (sp TEXT, nom PRIMARY KEY, fondation TEXT, foreuse TEXT, nourriture TEXT, temp TEXT, humi TEXT, diap TEXT, temp_diap TEXT,
            origine TEXT, nb_gyne TEXT, tp_nid, conseil TEXT)''')

class Create_sp:
    def __init__(self, sp, nom, fondation, foreuse, nourriture, temp, humi, diap, temp_diap, origine, nb_gyne, tp_nid, conseil):
        self.sp = sp
        self.nom = nom
        self.fondation = fondation
        self.foreuse = foreuse
        self.nourriture = nourriture
        self.temp = temp
        self.humi = humi
        self.diap = diap
        self.temp_diap = temp_diap
        self.origine = origine
        self.nb_gyne = nb_gyne
        self.tp_nid = tp_nid
        self.conseil = conseil
        self.v=[(self.sp, self.nom, self.fondation, self.foreuse, self.nourriture, self.temp, self.humi, self.diap, self.temp_diap, self.origine, self.nb_gyne, self.tp_nid, self.conseil)]
        c.executemany("INSERT INTO mirme VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", self.v)
    
def affiche_info_sp(espece, nom):
    esp = str(espece)
    n = str(nom)
    c.execute("SELECT * FROM mirme WHERE sp = ? AND nom = ?", (esp, n))
    lst_tuples = c.fetchall()
    for resultat in lst_tuples:
        sp = resultat[0]
        nom  = resultat[1]
        fondation = resultat[2]
        foreuse = resultat[3]
        nourriture = resultat[4]
        temp = resultat[5]
        humi = resultat[6]
        diap = resultat[7]
        temp_diap = resultat[8]
        origine = resultat[9]
        nb_gyne = resultat[10]
        type_nid = resultat[11]
        conseil = resultat[12]
        label21.configure(text=sp)
        label11.configure(text=nom)
        label12.configure(text=fondation)
        label13.configure(text=foreuse)
        label14.configure(text=nourriture)
        label16.configure(text=temp)
        label17.configure(text=humi)
        label18.configure(text=diap)
        label22.configure(text=temp_diap)
        label19.configure(text=origine)
        label20.configure(text=nb_gyne)
        label15.configure(text=type_nid)
        label25.configure(text=conseil)
        

def main():
    espece = value.get()
    nom = valuee.get()
    affiche_info_sp(espece, nom)


f1 = Create_sp("lasius", "niger", "claustrale", "non", "omnivore", "20 à 26°", "40 à 70%", "obligatoire", "5 à 10°", "Europe", "monogyne", "béton cellulaire, plâtre ou plexiglas", "C’est une espèce facile, elle pardonne bon nombres d’erreurs de débutant, et se développe rapidement même si les conditions ne sont pas respecté à la lettre. ")
f2 = Create_sp("lasius", "flavus", "claustrale", "non", "omnivore", "24 à 26°", "80 à 100%", "obligatoire", "6 à 15°", "Europe", "polygyne", "béton cellulaire ou plexiglas", " Elles se nourrissent de miellat de pucerons de racines. Leur nourriture est donc directement dans les galeries car elles les élèves. Une ADC au plus proche du nid sera donc parfait.")
f3 = Create_sp("lasius", "emarginatus", "claustrale", "non", "omnivore", "20 à 28°", "15 à 40%", "obligatoire", "5 à 10°", "Europe", "monogyne", "béton cellulaire, plâtre ou plexiglas", "Espèce facile à élever, l'étape de la fondation n'est pas compliqué à passer. L'éspèce ne sera pas embettante pour l'alimentation. Malgrés sa timidité au depart, elle gagnera vite en assurance grace a son nombre d'ouvrière.")
f4 = Create_sp("lasius","brunneus","claustrale","non","omnivore","20 à 28°","40 à 60%","obligatoire","5 à 10°","Europe","monogyne", "béton cellulaire, plâtre ou plexiglas", "Espèce facile à élever, l'étape de la fondation n'est pas compliqué à passer. L'éspèce ne sera pas embettante pour l'alimentation.")


fenetre = tk.Tk()
#===================================
#           On assigne les paramètre de la fenètre
#===================================
fenetre.iconbitmap('icone.ico')
fenetre.title('Dico des fourmis')
fenetre.configure(bg='#BDFFBE')

#explication de la fenètre
expliquation = tk.Label(fenetre, text="Cette fenêtre permets d'obtenir les informations voulue pour une espèce de fourmis.", bg='#BDFFBE')
expliquation.grid(row =1, column=0, columnspan = 9)


fonction = tk.Label(fenetre, text="Plus précisement elle vous donnera en fonction de nom et de l'espèce :", bg='#BDFFBE')
fonction.grid(row=2, column=0, columnspan = 9)

fonction = tk.Label(fenetre, text="type de fondation, si elle est foreuse, quelle nourriture, quelle température obtimal, quelle humidité, si besoins de diapause, quelle température de diapause", bg='#BDFFBE')
fonction.grid(row=3, column=0, columnspan = 9)

fonction = tk.Label(fenetre, text=" ", bg='#BDFFBE')
fonction.grid(row=4, column=0, columnspan = 9)

fonction = tk.Label(fenetre, text=" ", bg='#BDFFBE')
fonction.grid(row=6, column=0, columnspan = 9)

fonction = tk.Label(fenetre, text=" ", bg='#BDFFBE')
fonction.grid(row=9, column=0, columnspan = 9)

fonction = tk.Label(fenetre, text=" ", bg='#BDFFBE')
fonction.grid(row=12, column=0, columnspan = 9)

fonction = tk.Label(fenetre, text=" ", bg='#BDFFBE')
fonction.grid(row=15, column=0, columnspan = 9)

fonction = tk.Label(fenetre, text=" ", bg='#BDFFBE')
fonction.grid(row=18, column=0, columnspan = 9)

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

#frame 0
Frame0 = tk.Frame(fenetre, borderwidth=2)
Frame0.grid(row = 7, column=3)

# frame 1
Frame1 = tk.Frame(fenetre, borderwidth=2)
Frame1.grid(row = 7, column=4)

# frame 2
Frame2 = tk.Frame(fenetre, borderwidth=2)
Frame2.grid(row = 10, column=1)

# frame 3
Frame3 = tk.Frame(fenetre, borderwidth=2)
Frame3.grid(row = 10, column=2)

# frame 4
Frame4 = tk.Frame(fenetre, borderwidth=2)
Frame4.grid(row = 10, column=7)

# frame 5
Frame5 = tk.Frame(fenetre, borderwidth=2)
Frame5.grid(row = 13, column=1)

# frame 6
Frame6 = tk.Frame(fenetre, borderwidth=2)
Frame6.grid(row = 13, column=2)

# frame 7
Frame7 = tk.Frame(fenetre, borderwidth=2)
Frame7.grid(row = 13, column=7)

# frame 8
Frame8 = tk.Frame(fenetre, borderwidth=2)
Frame8.grid(row =13, column=8)

# frame 9
Frame9 = tk.Frame(fenetre, borderwidth=2)
Frame9.grid(row = 7, column=5)

# frame 10
Frame10 = tk.Frame(fenetre, borderwidth=2)
Frame10.grid(row = 7, column=6)

# frame 23
Frame23 = tk.Frame(fenetre, borderwidth=2)
Frame23.grid(row = 10, column=8)

# frame 24
Frame24 = tk.Frame(fenetre, borderwidth=2)
Frame24.grid(row = 16, column=1)
#===================================
#           CREATION DES FRAMES
#===================================

#===================================
#                 ZONE REPONSES
#===================================
# frame 21
Frame21 = tk.Frame(fenetre, borderwidth=2)
Frame21.grid(row = 8, column=3)

# frame 11
Frame11 = tk.Frame(fenetre, borderwidth=2)
Frame11.grid(row = 8, column=4)

# frame 12
Frame12 = tk.Frame(fenetre, borderwidth=2)
Frame12.grid(row = 11, column=1)

# frame 13
Frame13 = tk.Frame(fenetre, borderwidth=2)
Frame13.grid(row = 11, column=2)

# frame 14
Frame14 = tk.Frame(fenetre, borderwidth=2)
Frame14.grid(row = 11, column=7)

# frame 15
Frame15 = tk.Frame(fenetre, borderwidth=2)
Frame15.grid(row = 11, column=8)

# frame 16
Frame16 = tk.Frame(fenetre, borderwidth=2)
Frame16.grid(row = 14, column=1)

# frame 17
Frame17 = tk.Frame(fenetre, borderwidth=2)
Frame17.grid(row = 14, column=2)

# frame 18
Frame18 = tk.Frame(fenetre, borderwidth=2)
Frame18.grid(row = 14, column=7)

# frame 19
Frame19 = tk.Frame(fenetre, borderwidth=2)
Frame19.grid(row = 8, column=5)

# frame 20
Frame20 = tk.Frame(fenetre, borderwidth=2)
Frame20.grid(row = 8, column=6)

# frame 22
Frame22 = tk.Frame(fenetre, borderwidth=2)
Frame22.grid(row = 14, column=8)

# frame 25
Frame25 = tk.Frame(fenetre, borderwidth=2)
Frame25.grid(row = 17, columnspan=8)
#===================================
#                 ZONE REPONSES
#===================================

#===================================
#ATTRIBUTION DES DONNES AUX FRAMES
#===================================
label0 = tk.Label(Frame0, text="espèce")
label0.grid()
label1 = tk.Label(Frame1, text="nom")
label1.grid()
label2 = tk.Label(Frame2, text="type de fondation")
label2.grid()
label3 = tk.Label(Frame3, text="foreuse ?")
label3.grid()
label4 = tk.Label(Frame4, text="alimentation ?")
label4.grid()
label5 = tk.Label(Frame5, text="température")
label5.grid()
label6 = tk.Label(Frame6, text="humidité")
label6.grid()
label7 = tk.Label(Frame7, text="diapause ?")
label7.grid()
label8 = tk.Label(Frame8, text="température de diapause")
label8.grid()
label9 = tk.Label(Frame9, text="origine ?")
label9.grid()
label10 = tk.Label(Frame10, text="nombre de gyne")
label10.grid()
label23 = tk.Label(Frame23, text="type de nid")
label23.grid()
label24 = tk.Label(Frame24, text="conseil")
label24.grid()

label21 = tk.Label(Frame21, text="'affichage ici'")
label21.grid()
label11 = tk.Label(Frame11, text="'affichage ici'")
label11.grid()
label12 = tk.Label(Frame12, text="'affichage ici'")
label12.grid()
label13 = tk.Label(Frame13, text="'affichage ici'")
label13.grid()
label14 = tk.Label(Frame14, text="'affichage ici'")
label14.grid()
label15 = tk.Label(Frame15, text="'affichage ici'")
label15.grid()
label16 = tk.Label(Frame16, text="'affichage ici'")
label16.grid()
label17 = tk.Label(Frame17, text="'affichage ici'")
label17.grid()
label18 = tk.Label(Frame18, text="'affichage ici'")
label18.grid()
label19 = tk.Label(Frame19, text="'affichage ici'")
label19.grid()
label20 = tk.Label(Frame20, text="'affichage ici'")
label20.grid()
label22 = tk.Label(Frame22, text="'affichage ici'")
label22.grid()
label25 = tk.Label(Frame25, text="'affichage ici'")
label25.grid()
#===================================
#ATTRIBUTION DES DONNES AUX FRAMES
#===================================

tk.Button(text="Lancer la recherche", bg='#FF6767', command=main).grid(row=19, column=0, columnspan = 9)


#===================================
#           On ferme la fenètre
#===================================
fenetre.mainloop()

