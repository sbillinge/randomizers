import pathlib
from copy import deepcopy

from randomizers.io import load_json_inputs, \
    json_to_collection, \
    dump_object, \
    load_csv
from randomizers.tools import initialize_pairs, assigned_seating

from mdgp import random_assignment, assign_to_groups, _TRAITS, diversity_score

def main():
    # ppl_file = pathlib.Path("./tests/data/people.json")
    scores_file = pathlib.Path("./_build/juami_scores.json")
    scores = load_json_inputs(scores_file)
    # people_as_json = load_json_inputs(ppl_file)
    # people = json_to_collection(people_as_json)
    # people = load_csv("./_build/juami_augmented.csv")
    # people = load_csv("C:\Users\simon\simon\2023\service\juami")
    pair_set = initialize_pairs(people, scores)
    dump_object(pair_set, file="./_build/pairs.json")
    roundtripped_pairs = load_json_inputs("./_build/pairs.json")
    seating = assigned_seating(people, roundtripped_pairs)
    # seating_names = [f"{person.get('name')}, {person.get('work_continent')}, {person.get('gender')}, {person.get('institution')}" for person in seating]
    seating_names = [f"{person.get('name')}" for person in seating]
    print(seating_names)
    tables = [seating_names[x:x + 5] for x in range(0, len(seating_names), 5)]
    for i, table in enumerate(tables):
        print(f"Table {i+1}")
        for seat in table:
            print(f"  {seat}")


    # roundtripped_pairs = deepcopy(pair_set)
    # test_roundtrip = False
    # if roundtripped_pairs == pair_set:
    #     test_roundtrip = True
    # print(test_roundtrip)

def main2(n_groups):
    # people = load_csv("./_build/juami_augmented.csv")
    ppl_path = pathlib.Path().home() / "simon/2023/service/juami/juami_augmented.csv"
    people  = load_csv(ppl_path)
    people = [{"name": person.get("name"), "work_continent": person.get("work_continent"),
              "gender": person.get("gender"),"institution": person.get("institution")}
              for person in people]
    groups = assign_to_groups(people, n_groups)
    index = 0
    # for i, group in enumerate(groups):
    #     print(f"Row {row.pop()}, {lr.pop()} (looking towards the board)")
    #     for person in group:
    #         print(f"  {person.get('name')}")
    group_name = "Group"
    for i, group in enumerate(groups):
        print(f"{group_name}: {i+1}")
        for person in group:
            print(f"  {person.get('name')}")

    # print([grp.get("name") for grp in initial_groups])

def main3():
    '''
    write a file of first name last name of all students
    '''
    people = load_csv("./_build/juami_augmented.csv")
    names = [f"{person.get('name')}\n" for person in people]
    print(names)
    with open("juami_student_list.txt", "w") as f:
        f.writelines(names)

def main4(n_groups):
    people = load_csv("./_build/juami_augmented.csv")
    people = [{"name": person.get("name"), "work_continent": person.get("work_continent"),
              "gender": person.get("gender"),"institution": person.get("institution")}
              for person in people]
    groups = assign_to_groups(people, n_groups)
    index = 0
    for i, group in enumerate(groups):
        print(f"Row {row.pop()}, {lr.pop()} (looking towards the board)")
        for person in group:
            print(f"  {person.get('name')}")

if __name__ == "__main__":
    lr = ["Left", "Right", "Left", "Right", "Left", "Right", "Left", "Right",
          "Left", "Right", "Left", "Right", "Left", "Right", "Left", "Right",
          "Left", "Right"]
    row = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
    lr.reverse()
    row.reverse()
    # main()
    # main3(14)
    main2(10)
    # main4(16)
