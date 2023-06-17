import pathlib

from randomizers.io import load_json_inputs

def main():
    ppl_file = pathlib.Path("./tests/data/people.json")
    scores_file = pathlib.Path("./tests/data/scores.json")
    scores = load_json_inputs(scores_file)
    print(f"loading {ppl_file}")
    people = load_json_inputs(ppl_file)

if __name__ == "__main__":
    main()
