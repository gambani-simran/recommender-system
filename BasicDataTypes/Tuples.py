#TUPLES https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = list(map(int, raw_input().split()))
    t = tuple(integer_list)
    print hash(t)
