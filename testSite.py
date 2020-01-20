import requests
import PySimpleGUI as sg


def test_ssl(url):
    try:
        r = requests.get(url).content
        return True
    except requests.exceptions.SSLError:
        return False



url_list = [x.strip() for x in open("URLS to Test.txt") if len(x.strip()) > 0]
print(url_list)
failed_list = [y for y in url_list if not test_ssl(y)]
if len(failed_list) > 0:
    fail_text = "These links have bad ssl certificates\n\n" + "\n".join(failed_list)
    if len(failed_list) > 1:
        sg.popup_ok(fail_text, title="YOU HAVE FAILURES")
    else:
        sg.popup_ok(fail_text, title="YOU HAVE A FAILURE")

