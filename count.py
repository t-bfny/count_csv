import requests
import csv
import argparse
from io import StringIO

def count_csv_rows(url, has_header=True):
    response = requests.get(url)
    response.raise_for_status()  # ← 通信失敗時にエラーにする
    csv_data = response.text
    f = StringIO(csv_data)
    reader = csv.reader(f)

    if has_header:
        next(reader)  # ヘッダー行をスキップ

    count = sum(1 for _ in reader)
    print(f"行数（ヘッダー除く）: {count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, required=True, help="CSVファイルのURL")
    parser.add_argument("--no-header", action="store_true", help="ヘッダーを含む場合に指定")
    args = parser.parse_args()

    count_csv_rows(args.url, has_header=not args.no_header)
