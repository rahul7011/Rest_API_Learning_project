import requests


def main():
    #resp=requests.get('https://api.exchangeratesapi.io/latest?base=USD&symbols=INR')
    parameters={
        "base":"USD",
        "symbols":"INR"
    }
    resp=requests.get('https://api.exchangeratesapi.io/latest',params=parameters)
    if resp.status_code!=200:

        print("status code:",resp.status_code)      #for the status code
        raise Exception("Something went wrong")
        #print("header code:",resp.headers['Content-Type'])  #header for all the attributes and this example is only for the specific field
        #print("content:",resp.content)
        #print("text:",resp.text)
    data=resp.json()
    print("data:",data)

if __name__=="__main__":
    main()


    
    
    
