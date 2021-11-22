# Portfolio

All code available [here](https://github.com/msa455/msa455.github.io)

## [Billboard Scraper](https://github.com/msa455/msa455.github.io/tree/master/billboardScraper)

In this project, my goal is to analyze how lyrical complexity has changed over the years in pop music. To do so, I scraped all of the billboard top hit songs from Billboard.com back to the 1960's. I then used that data to search genius.com for the lyrics of each song. In addition to downloading this information for further analysis, I used the readability package to get the following reading level assessments from each song's lyrics: Flesch Kincaid Grade Level, ARI, Coleman-Liau, FleschReadingEase, GunningFOG, LIX, SMOGindex, RIX and DaleChallIndex. Now that I have gotten all of that information, my next step is to make a dashboard using Dash for the user to interact with the data, and also for me to better analyze it myself to see any trends. 

## [Horoscope Generator](https://github.com/msa455/msa455.github.io/tree/master/horoscopeGenerator)

In this project, I scraped all of the horoscope information from horoscope.com, then used it to train a Markov Chain that then spat out randomly generated horoscopes of my very own. The output is still very rough and usually grammatically incorrect, but it is interesting just how effect Markov Chains are at replicating styles of writing. Despite the fact that they are still gibberish, they have the feeling of real horoscopes in diction. There is still some work to be done here and I would like to try some more techniques for training the models.

## [Restaurant Maintenance](https://github.com/msa455/msa455.github.io/tree/master/restaurantMaintenance)

In my freetime, I run a website called eatingthedungeon.com that focuses on analyzing food and culinary traditions in the table-top roleplaying game Dungeons and Dragons. In one such project that I am working on, I have developed a new ruleset to allow players to manage their own restaurant in a more hands on manner. When developing new rules for a game that is based on chance, the first critique someone will give you is about the balance of your proposals. So anytime I make new rulesets based on rolling dice, I like to run Monte Carlo simulations to help me test them. This project is an analysis of different rules I could propose for keeping track of restaurant income over a period of time, and how balanced each different approach would be for the players. 

## [Gibberish Generator](https://github.com/msa455/msa455.github.io/tree/master/gibberish)

Many of my projects are focused on D&D and other table top roleplaying games, as I enjoy developing tools for helping my own game management and to allow other players to use in their own games. This is one such project that while specifically made for Dungeons and Dragons, could be easily expanded out to other applications. Put simply, it is a generator of gibberish. It does not translate text into another language, it simply translates text into syllables that "sound" like they are from a different language. The way this is done is simple, first segment each word in a sentence into its constituent number of syllables, then move those over to a set of "foreign language sounding" syllables. The second step is simple, I just scraped a bunch of Elvish and Goblin words from different fantasy media and seperated them into syllables. The first step is more interesting however. How do you efficiently seperate a word into syllables?

Doing so by hand is pretty tricky due to the inconsistent nature of English. In this project, I used a pretty interesting quick and dirty method. Just translate whatever text you have to Japanese characters, specifically to Katakana, then count the number of characters. Turns out that Japanese translators such as ja2conv are pretty efficient and translating English into Japanese naturally segments it into syllables by the nature of how the language is pronounced. There are definitely better alternative out there, and I'm sure packages like Spacy have developed something, but its always fun to find interesting solutions.

## [LockChain](https://github.com/msa455/msa455.github.io/tree/master/LockChain)

This was my capstone project for my senior year of my undergraduate degree in Computer Science. My project was a revocable access system that was built on top of the blockchain. My application was coded in Solidity and ran locally using Ganache and Truffle. It focused on a simple yet scalable system for managing access permissions among an unknown number of total participants. Building it on top of the Blockchain allowed for the access tokens to be stored as non fungible objects which could easily be passed through accounts in a program agnostic manner. The future goal for this project was to publish it on the Ethereum blockchain as a Dapp that other software could interface with for managing user permissions in a public manner.

In addition to the project, I wrote a paper analyzing the use cases of Blockchains, and specifically where they shine, along with where they fall flat compared to traditional technologies. If I find some time, I would like to go back and extend this project as I do feel I would be able to do it more justice now with my improved programming skills.

## [Text Simplifier](https://github.com/msa455/msa455.github.io/tree/master/nlp)

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

## [Hackathon Site](https://github.com/msa455/msa455.github.io/tree/master/Hackathon%20Site)

As Director of Operations for HackShanghai, I was also in charge of creating the website we would use for info and registration. 
This was a basic project, using just simple HTML/CSS, and Javascript. The whole site was hosted on AWS with Heroku and we used 
Typeform for handling our registrations.



