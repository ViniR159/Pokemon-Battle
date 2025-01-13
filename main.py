from pokebase import cache
import pokebase as pb
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

multiplicadores_tipo = {
    # Normal
    ('normal', 'rock'): 0.5,
    ('normal', 'ghost'): 0.0,
    ('normal', 'steel'): 0.5,

    # Fire
    ('fire', 'grass'): 2.0,
    ('fire', 'ice'): 2.0,
    ('fire', 'bug'): 2.0,
    ('fire', 'steel'): 2.0,
    ('fire', 'fire'): 0.5,
    ('fire', 'water'): 0.5,
    ('fire', 'rock'): 0.5,
    ('fire', 'dragon'): 0.5,

    # Water
    ('water', 'fire'): 2.0,
    ('water', 'ground'): 2.0,
    ('water', 'rock'): 2.0,
    ('water', 'water'): 0.5,
    ('water', 'grass'): 0.5,
    ('water', 'dragon'): 0.5,

    # Electric
    ('electric', 'water'): 2.0,
    ('electric', 'flying'): 2.0,
    ('electric', 'electric'): 0.5,
    ('electric', 'grass'): 0.5,
    ('electric', 'dragon'): 0.5,
    ('electric', 'ground'): 0.0,

    # Grass
    ('grass', 'water'): 2.0,
    ('grass', 'ground'): 2.0,
    ('grass', 'rock'): 2.0,
    ('grass', 'fire'): 0.5,
    ('grass', 'grass'): 0.5,
    ('grass', 'poison'): 0.5,
    ('grass', 'flying'): 0.5,
    ('grass', 'bug'): 0.5,
    ('grass', 'dragon'): 0.5,
    ('grass', 'steel'): 0.5,

    # Ice
    ('ice', 'grass'): 2.0,
    ('ice', 'ground'): 2.0,
    ('ice', 'flying'): 2.0,
    ('ice', 'dragon'): 2.0,
    ('ice', 'fire'): 0.5,
    ('ice', 'water'): 0.5,
    ('ice', 'ice'): 0.5,
    ('ice', 'steel'): 0.5,

    # Fighting
    ('fighting', 'normal'): 2.0,
    ('fighting', 'ice'): 2.0,
    ('fighting', 'rock'): 2.0,
    ('fighting', 'dark'): 2.0,
    ('fighting', 'steel'): 2.0,
    ('fighting', 'poison'): 0.5,
    ('fighting', 'flying'): 0.5,
    ('fighting', 'psychic'): 0.5,
    ('fighting', 'bug'): 0.5,
    ('fighting', 'fairy'): 0.5,
    ('fighting', 'ghost'): 0.0,

    # Poison
    ('poison', 'grass'): 2.0,
    ('poison', 'fairy'): 2.0,
    ('poison', 'poison'): 0.5,
    ('poison', 'ground'): 0.5,
    ('poison', 'rock'): 0.5,
    ('poison', 'ghost'): 0.5,
    ('poison', 'steel'): 0.0,

    # Ground
    ('ground', 'fire'): 2.0,
    ('ground', 'electric'): 2.0,
    ('ground', 'poison'): 2.0,
    ('ground', 'rock'): 2.0,
    ('ground', 'steel'): 2.0,
    ('ground', 'grass'): 0.5,
    ('ground', 'bug'): 0.5,
    ('ground', 'flying'): 0.0,

    # Flying
    ('flying', 'grass'): 2.0,
    ('flying', 'fighting'): 2.0,
    ('flying', 'bug'): 2.0,
    ('flying', 'electric'): 0.5,
    ('flying', 'rock'): 0.5,
    ('flying', 'steel'): 0.5,

    # Psychic
    ('psychic', 'fighting'): 2.0,
    ('psychic', 'poison'): 2.0,
    ('psychic', 'psychic'): 0.5,
    ('psychic', 'steel'): 0.5,
    ('psychic', 'dark'): 0.0,

    # Bug
    ('bug', 'grass'): 2.0,
    ('bug', 'psychic'): 2.0,
    ('bug', 'dark'): 2.0,
    ('bug', 'fire'): 0.5,
    ('bug', 'fighting'): 0.5,
    ('bug', 'poison'): 0.5,
    ('bug', 'flying'): 0.5,
    ('bug', 'ghost'): 0.5,
    ('bug', 'steel'): 0.5,
    ('bug', 'fairy'): 0.5,

    # Rock
    ('rock', 'fire'): 2.0,
    ('rock', 'ice'): 2.0,
    ('rock', 'flying'): 2.0,
    ('rock', 'bug'): 2.0,
    ('rock', 'fighting'): 0.5,
    ('rock', 'ground'): 0.5,
    ('rock', 'steel'): 0.5,

    # Ghost
    ('ghost', 'psychic'): 2.0,
    ('ghost', 'ghost'): 2.0,
    ('ghost', 'dark'): 0.5,
    ('ghost', 'normal'): 0.0,

    # Dragon
    ('dragon', 'dragon'): 2.0,
    ('dragon', 'steel'): 0.5,
    ('dragon', 'fairy'): 0.0,

    # Dark
    ('dark', 'psychic'): 2.0,
    ('dark', 'ghost'): 2.0,
    ('dark', 'fighting'): 0.5,
    ('dark', 'dark'): 0.5,
    ('dark', 'fairy'): 0.5,

    # Steel
    ('steel', 'ice'): 2.0,
    ('steel', 'rock'): 2.0,
    ('steel', 'fairy'): 2.0,
    ('steel', 'fire'): 0.5,
    ('steel', 'water'): 0.5,
    ('steel', 'electric'): 0.5,
    ('steel', 'steel'): 0.5,

    # Fairy
    ('fairy', 'fighting'): 2.0,
    ('fairy', 'dragon'): 2.0,
    ('fairy', 'dark'): 2.0,
    ('fairy', 'fire'): 0.5,
    ('fairy', 'poison'): 0.5,
    ('fairy', 'steel'): 0.5,
}


cache.API_CACHE

num = random.randint(1,151)
numadv = random.randint(1,1025)

# print(num)
# print(numadv)

pokemon = pb.pokemon(num)
hp = next(stat.base_stat for stat in pokemon.stats if stat.stat.name == "hp")
movimentos = [move.move for move in pokemon.moves]
movimentos_aleatorios = random.sample(movimentos, 4)
Atq = [movimentos_aleatorios[0], movimentos_aleatorios[1], movimentos_aleatorios[2], movimentos_aleatorios[3]]


print(Atq[0])
print(Atq[1])
print(Atq[2])
print(Atq[3])


pokemonAdv = pb.pokemon(numadv)
hpAdv = next(stat.base_stat for stat in pokemonAdv.stats if stat.stat.name == "hp")
movimentosAdv = [move.move for move in pokemonAdv.moves]
movimentos_aleatoriosAdv = random.sample(movimentosAdv, 4)
AtqAdv = [movimentos_aleatoriosAdv[0], movimentos_aleatoriosAdv[1], movimentos_aleatoriosAdv[2], movimentos_aleatoriosAdv[3]]

print(AtqAdv[0])
print(AtqAdv[1])
print(AtqAdv[2])
print(AtqAdv[3])

sprites = pokemon.sprites
spritesadv = pokemonAdv.sprites

# print(f"Sprite frontal estático: {sprites.front_default}")
# print(f"Sprite traseiro estático: {sprites.back_default}")

animated_sprites = sprites.versions.generation_v.black_white.animated
animated_spritesdv = spritesadv.versions.generation_v.black_white.animated

# print(f"Sprite frontal animado: {animated_sprites.front_default}")
# print(f"Sprite traseiro animado: {animated_sprites.back_default}")

# print(pokemonAdv)
# print(num)
# print("Tipos:")
# for tipo in pokemonAdv.types:
#     print(f"- {tipo.type.name}")
# print(f"Movimentos aleatórios de {pokemonAdv.name}:")
# for movimento in movimentos_aleatoriosAdv:
#     print(f"- {movimento}")

#self.ids.oponente.source = sprites.front_default
#print("AAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")

class Tela(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        sprite_urlAdv = spritesadv.front_default
        self.ids.pokemonAdv.source = sprite_urlAdv
        self.ids.NomeAdv.text = pokemonAdv.name.capitalize()
        self.ids.Atq1.text = Atq[0].name
        self.ids.Atq2.text = Atq[1].name
        self.ids.Atq3.text = Atq[2].name
        self.ids.Atq4.text = Atq[3].name
        sprite_url = sprites.back_default
        self.ids.pokemon.source = sprite_url
        self.ids.Nome.text = pokemon.name.capitalize() 

        self.ids.Vida.max = hp
        self.ids.VidaAdv.max = hpAdv
        self.ids.Vida.value = hp
        self.ids.VidaAdv.value = hpAdv
 


class pokemon_battle(App):
    Hp = hp
    HpAdv = hpAdv

    def build(self):
        self.tela = Tela()
        return self.tela

    def ataque(self, ataque):

        if isinstance(Atq[ataque].power, int):

            self.HpAdv -= Atq[ataque].power
            print("Dano causado")
            print(self.HpAdv)
        else:
            print(" não é um ataque de dano.")
            print(self.HpAdv)

        
        self.tela.ids.VidaAdv.value = max(0, self.HpAdv)
        self.tela.ids.Vida.value = max(0, self.Hp)

        botao = [self.tela.ids.Atq1, self.tela.ids.Atq2, self.tela.ids.Atq3, self.tela.ids.Atq4]
        

        if self.Hp <= 0:
            print("Seu Pokémon morreu!")
            self.tela.ids.pokemon.color = (0.5, 0.5, 0.5, 1)
            self.tela.ids.Nome.text = "Derrotado!"
            for botao in [self.tela.ids.Atq1, self.tela.ids.Atq2, self.tela.ids.Atq3, self.tela.ids.Atq4]:
                botao.disabled = True

        if self.HpAdv <= 0:
            print("O Pokémon adversário morreu!")
            self.tela.ids.pokemonAdv.color = (0.5, 0.5, 0.5, 1)
            self.tela.ids.NomeAdv.text = "Derrotado!"
            for botao in [self.tela.ids.Atq1, self.tela.ids.Atq2, self.tela.ids.Atq3, self.tela.ids.Atq4]:
                botao.disabled = True
            return        

pokemon_battle().run()
