def get_input():
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

