#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals, division
import json
from graph import Graph


with open('assets/cities_with_airports.json') as data_file:
    DATA = json.load(data_file)


def calculate_distance(point1, point2):
    """
    Calculate the distance (in miles) between point1 and point2.
    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.

    Modified and converted to Python from:
    http://www.movable-type.co.uk/scripts/latlong.html
    """
    import math

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3  # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])

    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * \
        math.cos(phi2) * math.sin(0.5 * delta_lam)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934  # convert km to miles


def create_city_coordinates_dict(data):
    """
    Create a dictionary that has coordinates for each city: <city: (lat_lon)>.
    """
    city_coord_dict = {}
    for city_dict in data:
        city_coord_dict.setdefault(city_dict['city'], city_dict['lat_lon'])
    return city_coord_dict


def short_json(data):
    """
    Clean up the data from the original json file.
    """
    short_json = []
    for city in data:
        short_json.append(
            {
                'city': city['city'],
                'lat_lon': city['lat_lon'],
                'destination_cities': city['destination_cities']
            }
        )
    return short_json


def all_connections(data, city_coord_dict):
    """
    Define all the connections and distance bettwen them.
    These are used to add edges for the graph.
    """
    edges = []
    for city in data:
        destinations = city['destination_cities']
        for destination in destinations:
            try:
                distance_from_origin = calculate_distance(
                    city_coord_dict[city['city']],  # origin airport
                    city_coord_dict[destination]  # destination airport
                    )
                edges.append(
                    (city['city'], destination, distance_from_origin)
                )
            except KeyError:
                pass
    return edges


def create_city_graph(edges):
    """
    Create a graph where nodes=<cities> and
    weighted edges=<connections with distances>.
    """
    graph = Graph()
    for edge in edges:
        try:
            graph.add_edge(edge[0], edge[1], edge[2])
        except ValueError:

            pass
    return graph

SHORT_JSON = short_json(DATA)

CITY_COOR_DICT = create_city_coordinates_dict(DATA)

EDGES = all_connections(
    SHORT_JSON, CITY_COOR_DICT)

GRAPH = create_city_graph(EDGES)


def path(city1, city2, graph=GRAPH):
    """
    Find the shortest path between 2 given cities using
    Dijkstra's algorithm.
    """
    path, distance = graph.shortest_path_dijkstras(city1, city2)
    print(path, 'traveled distanse is {} mi'.format(round(distance, 1)))
    return(path, round(distance, 1))


if __name__ == '__main__':
    print('Type <path(city1, city2)> to find path and distance'
          ' between 2 cities')
