#Nested List https://www.hackerrank.com/challenges/nested-list/problem

l = list()
n = int(raw_input())
for i in range(0,n):
    name = raw_input()
    score = float(raw_input())
    l.append([name,score])

scores = list()
for i in range(0,n):
    scores.append(l[i][1])
    
scores = set(scores)
scores = list(scores)
scores.sort()
final = list()
for i in range(0,n):
    if(l[i][1]==scores[1]):
        final.append(l[i][0])
        
final.sort()
for i in range(0,len(final)):
    print final[i]

