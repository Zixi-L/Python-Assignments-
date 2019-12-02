import csv
from collections import defaultdict
largestPopulation = 0
state_largestPopulation = ''
with open ('States.txt') as file:
    text = csv.reader(file, delimiter = ' ')
    states = defaultdict(dict)
    for line in text:
        state, region, population = line
        states[region][state] = int(population)
    region = 'Midwest'
    for state, population in states[region].items():
        if population > largestPopulation:
            largestPopulation = population
            state_largestPopulation = state
print('Highest population state in the Midwest is:',state_largestPopulation, largestPopulation)



target_state = ''
count = 0
p_name = []
with open ('USPresidents.txt','rt') as file2:
    text2 = csv.reader(file2, delimiter = '	') 
    president = defaultdict(list)
    for line in text2:
        state, name = line 
        president[state].append(name) 
for k,v in president.items():
    if len(v) > count:
        count = len(v)
        target_state = k
        p_name = v
print('The state with the most presidents is',target_state, 'with',count,'presidents:','\n'.join(p_name))




def president_State():
    US_president = (['CA', 'TX', 'FL', 'NY', 'IL', 'PA', 'OH', 'GA', 'NC', 'MI'])
    dict = {}
    with open("USPresidents.txt", "r") as file3:
        for i in file3:
            x = i.split()
            state = x[0]
            name = x[1]
            if state in dict:
                dict[state].append(name)
            else:
                dict[state] = [name]
    total = len(US_president)
    count = 0
    for k, v in sorted(dict.items()):
        if k in US_president:
            count += 1
    print(f"{count} of the {total} high population states have had presidents born in them: ")
    for k, v in sorted(dict.items()):
        if k in US_president:
            print(k, len(v))
president_State()
