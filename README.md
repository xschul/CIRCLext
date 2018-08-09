# CIRCLext
[Thunderbird](https://www.mozilla.org/en-US/thunderbird/) extension to verify safety of emails using [PyCIRCLeanMail](https://github.com/CIRCL/PyCIRCLeanMail).

## Install

First clone this repository. Then:

### Install dependencies

```
pip3 install -r requirements.txt
```

### Install the extension
* Go to the Thunderbird extension folder
  + **Windows**:  `%APPDATA%\Thunderbird\Profiles\<Profile Name>\extensions\ `
  + **Linux**:  `~/.thunderbird/<Profile Name>/extensions/ `
  + **MAC**:  `~/Library/Thunderbird/Profiles/<Profile Name>/extensions/ `
* Create in this folder a new file named `circlext@xav.sch` that contains the path to the extension. Example: `/home/user/Desktop/CIRCLext/circlext@xav.sch`

### Run the server
Execute the `run_server.sh` script.

## Try the extension
* Open an email
* View the source of this email or **CTRL+U**
* Click on `CIRCL` then `Is the email safe ?`
