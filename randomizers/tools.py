import random
from copy import copy, deepcopy
import numpy as np

def initialize_pairs(people, scores):
    """
    Create the list of all pairs given all the people

    Parameters
    ----------
    people: collection as list of dicts
      the collection of people
    scores: doc
      the attributes that will be used to score the pairs and their weights

    Returns
    -------
    the dictionary containing the matched arrays of pairs and  their static
    and dynamic scores (the latter initialized to zero)
    """

    for attribute, value in scores.items():
       for person in people:
           if person.get(attribute) is None and attribute != "previously_paired":
               print(f"WARNING: {person.get('_id')} is missing attribute {attribute}")

    person_ids = [person.get("_id") for person in people]
    person_ids2 = copy(person_ids)

    pair_sites = []
    for person1 in person_ids:
        person_ids2.remove(person1)
        for person2 in person_ids2:
            sites = (person1, person2)
            pair_sites.append(sites)

    pairset = []
    for pair in pair_sites:
        resultant = 0
        for attribute, value in scores.items():
            if attribute != "previously_paired":
                diff = compute_diff((pair[0],pair[1]), attribute, people)
                resultant += diff * value.get("score")
        pairset.append((pair[0], pair[1], resultant, 0))

    return pairset

def get_person(id, people):
    person = [person for person in people if person.get("_id") == id]
    if not person:
        person = [{}]
    return person[0]


def compute_diff(pair, attribute, people):
    attr1 = get_person(pair[0], people).get(attribute, 0)
    attr2 = get_person(pair[1], people).get(attribute, 0)

    if isinstance(attr1, (float, int)):
        diff = abs(get_person(pair[0], people).get(attribute, 0) -
            get_person(pair[1], people).get(attribute, 0))

    elif isinstance(attr1, str):
        if attr1 == attr2:
            diff = 0
        else:
            diff = 1

    return diff

def convert_attributes(scores, people):
    errmsg = "ERROR:attr not in cifer"
    decoded_people = []
    for person in people:
        decoded_person = deepcopy(person)
        for attribute, value in scores.items():
            if attribute != "previously_paired":
                cifer = value.get("cifer")
                if cifer: # if there is no cifer, pass through the entries untouched
                    decoded_person[attribute] = cifer.get(person.get(attribute), errmsg)
        decoded_people.append(decoded_person)
    return decoded_people

def assigned_seating(people, pairs):
    # pairs.sort(key=lambda a: a[2]+a[3], reverse=True)
    latest_person = random.choice(people)
    seating = [latest_person]
    iterations = len(people) -1
    # get all the pairs that involve latest_person
    for i in range(iterations):
        pairs_with_latest = [pair for pair in pairs
              if latest_person.get("_id") == pair[0]
              or latest_person.get("_id") == pair[1]]
        # from these, find the set of pairs with the max diversity and randomly select
        diversity = [get_diversity(pair) for pair in pairs_with_latest]
        max_diversity = max(diversity)
        pairs_with_max_diversity = [pair for pair in pairs_with_latest if get_diversity(pair) == max_diversity]
        chosen_pair = random.choice(pairs_with_max_diversity)
        if chosen_pair[0] != latest_person.get("_id"):
            next_neighbor_id = chosen_pair[0]
        else:
            next_neighbor_id = chosen_pair[1]
        next_neighbor = get_person(next_neighbor_id, people)
        seating.append(next_neighbor)
        pairs = [pair for pair in pairs
              if pair[0] != latest_person.get("_id")]
        pairs = [pair for pair in pairs
                 if pair[1] != latest_person.get("_id") ]
        latest_person = next_neighbor
    print(seating)
    return seating


def get_diversity(pair):
    return pair[2] + pair[3]
