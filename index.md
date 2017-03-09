# Portfolio

All code available at (https://github.com/msa455/msa455.github.io)

## Text Simplifier

This was my final project for my Natural Language Processing class. Me and my partner created a program that allows you to translate a 
difficult piece of English text into a standardized “simplified” English. We initially had to decide what “simple” meant, and 
came across a set of words compiled by Charles K. Ogden, a linguist who proposed that all of the English language can be reduced to
these words. We then chose the Bible as our training set, as it was the largest prealigned set of text we could find. We utilized the 
IBM Alignment Model 2 for creating a model for translation between difficult and simple English.

As we were dealing with quite a bit of data, scoring each entry by hand would take too much time, so we developed a program to
compare the basic semantic similarity of two sentences. We used the gensim package to utilize word2vec in training a model for 
comparing this semantic similarity. We then used this to score our translation tool, under the assumption that a good translation
will have two sentences that mean the same thing regardless of the words used. 

Overall, we received good results, though in further examination these were skewed by the translation techniques of the IBM Models. 
As they opted for term for term substitutions, this artificially inflated the sentiment analysis score to be higher than even that 
of Ogden’s manual translation that utilized more paraphrasing than term for term substitutions. 

I would like to work on this project further in the future, utilizing different alignment techniques to get more accurate translations. 
Afterwards, I’d like to make a site to utilize this program to be able to simplify users’ queries in real time.

## Hackathon Site

As Director of Operations for HackShanghai, I was also in charge of creating the website we would use for info and registration. 
This was a basic project, using just simple HTML/CSS, and Javascript. The whole site was hosted on AWS with Heroku and we used 
Typeform for handling our registrations. 

##Jeopardy Analysis

I’ve always loved jeopardy, so obviously I’ve wanted to try out for the show, but how do you study for it? That’s what I asked
myself when I came across a massive dataset of previous Jeopardy questions. This was my first attempt at a project using some 
of the data analysis techniques I had learned while working on my startup Datastack. I’d say this is the most interesting one 
when it comes to results over processes. The actual development time mainly consisted of cleaning up and properly categorizing 
data, but realizing just how broad the categories and questions for jeopardy are was eye opening. This made actually compiling 
a proper list of topics to focus on for studying rather difficult. I’d like to go back with some of the Natural Language Processing 
skills I’ve learned to better categorize jeopardy’s many category names that are puns or play on words and see if I get a more 
conclusive answer.

## Twitter Crawler

Valentine’s day is a pretty polarizing time of year, eliciting reactions from excitement to depression. This seemed like 
perfect subject matter for some in depth analysis, so I went to crawling twitter, compiled a dataset of around 10,000 tweets,
and then did some simple term frequency testing. This is my favorite project since as I get better at different natural language 
processing techniques, there’s always a feature to add. I’m currently working on adding sentiment analysis so I can geotag 
different locations and see how users in that region generally felt about the event. There’s a lot to do before it's completely
done, but I enjoy having at least one or two impossible to complete projects. 

