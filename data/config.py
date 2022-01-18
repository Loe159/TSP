# This file contains all the needed configuration variables.

"""
Access to the configuration variables.
"""


def C(configVariable):
    assert configVariable in config.keys(), f"Config variable \"{configVariable}\" not found, make sure it is defined in data/config.py"
    return config[configVariable]


config = {}
config["cities"] = ['Clermont-Ferrand', 'Bordeaux', 'Bayonne', 'Toulouse', 'Marseille', 'Nice', 'Nantes', 'Rennes',
                    'Paris', 'Lille', 'Dijon', 'Valence', 'Aurillac', 'Orléans', 'Reims', 'Strasbourg', 'Limoges',
                    'Troyes', 'Le Havre', 'Cherbourg', 'Brest', 'Niort']
config["distances_file"] = "../data/distances.json"
config["start_city"] = "Orléans"
config["search_distances"] = False  # Should we use the API to get the distances between cities (can be really slow) ?
config["salesperson_number"] = 1
config["mapquest_key"] = ""  # The key to access the mapquest API
config["map_center"] = [46.5, 2.0]  # The key to access the mapquest API
config["map_zoom"] = 5.5
