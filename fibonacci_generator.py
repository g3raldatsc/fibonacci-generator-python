import time

def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    print("Fibonacci Sequence Generator\n")
    try:
        n = int(input("Enter the number of terms to generate: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    print("\nGenerating Fibonacci sequence...\n")
    fibonacci_sequence = generate_fibonacci(n)
    for number in fibonacci_sequence:
        print(number, end=" ", flush=True)
        time.sleep(0.5)
    print("\n\nSequence complete.")

if __name__ == "__main__":
    main()