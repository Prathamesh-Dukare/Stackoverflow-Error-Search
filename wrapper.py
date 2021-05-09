from subprocess import Popen,PIPE
import requests
import webbrowser

def err_search():
    def err_scrap(cmd):
        args=cmd.split()
        proc=Popen(args ,stdout=PIPE, stderr=PIPE)
        out,err=proc.communicate()
        return out,err
    errors=err_scrap('python testfile.py')

    if(errors[1].decode()):
        print('Error is Occured : Searching for details...')
        err_str=errors[1].decode()
        possible_errs=['SyntaxError:','IndexError','AssertionError','AttributeError','ImportError','KeyError','NameError','MemoryError','TypeError']
        for i in possible_errs:
            if(i in err_str):
                index=err_str.find(i)
                err_msg=err_str[index:-1]
                print(err_msg)
                return err_msg
    else:
        print("No Error Occured :-)")

def apicall(err_msg):
    if(err_msg):
        api=f"https://api.stackexchange.com/2.2/search?fromdate=1556668800&order=desc&sort=activity&tagged=python&intitle={err_msg}&site=stackoverflow"
        responce=requests.get(api)
        data=responce.json()
        linklist=[]
        for item in data["items"]:
            if(("is_answered",True) in item.items()):
                if(len(linklist)<5):
                    linklist.append(item["link"])
    
        def open_links(linklist):
            print('Opening relevent threads on stackoverflow...')
            for link in linklist:
                webbrowser.open(link,new=2)
        open_links(linklist)

if __name__ == "__main__":
    apicall(err_search())