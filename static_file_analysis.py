from time import sleep
import requests
import json
import os


CRED_FILE = 'credentials.json'
ANALYZE_DIR = 'files_to_analyze'


def get_token(cred: str) -> str:
    '''
    Obtain an oauth token
    '''
    with open(cred, 'r') as content:
        x = json.loads(content.read())
        client_id = x['client-id']
        client_secret = x['client-secret']

    grant = {'grant_type': 'client_credentials'}
    token_resp = requests.post(
        'https://api.labs.sophos.com/oauth2/token',
        auth=(client_id, client_secret),
        data=grant
    )
    return token_resp.json()['access_token']


def analyze_file(some_token: str) -> list:
    '''
    Do a static analysis of files 
    '''
    l1 = []
    files_to_analyze = os.listdir(ANALYZE_DIR)
    for x in files_to_analyze:
        files = {'file': open(f'{ANALYZE_DIR}/{x}', 'rb')}
        static_file_resp = requests.post(
            'https://us.api.labs.sophos.com/analysis/file/static/v1',
            files=files,
            headers={'Authorization': some_token}
        )
        l1.append(static_file_resp.json())
    return l1   



def get_report(oauth_token: str, id: str) -> dict:
    '''
    Get analysis reports
    '''
    job = requests.get(
        f'https://us.api.labs.sophos.com/analysis/file/static/v1/reports/{id}?report_format=json',
        headers={'Authorization': oauth_token}
    )
    return job.json()


if __name__ == '__main__':
    token = get_token(CRED_FILE)
    report = analyze_file(token)

    for i in report:
        id = i['jobId']
        status = i['jobStatus']
        while status == 'IN_PROGRESS':
            print('STILL IN PROGRESS...')
            sleep(5)
            status = get_report(token, id)['jobStatus']

        print(get_report(token, id))