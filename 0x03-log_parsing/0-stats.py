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


def get_file_size_status_code(line: str, prog) -> Union[Tuple[str, int], None]:
    """
    valdate lne return state code, fle sze or None
    """
    m = re.search(prog, line)
    if m:
        result = (m.groups()[2], int(m.groups()[3]))
        return result
    return None


def display_result(
        file_size: int,
        result: Dict[str, int],
        status_codes: Tuple[str, ...]) -> None:
    """
    display result so far
    """
    print('File size: {}'.format(file_size))
    for s_code in status_codes:
        total = result[s_code]
        if total > 0:
            print('{}: {}'.format(s_code, total))
    sys.stdout.flush()


def main() -> None:
    """
    Entry Point
    """
    total_file_size = 0
    print_f_size = True
    status_codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    result = {code: 0 for code in status_codes}
    PATTERN = r'(\w*)\s*-\s*\[\d{4}-\d{2}-\d{2} '\
        r'\d{1,2}:\d{1,2}:\d{1,2}(\.\d+)?\] "GET '\
        r'\/projects\/260 HTTP\/1\.1" (\w*) (\d+)$'
    prog = re.compile(PATTERN)
    while True:
        for i in range(10):
            try:
                line = sys.stdin.readline().lstrip().rstrip()
                if not line:
                    if i > 0 or print_f_size:
                        display_result(total_file_size, result, status_codes)
                    return
                status_code_file_size = get_file_size_status_code(line, prog)
                if status_code_file_size:
                    if status_code_file_size[0] in result:
                        result[status_code_file_size[0]] += 1
                    total_file_size += status_code_file_size[1]
            except KeyboardInterrupt:
                display_result(total_file_size, result, status_codes)
                return
        display_result(total_file_size, result, status_codes)
        print_f_size = False


if __name__ == '__main__':
    main()
