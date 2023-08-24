#!/usr/bin/python3
import sys
import signal

# Dictionary to store the count of each status code
status_code_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

total_file_size = 0
line_count = 0

def print_statistics():
    print("Total file size:", total_file_size)
    for status_code in sorted(status_code_count.keys()):
        if status_code_count[status_code] > 0:
            print(f"{status_code}: {status_code_count[status_code]}")

def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()

        if len(parts) < 7:
            continue

        ip_address = parts[0]
        status_code = parts[-2]
        file_size = parts[-1]

        try:
            file_size = int(file_size)
        except ValueError:
            continue

        if status_code.isdigit():
            status_code = int(status_code)
            if status_code in status_code_count:
                status_code_count[status_code] += 1

        total_file_size += file_size
        line_count += 1

        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
