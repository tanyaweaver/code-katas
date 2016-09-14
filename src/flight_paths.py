#!/usr/bin/env python
# -*- coding: utf -8 -*-


from __future__ import unicode_literals, division
import os
import json
from graph import Graph
from pprint import pprint


with open('cities_with_airports.json') as data_file:
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


def create_airport_coordinates_dict(data):
    city_coord_dict = {}
    for city_dict in data:
        city_coord_dict[city_dict['airport']] = city_dict['lat_lon']
    return city_coord_dict

def short_json(data):
    short_json = []
    for city_dict in data:
        short_json.append(
            {
                'city': city_dict['city'],
                'airport': city_dict['airport'],
                'lat_lon': city_dict['lat_lon'],
                'destination_airports': city_dict['destination_airports']
            }
        )
    return short_json

SHORT_JSON = short_json(DATA)


def all_connections(data, airport_coord_dict):  # edges for the future graph
    edges = []
    for city_dict in data:
        destinations = city_dict['destination_airports']
        for destination in destinations:
            try:
                distance_from_origin = calculate_distance(
                    airport_coord_dict[city_dict['airport']],  # origin airport
                    airport_coord_dict[destination]  # destination airport
                    )
           
                edges.append(
                    (city_dict['airport'], destination, round(distance_from_origin, 1))
                )
            except KeyError:
                pass
    return edges


def create_airports_graph(edges):
    graph = Graph()
    for edge in edges:
        #import pdb; pdb.set_trace()
        try:
            graph.add_edge(edge[0], edge[1], edge[2])
        except ValueError:
            pass
    return graph


EDGES = all_connections(
    SHORT_JSON, create_airport_coordinates_dict(SHORT_JSON))

GRAPH = create_airports_graph(EDGES)


def find_airport_path(airport1, airport2):
    path, distance = GRAPH.shortest_path_dijkstras(airport1, airport2)
    print(path, distance, 'mi')


def airport_list(data):
    airport_list = []
    for city_dict in data:
        airport_list.append(city_dict['airport'])
    return sorted(airport_list)

if __name__ == '__main__':
    print('airport_list: ', airport_list(SHORT_JSON)[:100])
    print('type: find_airport_path(airport1, airport2) to find path and distance')
    #city_list(SHORT_JSON)
    #pprint(SHORT_JSON)
    #pprint (AIRPORT_COORD_DICT)
    #pprint (len(CITY_COORD_DICT.keys()))
    # for city in DATA:
    #     if city['city'].startswith('Washington'):
    #         print(city['city'], city['airport'], city['lat_lon']) 
    #print(DATA[0], DATA[1])
    #print(calculate_distance(DATA[0]['lat_lon'], DATA[1]['lat_lon']))
    #print(list_distance_to_airport(DATA, AIRPORT_COORD_DICT))
    #pprint(SHORT_JSON[0])
    #create_connections(SHORT_JSON, AIRPORT_COORD_DICT)
    #counter = 0
    # for city in SHORT_JSON:
    #     counter +=1
    #     if city['airport'].startswith('Prince'):
    #         print(city['city'], city['airport'])
    # print('nope', counter)
    #print(EDGES[0], EDGES[1], EDGES[2], EDGES[3])
