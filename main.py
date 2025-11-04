###
"""
J'ai créé une application de simulation de mise à jour de téléphone avec :

Formulaire de saisie pour entrer le nom du téléphone et sa version actuelle
Animation de progression réaliste avec étapes de mise à jour (téléchargement, installation de modules, optimisation matériel)
Écran récapitulatif affichant la nouvelle version, les modules installés et les optimisations matérielles
Design moderne inspiré des interfaces smartphone avec dégradés bleu/violet et animations fluides
Boutons "Redémarrer" et "Nouvelle mise à jour" pour recommencer le processus"""
###
"""
#################################################
#                                               #
#          AAAAA  L       EEEEE  X   X          #
#         A     A L       E      X X            #
#         AAAAAAA L       EEEE    X             #
#         A     A L       E      X X            #
#         A     A LLLLL   EEEEE  X   X          #
#                                               #
#   DDDD    Y   Y  N   N   AAAAA  M   M   OOO   #
#   D   D    Y Y   NN  N  A     A MM MM  O   O  #
#   D   D     Y    N N N  AAAAAAA M M M  O   O  #
#   D   D     Y    N  NN  A     A M   M  O   O  #
#   DDDD      Y    N   N  A     A M   M  OOO    #
#                                               #
#################################################
"""

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.clock import Clock
import random
Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"


class GradeBook(MDApp):

    def build(self):
        self.index = 0  # Index du texte affiché
        self.modules = [
            "Téléchargement des licences systèmes",
            "Téléchargement des fichiers systèmes",
            "Installation des nouveaux modules",
            "Mise à jour du système",
            "Mise à jour du matériel",
            "Optimisation du système",
            "Optimisation du matériel",
            "Finalisation",
            "Ne pas éteindre votre appareil pendant la mise à jour"
        ]

        self.screen_manager = ScreenManager()
        for screen in ["home", "mise_encour", "mise_end"]:
            self.screen_manager.add_widget(Builder.load_file(screen + ".kv"))

        return self.screen_manager

    def mise(self, nom_tel, version_tel):
        self.screen_manager.transition.direction = "left"
        self.screen_manager.current = "mise_en_cor"
        screen = self.screen_manager.get_screen("mise_en_cor")
        screen_end = self.screen_manager.get_screen("mise_end")

        screen_end.tel_name_complet.text=screen.tel_name.text = nom_tel
        screen.tel_version.text = version_tel
        screen_end.version_name_complet.text = str(int(version_tel) +1)
        screen_end.version_name_pre.text= f"Version précédente: {version_tel}"
        # Lancement de la mise à jour
        v=random.randint(2,5) 
        self.event = Clock.schedule_interval(self.changer_texte, v)

    def changer_texte(self, dt):
        screen = self.screen_manager.get_screen("mise_en_cor")
        value = screen.valeur.value + 1
        screen.valeur.value = value

        if value <= 100:
            screen.val_progress_oper.text = f"{value}%"
            # Changer de texte toutes les 10%
            if value % 10 == 0 and self.index < len(self.modules):
                screen.progress_oper.text = self.modules[self.index]
                self.index += 1

        else:
            self.event.cancel()
            self.screen_manager.get_screen("acceuil").nom_tel.text=""
            self.screen_manager.get_screen("acceuil").version_tel.text=""
            self.screen_manager.transition.direction = "left"
            self.screen_manager.current = "mise_end"


if __name__ == "__main__":
    GradeBook().run()
