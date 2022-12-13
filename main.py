import pprint
from typing import Dict, Tuple

import requests
from bs4 import BeautifulSoup
from ping3 import ping


URL = "https://looking.house/company.php?id=105"


def parse_looking_house(url: str) -> Dict[str, str]:
    """
    Parse LookingHouse for any company.
    
    :param str url: Link to company page on LookingHouse
                    ("https://looking.house/company.php?id=105", for example).
    :rtype: Dict[str, str]
    :return: Dictionary, where key is IP address, value is country or city.
    """
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    result = dict()
    for tr_elem in soup.find_all('tr')[1:]:
        dirty_ip = tr_elem.find_all('td')[0].text.replace("\n", "")
        
        dot_count = 0
        clear_ip = str()
        for symbol in dirty_ip:
            if symbol == ".":
                dot_count += 1
            if dot_count == 3:
                if symbol in "0123456789.":
                    clear_ip += symbol
                else:
                    break
            else:
                clear_ip += symbol

        result[clear_ip] = "".join([
            s for s in tr_elem.find_all('td')[1].text
            if s not in "\n\t\r"
        ])
    
    return result


def ping_hosts(
    ip_to_location: Dict[str, str],
    ping_count: int = 10
) -> Dict[str, Tuple[str, float]]:
    """
    Pings all ip addresses and counts the average ping.
    
    :param Dict[str, str] ip_to_location: Dictionary, where key is IP address,
                                                      value is country or city.
    :rtype: Dict[str, str]
    :return: Dictionary, where key is IP address, value is tuple of country or city and average ping value.
    """
    for ip in ip_to_location.keys():
        pings = list()
        
        for _ in range(ping_count):
            new_ping = ping(ip, unit='ms')
            if new_ping is None:
                break
            pings.append(new_ping)

        if len(pings) != ping_count:
            ip_to_location[ip] = (ip_to_location[ip], -1.)
        else:
            ip_to_location[ip] = (ip_to_location[ip], round(sum(pings) / ping_count, 2))
    
    return ip_to_location


if __name__ == '__main__':
    ip_to_location = parse_looking_house(URL)
    ip_to_location = ping_hosts(ip_to_location)
    pprint.pprint(ip_to_location)

