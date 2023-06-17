import json
import os
import tempfile
# from copy import deepcopy, copy
from unittest import mock
import pytest

scores = {"african_or_US": 3,
  "woman_or_man": 2,
  "previously_paired": 3,
  "same_institution": 1
}

people = {"one":{
  "name": "number one",
  "gender": "M",
  "work_continent": "africa",
  "institution": "af_1"
},
"two":{
  "name": "number two",
  "gender": "F",
  "work_continent": "africa",
  "institution": "af_1"
},
"three":{
  "name": "number three",
  "gender": "M",
  "work_continent": "africa",
  "institution": "af_1"
},
"four":{
  "name": "number four",
  "gender": "F",
  "work_continent": "africa",
  "institution": "af_2"
},
"five": {
  "name": "number five",
  "gender": "M",
  "work_continent": "africa",
  "institution": "af_2"
},
"six": {
  "name": "number six",
  "gender": "F",
  "work_continent": "africa",
  "institution": "af_2"
},
"seven": {
  "name": "number seven",
  "gender": "M",
  "work_continent": "africa",
  "institution": "af_3"
},
"eight": {
  "name": "number eight",
  "gender": "F",
  "work_continent": "africa",
  "institution": "af_3"
},
"nine": {
  "name": "number nine",
  "gender": "M",
  "work_continent": "africa",
  "institution": "af_3"
},
"ten": {
  "name": "number ten",
  "gender": "F",
  "work_continent": "africa",
  "institution": "af_4"
},
"eleven": {
  "name": "number eleven",
  "gender": "M",
  "work_continent": "africa",
  "institution": "af_4"
},
"twelve": {
  "name": "number twelve",
  "gender": "M",
  "work_continent": "africa",
  "institution": "af_4"
},
"uone": {
  "name": "number uone",
  "gender": "M",
  "work_continent": "africa",
  "institution": "us_1"
},
"utwo": {
  "name": "number utwo",
  "gender": "F",
  "work_continent": "africa",
  "institution": "us_1"
},
"uthree": {
  "name": "number uthree",
  "gender": "M",
  "work_continent": "africa",
  "institution": "us_2"
},
"ufour": {
  "name": "number ufour",
  "gender": "F",
  "work_continent": "africa",
  "institution": "us_2"
},
"ufive": {
  "name": "number ufive",
  "gender": "M",
  "work_continent": "africa",
  "institution": "us_3"
},
"usix": {
  "name": "number usix",
  "gender": "F",
  "work_continent": "africa",
  "institution": "us_4"
},
"useven": {
  "name": "number useven",
  "gender": "M",
  "work_continent": "africa",
  "institution": "us_5"
},
"ueight": {
  "name": "number ueight",
  "gender": "F",
  "work_continent": "africa",
  "institution": "us_6"
},
"unine": {
  "name": "number unine",
  "gender": "M",
  "work_continent": "africa",
  "institution": "us_7"
}
}

# @pytest.fixture()
# def make_input_files():
#     """A test fixture that creates and destroys a sest of inputs in a temporary
#     directory.
#     This will yield the path to the repo.
#     """
#     cwd = os.getcwd()
#     name = "input_files"
#     input_files = os.path.join(tempfile.gettempdir(), name)
#     if os.path.exists(input_files):
#         rmtree(input_files)
#     os.path.
#     os.chdir(input_files)
#     with open("people.json", "w") as f:
#         json.dump(people)
#     with open("scores.json", "w") as f:
#         json.dump(scores)
#     # fspath = os.path.join(repo, 'db')
#     # os.mkdir(fspath)
#     # exemplars_to_fs(fspath)
#     yield input_files
#     os.chdir(cwd)
#     if not OUTPUT_FAKE_DB:
#         rmtree(input_files)
