import numpy as numpy

class player:

    def __init__(self, life, position, gold = 0, level = 0, inventory = set()):
        self.life = life
        self.gold = gold
        self.inventory = inventory
        self.level = level
        self.position = position
    


class niveau:
    def __init__(etage, objets, ennemies, taille_x, taille_y):
        self.etage = etage
        self.objets = objets
        self.ennemies = ennemies
        self.id = 0

class etage:
    def __init__(salles, couloirs):
        self.terrain = [[O for i in range(taille_y)] for j in range(taille_x)]
        # 0 fait rien, 1 c'est . , 2 c'est -, 3 c'est |, 4 c'est @, 5 c'est couloir, 6 c'est porte
        self.salles = salles
        self.couloirs = couloirs

    def remplir_terrain_couloir:
        #indice va commencer à 0 et finir un indice avant l'indice de fin d'un couloir
        def indice_qui change(indice_couloir, indice_virage):
            x_1 = self.couloirs[]

    def remplir_terrain_salles:
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
            for h in range(sallles[i][3]):
                self.terrain[x][y + h] = 3
                self.terrain[x + salles[i][2] - 1][y+h] = 3

            

    

salles = [(0,0,7,4), (6,5,5,6), (12,4,6,7)]
couloirs = [ [(2,3),(2,8),(4,8),(4,7),(6,7)] , [(8,5),(8,1),(14,1),(14,4)] , [(10,8),(11,8),(11,7),(12,7)]]
