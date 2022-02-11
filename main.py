import requests
import datetime
import argparse
from requests.structures import CaseInsensitiveDict

# apirequest v0.1
# 2022-02-10
# Author: Kmitzitz

now = datetime.datetime.now()
tStamp = now.strftime("%m/%d/%Y, %H:%M:%S")

def user(desc = "#"):
    if desc:
        i = input(desc, "\n# USER: ")
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
    elif u == "get":
        get()
    elif u == "post":
        post()
    else:
        menu()


def get():
    print(tStamp, "! ", messaging["GT_star"])
    user()
    resp = requests.get(i)
    print(tStamp, "! ", messaging["GT_rtrn"])
    print(resp)
    menu()


def fileloader():
    print(tStamp, "! ", messaging["FF_star"])
    try:
        f = open("body.json")
        return f
    except FileNotFoundError:
        print()
    try:
        f = open("body.xml")
        return f
    except FileNotFoundError:
        print(tStamp, "! ", messaging["FF_noEr"])



def post():
    url = user("Provide URL")
    if url == "":
        url = "https://reqbin.com/sample/post/json"
    else:
        enc = user("Body? (no/auto/xml/json)")
        if enc == "no":
            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/json"
            headers["Content-Length"] = "0"

            resp = requests.post(url, headers=headers)
        else:
            fileloader()

    print(resp.status_code)
    menu()


def cmds():
    print("\nversion v0.1, only get/post calls are supported as a PoC")
    print("request <url>    - API call with no authentication\n\n")
    menu()



messaging = {
    "MN_star" : "\napirequest v0.1, hello there!\n ",
    "MN_menu" : "Type 'help' for help",
    "GT_star" : "GET URL: ",
    "GT_rtrn" : "STATUS: ",
    "MN_reqt" : "Choose the type of request (POST/GET/DELETE):",
    "FF_star" : "Detecting request body",
    "FF_noJS" : "JSON not found",
    "FF_noXM" : "XML not found",
    "FF_noEr" : "No request body detected. Testing empty API call to https://reqbin.com/sample/post/json"
}


def main():
    print(tStamp, "! ", messaging["MN_star"])
    menu()



if __name__ == '__main__':
    main()
#    resp = requests.get('https://google.com/')
#    print(resp)