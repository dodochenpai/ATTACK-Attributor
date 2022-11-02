import json
import csv

groups = {}

def groupmapper():
    with open('grouptechniques.csv', encoding="mbcs") as csvfile:
        line = csvfile.readline()
        line = csvfile.readline()
        i = 0
        while line:
            splitline = line.split(',')
            if splitline[4] not in groups:
                groups[splitline[4]] = [splitline[0]]
            else:
                groups[splitline[4]].append(splitline[0])
            i += 1
            line = csvfile.readline()

    with open('groupmappings.json','w') as f:
        f.write(json.dumps(groups, indent=4))

def attributor():
    with open('layer.json','r') as f:
        with open('groupmappings.json','r') as k:
            count = {}
            apts = json.load(k)
            target = json.load(f)
            numtechniques = 0
            for technique in target['techniques']:
                if 'score' in technique:
                    numtechniques+=1
                    try:
                        for group in apts[technique['techniqueID']]:
                            if group not in count:
                                count[group] = 1
                            else:
                                count[group] += 1
                    except:
                        continue
    top = sorted(count, key=count.get, reverse=True)[0:10]
    for group in top:
        print(group, count[group]/numtechniques)

attributor()
