from copy import copy
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

    pairset = {}
    for attribute, value in scores.items():
       for person in people:
           if person.get(attribute) is None and attribute != "previously_paired":
               print(f"WARNING: {person.get('_id')} is missing attribute {attribute}")

    person_ids = [person.get("_id") for person in people]
    person_ids2 = copy(person_ids)
    pair_ids, pair_sites, static_scores = [], [], []

    # build the set of pairs as tuples of the pair members
    for person1 in person_ids:
        person_ids2.remove(person1)
        for person2 in person_ids2:
            sites = (person1, person2)
            pair_sites.append(sites)

    for pair in pair_sites:
        pair_ids.append(f"{pair[0]}-{pair[1]}")
        resultant = 0
        for attribute, value in scores.items():
            diff = compute_diff()
            resultant += diff
        static_scores.append(resultant)

    pairset.update({"pair_ids": pair_ids,
                    "pair_sites": pair_sites,
                    "paired": np.zeros(len(pair_ids)),
                    "static_scores": static_scores})

    return pairset

def get_person(id, people):
    person = [person for person in people if person.get("_id") == id]
    if not person:
        person = [{}]
    return person[0]


def compute_diff(pair, attribute, people):
    attr1 = get_person(pair[0], people).get(attribute, 0)
    attr1 = get_person(pair[0], people).get(attribute, 0)

    if attr1 istype(number):
        diff = abs(get_person(pair[0], people).get(attribute, 0) -
            get_person(pair[1], people).get(attribute, 0))

    elif attr1 istype(str):
        if attr1 == attr2:
            diff = 0
        else:
            diff = 1

    return diff
