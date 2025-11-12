def read_numbers_from_file(path):
    # naive CSV-like reader: numbers separated by spaces or commas
    with open(path, "r") as f:
        txt = f.read().strip()
        parts = txt.replace(",", " ").split()
        nums = []
        for p in parts:
            try:
                nums.append(float(p))
            except Exception:
                pass # silently ignore anything not a number
        return nums