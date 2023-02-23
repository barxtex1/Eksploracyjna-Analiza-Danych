import pandas as pd
import requests
import json
import sqlite3


def attack_against(attacker: str, attacked: str, database: pd.DataFrame):
    type_attacked = database.loc[database["name"] == attacked, ["type_1", "type_2"]]
    types = [type_ for type_ in type_attacked.iloc[0, :]]
    data_against = get_data_against(attacker, types)
    return data_against



def list_pokemons_names():
    possible_pokemon = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100000")
    possible_pokemon = json.loads(possible_pokemon.text)
    names = [name["name"] for name in possible_pokemon["results"]]
    return names


def fill_pokedex(pokedex):
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
    return pokedex


def get_data_against(attacker, types):
    conn = sqlite3.connect("pokemon_against.sqlite")
    c = conn.cursor()
    if None in types:
        command = f'SELECT against_{types[0]} FROM against_stats WHERE name LIKE "{attacker}"'
    else:
        command = f'SELECT against_{types[0]}, against_{types[1]} FROM against_stats WHERE name LIKE "{attacker}"'
    data = c.execute(command)
    headers = [header[0] for header in data.description]
    data_against = pd.DataFrame(data=data, columns=headers, index=[attacker])
    return data_against


def main():
    pokedex = pd.DataFrame(pd.read_hdf("pokedex_history.hdf5"))
    pokedex = fill_pokedex(pokedex)
    attacker = "Wynaut"
    attacked = "hippopotas"
    attack = attack_against(attacker, attacked, pokedex)
    print(attack)


if __name__ == "__main__":
    main()
