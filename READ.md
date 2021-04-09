# Movie Recommender System
> A simple Movie Recommender using Python and GUI using Tkinter.
> In this project I used Weighted Average and Content Based Recommendation. The Formula for Weighted Average is given by:
![](/formula.png)

## Table of Content
* [Installation](#Installation)
* [Data](#Data)
* [Usage](#Usage)

### Installation
**Downlaod the Repo**
Clone the base repo onto your desktop with `git` as follows:
```console
$ git clone https://github.com/shinigamiloveapple/Movie_Recommendation_System.git
```
### Data
The Data used here is **5000 TMBD Dataset** This dataset have movies from different websites with rating given by users after watching the movie.
The Dataset contains two files;
* The ***tmdb_5000_credits.csv***:
    * It contains *movie_id*,*title*,*cast*,*crew*.
* The ***tmdb_5000_movies.csv***:
    * It contains *budget*, *genres*, *homepage*, *id*, *keywords*, *original_language*, *original_title*, *overview*, *popularity*, *production_companies*,  *production_countries*, *release_date*, *revenue*, *runtime*,*spoken_languages*, *status*, *tagline*, *title*, *vote_average*, *vote_count*

### Usage
Install python dependencies via command:
```console
$ pip install -r requirements.txt
```
To launch the GUI, Launch it as follows:
```console
$ python gui.py
```
