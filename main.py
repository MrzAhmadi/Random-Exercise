from random import seed
from random import randint

jumpCounts = [200,225,250,275,300,325,350,375,400,425,450,475,500]
jumpRopeColorie = jumpCounts[randint(0, len(jumpCounts)-1)]
push_sit_up = randint(20,40)

print("\n\n==== Today workout plan =====\n")

d = {1: ["Jump rope", jumpRopeColorie, 'Consumption calories'],
2: ["Push up", push_sit_up, 'time'],
3: ["Sit up", push_sit_up, 'time'],
}
print ("{:<8} {:<15} {:<10} {:<10}".format('Pos','Exercise','Amount','Unit'))
for k, v in d.items():
    lang, perc, change = v
    print ("{:<8} {:<15} {:<10} {:<10}".format(k, lang, perc, change))

print("\n============================\n")
