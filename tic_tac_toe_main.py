# JEU DU MORPION

import tkinter as tk
import tkinter.messagebox

# Création d'une fenêtre principale en définissant sa taille et son titre
window = tk.Tk()
window.geometry("250x343")
window.title("Morpion")

# Création d'un tableau de 9 boutons pour représenter les cases du morpion
buttons = []
for i in range(9):
    button = tk.Button(window, text=" ", font=("Arial 20"), width=4, height=2)
    button.grid(row=i//3, column=i%3, sticky="nsew", padx=5, pady=5)
    buttons.append(button)

for i in range(9):
    buttons[i].config(command=lambda index=i: on_button_click(index))

# Vérification pour savoir si un joueur a gagné en parcourant toutes les combinaisons gagnantes possibles (lignes, colonnes et diagonales)
def check_win():
    # Vérifie les lignes
    for row in range(3):
        if buttons[row*3].cget("text") == buttons[row*3+1].cget("text") == buttons[row*3+2].cget("text") and buttons[row*3].cget("text") != " ":
            return True
    # Vérifie les colonnes
    for col in range(3):
        if buttons[col].cget("text") == buttons[col+3].cget("text") == buttons[col+6].cget("text") and buttons[col].cget("text") != " ":
            return True
    # Vérifie les diagonales
    if buttons[0].cget("text") == buttons[4].cget("text") == buttons[8].cget("text") and buttons[0].cget("text") != " ":
        return True
    if buttons[2].cget("text") == buttons[4].cget("text") == buttons[6].cget("text") and buttons[2].cget("text") != " ":
        return True
    return False


# Afficher quel joueur doit jouer
label = tk.Label(window, text="Joueur X a joué", font=("Arial 7"))
label.grid(row=3, column=0)

# Compte le nombre de tours joués et utilisez-la pour vérifier si la partie est terminée en cas d'égalité
# Gestion des événements de clic sur les boutons et mise à jour du contenu du bouton en fonction du joueur qui a joué 
turns = 0

def on_button_click(index):
    global turns
    player = "X" if turns % 2 == 1 else "O"
    buttons[index].config(text=player)
    label.config(text=f"Joueur {player} a joué")
    if check_win():
        tk.messagebox.showinfo("Gagnant", f"Le joueur {player} a gagné!")
        reset_game()
    turns += 1
    if turns == 9:
        tk.messagebox.showinfo("Egalité", "La partie est terminée en cas d'égalité!")
        reset_game()

# Remet à zéro tous les boutons
def reset_game():
    global turns
    turns = 0
    for button in buttons:
        button.config(text=" ")

# Création d'un bouton pour relancer la partie en définissant sa taille
reset_button = tk.Button(window, text="Relancer", font=("Arial 10"), width=8, height=1, command=reset_game)
reset_button.grid(row=3, column=1, pady=15)

# Affichage de la fenêtre de jeu
window.mainloop()
