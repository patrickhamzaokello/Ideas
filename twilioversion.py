import sys
import urllib.request
import urllib.parse
import re
from urllib.request import urlopen as ureqs
from bs4 import BeautifulSoup as soup
from googleapiclient.discovery import build

from twilio.rest import Client




query = input("enter the query\n")
print("1) Google Search Results\n")
print("2) Youtube Links\n")
choice=input("Enter The choice\n")

if choice == "1":
    my_api_key = "AIzaSyDF7QebgYORST0NLYY165UR9F9CM9ZrX98"
    my_cse_id = "009133144284874463065:zw_ftho5-u8"
    
    def google_search(search_term, api_key, cse_id, **kwargs):
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
        return res

    results = google_search(query, my_api_key, my_cse_id)

    print("\n*********Google Search Results*********\n")
    i = 0
    while i < 6:
        print("Title == " +results['items'][i]['title'])
        print("Link ==" +results['items'][i]['link'])
        snippet=results['items'][i]['snippet'].replace('\n',"")
        html_snippet=results['items'][i]['htmlSnippet'].replace('\n',"")
        html_snippet= html_snippet.replace("<b>","")
        html_snippet= html_snippet.replace("</b>","")
        html_snippet= html_snippet.replace("<br>","")
        html_snippet= html_snippet.replace("&nbsp;…",".")
        print("Description == " + snippet+html_snippet)
        print("\n\n")
        i += 1

if choice == "2":
    query_string = urllib.parse.urlencode({"search_query": query})

    html_content = urllib.request.urlopen("https://www.youtube.com/results?"+query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})',html_content.read().decode())

    def remove_duplicates(string):
        final_list=[]
        for q in string:
            if q not in final_list:
                final_list.append(q)
        return final_list

    final_search=remove_duplicates(search_results)
    print("\n********YouTube Links*********\n")
    totalresults = len(final_search)

    i = 0

    while i < 6:
        print("Video Link")
        print("http://www.youtube.com/watch?v=" + final_search[i])
        print(" Video Thumbnail")
        print("https://img.youtube.com/vi/"+final_search[i]+"/0.jpg")
        i += 1



    
