import urllib

def read_text():
    quotes = open("C:\Users\shreya\Desktop\qyest. of html-css.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    #quotes is an object or instance of file
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    #urlopen helps open a connection to a website on the internet
    output=connection.read()
    print(output)
    connection.close() 

read_text() 
