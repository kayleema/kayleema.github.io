import sys

import requests

api_token = sys.argv[-1]
api_url_assignments = "https://api.wanikani.com/v2/assignments"
api_url_subjects = "https://api.wanikani.com/v2/subjects"

wanikani_headers = {
    "Wanikani-Revision": "20170710",
    "Authorization": "Bearer " + api_token
}


def get_all_burned_kanji_assignments():
    response = requests.get(
        api_url_assignments + "?subject_types=kanji&burned=true",
        headers=wanikani_headers
    )
    data = response.json()['data']

    while response.json()['pages']['next_url']:
        print('.', end="", flush=True)
        response = requests.get(
            response.json()['pages']['next_url'],
            headers=wanikani_headers
        )
        data += response.json()['data']
    print()

    sorted_data = sorted(data, key=lambda item: item['data']['burned_at'])
    return sorted_data


def get_all_kanji_subjects():
    response = requests.get(
        api_url_subjects + "?types=kanji",
        headers=wanikani_headers
    )
    data = response.json()['data']

    while response.json()['pages']['next_url']:
        print('.', end="", flush=True)
        response = requests.get(
            response.json()['pages']['next_url'],
            headers=wanikani_headers
        )
        data += response.json()['data']
    print()

    return data


def print_kanji_by_burned(subjects, assignments):
    for assignment in assignments:
        subject = next(s for s in subjects if s['id'] == assignment['data']['subject_id'])
        print(assignment['data']['burned_at'], subject['data']['characters'])


subjects = get_all_kanji_subjects()
assignments = get_all_burned_kanji_assignments()

print(len(subjects), 'subjects and', len(assignments), 'burned assignments')

print_kanji_by_burned(subjects, assignments)

print(len(subjects) - len(assignments), 'remaining')

for subject in subjects:
    try:
        assignment = next(a for a in assignments if subject['id'] == a['data']['subject_id'])
    except StopIteration:
        print(
            subject['data']['characters'],
            end="", flush=True
        )
print()
