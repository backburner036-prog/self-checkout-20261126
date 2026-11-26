import os

# One line, one voice: a smug self-checkout machine judging your basket.
LINE = "Scan complete: twelve yoghurts and one banana. The banana is for plausible deniability."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.replace(tmp_path, entry_path)
    with open(entry_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == LINE + "\n", "entry.txt content mismatch"
    assert len(LINE) == 87, "LINE must be 87 characters"
    print(LINE)

if __name__ == "__main__":
    main()
