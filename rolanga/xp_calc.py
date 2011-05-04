#! -*-coding: utf8-*-
"""
Calculadora de nivel de encuentro para dungeons & dragons 3.5
"""
import tables

class XpCalc(object):
    
    def __init__(self, party):
        """
        self.party es una lista de objetos player
        """
        self.party = party

    def add_party_experience(self, encounter_level):
        """
        suma los puntos de experiencia a cada miembro del
        party
        """
        party_size = len(self.party)
        for player in self.party:
            player.xp = self.get_experience_for(player.level, 
                                                encounter_level, 
                                                party_size)

    def get_experience_for(self, level, encounter_lvl, size):
        """Retorna la experiencia, para determinado nivel de encuentro,
            nivel de jugador, y tamaño del party"""

        #obtenemos la experiencia
        xp = 120
        return xp/size

    def experience_table(level, encounter_lvl):
        """La tabla del manual"""


