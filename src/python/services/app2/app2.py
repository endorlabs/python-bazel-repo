import requests

def get_external_ip():
    response = requests.get("https://api.ipify.org?format=json")
    ip = response.json()["ip"]
    return ip

def main():
    print(f"My external IP is: {get_external_ip()}")

if __name__ == "__main__":
    main()

