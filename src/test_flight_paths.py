#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals, division
import pytest
from flight_paths import (
    CITY_COOR_DICT,
    SHORT_JSON,
    EDGES, GRAPH,
    path, Graph
    )


def test_create_city_coordinates_dict():
    """
    Prove that Chelyabinsk has the same lat_lon in
    CITY_COOR_DICT as in original json.
    """
    for x in SHORT_JSON:
        if x['city'] == 'Chelyabinsk':
            lat_lon = x['lat_lon']
    assert CITY_COOR_DICT['Chelyabinsk'] == lat_lon


def test_all_connections():
    """
    prove that Seattle has the same number of connections in the
    created connections as in the original json.
    """
    connections_Seattle_data, connections_Seattle_edges = [], []
    for x in EDGES:
        if x[0] == 'Seattle':
            connections_Seattle_edges.append(x[1])
    for x in SHORT_JSON:
        if x['city'] == 'Seattle':
            for dest in x['destination_cities']:
                connections_Seattle_data.append(dest)
    assert len(connections_Seattle_data) == len(connections_Seattle_edges)


def test_create_city_graph():
    """
    prove that Seattle has the same number of connections in the
    created graph as in the original json.
    """
    connections_Seattle_data, connections_Seattle_graph = set(), []
    for x in GRAPH._dict['Seattle']:
        connections_Seattle_graph.append(x)
    for x in SHORT_JSON:
        if x['city'] == 'Seattle':
            for dest in x['destination_cities']:
                connections_Seattle_data.add(dest)
    assert len(connections_Seattle_data) == len(connections_Seattle_graph)


CITIES = [1, 2, 3, 4, 5, 6, 7]
CONNECTIONS = [
    (1, 2, 4), (1, 3, 13), (1, 5, 2), (1, 6, 10),
    (2, 4, 2),
    (3, 4, 3),
    (4, 6, 2), (4, 3, 5),
    (5, 3, 4),
    (5, 6, 2)
    ]
SHORTEST_PATH = [
    (1, 2, ([1, 2], 4)),
    (1, 3, ([1, 5, 3], 6)),
    (1, 6, ([1, 5, 6], 4)),
]


@pytest.fixture
def gr():
    gr = Graph(CITIES)
    for x in CONNECTIONS:
        gr.add_edge(x[0], x[1], x[2])
    return gr


@pytest.mark.parametrize('city1, city2, path_distance', SHORTEST_PATH)
def test_path1(city1, city2, path_distance, gr):
    """
    Prove that the path and distance between 2 cities are as expected.
    """
    assert path(city1, city2, graph=gr) == path_distance


def test_error_if_no_path1(gr):
    """
     Test whether a Value Error is raised when there is no path between 2 nodes
     (one of the nodes has no edges.)
     """
    with pytest.raises(ValueError):
        path(7, 2, graph=gr)


def test_error_if_no_path2(gr):
    """
    Test whether a Value Error is raised when there is no path between 2 nodes.
    """
    with pytest.raises(ValueError):
        path(3, 2, graph=gr)


def test_error_if_no_city33(gr):
    """
    Test whether a Value Error is raised when city1 is not on the json list.
    """
    with pytest.raises(ValueError):
        path(33, 2, graph=gr)


def test_error_if_no_city22(gr):
    """
    Test whether a Value Error is raised when city2 is not on the json list.
    """
    with pytest.raises(ValueError):
        path(3, 2, graph=gr)
