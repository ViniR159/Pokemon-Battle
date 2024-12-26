from pokebase import cache
import pokebase as pb
import random

cache.API_CACHE

num = random.randint(1,1025)

pokemonAdv = pb.pokemon(num)
movimentosAdv = [move.move.name for move in pokemonAdv.moves]
movimentos_aleatorios = random.sample(movimentosAdv, 4)


# charmander = pb.pokemon('charmander')
# numero_do_charmander = charmander.id


sprites = pokemonAdv.sprites

print(f"Sprite frontal estático: {sprites.front_default}")
print(f"Sprite traseiro estático: {sprites.back_default}")

animated_sprites = sprites.versions.generation_v.black_white.animated

print(f"Sprite frontal animado: {animated_sprites.front_default}")
print(f"Sprite traseiro animado: {animated_sprites.back_default}")

print(pokemonAdv)
print(num)
print("Tipos:")
for tipo in pokemonAdv.types:
    print(f"- {tipo.type.name}")
print(f"Movimentos aleatórios de {pokemonAdv.name}:")
for movimento in movimentos_aleatorios:
    print(f"- {movimento}")
