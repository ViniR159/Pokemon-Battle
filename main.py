from pokebase import cache
import pokebase as pb
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


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


print(Atq[0].power)


pokemonAdv = pb.pokemon(numadv)
hpAdv = next(stat.base_stat for stat in pokemonAdv.stats if stat.stat.name == "hp")
movimentosAdv = [move.move for move in pokemonAdv.moves]
movimentos_aleatoriosAdv = random.sample(movimentosAdv, 4)


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

    def ataque(self, atq):
        if isinstance(Atq[0].power, int):

            self.HpAdv -= Atq[0].power
            print("Dano causado")
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
