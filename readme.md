# Sophos Intelix

Uses Intelix to analyze files and links for malicious content.

## Prerequistes

- Python3 (Tested on python 3.7.9)
- AWS account
- Subscribe to Sophos Intelix in [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-k4jb2agd65ses)

## Setup

Obtain an Intelix credentials json file and place it in the project's root directory.

## Static File Analysis

- Put files to analyze in `files_to_analyze` folder
- Execute static_file_analysis.py script in the `src` folder

```
python3 static_file_analysis.py
```

## Commandline

Place the Intelix credentials.json file in your home directory within an `.intelix` folder. 

`/home/username/.intelix/credentials.json`

__COMMANDS__
- intelix-static

Example Intelix Static File Analysis
```
intelix-static -f <filename>

```
### TODO

- Setup dynamic file analysis
- Setup URL checker
- Create a commandline tool
