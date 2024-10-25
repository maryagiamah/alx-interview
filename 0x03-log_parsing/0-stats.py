#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics"""
import sys
import re

total_size = 0
count = 0
status_code = {
        "200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
        "404": 0, "405": 0, "500": 0
    }

try:
    for line in sys.stdin:
        pattern = (
                r"^(\d{1,3}\.?){4} - \[.*?\] "
                r"\"GET \/projects\/260 HTTP\/1.1\" (\d{0,3}) (\d{1,4})"
            )
        match = re.fullmatch(pattern, line.strip())

        if match:
            code = match.group(2)
            total_size += int(match.group(3))

            if code in status_code.keys():
                status_code[code] = status_code.get(code) + 1
                count += 1

        if count % 10 == 0:
            print(f"File size: {total_size}")
            for k, v in status_code.items():
                if v > 0:
                    print(f"{k}: {v}")
except Exception:
    pass
finally:
    print(f"File size: {total_size}")
    for k, v in status_code.items():
        if v > 0:
            print(f"{k}: {v}")
