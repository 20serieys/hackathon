import numpy as numpy

class player:

    def __init__(self, life, position, gold = 0, level = 0, inventory = set()):
        self.life = life
        self.gold = gold
        self.inventory = inventory
        self.level = level
        self.position = position
    


class niveau:
    def __init__(etage, objets, ennemies, taille):
        self.terrain = [[O for i in range(taille)] for j in range(taille)]
        # 0 fait rien, 1 est un point, 2 c'est -, 3 c'est |, 4 c'est @,...
        self.etage = etage
        self.objets = objets
        self.ennemies = ennemies
        self.id = 0

class etage:
    def __init__(salles, couloirs):
        self.salles = salles
        self.couloirs = couloirs
    
