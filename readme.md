# Sophos Intelix Cli

Uses Intelix to analyze files and links for malicious content.

*Supported OS:*
- MacOS
- Linux

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

**Installing and uninstalling CLI Tool**

Use the `make` command to install and uninstall.

INSTALL:

```
make install
```

UNINSTALL

```
make uninstall
```

Place the Intelix credentials.json file in your home directory within `.intelix` folder.

`/home/username/.intelix/credentials.json`

**COMMANDS**

- intelix-static

Example Intelix static file analysis

```
intelix-static -f <filename>
```

- intelix-dynamic

```
intelix-dynamic -f <filename>
```

### TODO

- Setup URL checker
