#Second-largest-number https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(raw_input())
    a = list(map(int, raw_input().split()))
    arr = set(a)
    ar = list(arr)
    ar.sort()
    print ar[-2]
    
