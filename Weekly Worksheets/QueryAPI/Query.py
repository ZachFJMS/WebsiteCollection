import  requests, json

def location_query_url():
    from secrets import IPINFO_KEY

    return f'https://ipinfo.io/json?token={IPINFO_KEY}'

def l_get_all_from_ipinfo():

    response = requests.get(location_query_url())
    facts_dict = json.loads(response.text)

    return facts_dict


if __name__ == '__main__':

    try:
        facts = l_get_all_from_ipinfo()

        print(f'Your current IP address is {facts['ip']}, which is probably located in {facts['city']}.')
    except (requests.ConnectionError, requests.HTTPError, requests.Timeout,):
        print('Error accessing the IPInfo server.')