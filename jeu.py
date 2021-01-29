import numpy as np
import pygame as pg 


salles = [(0,0,7,4), (6,5,5,6), (12,4,6,7)]
couloirs = [ [(2,3),(2,8),(4,8),(4,7),(6,7)] , [(8,5),(8,1),(14,1),(14,4)] , [(10,8),(11,8),(11,7),(12,7)]]
ennemies = set()
objets = set()
taille_x = 20
taille_y = 20


class player:

    def __init__(self,life, gold, inventory, level, position, objets, ennemies, taille_x, taille_y, salles, couloirs):
        self.life = life
        self.gold = gold
        self.inventory = inventory
        self.level = level
        self.position = position
        self.niveau = niveau(objets,ennemies,taille_x,taille_y, salles, couloirs)
    
    def can_move(self,direction):
        i, j = np.array(self.position) + np.array(direction)
        if self.niveau.etage.terrain[i][j] in [0,1]:
            return True
        return False

    def augmenterGold (self,nombreOr):
        self.gold += nombreOr
    
    def augmenterVie (self, gainVie):
        self.life += gainVie

    def perdreVie (self, perteVie):
        self.life -= perteVie
    
    def augmenterLevel(self):
        self.level += 1
    
    def deplacement(self, move): # move est une liste de deux éléments (ex : [1,0] si on se déplace à droite)
        if estPosstibleDeplacement(move):
            self.position[0]+=move[0]
            self.position[1]+=move[1]
        
    
    def afficher_player(self): # Renvoie la valeur qui était à l'endroit position pour la garder en mémoire 
        a, b = self.position[0], self.position[0]
        valeur = self.niveau.etage.terrain[a][b]
        self.niveau.etage.terrain[a][b] = 4
        return valeur
    
    def remettre(self,valeur):
        a, b = self.position[0], self.position[1]
        self.niveau.etage.terrain[a][b] = valeur


    # ATTENTION appeler la fonction remplir terrain couloir APRES remplir terrain salle

def display(terrain):
    k, l = terrain.shape()
    for i in range(k):
        chaine = ''
        for j in range(l):
            if terrain[i][j] == 0:
                chaine = chaine + ' '
            if terrain[i][j] == 1:
                chaine = chaine + '.'
            if terrain[i][j] == 2:
                chaine = chaine + '_'
            if terrain[i][j] == 3:
                chaine = chaine + '|'
            if terrain[i][j] == 4:
                chaine = chaine + '@'
            if terrain[i][j] == 5:
                chaine = chaine + '#'
            if terrain[i][j] == 6:
                chaine = chaine + '+'
        print(chaine)
    


class niveau:
    def __init__(self, objets, ennemies, taille_x, taille_y, salles, couloirs):
        self.etage = etage(salles, couloirs)
        self.objets = objets
        self.ennemies = ennemies
        self.id = 0

class etage:
    def __init__(self, salles, couloirs):
        self.terrain = np.zeros((taille_x,taille_y))
        # 0 fait rien, 1 c'est . , 2 c'est -, 3 c'est |, 4 c'est @, 5 c'est couloir, 6 c'est porte
        self.salles = salles
        self.couloirs = couloirs
        self.remplir_terrain_salles()
        self.remplir_terrain_couloir()

    def remplir_terrain_couloir(self):
        #indice va commencer à 0 et finir un indice avant l'indice de fin d'un couloir
        def indice_qui_change(indice_couloir, indice_virage):
            x_1 = self.couloirs[indice_couloir][indice_virage][0]
            y_1 = self.couloirs[indice_couloir][indice_virage][1]
            x_2 = self.couloirs[indice_couloir][indice_virage + 1][0]
            y_2 = self.couloirs[indice_couloir][indice_virage + 1][1]
            if x_1 != x_2:
                return 0
            if x_1 == x_2:
                return 1

        for i in range(len(self.couloirs)):
            for j in range(len(self.couloirs[i]) - 1):
                axe = indice_qui_change(i,j)
                if axe == 0:
                    x_1 = min(self.couloirs[i][j][0],self.couloirs[i][j + 1][0])
                    x_2 = max(self.couloirs[i][j][0],self.couloirs[i][j + 1][0])
                    y = self.couloirs[i][j][1]
                    diff = x_2 - x_1
                    for k in range(diff + 1):
                        self.terrain[x_1 + k][y] = 5
                if axe == 1:
                    y_1 = min(self.couloirs[i][j][1],self.couloirs[i][j + 1][1])
                    y_2 = max(self.couloirs[i][j][1],self.couloirs[i][j + 1][1])
                    x = self.couloirs[i][j][1]
                    diff = y_2 - y_1
                    for k in range(diff + 1):
                        self.terrain[x][y_1 + k] = 6
            # il reste à mettre les portes
            a_1 = self.couloirs[i][0][0]
            a_2 = self.couloirs[i][0][1]
            b_1 = self.couloirs[i][-1][0]
            b_2 = self.couloirs[i][-1][1]
            self.terrain[a_1][a_2] = 6
            self.terrain[b_1][b_2] = 6



    def remplir_terrain_salles(self):
        for i in range(len(salles)):
            # on rentre va afficher la salle i : 
            x,y = salles[i][0], salles[i][1]
            for l in range(salles[i][2]):
                for h in range(salles[i][3]):
                    self.terrain[x + l][y + h] = 1 # on met des points partout dans la salle
            # il reste à mettre les - et |
            for l in range(salles[i][2]):
                self.terrain[x + l][y] = 2
                self.terrain[x + l][y + salles[i][3] - 1] = 2
                # on a mis les -
            for h in range(salles[i][3]):
                self.terrain[x][y + h] = 3
                self.terrain[x + salles[i][2] - 1][y+h] = 3
    


joueur = player(100, 0,set(), 0, [1,1], objets, ennemies, taille_x, taille_y, salles, couloirs) 

clock = pg.time.Clock()
running = True
while running:
    clock.tick(50)

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                direction = [0,1]
                player.deplacement(direction)
                valeur = player.afficher_player()
                display(player.niveau.etage.terrain)
                player.remettre(valeur)
            elif event.key == pg.K_UP:
                direction = [0,-1]
                player.deplacement(direction)
                valeur = player.afficher_player()
                display(player.niveau.etage.terrain)
                player.remettre(valeur)
            elif event.key == pg.K_LEFT:
                direction = [-1,0]
                player.deplacement(direction)
                valeur = player.afficher_player()
                display(player.niveau.etage.terrain)
                player.remettre(valeur)
            elif event.key == pg.K_RIGHT:
                direction = [1,0]
                player.deplacement(direction)
                valeur = player.afficher_player()
                display(player.niveau.etage.terrain)
                player.remettre(valeur)