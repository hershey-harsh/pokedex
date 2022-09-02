# Pokedex
An python wrapper to bring pokédex data into python

## Installation
This is a Python module available through the PyPI. Before installing, download and install Python. This latest version of the library is compatible with Python 3.10.5 and above.

Below are 2 ways on how to install this library

```
$ pip install pokedex
```
```
$ pip install git+https://github.com/futureslinky/pokedex
```

## Examples
### Getting pokémon data using an pokémon image:
```py
from pokedex.api import Pokemon
pokemon = Pokemon(url="https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png")
```
### Getting pokémon data using an pokémon name:
```py
from pokedex.api import Pokemon
pokemon = Pokemon(name="Pikachu")
```
### Attributes:
```py
pokemon.name # Returns the pokémon name
pokemon.description # Returns the pokémon description
pokemon.names # Returns global names
pokemon.region # Returns the region of the pokémon
pokemon.types # Returns the pokémon types
pokemon.evolution # Returns the pokémon evolution if it exists
pokemon.dex_number # Returns the pokémons dex number
pokemon.appearance # Returns a dictionary containing the pokémons height and weight
pokemon.height # Returns the pokémons height
pokemon.weight # Returns the pokémons weight
pokemon.base_stats # Returns a dictionary listing the pokémons stats
pokemon.attack # Returns the pokémons attack stats
pokemon.defense # Returns the pokémons defense stats
pokemon.hit_points # Returns the pokémons hit points
pokemon.speed # Returns the pokémons speed stats
pokemon.speed_attack # Returns the pokémons speed attack stats
pokemon.speed_defense # Returns the pokémons spped defense stats
```
