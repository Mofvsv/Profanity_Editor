def read_text():
    quotes = open(r'C:\Users\TheHomie\Documents\Udacity\Github\Programming Foundations with Python\Profanity Editor\movie_quotes.txt')
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
read_text()
