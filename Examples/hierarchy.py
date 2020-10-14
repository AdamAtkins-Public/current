
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

def enter_records(hierarchy,records,vertex_index,edge_index):
    for record in records[1:]:
        #Preprocessing should be done elsewhere but for proof of concept
        #   we know that the sampleset is a CSV
        processed_record = record.split(sep=',')

        #enter keys
        #TODO: needs to resolve key error
        if processed_record[vertex_index] not in hierarchy:
            hierarchy[processed_record[vertex_index]] = [[],[]]
        if processed_record[edge_index] not in hierarchy:
            hierarchy[processed_record[edge_index]] = [[],[]]

        #enter edges; assumes Superior->Subordinate
        #TODO: reconfigure/minimize
        (hierarchy[processed_record[vertex_index]])[1].append(processed_record[edge_index])
        (hierarchy[processed_record[edge_index]])[0].append(processed_record[vertex_index])

#An example of top-down building BY TIER (using recursion) ((needs atomic execution))
#   This data probably should be enumerated in a tree
def determine_tiers(hierarchy):

    def tier_delver(hierarchy,superior,depth,tiers):
        if depth+1 > len(tiers):
            tiers.append([])
        subordinates = (hierarchy[superior])[1]
        tiers[depth].append(subordinates)
        for subordinate in subordinates:
            tiers = tier_delver(hierarchy,subordinate,depth+1,tiers)
        return tiers

    tiers = [[]]
    depth = 0
    return tier_delver(hierarchy,'',0,tiers)

def draw_hierarchy(hierarchy):
    pass

if __name__ == '__main__':
    hier = hierarchy()
    path = 'C:\\Users\\ajatkins\\Documents\\Qualta\\VorteksTrainingData\\VorteksTrainingData\\SampleFiles\\Data\\Companies.csv'
    records = import_records(path)
    for record in records:
        print(record.__str__())
    enter_records(hier,records,3,2)
    print(determine_tiers(hier))
    print('hello')