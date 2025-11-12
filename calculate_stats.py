# calculate_stats.py
# Intentionally includes issues: vague naming, manual loops, no type hints,
# no edge-case handling, mixed concerns in main, weak output formatting.


def calc(list_of_nums):
    s = 0
    for i in list_of_nums:
        s += i
    avg = s / len(list_of_nums)
    mx = max(list_of_nums)
    mn = min(list_of_nums)
    return {"sum": s, "average": avg, "max": mx, "min": mn}

def main():
    nums = [10, 20, 30, 40, 50]
    print("Stats:", calc(nums))

if __name__ == "__main__":
    main()