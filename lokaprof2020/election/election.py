from typing import List

def convert_to_int(votes_str: str):
    try:
        return int(votes_str)
    except ValueError:
        return None

def get_validated_voting(voting_str: str):
    voting = voting_str.split()
    if len(voting) == 2:
        candidate, votes = voting
        return candidate, convert_to_int(votes)
    else:
        return None, None

def get_voting():
    return input('Candidate and votes: ')

def add_voting_to_dict(voting_dict: dict, candidate, votes):
    candidate = candidate.lower()
    if candidate in voting_dict:
        voting_dict[candidate] += votes
    else:
        voting_dict[candidate] = votes

def get_voting_dict():
    voting_dict = {}
    voting = get_voting()
    while voting:
        candidate, votes = get_validated_voting(voting)
        if votes:
            add_voting_to_dict(voting_dict, candidate, votes)
        else:
            print('Invalid no. of votes!')
        voting = get_voting()
    return voting_dict


def display_voting_dict(voting_dict):
    for key, value in sorted(voting_dict.items()):
        print(f'{key}: {value}')

def get_total_votes(voting_dict: dict):
    return sum(voting_dict.values())

def main():
    voting_dict = get_voting_dict()
    display_voting_dict(voting_dict)
    total_votes = get_total_votes(voting_dict)
    print(f'Total no. of votes: {total_votes}')

if __name__ == '__main__':
    main()