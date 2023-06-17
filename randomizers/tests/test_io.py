# # import os
# # import sys
#
# import pytest

from randomizers.io import json_to_collection
from randomizers.tests.conftest import scores, people

# # @pytest.mark.parametrize("bm", builder_map)
# def test_load_people(make_input_files ):
#     input_files = make_input_files
#     actual = load_people()
#     os.chdir(input_files)
#     # assert expected == actual
#     assert True
people_coll_as_list = [{'_id': 'one', 'name': 'number one', 'gender': 'M', 'work_continent': 'africa', 'institution': 'af_1'}, {'_id': 'two', 'name': 'number two', 'gender': 'F', 'work_continent': 'africa', 'institution': 'af_1'}, {'_id': 'three', 'name': 'number three', 'gender': 'M', 'work_continent': 'africa', 'institution': 'af_1'}, {'_id': 'four', 'name': 'number four', 'gender': 'F', 'work_continent': 'africa', 'institution': 'af_2'}, {'_id': 'five', 'name': 'number five', 'gender': 'M', 'work_continent': 'africa', 'institution': 'af_2'}, {'_id': 'six', 'name': 'number six', 'gender': 'F', 'work_continent': 'africa', 'institution': 'af_2'}, {'_id': 'seven', 'name': 'number seven', 'gender': 'M', 'work_continent': 'africa', 'institution': 'af_3'}, {'_id': 'eight', 'name': 'number eight', 'gender': 'F', 'work_continent': 'africa', 'institution': 'af_3'}, {'_id': 'nine', 'name': 'number nine', 'gender': 'M', 'work_continent': 'africa', 'institution': 'af_3'}, {'_id': 'ten', 'name': 'number ten', 'gender': 'F', 'work_continent': 'africa', 'institution': 'af_4'}, {'_id': 'eleven', 'name': 'number eleven', 'gender': 'M', 'work_continent': 'africa', 'institution': 'af_4'}, {'_id': 'twelve', 'name': 'number twelve', 'gender': 'M', 'work_continent': 'africa', 'institution': 'af_4'}, {'_id': 'uone', 'name': 'number uone', 'gender': 'M', 'work_continent': 'africa', 'institution': 'us_1'}, {'_id': 'utwo', 'name': 'number utwo', 'gender': 'F', 'work_continent': 'africa', 'institution': 'us_1'}, {'_id': 'uthree', 'name': 'number uthree', 'gender': 'M', 'work_continent': 'africa', 'institution': 'us_2'}, {'_id': 'ufour', 'name': 'number ufour', 'gender': 'F', 'work_continent': 'africa', 'institution': 'us_2'}, {'_id': 'ufive', 'name': 'number ufive', 'gender': 'M', 'work_continent': 'africa', 'institution': 'us_3'}, {'_id': 'usix', 'name': 'number usix', 'gender': 'F', 'work_continent': 'africa', 'institution': 'us_4'}, {'_id': 'useven', 'name': 'number useven', 'gender': 'M', 'work_continent': 'africa', 'institution': 'us_5'}, {'_id': 'ueight', 'name': 'number ueight', 'gender': 'F', 'work_continent': 'africa', 'institution': 'us_6'}, {'_id': 'unine', 'name': 'number unine', 'gender': 'M', 'work_continent': 'africa', 'institution': 'us_7'}]
def test_json_to_collection():
    actual = json_to_collection(people)
    expected = people_coll_as_list
    assert expected == actual




    # if bm == "html":
    #     os.makedirs("templates/static", exist_ok=True)
    # if bm == "reimb" or bm == "recent-collabs":
    #     main(["build", bm, "--no-pdf", "--people", "scopatz"])
    # # main(["build", bm, "--no-pdf"])
    # os.chdir(os.path.join(repo, "_build", bm))
    # expected_base = os.path.join(os.path.dirname(__file__), "outputs")
    # if bm == "internalhtml":
    #     def mockreturn(*args, **kwargs):
    #         mock_article = {'message': {'author': [{"given":"SJL","family":"B"}],
    #                                     "short-container-title": ["J Club Paper"],
    #                                     "volume": 10,
    #                                     "title": ["title"],
    #                                     "issued": {"date-parts":[[1971]]}}
    #                         }
    #         return mock_article
    #     monkeypatch.setattr(habanero.Crossref, "works", mockreturn)
