#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []

    ticketsTable = {}

    #loop over entire tickets array
    for ticket in tickets:
        #store all tickets in ticketsTable, with keys as the ticket sources and values as the corresponding ticket destination
        ticketsTable[ticket.source] = ticket.destination

    #get starting ticket, which will have a key as NONE
    startingTicket = ticketsTable.get("NONE")
    #get ending ticket by searching dictionary for a value of NONE. list comprehension will return an array of a single match, so you can access the string directly at position 0 in the array
    endingTicket = [k for k, v in ticketsTable.items() if v == "NONE"][0] 

    #loop starting from the start ticket, until you reach the ending ticket, adding flights to the route along the way
    current = startingTicket
    while (current != endingTicket):   
        route.append(current)
        current = ticketsTable.get(current)

    route.append(current) #append the last current destination to all routes
    route.append("NONE") #append the ending destination to all routes as "NONE"
        

    return route
