# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    #create queriesTable, by adding all queries to the table as keys, with values of empty arrays that will eventually contain a list of the files that contain that specific query in them
    queriesTable = {}
    for query in queries:
        queriesTable[query] = []

    #
    result = []
    for file in files:
        foundFiles = [file for q in queries if q in file]
        print(foundFiles)
        
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
