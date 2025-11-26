import sys
import calc

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <add|sub|mul|div> <num1> <num2>")
        sys.exit(1)

    op = sys.argv[1]
    a = float(sys.argv[2])
    b = float(sys.argv[3])

    if op == "add":
        result = calc.add(a, b)
    elif op == "sub":
        result = calc.sub(a, b)
    elif op == "mul":
        result = calc.mul(a, b)
    elif op == "div":
        try:
            result = calc.div(a, b)
        except ValueError as e:
            print(e)
            sys.exit(1)
    else:
        print("Unknown operation")
        sys.exit(1)

    print("Result:", result)

if __name__ == "__main__":
    main()
