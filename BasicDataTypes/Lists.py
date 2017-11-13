#LISTS https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    l = list()
    n = int(raw_input())
    for i in range (0,n):
        inp = raw_input().split()
        if inp[0] == "insert":
            l.insert(int(inp[1]),int(inp[2]))
        elif inp[0] == "print":
            print l
        elif inp[0] == "remove":
            l.remove(int(inp[1]))
        elif inp[0] == "append":
            l.append(int(inp[1]))    
        elif inp[0] == "sort":
            l.sort()
        elif inp[0] == "pop":
            l.pop()
        elif inp[0] == "reverse":
            l.reverse()
