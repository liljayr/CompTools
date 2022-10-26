from pickle import APPEND
import re
import pandas as pd
import numpy as np
import json
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager




def clean_books(words):
    # Remove all the special characters
    words = re.sub("\'", "", words)

    # remove all single characters
    words = re.sub("[^a-zA-Z]"," ",words)

    # Remove single characters from the start
    words = re.sub('\^[a-zA-Z]\s+', ' ', words) 
    
    # Substituting multiple spaces with single space
    words = re.sub('\s+', ' ', words, flags=re.I)
    
    # Converting to Lowercase
    words = words.lower()

    return words


def clean_ratings(ratings):
    ratings = re.sub("[^0-9]", "", "sdkjh987978asd098as0980a98sd")
    '987978098098098'
    return ratings 



