import requests
from json import dump, dumps, load, loads
from graphe import *
from main import C


def get_distances(cities, file):
    assert isinstance(cities, list) and len(cities) >= 2, "Invalid cities list, please check it in the config file."

    if C('search_distances'):
        # If we have to search distances, search them and save them.
        data = search_distances(cities)
        save_distances(data, file)
    return load_distances(file)


def search_distances(cities):
    assert isinstance(cities, list) and len(cities) >= 2, "Invalid cities list, please check it in the config file."
    assert C('mapquest_key'), "Empty MapQuest API key, please check it in the config file."

    distances = {}
    n = 1
    for city_from in cities:
        print("Get distances : " + str(n) + "/" + str(len(cities)))

        processCities = cities.copy()

        # Move the city we are looking for at the beginning.
        processCities.pop(processCities.index(city_from))
        processCities.insert(0, city_from)

        # Prepare the request...
        payload = {
            "locations": [{'country': 'France', 'city': city} for city in processCities],
            'options': {'allToAll': False, "unit": "k", }
        }

        # and send it.
        r = requests.post("http://www.mapquestapi.com/directions/v2/routematrix?key=" + C('mapquest_key'),
                          data=dumps(payload))

        # Format the response to manipulate it easier.
        result = loads(r.text)["distance"]
        del result[0]
        distances[processCities[0]] = {}
        i = 0
        for city_to in result:
            i += 1
            distances[processCities[0]][processCities[i]] = city_to

        n = n + 1

    return distances


def save_distances(distances, file):
    with open(file, 'w', encoding='utf-8') as f:
        dump(distances, f, ensure_ascii=False, indent=4)


def load_distances(file):
    with open(file) as f:
        return load(f)


def create_graph_from_distances(g, distances):
    for city_from in distances:
        for city_to in distances[city_from]:
            g.ajouter_arete(city_from, city_to, distances[city_from][city_to])
