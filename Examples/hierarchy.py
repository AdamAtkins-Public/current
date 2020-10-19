
import os

def hierarchy():
    hierarchy = dict()
    return hierarchy

def import_records(path):
    records = []
    with open(path) as file:
        for line in file:
            records.append(line[:-1])#scrub newline
    return records

def enter_records(hierarchy,records,from_index,to_index):
    for record in records[1:]:
        #Preprocessing should be done elsewhere but for proof of concept
        #   we know that the sampleset is a CSV
        processed_record = record.split(sep=',')

        #enter keys
        if processed_record[from_index] not in hierarchy and \
           processed_record[from_index] != '': hierarchy[processed_record[from_index]] = [set(),set()]
        if processed_record[to_index] not in hierarchy and \
           processed_record[to_index] != '': hierarchy[processed_record[to_index]] = [set(),set()]

        #enter edges
        if processed_record[from_index] != '' and processed_record[to_index] != '':
            (hierarchy[processed_record[from_index]])[1].add(processed_record[to_index])
            (hierarchy[processed_record[to_index]])[0].add(processed_record[from_index])

#An example of top-down building BY TIER (using recursion) ((needs atomic execution))
#   This data probably should be enumerated in a tree
def determine_tiers(hierarchy):

    #topological sort
    def tier_delver(hierarchy,superior,depth,tiers):
        if depth+1 > len(tiers):
            tiers.append([])
        subordinates = (hierarchy[superior])[1]
        tiers[depth].append(list(subordinates))
        for subordinate in subordinates:
            tiers = tier_delver(hierarchy,subordinate,depth+1,tiers)
        return tiers

    #find roots; keys: such that len((dict[key])[0])==0 ie if the Superior set is Empty
    roots = []
    for key in list(hierarchy):
        if len((hierarchy[key])[0])==0:
            roots.append(key)

    tiers = [[]]
    depth = 0
    for root in roots:
        tiers[0].append(root)
        tiers = tier_delver(hierarchy,root,depth+1,tiers)
    return tiers

def draw_hierarchy(hierarchy):
    pass

if __name__ == '__main__':
    #data
    path = 'C:\\Users\\ajatkins\\Documents\\Qualta\\VorteksTrainingData\\VorteksTrainingData\\SampleFiles\\Data\\Companies_fatter.csv'
    records = import_records(path)
    for record in records:
        print(record.__str__())
    #structure
    hier = hierarchy()
    enter_records(hier,records,2,4)
    print(determine_tiers(hier))
    hier.clear()
    enter_records(hier,records,3,2)
    print(determine_tiers(hier))
    #communication
    print('hello there')