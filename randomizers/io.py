import pathlib
import sys
import json

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
    if not pathlib.Path.exists(file):
        raise RuntimeError(f"file: {file} not found")
    with open(file, "r", encoding='utf-8') as f:
        doc = json.load(f)
    return doc



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

