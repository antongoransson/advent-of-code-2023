import requests
from datetime import date
import browser_cookie3
import sys

# Get cookies from the browser
year = 2023
cj = browser_cookie3.firefox()
if not ('.adventofcode.com' in str(cj)):
    cj = browser_cookie3.chrome()

day_today = int(date.today().strftime('%d'))
if len(sys.argv) > 1:
    day = int(sys.argv[1])
    if day < 0 or day > 31 or day > int(day_today):
        exit('Day is not valid')
else:
    day = day_today
r = requests.get(
    f'https://adventofcode.com/{year}/day/{day}/input', cookies=cj)
s_day = '0' * (day < 10) + str(day)

if r.status_code == 200:
    print(f'Successfully fetched input for day {day} year {year}')
    with open(f'day{s_day}/in.txt', 'w') as f:
        f.write(r.text)
else:
    print(f'Fetch failed with status: {r.status_code}')
    print(f'Message: {r.text}')
