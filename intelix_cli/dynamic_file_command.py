from time import sleep
import intelix_cli
import requests
import sys


def analyze_file(some_token: str, sus: str) -> list:
    '''
    Does a dynamic analysis of files 
    '''
    files = {"file": open(f'{sus}', "rb")}
    dynamic_file_resp = requests.post(
        'https://us.api.labs.sophos.com/analysis/file/dynamic/v1/',
        files=files,
        headers={"Authorization": some_token}
    )
    return dynamic_file_resp.json()


def get_report(oauth_token: str, id: str) -> dict:
    '''
    Gets analysis reports

    Change the format of reports by changing the query string
    report formats: json, html, text
    '''
    job = requests.get(
        f"https://us.api.labs.sophos.com/analysis/file/dynamic/v1/reports/{id}?report_format=json",
        headers={"Authorization": oauth_token}
    )
    return job.json()


def main():
    parser = intelix_cli.parser
    token = intelix_cli.get_token()
    inputs = intelix_cli.args.__dict__

    if inputs["file"] == None and inputs["dir"] == None:
        parser.print_help()
        sys.exit(1)
    
    report = analyze_file(token, inputs["file"])
    try:
        status = report["jobStatus"]
        id = report["jobId"]
        while status == "IN_PROGRESS":
            sleep(3)
            status = get_report(token, id)["jobStatus"]
        print(get_report(token, id))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()