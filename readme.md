# This script takes a png and turns it into a *.icns file

<img src="https://github.com/madeinouweland/create-macos-icns/blob/master/logo.png" width="200px"/>

This script:

- loads icon.png
- creates icons icon_64x64.png, ..., icon_1024x1024.png
- uses the macOS iconutil command to create the iconset

## Install

- Download the repo
- Open a terminal and go to the project folder
- Type:

```
python3 -m venv env
source env/bin/activate
pip install -r requirements
```

## Usage

```
python3 create.py
```
