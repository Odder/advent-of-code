import requests
import argparse

session_token="53616c7465645f5fa65a73eade735b3db23a5d012394031004257cddbe4559ef0a1df21ae2558ca7907770c9f9664d4ec052f938f589244d852b98fea12b0d6b"
cookies = {
    'session': session_token
}


def endpoint(day, year=2023):
    return 'https://adventofcode.com/{year}/day/{day}'


def get_input(day, year=2023):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    print(url)
    response = requests.get(url, cookies=cookies)

    if response.status_code != 200:
        print('Failed to fetch input')
        print(response)

    with open(f'{year}/{day:0>2}/input', 'w') as f:
        f.write(response.text)


def generate_file(day, year=2023):
    with open(f'{year}/template.py', 'r') as temp:
        with open(f'{year}/{day:0>2}/solve.py', 'w') as f:
            for line in temp.read():
                f.write(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download Advent of Code input for a specific day and year.')
    parser.add_argument('day', type=int, help='The day of the event.')
    args = parser.parse_args()
    get_input(args.day, 2021)
    generate_file(args.day, 2021)
