# TwitterProject
> #### Project Description?
> #### How to use it?
> #### Attention Problem?

## OverView
### 1.Project Description?
This **TwitterProject** includes two projects,one is **twitterCrawl** and the other is **twitterShow**. TwitterCrawl mainly crawls data, and twittershow mainly shows data. The static data such as image, video which by crawling save in the directory of ./twitter/twitterShow/static/.Specific information under the **Attention Problem** topic.

# Requirement

> + Python 3.X
> + Django 2.X
> + Mysql 5.x

### 2.How to use it?
clone project :
     
     $ git clone git@gitlab.com:availinkAI/twitter.git

twitterCrawl project Install dependency:


    $ cd ./twitter/twitterCrawl
    $ pip install -r requirements.txt

twitterShow project Install dependency:

    $ cd ./twitter/twitterShow
    $ pip install -r requirements.txt

Build database in the twitterShow directory(make sure you have installed  Mysql)

    $ python manage.py migrate
    $ python manage.py makemigrations

*If you enter mysql database, you can see some tables have been created.Basically, the account table  and the tweet table is the model which created manually.*

Crawl Data:

    $ python ./twitter/twitterCrawl/timedTask.py

*If you enter mysql database, you can see some data.*
***

### 3.Attention Problem

 1.  about timedTask.py and /twitterCrawl/main.py

> If use **python main.py** can also start crawler, but just one time.The file timedTask.py is a timed task, which starts every three hours. So, you shoud use **python timedTask.py**.


 2. create twitter developer app.


> You must has an application, then you can have access to use **Twitter API**.
Visit: **[Twitter Developer Website](https://developer.twitter.com/en.html)***


 3. about twitterAPI

>The length of some tweets is cut off due to the limitation of twitterAPI, but I attach a link. If you can visit twitter, you will visit the details by clicking it. 

### 4.Others

Contact information:https://github.com/west789