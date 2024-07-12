import random

class Pokemon:
    def __init__(self, name, hit_points, attack_damage):
        self.name = name
        self.hit_points = hit_points
        self.attack_damage = attack_damage

    def attack(self, other):
        damage = random.randint(1, self.attack_damage)
        other.hit_points -= damage
        return damage

def battle(pokemon1, pokemon2):
    print(f"Battle start between {pokemon1.name} and {pokemon2.name}!")

    while pokemon1.hit_points > 0 and pokemon2.hit_points > 0:
        damage = pokemon1.attack(pokemon2)
        print(f"{pokemon1.name} attacks {pokemon2.name} for {damage} damage. {pokemon2.name} has {pokemon2.hit_points} HP left.")

        if pokemon2.hit_points <= 0:
            print(f"{pokemon2.name} has fainted! {pokemon1.name} wins the battle!")
            return

        damage = pokemon2.attack(pokemon1)
        print(f"{pokemon2.name} attacks {pokemon1.name} for {damage} damage. {pokemon1.name} has {pokemon1.hit_points} HP left.")

        if pokemon1.hit_points <= 0:
            print(f"{pokemon1.name} has fainted! {pokemon2.name} wins the battle!")
            return

# Define player's Pokemon
player_pokemon = Pokemon(name="Pikachu", hit_points=30, attack_damage=10)

# Define computer's Pokemon
computer_pokemon = Pokemon(name="Charmander", hit_points=30, attack_damage=10)

# Start the battle
battle(player_pokemon, computer_pokemon)
