# Focused Web Crawler For New House Development
This project is about developing focused web crawler which crawls pages related to new house developments.

## Components 
There are two major components of this project -
- A classifier - which uses anchor text, page title head>title, and body>p data to classify relevance of the page. It provides score either 0 or 1. however it can be extended and improved to provide
score value between 0 to 1.
- Web crawler - Priority based DFS algorithm which crawls more relevance of the links first then less relevance pages. It also stops crawling if relevance of page goes to zero or lesser.

### Classifier
Lets talk about classifier first, there is abstract base class called WebClassifier (refer classifier.py file).
An inherit class needs to implement getClassifier and score function of this base class to define your own classifier.
For this project, I had implemented naive bayes based classifier (refer naive_bayes_classifier.py file) which provide score 0 if page is not relevance and 1 if page is related to house development.
But are feel free to define your own classifier and sample training data.

### Training data set for classifier
On side note - Since I could not find out training dataset for classifier so I ended up creating my own training data set by using raw output of google search results and converting to metapy format
you are refer sample_data_generator folder.

dataset/raw/new_homes - google search result of new house data in json format and put into files. You can add more files in this folder and later run sample_generation_script.py

dataset/raw/others - google search results of non new house data. Same thing applied here

After running sample_generation_script.py it will generate sample data under sample. Copy sample folder and dataset-full-corpus.txt and place it under focus-web-crawler/dataset


### Web crawler
This components takes inputs of seeds urls and classifier instance which inherited class WebClassifier. Using seed urls
it started crawling and started extracting anchor text, page title (head > title html tag) and body data (body > p tags)
pass this information to score function of classifier instance. Score function returns double values between 0 to 1.
Using this score, it decides priority of crawling using formula (priority = int(score * 1000000)). Higher priority value implies of 
giving higher precedence to that url, and lower value belong to lower priority. If score reaches to zero then it stop crawling that url

# Installation of Dependencies
This projects uses some third party components, you have to install these components first to run this project

## Dependencies
python 2.7.3 and above
scrapy 1.4.0
metapy
Beautiful Soup version 4

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

Go to folder focused-web-crawler then run the following command - (Due to lack of time this project uses some relative
 path so make sure you run this script under focused-web-crawler folder)

```
python run.py seed_url1,seed_url2
```

For  example -
```
 python run.py http://newhomesource.com,https://stackoverflow.com
```
This command will generate create two folder idx, output. Idx folder is being created by metapy which hold forward and
inverted index information to sample dataset. At same time output folder holds output of scripts along with log file.
At same time script also print url and its relevance score.

**output/newhouse_output_all** - hold all crawled url with their score.

**output/newhouse_output_positive_score.txt** - hold all crawled url and score which score greater than zero. Since naive bayes classifier either gives score 0 or 1. So you would see score 1 in this file

**output/log** -> contains log file.

**idx** -> It is generated by metapy. It holds forward and inverted index files. If user changes either dataset or config.toml then delete this folder otherwise new index is not being created

# How to stop crawling
This project will keep crawling until resources is exhausted or no more relevant url to crawl. If you want to stop it
then press [ctrl^c], this will given signal to crawler to stop. Since it does graceful stop and lot of process are running asynchronously so it will stop it after few seconds. However if you want to
force stop then press [ctrl^c] one more time.
In short -
Pressing  [ctrl^c] one time is safe shutdown. It may takes few seconds
Pressing twice [ctrl^c] is force shutdown. It will stop right away but it's unsafe stop

# Future work
## Evaluation of classifier
We can extend project and add evaluation of results of classifier
## Training dataset
Since this is manual defined training set, it has lot of score to improve
## Implement better classifier
We can improve classifier and output score between 0 and 1 instead of only 0 or 1
## Add ranking algorithm
We can add ranking algorithm to improve output result
