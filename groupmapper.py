import json
import sys

# Pull out the technique to group mappings from 
# the MITRE ATTACK Excel spreadsheet
def groupmapper():
    groups = {}
    with open('grouptechniques.csv', encoding="mbcs") as csvfile:
        # Skip the first line
        line = csvfile.readline()
        line = csvfile.readline()
        # Files the dictionary with {technique:[groups]} mappings
        while line:
            splitline = line.split(',')
            if splitline[4] not in groups:
                groups[splitline[4]] = [splitline[0]]
            else:
                groups[splitline[4]].append(splitline[0])
            line = csvfile.readline()

    # Writes the dictionary to disk
    with open('groupmappings.json','w') as f:
        f.write(json.dumps(groups, indent=4))

# Reads an input json file and finds the APTs with the most
# matching techniques
def attributor(inputfile):
    with open(inputfile,'r') as f:
        with open('groupmappings.json','r') as k:
            count = {}
            apts = json.load(k)
            target = json.load(f)
            numtechniques = 0
            # For each technique in the given json, tally the groups
            # that use the technique
            for technique in target['techniques']:
                if 'score' in technique:
                    numtechniques+=1
                    for group in apts[technique['techniqueID']]:
                        if group not in count:
                            count[group] = 1
                        else:
                            count[group] += 1

    # Sort the dictionary and print the top 10
    top = sorted(count, key=count.get, reverse=True)[0:10]
    print("APT   | Match")
    for group in top:
        print(group,'|',100*count[group]/numtechniques,'%')

inputfile = sys.argv[1]
attributor(inputfile)
