import pandas as pd
import requests
import json


def attack_against(attacker: str, attacked: str, database: pd.DataFrame):
    pass


def list_pokemons_names():
    possible_pokemon = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100000")
    possible_pokemon = json.loads(possible_pokemon.text)
    names = [name["name"] for name in possible_pokemon["results"]]
    return names


def main():
    pokedex = pd.DataFrame(pd.read_hdf("pokedex_history.hdf5"))
    pokedex["name"] = pokedex["name"].str.lower()
    pokemon_names = list_pokemons_names()
    for name in pokedex["name"]:
        if name in pokemon_names:
            pokemon_data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
            file = open("pokemon_example.txt", "w")
            file.write(pokemon_data.text)
            file.close()
            pokemon_data = json.loads(pokemon_data.text)
            for stat in pokemon_data["stats"]:
                pokedex.loc[pokedex["name"] == name, stat["stat"]["name"]] = stat["base_stat"]

            if len(pokemon_data["types"]) == 1:
                pokedex.loc[pokedex["name"] == name, "type_1"] = pokemon_data["types"][0]["type"]["name"]
                pokedex.loc[pokedex["name"] == name, "type_2"] = None
            elif len(pokemon_data["types"]) == 2:
                pokedex.loc[pokedex["name"] == name, "type_1"] = pokemon_data["types"][0]["type"]["name"]
                pokedex.loc[pokedex["name"] == name, "type_2"] = pokemon_data["types"][1]["type"]["name"]

    print(pokedex)
    pokedex.to_csv("my_pokedex.csv")


if __name__ == "__main__":
    main()
