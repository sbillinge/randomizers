import numpy as np
import pytest
import unittest.mock as mock

from randomizers.tools import initialize_pairs,\
    get_person,\
    compute_diff,\
    convert_attributes,\
    assigned_seating

ip_people = [{"_id": "one", "thing1": 1, "thing2": 0},
             {"_id": "two", "thing1": 0, "thing2": 1},
             {"_id": "three", "thing1": 1, "thing2": 1}]
ip_scores = {"thing1": {"score": 1}, "thing2": {"score": 2}}
initial_pairs = [("one", "two", 3, 0),("one", "three", 2, 0), ("two", "three", 1, 0)]


def test_initialize_pairs():
    expected = initial_pairs
    actual = initialize_pairs(ip_people, ip_scores)
    assert expected == actual

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


cd_tests = [([("test", "test2"),"a1", [{"_id": "test", "a1": 1}, {"_id": "test2", "a1": 2}]], 1),
             ([("test2", "test"), "a1", [{"_id": "test", "a1": 1}, {"_id": "test2", "a1": 2}]], 1),
             ([("test", "test2"), "a1",
               [{"_id": "test", "a1": "same string"}, {"_id": "test2", "a1": "same string"}]], 0),
             ([("test", "test2"), "a1", [{"_id": "test", "a1": "string"}, {"_id": "test2", "a1": "different string"}]], 1),
             ]
@pytest.mark.parametrize("cd", cd_tests)
def test_compute_diff(cd):
    actual = compute_diff(cd[0][0], cd[0][1], cd[0][2])
    expected = cd[1]
    assert expected == actual

ca_tests = [([{"a1": {"score": 1, "cifer": {"a": 1, "b":0}},
               "a2": {"score": 2, "cifer": {"ku": 1, "dos":0}},
               "a3": {"score": 3, "cifer": {}}},
             [{"_id": "test", "a1": "a", "a2": "ku", "a3": "text"},
              {"_id": "test2", "a1": "b", "a2": "dos", "a3": "text"}]],
             [{"_id": "test", "a1": 1, "a2": 1, "a3": "text"},
              {"_id": "test2", "a1": 0, "a2": 0, "a3": "text"}]
                                                              ),
            ([{"a1": {"score": 1, "cifer": {"a": 1, "b": 0}},
               "a2": {"score": 2, "cifer": {"ku": 1, "dos": 0}},
               "a3": {"score": 3, "cifer": {}}},
             [{"_id": "test", "a1": "a", "a2": "ku", "a3": "text"},
              {"_id": "test2", "a1": "b", "a2": "quest", "a3": "text"}]],
             [{"_id": "test", "a1": 1, "a2": 1, "a3": "text"},
              {"_id": "test2", "a1": 0, "a2": "ERROR:attr not in cifer", "a3": "text"}]
             ),
            ]
@pytest.mark.parametrize("ca", ca_tests)
def test_convert_attributes(ca):
    actual = convert_attributes(ca[0][0], ca[0][1])
    expected = ca[1]
    assert expected == actual


@mock.patch('random.choice')
def test_assigned_seating(mocked_choice):
    mocked_choice.side_effect = [{"_id": "three", "thing1": 1, "thing2": 1}, ('one', 'three', 2, 0), ("two", "three", 1, 0)]
    with mock.patch('random.choice', mocked_choice):
        actual  = assigned_seating(ip_people, initial_pairs)
        expected = [{'_id': 'three', 'thing1': 1, 'thing2': 1}, {'_id': 'one', 'thing1': 1, 'thing2': 0}, {'_id': 'two', 'thing1': 0, 'thing2': 1}]
        assert expected == actual
