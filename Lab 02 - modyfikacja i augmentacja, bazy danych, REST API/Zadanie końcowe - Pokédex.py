import pandas as pd
import h5py
import sqlite3
import numpy as np



def readPokemon():
    with h5py.File("Pokedex/pokedex_history.hdf5", "r") as f:
        # a_group_key = list(f.keys())[0]
        # # Get the data
        data = f["data"]
        print(data['axis0'])
        print(data['axis0'][0])
        print(list(data['axis0'][0]))
        print(data['axis1'])
        print(data['block0_items'])
        print(data['block0_values'])
        print(data['block1_items'])
        print(data['block1_values'])
        print(data['axis0'][0])
        print(list(data))
        print(list(data['axis0']))
        print(list(data['axis1']))
        print("axis0 data: {}".format(data['axis0']))
        print("axis1 data attributes: {}".format(list(data['axis0'].attrs)))
        print("axis1 data attributes: {}".format(data['axis1'].attrs['name']))


if __name__ == "__main__":
    readPokemon()