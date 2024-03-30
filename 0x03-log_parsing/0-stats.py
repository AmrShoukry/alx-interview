#!/usr/bin/python3
""" STATS """

import sys
import re

status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

lines_count = 0
total_size = 0

pattern = (
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - \[(?P<date>[^\]]+)\] '
    r'"GET /projects/260 HTTP/1.1" (?P<status_code>\d+) (?P<file_size>\d+)'
)


def get_details():
    """ Get details """
    print(f"File size: {total_size}")
    for key in sorted(status_codes.keys()):
        value = status_codes[key]
        if value > 0:
            print(f"{key}: {value}")


def detect_status_code():
    """ Detect status code """
    for key, value in status_codes.items():
        if log_info['status_code'] == key:
            status_codes[key] += 1


try:
    for line in sys.stdin:
        match = re.match(pattern, line.strip())
        if match:
            log_info = match.groupdict()
        else:
            continue

        if (lines_count != 0 and lines_count % 10 == 0):
            get_details()

        detect_status_code()

        lines_count += 1
        total_size += int(log_info['file_size'])

except KeyboardInterrupt:
    get_details()