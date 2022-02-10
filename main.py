import requests
import datetime
import argparse

# apirequest v0.1
# 2022-02-10
# Author: Kmitzitz

now = datetime.datetime.now()
tStamp = now.strftime("%m/%d/%Y, %H:%M:%S")

def user(desc = ""):
    if desc:
        i = input("# USER (", desc, "):")
    else:
        i = input('# USER: ')
    if i == "":
        user()
    else:
        return i


def menu():
    print(tStamp, "! ", messaging["MN_menu"])
    u = user()
    if u == "help":
        cmds()
    else:
        menu()


def get():
    print(tStamp, "! ", messaging["GT_star"])
    i = input("! User: ")
    resp = requests.get(i)
    print(tStamp, "! ", messaging["GT_rtrn"])
    print(resp)
    menu()


def fileloader():
    print(tStamp, "! ", messaging["FF_star"])
    try:
        f = open("body.json")
    except FileNotFoundError:
        print(tStamp, "! ", messaging["FF_noJS"])
        
    try:
        f = open("body.xml")
    except FileNotFoundError:
        print(tStamp, "! ", messaging["FF_noEr"])


def cmds():
    print("\nversion v0.1, only get call is supported as a PoC")
    print("request <url>    - API call with no authentication\n\n")
    menu()



messaging = {
    "MN_star" : "\napirequest v0.1, hello there!\n ",
    "MN_menu" : "Type 'help' for help",
    "MN_reqt" : "Choose the type of request (POST/GET/DELETE):",
    "GT_star" : "GET URL: ",
    "GT_rtrn" : "STATUS: ",
    "FF_star" : "Detecting request body",
    "FF_noJS" : "JSON not found",
    "FF_noXM" : "XML not found",
    "FF_noEr" : "No request body detected. Provide body.json or body.xml file to directory"
}


def main():
    print(tStamp, "! ", messaging["MN_star"])
    menu()



if __name__ == '__main__':
    main()
#    resp = requests.get('https://google.com/')
#    print(resp)