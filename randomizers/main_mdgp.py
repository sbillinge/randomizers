import pathlib
from copy import deepcopy

from randomizers.io import load_json_inputs, \
    json_to_collection, \
    dump_object, \
    load_csv
from randomizers.tools import initialize_pairs, assigned_seating

def main():
    # ppl_file = pathlib.Path("./tests/data/people.json")
    scores_file = pathlib.Path("./_build/juami_scores.json")
    scores = load_json_inputs(scores_file)
    # people_as_json = load_json_inputs(ppl_file)
    # people = json_to_collection(people_as_json)
    people = load_csv("./_build/juami_augmented.csv")
    pair_set = initialize_pairs(people, scores)
    dump_object(pair_set, file="./_build/pairs.json")
    roundtripped_pairs = load_json_inputs("./_build/pairs.json")
    seating = assigned_seating(people, roundtripped_pairs)
    seating_names = [f"{person.get('name')}, {person.get('work_continent')}, {person.get('gender')}, {person.get('institution')}" for person in seating]
    print(seating_names)
    chunks = [seating_names[x:x + 6] for x in range(0, len(seating_names), 6)]
    print(chunks)

    # roundtripped_pairs = deepcopy(pair_set)
    # test_roundtrip = False
    # if roundtripped_pairs == pair_set:
    #     test_roundtrip = True
    # print(test_roundtrip)



if __name__ == "__main__":
    main()
