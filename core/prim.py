class Prim:
    def __init__(self, distances, cities, start_city, salesperson_number):
        assert len(distances) == len(cities) and start_city in cities and 0 < salesperson_number < len(cities), \
            "Invalid parameters"
        self.distances = distances
        self.cities = cities
        self.total_distance = 0

    # Display the solutions
    def display(self):
        for salesperson in self.salespersons:
            cities = [self.cities[city] for city in salesperson.cities]
            cities = " → ".join(cities)
            print("Salesperson N°%s: %s" % (salesperson.id+1, cities))
        print("Total distance: %s" % self.total_distance)

    def main(self, start_city, salesperson_number):

        # Initialize some variables
        start_city = self.cities.index(start_city)
        visited = [0] * len(self.cities)
        city_index = start_city
        visited[start_city] = True
        g = self.distances.copy()

        # Make a list of salespersons
        self.salespersons = [Salesperson(i, start_city) for i in range(salesperson_number)]

        # Loop until all cities are visited
        while False in visited:
            moved = [False] * (len(self.salespersons))

            # Loop through all salespersons.
            for salesperson in self.salespersons:
                min_distance = float("inf")
                min_found = False

                # Loop through all cities visited by the salesperson...
                for i in salesperson.cities:
                    # and loop through all cities.
                    for j in range(len(g)):
                        # Find the closest city which is not visited yet.
                        if (not visited[j]) and g[i][j] and g[salesperson.cities[-1]][j] == min(
                                [g[s.cities[-1]][j] for s in self.salespersons if
                                 not moved[s.id]]):
                            if min_distance > self.distances[i][j] != 0:
                                min_distance = self.distances[i][j]
                                min_j = j
                                min_found = True

                # If a city has been found, add it to the salesperson's cities.
                if min_found:
                    moved[salesperson.id] = True
                    salesperson.cities.append(min_j)
                    visited[min_j] = True

                    # Update the total distance.
                    if min_distance != float("inf"):
                        self.total_distance += min_distance

                if city_index <= len(self.cities):
                    # Increase the index for the next iteration
                    city_index += 1
                else:
                    # or restart from the beginning if we reached the end of the list.
                    city_index = 0

        # Go back to the first city at the end of the trip.
        for salesperson in self.salespersons:
            salesperson.cities.append(start_city)

        self.display()
        return self.salespersons


class Salesperson:
    def __init__(self, id, start):
        self.id = id
        self.start = start
        self.cities = [start]
