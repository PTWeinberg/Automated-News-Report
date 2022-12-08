import streamlit as st
import pandas as pd
import requests

#print(response.text)

st.title("Onsemi Article Display")

#df = pd.read_csv(r"")

bus = st.selectbox("Select a business", ("Onsemi","Texas Instruments",
    "Infineon",
    "ST Microelectronics",
    "Analog Devices",
    "NXP Semiconductor",
    "Renesas Electronics",
    "Nordic Semiconductor",
    "Monolithic Power Systems",
    "Microchip",
    "Power Integrations",
    "Nvidia",
    "Intel",
    "Qualcomm"))

url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/search/NewsSearchAPI"

querystring = {"q":bus,"pageNumber":"1","pageSize":"10","autoCorrect":"true","fromPublishedDate":"null","toPublishedDate":"null"}

headers = {
	"X-RapidAPI-Key": "4a99075200msh4a16c774fd8a191p156c20jsn1f27a61601cc",
	"X-RapidAPI-Host": "contextualwebsearch-websearch-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

st.write("You selected:", bus)

rp_json = response.json()
value= rp_json['value']
body = [d['body']for d in value]
titles = [d['title']for d in value]
i = 0
while i < len(body):
    st.subheader(titles[i])
    newBody = body[i].replace("$","\\$")
    newBody
    i+=1
    if i > 15:
        break