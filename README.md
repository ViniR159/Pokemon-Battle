# Pokebase [![swampert](https://veekun.com/dex/media/pokemon/main-sprites/heartgold-soulsilver/260.png)](https://pokeapi.co/api/v2/pokemon/swampert)

[![actions](https://github.com/PokeAPI/pokebase/actions/workflows/unit.yml/badge.svg)](https://github.com/PokeAPI/pokebase/actions/workflows/unit.yml)
[![pypi](https://img.shields.io/badge/pypi-1.3.0-blue.svg)](https://pypi.python.org/pypi/pokebase)

pokebase is a simple but powerful Python interface to the [PokéAPI
database](https://pokeapi.co/)

Maintainer: [GregHilmes](https://github.com/GregHilmes)

## Installation

`pip install pokebase`

It can't get much easier than that.

Pokebase has been tested against Python 3.6 and Python 3.6 only. If this
is too old for your needs, see the above note about the construction.
Pokebase may function under other versions of Python, but bugs may
occur.

## Usage

```python console

>>> import pokebase as pb
>>> chesto = pb.APIResource('berry', 'chesto')
>>> chesto.name
'chesto'
>>>
chesto.natural_gift_type.name
'water'
>>> charmander = pb.pokemon('charmander') # Quick lookup.
>>> charmander.height
6
>>> # Now with sprites! (again!)
>>> s1 = pb.SpriteResource('pokemon', 17)
<pokebase.interface.SpriteResource object at 0x7f2f15660860>
>>> s1.url
'<https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/17.png>'
>>> s2 = pb.SpriteResource('pokemon', 1, other=True, official_artwork=True)
>>> s2.path
'/home/user/.cache/pokebase/sprite/pokemon/other-sprites/official-artwork/1.png'
>>> s3 = pb.SpriteResource('pokemon', 3, female=True, back=True)
>>> s3.img_data b'x89PNGrnx1anx00x00x00rIHDRx00x00x00 ... xca^x7fxbbd\*x00x00x00x00IENDxaeB`x82'
```
... And it's just that simple.

## Version Support

pokebase 1.3.0 supports Python 3.6

pokebase 1.4.0 drops support for Python 3.6 and adds support for Python
\>=3.8 \<=3.12. Install it with
`pip install https://github.com/PokeAPI/pokebase/archive/1.4.0.zip`

## Nomenclature

> -   an `endpoint` is the results of an API call like
>     `http://pokeapi.co/api/v2/berry` or
>     `http://pokeapi.co/api/v2/move`
> -   a `resource` is the actual data, from a call to
>     `http://pokeapi.co/api/v2/pokemon/1`

## Testing

Python unit tests are in a separate `tests` directory and can be run via
`python -m tests`.

### Notes to the developer using this module

The quick data lookup for a Pokémon type, is
`pokebase.type_('type-name')`, not `pokebase.type('type-name')`. This is
because of a naming conflict with the built-in `type` function, were you
to `from pokebase import *`.

When changing the cache, avoid importing the cache constants directly.
You should only import them with the whole cache module. If you do not
do this, calling `set_cache` will not change your local copy of the
variable.

NOT THIS!
```python console
>>> from pokebase.cache import API_CACHE
```

Do this :)

```python console
>>> from pokebase import cache
>>> cache.API_CACHE
```
