# Sophos Intelix

Uses Intelix to analyze files and links for malicious content.

## Prerequistes

- AWS account
- Subscribe to Sophos Intelix in [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-k4jb2agd65ses)

## Setup

Obtain a Intelix credentials json file and place it in the project's root directory.

## Static File Analysis

- Put files to analyze in `files_to_analyze` folder
- Execute static_file_analysis.py script

```
python3 static_file_analysis.py
```

### TODO

- Setup dynamic file analysis
- Setup URL checker
- Create a commandline tool
