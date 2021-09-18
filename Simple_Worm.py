import requests as r
import time as t

from requests.models import Response
flag = 0

def get(url,name):
    global flag,temp
    try:
        temp = r.get(url)
        temp.raise_for_status()
        wri(name)
    except:
        if flag < 5:
            flag += 1
            print(f"Fail! {flag} -times")
            print("Retrying!")
            t.sleep(1)
            get(url,name)
        else:
            print("We are in trouble!Please try again!")
        
def wri(name):
    global temp
    try:
        with open(name,"wb") as r:
            r.write(temp._content)
        print("Success!")
    except:
        print("An error occured when trying to create a document!")
    
if __name__ == "__main__":
    while True:
        flag = 0
        url = input("Your url:")
        name = input("File name:")
        get(url,name)
