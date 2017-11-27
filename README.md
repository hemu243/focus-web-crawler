# Focus Web Crawler
## Introduction
This project is about developing focus web crawler which classified web page related to new house development. In this web crawler to predict page relevance, it considers URL Word, URL Path, Anchor Tag, Parent Page, and soundaring text to predict page relevance and rank relevance document appropiately.

## Dependencies
Web crawler component depends on scrapy. Before running this project, install scrapy using following commands

To install Scrapy using conda, run:
```
conda install -c conda-forge scrapy
```

Alternatively, if you’re on Linux or Mac OSX, you can directly install scrapy by:
```
pip install scrapy
```

In case you see below error (openSSL version issue)
```  
File "/Library/Python/2.7/site-packages/twisted/internet/_sslverify.py", line 38, in <module>
    TLSVersion.TLSv1_1: SSL.OP_NO_TLSv1_1,
AttributeError: 'module' object has no attribute 'OP_NO_TLSv1_1'
```
then updating openSSL will fix this issue using this command 
```
sudo pip install --upgrade --ignore-installed pyopenssl
```

## Inputs
Seed Urls
Fetch all link by going through seed urls

## Features

## Usages
To run this program - 

