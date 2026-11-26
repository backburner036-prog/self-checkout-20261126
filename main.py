import os

# One line, one voice: a smug self-checkout machine judging your basket.
LINE = "Scan complete: twelve yoghurts and one banana. The banana is for plausible deniability."

def main():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)

if __name__ == "__main__":
    main()
