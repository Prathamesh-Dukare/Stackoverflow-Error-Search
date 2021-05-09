from subprocess import Popen,PIPE
import requests
import webbrowser

def err_search():
    def err_scrap(cmd):
        args=cmd.split()
        proc=Popen(args ,stdout=PIPE, stderr=PIPE)
        out,err=proc.communicate()
        return out,err
    errors=err_scrap('python main.py')

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