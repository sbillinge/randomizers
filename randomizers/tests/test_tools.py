import numpy as np
import pytest

from randomizers.tools import initialize_pairs, get_person

ip_people = [{"_id": "one", "thing1": 1, "thing2": 0},
             {"_id": "two", "thing1": 0, "thing2": 1},
             {"_id": "three", "thing1": 1, "thing2": 1}]
ip_scores = {"thing1": 1, "thing2": 2}
initial_pairs = {"pair_ids":["one-two", "one-three", "two-three"],
                 "pair_sites":[("one", "two"), ("one", "three"), ("two", "three")],
                 "paired": np.array([0, 0, 0]),
                 "static_scores": np.array([3, 2, 1])
                 }

def test_initialize_pairs():
    expected = initial_pairs
    actual = initialize_pairs(ip_people, ip_scores)
    assert expected.get("pair_ids") == actual.get("pair_ids")
    assert expected.get("paired").all() == actual.get("paired").all()
    assert expected.get("pair_sites") == actual.get("pair_sites")

gp_people = [{"_id": "test", "a1": 1}, {"_id": "test2", "a1": 2},
 {"_id": "test3", "a1": 3}]
gpp_tests = [("test", {"_id": "test", "a1": 1}),
             ("bad_id", {})
            ]
@pytest.mark.parametrize("gpp", gpp_tests)
def test_get_person(gpp):
    actual = get_person(gpp[0], gp_people)
    expected = gpp[1]
    assert expected == actual
