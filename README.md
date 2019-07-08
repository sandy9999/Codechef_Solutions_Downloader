# Codechef Solutions Downloader

 Codechef Solutions Downloader is a script to download your Codechef solutions locally on your PC.
 
### Requirements
Platform: Linux

Python version >=3.6.5

Please ensure that you are logged out from Codechef and have 0 existing sessions before running this script.

### Installation

Build from Source:
```sh
$ git clone https://github.com/sandy9999/Codechef_Solutions_Downloader
$ cd Codechef_Solutions_Downloader
$ pip install -r requirements.txt
$ cp conf_example.py conf.py
```
Edit conf.py with your credentials.

To run:
```sh
$ python3 codechef.py
```

Note: Only your latest submission is downloaded for every completely and partially solved problem.
