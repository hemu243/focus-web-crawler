# Focused Web Crawler For New House Development
This project is about developing focused web crawler which crawls new house development relevance page.

## Components 
There are two major components of this project -
- A classifier - which uses anchor text, page title head>title, and body>p data to classify relevance of the page. It provides score either 0 or 1. however it can be extended and improved to provide
score value between 0 to 1.
- Web crawler - priority based DFS crawling algorithm (also known as Best Fit Algorithm) which crawls more relevance of the links first then less relevance pages. It stops crawling page if relevance score goes to zero or lesser.

### Classifier
Lets talk about classifier first, there is abstract base class called WebClassifier (refer classifier.py file).
An inherit class needs to implement getClassifier and score function of this class to define your own classifier.
In this project, I had implemented naive bayes based classifier (refer naive_bayes_classifier.py file) which provide score 0 if page is not related to new house development and 1 if page is related to house development.
However you can extend base class and define your own classifier. Webcrawler components accepts instance of classifier.

**_Training data set for classifier_** -
since I could not find out training data set for classifier so I ended up creating my own training data set by using raw output of google search results and converting to metapy format.
For more information you are refer sample_data_generator folder. In this folder you will find the following sub folders -

dataset/raw/new_homes - raw google search result of new house data in json format and put into files. You can add more files in this folder and run sample_generation_script.py to generate new sample data for metapy.

dataset/raw/others - raw google search results of non new house data. You can add more files in this folder and later run sample_generation_script.py to generate new sample data for metapy.

After running sample_generation_script.py it will generate sample data under sample folder. Copy sample folder and dataset-full-corpus.txt and paste it at focus-web-crawler/dataset


### Web crawler
This component takes two inputs  seed urls and classifier instance which has to inherited from WebClassifier. Using seed urls
it started crawling and started extracting anchor text, page title (head > title html tag) and body data (body > p tags) from html pages, and
passes this information to score function of classifier instance. Score function returns double values between 0 to 1.
Using this score, it decides priority of crawling using formula (priority = int(score * 1000000)). Higher priority value implies of 
giving higher precedence to that url, and lower value belong to lower priority. If score reaches to zero then it stops crawling for that url.

# Project Dependencies
This projects uses some third party components, you have to install these components first to run this project

## Dependencies
* python 2.7.3 and above.
* scrapy 1.4.0
* metapy
* Beautiful Soup version 4

### Install scrapy
Web crawler component depends on scrapy. Before running this project, install scrapy using following commands

If conda is being install then use the following command to install scrapy using conda -
```
conda install -c conda-forge scrapy
```

Alternatively, if you’re on Linux or Mac OSX, you can directly install scrapy by:
```
pip install scrapy
```

In case you see below error (openSSL version issue) - which I had seen on my dev environment
```  
File "/Library/Python/2.7/site-packages/twisted/internet/_sslverify.py", line 38, in <module>
    TLSVersion.TLSv1_1: SSL.OP_NO_TLSv1_1,
AttributeError: 'module' object has no attribute 'OP_NO_TLSv1_1'
```
then updating openSSL will fix this issue using this command 
```
sudo pip install --upgrade --ignore-installed pyopenssl
```

### Install metapy
We are using metapy---Python bindings for MeTA. 

```bash
# Ensure your pip is up to date
pip install --upgrade pip
```

```bash
# install metapy!
pip install metapy pytoml
```

If you're on an EWS machine

```bash
module load python3
# install metapy on your local directory
pip install metapy pytoml --user
```


### Install Beautiful Soup
use below command to install beautiful soup
```bash
pip install beautifulsoup4
```

# How to run the project
There is run.py file which needs to be invoked by passing seed_urls (comma separated urls)

Go to folder focused-web-crawler then run the following command - (This project uses some relative
 path so make sure you run this script under focused-web-crawler folder)

```
python run.py seed_url1,seed_url2
```

For  example -
```
 python run.py http://newhomesource.com,https://news.ycombinator.com/
```

This command will generate output at two folders
* idx
* output - empty folder might have existed

**idx** folder is being created by metapy which hold forward and inverted index information to sample dataset. If you change either dataset or config.toml then delete this folder otherwise new indexes is not being created.

**output** folder holds output of scripts along with log file.
Script also print out url and its relevance score to console as well.

**output/newhouse_output_all** - hold all crawled urls with their relevance score.

**output/newhouse_output_positive_score.txt** - hold crawled urls where relevance score greater than zero. Since naive bayes classifier either provide score 0 or 1. So you will see all scores to 1 only in this file.

**output/log** -> contains log file.

## How to stop crawling
This project will keep crawling until resources is exhausted or no more relevant url to crawl. If you want to stop it then press [ctrl^c], this command will given signal to crawler to stop. crawler graceful stops in few seconds.
If you want to stop crawling immediately then press [ctrl^c] which unsafely stop crawler immediately.

# Future work
## Evaluation of classifier
We can extend project and add evaluation of results of classifier
## Refine training data set
Since this is manual defined training set, it has lot of scope to improve.
## Improve classifier
We can improve classifier and output score between 0 and 1 instead of only 0 or 1
## Add ranking algorithm
We can add page ranking algorithm to improve output result
## Persistence state of crawler
Right now, crawler does not support persisted state between two runs. You can extend this project by implementing persistence state of crawler so it can resume the work from previous state.
