import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        # Урон зависит от силы атаки (attack_power), добавлен рандомный фактор
        damage = random.randint(self.attack_power - 10, self.attack_power + 10)
        return damage

    # Метод получения урона, уменьшает здоровье
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    # Проверка, жив ли герой
    def is_alive(self):
        return self.health > 0

# Класс Game управляет процессом игры
class Game:
    def __init__(self, player_name, computer_name="Computer"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    # Метод, который запускает игру
    def start(self):
        print(f"Игра начинается! {self.player.name} против {self.computer.name}.\n")
        # Игра продолжается, пока один из героев жив
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            player_damage = self.player.attack()
            self.computer.take_damage(player_damage)
            print(f"{self.player.name} атакует {self.computer.name} и наносит {player_damage} урона.")
            print(f"У {self.computer.name} осталось {self.computer.health} здоровья.\n")
            if not self.computer.is_alive():
                print(f"{self.computer.name} погиб. {self.player.name} победил!")
                break

            # Ход компьютера
            computer_damage = self.computer.attack()
            self.player.take_damage(computer_damage)
            print(f"{self.computer.name} атакует {self.player.name} и наносит {computer_damage} урона.")
            print(f"У {self.player.name} осталось {self.player.health} здоровья.\n")
            if not self.player.is_alive():
                print(f"{self.player.name} погиб. {self.computer.name} победил!")
                break

if __name__ == "__main__":
    game = Game(player_name="Игрок")
    game.start()
