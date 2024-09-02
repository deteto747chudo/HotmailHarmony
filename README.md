# 🧨HotmailHarmony🧨

## Introduction
HotmailHarmony is a Python-based project designed for managing console-based operations with utilities for Hotmail Account Proxyless Checker , Proxy Scraper , Proxy Checker and more. 

## Table of Contents
- [Installation](#installation)
- [Dependencies](#dependencies)
- [For Developers](#developers)
- [Project Structure Explained](#project-structure)

## Installation

To install the necessary dependencies, ensure you have Python installed and run:

```bash
pip install -r requirements.txt
```
To start the program execute:
```bash
python3 main.py  
```

## Dependencies

```bash
.
└── ./HotmailHarmony/
    ├── ./HotmailHarmony/engine/
    │   └── ./HotmailHarmony/engine/ProxyToolEngine/
    │       ├── ./HotmailHarmony/engine/ProxyToolEngine/retrieve_proxy_output.py
    │       ├── ./HotmailHarmony/engine/ProxyToolEngine/run_proxy_checker.py
    │       ├── ./HotmailHarmony/engine/ProxyToolEngine/run_proxy_scraper.py
    │       └── ./HotmailHarmony/engine/ProxyToolEngine/save_proxy_output.py
    ├── ./HotmailHarmony/init/
    │   ├── ./HotmailHarmony/init/output/
    │   │   ├── ./HotmailHarmony/init/output/dead.txt
    │   │   └── ./HotmailHarmony/init/output/live.txt
    │   ├── ./HotmailHarmony/init/retrieve/
    │   │   ├── ./HotmailHarmony/init/retrieve/deadretrieve.py
    │   │   └── ./HotmailHarmony/init/retrieve/liveretrieve.py
    │   ├── ./HotmailHarmony/init/save_output/
    │   │   └── ./HotmailHarmony/init/save_output/save_output.py
    │   └── ./HotmailHarmony/init/hotmail_selection.py
    ├── ./HotmailHarmony/initv2/
    │   └── ./HotmailHarmony/initv2/proxy_selector.py
    ├── ./HotmailHarmony/modules/
    │   ├── ./HotmailHarmony/modules/module_hotmailchecker/
    │   │   ├── ./HotmailHarmony/modules/module_hotmailchecker/dead.txt
    │   │   ├── ./HotmailHarmony/modules/module_hotmailchecker/emails.txt
    │   │   ├── ./HotmailHarmony/modules/module_hotmailchecker/live.txt
    │   │   └── ./HotmailHarmony/modules/module_hotmailchecker/main.py
    │   ├── ./HotmailHarmony/modules/module_proxytool
    │   ├── ./HotmailHarmony/modules/.flake8
    │   ├── ./HotmailHarmony/modules/proxyChecker.py
    │   ├── ./HotmailHarmony/modules/proxyScraper.py
    │   └── ./HotmailHarmony/modules/user_agents.txt
    ├── ./HotmailHarmony/output/
    │   ├── ./HotmailHarmony/output/dead.txt
    │   ├── ./HotmailHarmony/output/live.txt
    │   └── ./HotmailHarmony/output/proxies.txt
    ├── ./HotmailHarmony/main.py
    ├── ./HotmailHarmony/requirements.txt
    └── ./HotmailHarmony/dev_requirements.txt
```

## Developers

If you are advanced developer you can use:
```bash
pip install dev_requirements.txt
```
It will give you access to all the dependencies you need if you want to modify the program!

Also you can use proxyChecker.py & proxyScraper.py from path : modules/module_proxytool/proxyChecker.py/proxyScraper.py without the program interface with added options like :

#### For Scraping Proxies:

```bash
proxy_scraper -p http
```

- With `-p` or `--proxy`, you can choose your proxy type. Supported proxy types are: **HTTP - HTTPS - Socks (Both 4 and 5) - Socks4 - Socks5**.
- With `-o` or `--output`, specify the output file name where the proxies will be saved. (Default is **output.txt**).
- With `-v` or `--verbose`, increase output verbosity.
- With `-h` or `--help`, show the help message.

#### For Checking Proxies:

```bash
proxy_checker -p http -t 20 -s https://google.com -l output.txt
```

- With `-t` or `--timeout`, set the timeout in seconds after which the proxy is considered dead. (Default is **20**).
- With `-p` or `--proxy`, check HTTPS, HTTP, SOCKS4, or SOCKS5 proxies. (Default is **HTTP**).
- With `-l` or `--list`, specify the path to your proxy list file. (Default is **output.txt**).
- With `-s` or `--site`, check proxies against a specific website like google.com. (Default is **https://google.com**).
- With `-r` or `--random_agent`, use a random user agent per proxy.
- With `-v` or `--verbose`, increase output verbosity.
- With `-h` or `--help`, show the help message.

### Running Directly from Source

If you prefer running the scripts directly from the source code, you can use the following commands:

#### For Scraping:

```bash
python3 proxyScraper.py -p http
```

#### For Checking:

```bash
python3 proxyChecker.py -p http -t 20 -s https://google.com -l output.txt
```


## Project Structure

#### HotmailHarmony > engine > ProxyToolEngine
```bash
    retrieve_proxy_output.py - Retrieve proxy data in CMD terminal
    run_proxy_checker.py - The Engine for running proxyChecker.py
    run_proxy_scraper.py - The Engine for running proxyScraper.py 
    save_proxy_output.py - Save the proxy output to output folder
```
#### HotmailHarmony > init > output
```bash
    dead.txt - Store dead hotmail account till the next instance
    live.txt - Store live hotmail account till the next instance
```
#### HotmailHarmony > init > retrieve
```bash
    deadretrieve.py - Retrieve data for the dead hotmail accounts to save_output.py
    liveretrieve.py - Retrieve data for the live hotmail accounts to save_output.py
```
#### HotmailHarmony > init > save_output
```bash
    save_output.py - saves the output in temp output folder
```
#### HotmailHarmony > init
```bash
    hotmail_selector.py - The CMD terminal menu for hotmail accounts
```

#### HotmailHarmony > initv2
```bash
    proxy_selectr.py - The CMD terminal menu for proxy tool
```

#### HotmailHarmony > modules > module_hotmailchecker
```bash
    dead.txt - temp txt for dead proxies
    live.txt - temp txt for live proxies
    emails.txt - user need to put hotmail emails here
    main.py - hotmail checker smtp
```
#### HotmailHarmony > modules > module_proxytool
```bash
    .flake8 - package for proxyScraper.py , proxyChecker.py
    proxyChecker.py - check proxies from output.txt ( before saving to the folder )
    proxyScraper.py - scrape prohies from different websites
    user_agents.txt - user agents for firefox
```

#### HotmailHarmony > output
```bash
    dead.txt - permament txt for dead hotmail accounts
    live.txt - premament txt for live hotmail accounts
    output.txt - permament txt for valid proxies
```

#### HotmailHarmony
```bash
    dev_requirements.txt - developer packages
    requirements.txt - user packages to make the program work
    main.py - entry program point , main file
```

# All credits goes to deteto_chudo for creating this program! The program is open-source and can be modified and used , but giving credit will help me create more programs like this!