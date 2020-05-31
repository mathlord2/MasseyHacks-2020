import requests, argparse

parser = argparse.ArgumentParser(description="make a simple post request")
parser.add_argument("data")
args = parser.parse_args()

url = "http://localhost:5000/upload_url"
data = args.data

response = requests.post(url, data=data)

print(response)