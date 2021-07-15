import colorama
colorama.init()


class MagicPen:
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type

    def get_info(self):
        return f'MagicPen  {self.name} має ({self.color} кольор;  {self.type} тип шрифта)'

    def write(self, text):
        colors = {
            'red': colorama.Fore.RED,
            'blue': colorama.Fore.BLUE,
            'black': colorama.Fore.BLACK,
            'white': colorama.Fore.WHITE
        }
        color = colors[self.color]

        if self.type == 1:
            text = text.upper()
        elif self.type == 3:
            text = text.lower()
        print(f"{color}{self.name}: {text}{colorama.Fore.RESET}")


pen1 = MagicPen('RedScript', 'red', 1)
pen2 = MagicPen('WhiteScript', 'white', 3)
pen3 = MagicPen('BlueScript', 'blue', 2)


pen3.write('Привіт!')
pen1.write('Будь ласка, не вводьте числа!')
pen2.write('Ось тобі мій дар')

pen1.write('Проблема!')
