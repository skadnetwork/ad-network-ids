import requests
import re

from bs4 import BeautifulSoup

def scrape_appsflyer():
    request = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vSqwIBW3FzbrXKqluDQ2hEec7zcvVrxQ02ivWsHnGQTvLMeFmHHjGz1R5TVy6_cqAIVh0pAy4Yud7Qx/pubhtml#")
    soup = BeautifulSoup(request.content, "html5lib")
    # print(soup.prettify())

    discovered_networks = []

    sheets_viewport = soup.find("div", attrs = { "id": "sheets-viewport" })
    sheets_table = sheets_viewport.find("tbody")

    for sheets_row in sheets_table.findAll("tr")[1:]:
        sheets_row_group = sheets_row.findAll("td")

        if len(sheets_row_group) != 2:
            continue

        network = {}
        network["name"] = sheets_row_group[0].text
        network["network"] = sheets_row_group[1].text

        if not network["name"] or not network["network"]:
            continue

        discovered_networks.append(network)

    return discovered_networks

def filter_not_found_in_readme(networks):
    filtered_networks = []

    with open("README.md") as readme_file:
        readme = readme_file.read()

        for network in networks:
            if re.search(r"\\|%s" % network["network"].split(".")[0], readme, re.MULTILINE) == None:
                filtered_networks.append(network)
        
    return filtered_networks


appsflyer_networks = scrape_appsflyer()
networks_missing_from_readme = filter_not_found_in_readme(appsflyer_networks)

# for network in appsflyer_networks:
    # print("Discovered Network: %s [%s]" % (network["name"], network["network"]))

print("Found %i networks, %i require addition." % (len(appsflyer_networks), len(networks_missing_from_readme)))
print("Networks requiring readme addition:")

for network in networks_missing_from_readme:
    print("|[%s]()|%s||" % (network["name"].split("_")[0], network["network"].split(".")[0]))
