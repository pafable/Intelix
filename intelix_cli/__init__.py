import argparse
import requests
import json
import os

'''
Commands used by all of the scripts
'''
parser = argparse.ArgumentParser(description='Intelix CLI Commands')
parser.add_argument('-f', '--file', type=str, help='scans file')
parser.add_argument('-d', '--dir', type=str, help='scans directory | EXPERIMENTAL')
args = parser.parse_args()

CRED_FILE = f"{os.path.expanduser('~')}/.intelix/credentials.json"

def get_token() -> str:
    '''
    Obtain an oauth token
    '''
    with open(CRED_FILE, "r") as content:
        x = json.loads(content.read())
        client_id = x["client-id"]
        client_secret = x["client-secret"]

    token_resp = requests.post(
        "https://api.labs.sophos.com/oauth2/token",
        auth=(client_id, client_secret),
        data={"grant_type": "client_credentials"}
    )
    return token_resp.json()["access_token"]


if __name__ == "__main__":
    try:
        print(get_token())
    except Exception as e:
        print(e)