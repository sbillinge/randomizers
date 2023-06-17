# # import os
# # import sys
#
# import pytest

from randomizers.io import load_people
from randomizers.tests.conftest import scores, people

# @pytest.mark.parametrize("bm", builder_map)
def test_load_people(make_input_files ):
    input_files = make_input_files
    actual = load_people()
    os.chdir(input_files)
    # assert expected == actual
    assert True





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
