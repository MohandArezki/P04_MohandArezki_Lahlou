from console.utils import wait_key
import os


class Menu:
    def __init__(self, title="Menu", subtitle=None):
        self.width = 0
        self.title = title
        self.subtitle = subtitle
        self.items = []
        self.options = []
        self.selected = 99

    def add(self, itemText, itemFunction):
        self.items.append({'Texte': itemText, 'func': itemFunction})
        self.options.append(itemText[0])

    def getWidth(self):
        self.width = len(max(self.items, key=len)['Texte']) +7

    def selectOption(self):
        try:
            self.selected = int(input('Votre Choix: '))
        except print("Vérifiez votre choix !"):
            wait_key()

    def run(self):
        self.getWidth()
        while True:
            os.system('cls||clear')
            print("─" * (self.width), end='\n')
            print(self.title.center(self.width), end='\n')
            if self.subtitle:
                print(self.subtitle.center(self.width), end='\n')
            print("─" * (self.width), end='\n')
            for item in self.items:
                print(item['Texte'].ljust(self.width, ' '), end='\n')
            print('0] - Quitter le menu'.ljust(self.width, ' '), end='\n')
            print("─" * (self.width), end='\n')
            self.selectOption()
            if self.selected == 0:
                break
            else:
                self.items[self.selected-1]['func']()
