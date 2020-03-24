import requests


def main():
    resp=requests.get('https://google.com')
    #print("status code:",resp.status_code)      #for the status code
    #print("header code:",resp.headers['Content-Type'])  #header for all the attributes and this example is only for the specific field
    #print("content:",resp.content)
    #print("text:",resp.text)

if __name__=="__main__":
    main()


    
    
    
