import random
from json import dumps, loads
from os.path import exists
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from IPython.display import clear_output

USER_AGENT_LIST = (
    # Chrome
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    # Firefox
    "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
    "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
)
PROXIES_FILE = "proxies.txt"

# Here I provide some proxies for not getting caught while scraping
ua = UserAgent()  # From here we generate a random user agent
proxies = []  # Will contain proxies [ip, port]


# Main function
def generate_proxies() -> None:
    global proxies

    if exists(PROXIES_FILE):
        try:
            with open(PROXIES_FILE, "r") as file:
                proxies = loads(file)

        except Exception:
            pass

        else:
            return

    # Retrieve latest proxies
    # proxies_req = Request("https://www.sslproxies.org/")
    # proxies_req.add_header("User-Agent", ua.random)
    # proxies_doc = urlopen(proxies_req).read().decode("utf8")

    with open("sslproxies.org.html", "r") as file:
        soup = BeautifulSoup(file, "html.parser")

    proxies_table = BeautifulSoup(str(soup.find_all(id="list"))).find_all("table")[0]

    # Save proxies in the array
    for row in proxies_table.tbody.find_all("tr"):
        proxies.append(
            {"ip": row.find_all("td")[0].string, "port": row.find_all("td")[1].string}
        )

    # Choose a random proxy
    proxy_index = _random_proxy()
    proxy = proxies[proxy_index]

    for n in range(1, 20):
        req = Request("http://icanhazip.com")
        req.set_proxy(proxy["ip"] + ":" + proxy["port"], "http")

        # Every 10 requests, generate a new proxy
        if n % 10 == 0:
            proxy_index = _random_proxy()
            proxy = proxies[proxy_index]

        # Make the call
        try:
            my_ip = urlopen(req).read().decode("utf8")
            print("#" + str(n) + ": " + my_ip)
            clear_output()

        except Exception:  # If error, delete this proxy and find another one
            del proxies[proxy_index]
            print("Proxy " + proxy["ip"] + ":" + proxy["port"] + " deleted.")
            proxy_index = _random_proxy()
            proxy = proxies[proxy_index]

    with open(PROXIES_FILE, "w") as file:
        file.write(dumps(proxies))


def get_random_proxy() -> list:
    return random.choice(proxies)


def get_random_user_agent() -> str:
    return random.choice(USER_AGENT_LIST)


# Retrieve a random index proxy (we need the index to delete it if not working)
def _random_proxy():
    return random.randint(0, len(proxies) - 1)
