import sys

def get_input():
    get_in = []
    for line in sys.stdin:
        get_in.append(line.split())
    return get_in

def main():
    ### Get input, create 0'd array
    inp = get_input()
    n = int(inp[0][0])
    m = int(inp[0][1])
    zeros = [0] * n

    ### Go through each line, update array
    iter_input = iter(inp)
    next(iter_input)
    for line in iter_input:
        a = int(line[0])
        b = int(line[1])
        c = int(line[2])
        for i in range(a-1,b):
            zeros[i] += c

    print max(zeros)





if __name__ == "__main__":
    main()
