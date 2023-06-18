import pathlib
from copy import deepcopy

from randomizers.io import load_json_inputs, json_to_collection, dump_object
from randomizers.tools import initialize_pairs

def main():
    ppl_file = pathlib.Path("./tests/data/people.json")
    scores_file = pathlib.Path("./tests/data/scores.json")
    scores = load_json_inputs(scores_file)
    people_as_json = load_json_inputs(ppl_file)
    people = json_to_collection(people_as_json)
    pair_set = initialize_pairs(people, scores)
    dump_object(pair_set, file="./_build/pairs.json")
    roundtripped_pairs = load_json_inputs("./_build/pairs.json")
    # roundtripped_pairs = deepcopy(pair_set)
    # test_roundtrip = False
    # if roundtripped_pairs == pair_set:
    #     test_roundtrip = True
    # print(test_roundtrip)



if __name__ == "__main__":
    main()
