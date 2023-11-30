import sys
import subprocess
from datetime import date


def setup_day(d):
    p = subprocess.call(
        ['mkdir', f'day{d}'], cwd='./', stdout=subprocess.PIPE)
    s = subprocess.call(
        ['cp', '../template.py', f'day{d}.py'], cwd=f'./day{d}', stdout=subprocess.PIPE)
    a = subprocess.call(
        ['touch', 'ex.txt'], cwd=f'./day{d}', stdout=subprocess.PIPE)


def main():
    day = int(date.today().strftime('%d'))
    if len(sys.argv) == 2:
        day = int(sys.argv[1])
    s_day = '0' * (day < 10) + str(day)
    setup_day(s_day)


if __name__ == '__main__':
    main()
