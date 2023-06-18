import pathlib
import sys
import json
import numpy
from json import JSONEncoder

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

def load_json_inputs(file):
    """
    Loads the people collection from files system json

    Parameters
    ----------
    file: pathlib.Path object
      the path to the file with the people collection in it

    Returns
    -------
    the people collection
    """
    if isinstance(file, str):
        file = pathlib.Path(file)
    if not pathlib.Path.exists(file):
        raise RuntimeError(f"file: {file} not found")
    with open(file, "r", encoding='utf-8') as f:
        doc = json.load(f)
    return doc

def dump_object(object, file):
    """
    dumps pairs object to json to file system

    Parameters
    ----------
     pairs: pairs object
     the pairs arrays to be written to disc
    file: pathlib.Path object
      the path to the file that will be written.  If None write in current directory

    Returns
    -------
    None
    """
    file_path = pathlib.Path(file)
        # file.parent.mkdir(parents=True, exist_ok=True)
    # try:
        with open(file_path, "w", encoding='utf-8') as f:
            doc = json.dump(object, f)
    # except
    return

def json_to_collection(doc):
    coll = []
    for item in doc.items():
        entry = {"_id": item[0]}
        entry.update(item[1])
        coll.append(entry)
    return coll



def get_input():
    '''Command-line argument parser function for JUAMI randomizers


    Returns
    -------
    i : file object
        the file object of the opened file of items to randomize

    '''
    if len(sys.argv) == 1:  # elegant exit if user doesn't give a filename
        print("usage: python {} <filename>".format(sys.argv[0]))
        exit()

    try:  # elegant exit if there is an error in the filename
        open(sys.argv[1], 'r')
    except IOError:
        print("sorry, I can't find a file called '" + sys.argv[
            1] + "', please try again.")
        exit()

    i = open(sys.argv[1], 'r')
    return i

