def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    table = {}

    #loop over every number in the list, and add the absolute value of each num to the list as a key, with a value count of 0.
    for num in a:
        #if we see the number in the table already as a key (can be positive or negative),
        #check if the number we are currently on is an opposite sign as to what is already in the table for that number,
        #and if so, change the count of the abs(num) to 1 to indicate a match of both positive and negative of the same num seen.
        if abs(num) in table or -num in table:
            #if number is positive, and the num in the table that already exists is negative, increase count
            if num > 0 and -num in table:
                table[-num] = 1
            
            #if number is negative, and the num in the table that already exists is positive, increase count
            if num < 0 and abs(num) in table:
                table[abs(num)] = 1

        #if we haven't seen the number in the table yet, add it to the table as a key with a value count of 0
        else:
            table[num] = 0

    #fill results array with all keys (positive) where the value is 1 (to indicate a match of positive and negative numbers within the list)
    result = [abs(k) for k, v in table.items() if v == 1]
    
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
