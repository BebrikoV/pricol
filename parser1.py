import requests
response = requests.get("https://coinmarketcap.com")
response_text = response.text
response_parse = response_text.split("<span>")
print(response_parse)
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$"):
                print(parse_elem_1)