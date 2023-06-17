import pathlib

from randomizers.io import load_json_inputs, json_to_collection
from randomizers.tools import initialize_pairs

def main():
    ppl_file = pathlib.Path("./tests/data/people.json")
    scores_file = pathlib.Path("./tests/data/scores.json")
    scores = load_json_inputs(scores_file)
    people_as_json = load_json_inputs(ppl_file)
    people = json_to_collection(people_as_json)
    pair_set = initialize_pairs(people, scores)

if __name__ == "__main__":
    main()
