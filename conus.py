import json
from collections.abc import Iterable

def flatten(x):
    for l in x:
        if isinstance(l, Iterable):
            yield from flatten(l)
        else:
            yield l

if __name__ == '__main__':
    with open('us.json', 'r') as f:
        us = json.load(f)

    state_arcs = []
    for i, state in enumerate(us['objects']['states']['geometries']):
        name = state['properties']['name']
        if name == 'Alaska' or name == 'Hawaii':
            state_arcs.extend(list(set(flatten(state['arcs']))))
            del us['objects']['states']['geometries'][i]

    for i, county in enumerate(us['objects']['counties']['geometries']):
        county_arcs = list(set(flatten(county['arcs'])))
        if not set(state_arcs).isdisjoint(set(county_arcs)):
            for arc in county_arcs:
                state_arcs.append(arc)
            del us['objects']['counties']['geometries'][i]

    for i, arcs in enumerate(us['objects']['nation']['geometries'][0]['arcs']):
        nation_arcs = set(flatten(arcs))
        if not set(state_arcs).isdisjoint(nation_arcs):
            del us['objects']['nation']['geometries'][0]['arcs'][i]

    with open('us.json', 'w') as f:
        json.dump(us, f)