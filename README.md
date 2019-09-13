# NearestSentence
The goal is to find the two nearest sentences (in a meaning/semantic way) in the articles on the same topic.

# How does it work ?
## Install
First of all, install NLTK 3.0, downloadable for free from at https://www.nltk.org/install.html.
Follow the instructions there to download the version required for your platform.

Then clone the project

```{}
git clone  https://github.com/leirbag95/NearestSentence.git
```
## Find articles
Go on Google News and select 2 press articles (2 about the same topic).
Copy/paste the text content of each article in 2 separate files.

## Run it
For running the project copy/paste the follow command line
```{}
python3 wp1.py your_article1.txt your_article2.txt
```
[Debug mode]

```{}
python3 wp1.py your_article1.txt your_article2.txt -
```


## Result

For this example I selected 2 topics about the new iPhone (11 / 11 Pro)




## Zipf's law

Verify if your 3 articles respect the Zipf’s law with showZipfSLow function

![Screenshot from 2019-09-13 13-46-08](https://user-images.githubusercontent.com/17054452/64860255-e9bea000-d62c-11e9-8c9c-d74599f3529a.png)



