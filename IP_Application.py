import requests

def get_ip_info():
    # Public API for fetching IP details (you can also use ipstack.com or others)
    url = 'https://ipapi.co/json/'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors

        # Parse the JSON response
        data = response.json()

        # Display IP information
        print(f"IP Address (IPv4): {data.get('ip', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"Country: {data.get('country_name', 'N/A')} ({data.get('country', 'N/A')})")
        print(f"Latitude: {data.get('latitude', 'N/A')}")
        print(f"Longitude: {data.get('longitude', 'N/A')}")
        print(f"ISP: {data.get('org', 'N/A')}")
        print(f"ASN: {data.get('asn', 'N/A')}")
        print(f"Timezone: {data.get('timezone', 'N/A')}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching IP information: {e}")

if __name__ == "__main__":
    get_ip_info()
