def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    table = {}
    seenAlreadyInList = []

    #loop over list of lists. Fill table with the numbers in each list as keys, and their values as how many times that particular number has been seen (once per list)
    for array in arrays:
        #loop over every number in individual list
        for num in array:
            #if number is already in the table
            if num in table:
                #check that number has not yet been seen in this same list yet, as we only want to increase the count value once per list
                if not num in seenAlreadyInList:
                    table[num]+=1
                    seenAlreadyInList.append(num)
            #if number is not yet in the table, add it and set count to 1
            else:
                table[num] = 1
                seenAlreadyInList.append(num)

        #reset seen number list
        seenAlreadyInList = []
        
    #fill result array with keys within table of the numbers that were seen a total of *count* times, where *count* is the length of the array passed in to the function (which is the num of lists in the arrays)
    result = [k for k, v in table.items() if v == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
