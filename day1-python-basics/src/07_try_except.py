print("Day 1 - Try Except")

try:
    x = 10 / 2
    print("Result:", x)
except Exception as e:
    print("Error:", e)

print("-" * 40)

try:
    x = 10 / 0
    print("Result:", x)
except Exception as e:
    print("Error happened:", e)

print("-" * 40)


def safe_process(number):
    try:
        result = 100 / number
        print("Result:", result)
    except Exception as e:
        print("Failed to process:", e)


safe_process(5)
safe_process(0)
