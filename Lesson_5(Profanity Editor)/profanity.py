import urllib.request
import urllib.parse
def read_text():
    contents = open(r"C:\Users\Piyush Goel\Downloads\Programming Foundations with Python\Lesson_5(Profanity Editor)\readmine.txt")
    output = contents.read()
    print(output)
    contents.close()
    check_curse(output)

def check_curse(text):
    url = urllib.parse.quote(text)
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+url)
    #connection = urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text=input")
    result = connection.read()
    out_str = result.decode("utf-8")
    print(out_str)
    connection.close()
    if 'true' in out_str:
        print("Careful!! Profanity Found")
    elif 'false' in out_str:
        print("You are good to go.")
    else :
        print("Process cannot be completed successfully! File not read properly.")

read_text()
