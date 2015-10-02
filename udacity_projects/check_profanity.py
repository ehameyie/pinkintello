import urllib

def read_text():
    quotes = open("/Users/xxx/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    # contents_filtered = filter(lambda x: x == "believe", contents_of_file)
    # print(contents_filtered)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+ text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document is clean, girl!!")
    else:
        print("Could not scan document, sorry girlie!")
    
read_text()
