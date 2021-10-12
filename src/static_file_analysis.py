from time import sleep
from token import get_token
import requests
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(asctime)s %(message)s'
)

ANALYZE_DIR = '../files_to_analyze'

def analyze_file(some_token: str) -> list:
    '''
    Does a static analysis of files 
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
    Gets analysis reports

    Change the format of reports by changing the query string
    report formats: json, html, text
    '''
    job = requests.get(
        f'https://us.api.labs.sophos.com/analysis/file/static/v1/reports/{id}?report_format=json',
        headers={'Authorization': oauth_token}
    )
    return job.json()


if __name__ == '__main__':
    token = get_token()
    report = analyze_file(token)

    for i in report:
        try:
            status = i['jobStatus']
            id = i['jobId']
            logging.info(f'STATUS: {status}')
            logging.info(f'ID: {id}')

            while status == 'IN_PROGRESS':
                logging.info('STILL IN PROGRESS...')
                sleep(5)
                status = get_report(token, id)['jobStatus']

            print(f'\n{get_report(token, id)}')
        except Exception as e:
            pass
