#Finding the percenteage https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(raw_input())
    s = 0
    student_marks = {}
    for i in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    #for i in range(len(scores)):
        #s = s + student_marks[query_name]
    s = sum(map(float,student_marks[query_name]))/len(scores)
    
    print format(s,'.2f')
    
        
    
