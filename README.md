Travelling Salesman Problem (TSP)
===================================================

This project, integrally in Python, solves the travelling salesman problem: a problem that consists in determining, given a list of cities, the shortest circuit that passes through each city once and only once before returning to the starting city.

To do this, we use the MapQuest API to obtain distances between cities and a PRIM algorithm.
 
Installation
------------

Clone the repository:
```sh
git clone https://github.com/Loe159/TSP.git
```

Install the dependencies:
```sh
pip install requests
```

Usage
-----
Run the script:
```sh
python core/main.py
```

Configuration
-----
You can configure the script by editing the `[config](https://github.com/Loe159/TSP/tree/master/data)` file.

If you want to use your own cities :
1. Change the `cities` variable with your cities list.
2. Change the `search_distances` variable to **True**
3. Fill the `mapquest_key` variable with your MapQuest API key.
4. Delete the `[distances.json](https://github.com/Loe159/TSP/blob/master/data/distances.json)` file.
5. Run the script 😜
