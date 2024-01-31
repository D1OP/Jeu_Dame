from tkinter import *

#Mise en place de l'interface
def interface():
    global fenetre, can, btn, chaine
    fenetre = Tk()
    fenetre.title("Jeu de Dame")
    can = Canvas(fenetre, width=400, height=400, bg='grey')
    can.pack(side=TOP)
    chaine = Label(fenetre)
    chaine.pack()
    btn = Button(fenetre, text='Recommencer', command=restart)
    btn.pack(side=RIGHT)
    
    damier()
    repartition_pions()
    
    fenetre.mainloop()

#Mise en place du damier
def damier():
    i = 0
    while i < 8:
        j = 0
        while j < 8:
            if (i%2)==0:
                if (j%2)==0:
                    can.create_rectangle(j*case, i*case, (j*case)+case, (i*case)+case, fill='black')
                else:
                    can.create_rectangle(j*case, i*case, (j*case)+case, (i*case)+case,fill='white')
            else:
                if (j%2)==0:
                    can.create_rectangle(j*case, i*case, (j*case)+case, (i*case)+case, fill='white')
                else:
                    can.create_rectangle(j*case, i*case, (j*case)+case, (i*case)+case, fill='black')
            j+=1
        i+=1

#Répartition des pions
def repartition_pions():
    i = 0
    while i < len(pions_b):
        if pions_b[i] != -1:
            y = (((pions_b[i]/8)*case) + case/2)
            x = ((pions_b[i]%8)*case) + case/2
            if i in dame_b:
                can.create_rectangle(x-8, y-8, x+8, y+8, fill='#DFCAA0')
            else:
                can.create_oval(x-10, y-10, x+10, y+10, fill='#DFCAA0')
        i += 1
    # ensuite les pions noirs (bleu)
    i = 0
    while i < len(pions_m):
        if pions_m[i] != -1:
            y = (((pions_m[i]/8)*case) + case/2)
            x = ((pions_m[i]%8)*case) + case/2
            if i in dame_m:
                can.create_rectangle(x-8, y-8, x+8, y+8, fill='#481F01')
            else:
                can.create_oval(x-10, y-10, x+10, y+10, fill='#481F01')
        i += 1

#Redémarer la partie
def restart():
    global pions_b, piont1, piont2, pions_m, selected, joueur, dame_b, dame_m, started
    piont1, piont2, selected, joueur = 0, 0, -1, 0
    pions_b = [0, 2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22]
    pions_m = [60, 62, 64, 66, 68, 71, 73, 75, 77, 79, 80, 82]
    dame_m = []
    dame_b = []
    started = False
    damier()
    repartition_pions()

#Sélection pion pour jouer   
def select(event):
    pass

#Gestion des déplacements
def deplacement(dpl):
    pass

#Gestion des possibilitées
def possibilites(glob=True, num_case=0):
    pass

#Programme principal 
started = True
selected = -1
piont1 = 0
piont2 = 0
case = 32

#Début du jeu
pions_b = [0, 2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22]
dame_b = []
pions_m = [60, 62, 64, 66, 68, 71, 73, 75, 77, 79, 80, 82]
dame_m = []
    
interface()

