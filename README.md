# twitter_crawler
-----------

### About this proejct
a crawler to crawl twitter

### Setup
First, download the source code
```
$ git clone https://github.com/yuting-tseng/twitter_crawler.git
$ cd twitter_crawler/
```
Launch python virtual environment
```
$ virtualenv --no-site-packages --python /usr/bin/python3 .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```
### Usage
```
$ python run.py <HashTag> <OutputDirectory>
```
For example,
```
$ python run.py dating output/
```
