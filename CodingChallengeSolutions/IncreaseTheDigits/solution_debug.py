from solution import solution1

# print input and output
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python3 IncreaseTheDigits_debug.py input.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        line = f.read().strip()
        n = eval(line) 

    print("######## input ########")
    print("input  is " + str(n))

    result = solution1(n)

    print("######## result ########")
    print("result is " + str(result))