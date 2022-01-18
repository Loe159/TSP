import folium
from data.config import C

class Map:
    def __init__(self, center, zoom, cities):
        self.center = center
        self.zoom = zoom
        self.cities = cities
        self.map = folium.Map(center, zoom_start=zoom)

    def add_point(self, points, color = "black"):
        for point in points:
            folium.Marker(
                location=point,
                popup=data.iloc[i]['name'],
            ).add_to(m)
        folium.PolyLine(points, color=color).add_to(self.map)

    def save(self):
        self.map.save("map.html")


if __name__ == "__main__":
    m = Map(C("map_center"), C("map_zoom"), "")
    m.add_point([(46.4, 3), (45.7, 1), (45, 2.5)])
    m.save()