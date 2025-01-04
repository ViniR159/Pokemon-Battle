from pokebase import cache
import pokebase as pb
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

cache.API_CACHE

num = random.randint(1,151)
numadv = random.randint(1,1025)

print(num)
print(numadv)

pokemon = pb.pokemon(num)
movimentos = [move.move.name for move in pokemon.moves]
movimentos_aleatorios = random.sample(movimentos, 4)

pokemonAdv = pb.pokemon(numadv)
movimentosAdv = [move.move.name for move in pokemonAdv.moves]
movimentos_aleatoriosAdv = random.sample(movimentosAdv, 4)



# charmander = pb.pokemon('charmander')
# numero_do_charmander = charmander.id

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
        sprite_url = sprites.back_default
        self.ids.pokemon.source = sprite_url
        self.ids.Nome.text = pokemon.name.capitalize()
        

class pokemon_battle(App):
    def build(self):
        return Tela()
        

pokemon_battle().run()
