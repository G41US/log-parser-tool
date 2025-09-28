import sys
import pandas as pd

def parse_log(filepath):
    # Example parser for Apache logs: "IP - - [date] \"METHOD URL PROTO\" STATUS SIZE"
    data = []
    with open(filepath) as f:
        for line in f:
            parts = line.split()
            if len(parts) < 9:
                continue
            ip, method, url, status = parts[0], parts[5].strip('"'), parts[6], parts[8]
            data.append({"ip": ip, "method": method, "url": url, "status": status})
    return pd.DataFrame(data)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python src/parser.py <input_log> <output_csv>")
        sys.exit(1)

    infile, outfile = sys.argv[1], sys.argv[2]
    df = parse_log(infile)
    df.to_csv(outfile, index=False)
    print(f"Saved parsed log to {outfile}")
