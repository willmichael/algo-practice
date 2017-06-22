import sys

def get_input():
    get_in = []
    for line in sys.stdin:
        get_in.append(line.split())
    return get_in

def main():
    inp = get_input()
    
    ### Get N Strings
    n = int(inp[0][0])
    n_strings = []
    for i in range(1,n+1):
        n_strings.append(inp[i][0])
        
    ### Get Q Queries
    q = int(inp[n+1][0])
    q_queries = []
    for i in range(n+2, n+q+2):
        q_queries.append(inp[i][0])

    ### Search strings for queries
    q_counts = []
    for q in q_queries:
        count = 0
        for n in n_strings:
            if n == q:
                count += 1
        q_counts.append(count)
    
    ### Display answer
    for q in q_counts:
        print q


if __name__ == '__main__':
    sys.exit(main())
