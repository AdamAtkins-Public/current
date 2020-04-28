###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time
import os

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(os.path.abspath(filename), 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cows_l= list(cows)
    remaining_cows = list()
    #n + nlgn
    for cow in cows_l:
        remaining_cows.append((cow,int(cows.get(cow))))
    remaining_cows = sorted(remaining_cows,key=lambda x: x[1], reverse=True)

    #n^2?
    trips, removed = list(), list()
    space = int(0)
    while len(remaining_cows) != 0:
        trip = list()
        removed.clear()
        space = limit
        for r_cow in remaining_cows:
            if r_cow[1] < space:
                trip.append(r_cow[0])
                space -= r_cow[1]
                removed.append(r_cow)
        for item in removed:
            remaining_cows.remove(item)
        trips.append(trip)
    return trips



# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here

    def bell_triangle(n):
        row, prev_row = list(), list()
        #B_0 = 1
        row.append(1)
        for k in range(1,n):
            prev_row = row.copy()
            row.clear()
            row.append(prev_row[-1])
            for i in range(len(prev_row)):
                row.append(prev_row[i] + row[i])
        return row[-1]

    l_cows = list(cows)
    min_length = len(l_cows)+1
    partitions = get_partitions(l_cows)

    #weight of cow
    cow_weight = lambda x,y: x[y]
    trips = None
    for i in range(bell_triangle(len(l_cows))):
        partition = partitions.__next__()
        valid = True
        for trip in partition:
            if valid:
                trip_weight = 0
                for cow in trip:
                    trip_weight += cow_weight(cows,cow)
                    if trip_weight > limit:
                        valid = False
                        break
            else:
                break
        if valid and (len(partition) < min_length):
            min_length = len(partition)
            trips = partition
    return trips

        
# Problem 3
def compare_cow_transport_algorithms(cows):
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    stime = time.time()
    greedy_cow_transport(cows)
    print('Runtime Greedy:', time.time()-stime)

    stime = time.time()
    brute_force_cow_transport(cows)
    print('Runtime Brute Force:', time.time()-stime)
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("Online_Courses\\6.00.2x\\data\\ps1_cow_data.txt")
limit=10
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))
compare_cow_transport_algorithms(cows)


