#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:
- Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
(if the format is not this one, the line must be skipped)
- After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
    - Total file size: File size: <total size>
    - where <total size> is the sum of all previous <file size>
    (see input format above)
    - Number of lines by status code:
        - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
        - if a status code doesn’t appear or is not an integer,
        don’t print anything for this status code
        - format: <status code>: <number>
        - status codes should be printed in ascending order
"""
import sys
import re
from typing import Union, Tuple, Dict


def get_file_size_status_code(line: str) -> Union[Tuple[str, int], None]:
    PATTERN = r'^(\d{1,4}\.){3}\d{1,4} - '\
        r'\[\d{4}-\d{2}-\d{2} \d{1,2}:\d{1,2}:\d{1,2}(\.\d+)?\]'\
        r' "GET \/projects\/260 HTTP\/1\.1" '\
        r'(200|301|400|401|403|404|405|500){1} (\d+)$'
    m = re.fullmatch(PATTERN, line)
    if m:
        return (m.groups()[2], int(m.groups()[3]))
    return None


def display_result(
        file_size: int,
        result: Dict,
        status_codes: Tuple[str]) -> None:
    print('File size: {}'.format(file_size))
    for s_code in status_codes:
        sum = result.get(s_code)
        if sum > 0:
            print('{}: {}'.format(s_code, sum))


def main() -> None:
    """
    Entry Point
    """
    total_file_size = 0
    status_codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    result = {code: 0 for code in status_codes}
    while True:
        for i in range(10):
            try:
                line = sys.stdin.readline()
                if not line:
                    return
                line = line.rstrip().lstrip()
                status_code_file_size = get_file_size_status_code(line)
                if status_code_file_size and \
                   status_code_file_size[0] in result:
                    result[status_code_file_size[0]] += 1
                    total_file_size += status_code_file_size[1]
            except KeyboardInterrupt:
                display_result(total_file_size, result, status_codes)
                sys.stdout.flush()
                return
        display_result(total_file_size, result, status_codes)


if __name__ == '__main__':
    main()
