import requests
url = "https://kauth.kakao.com/oauth/token"
rest_api_key = "ae26094c86e9e55680461930e4d16e13"
redirect_uri = "https://example.com/oauth"  # APP에서 등록한 redirect_url
authorize_code = "VmG2ZrIvgnFIYTrNIvJjayz-1wfy2gg1ei2jFh0xyvMHXZxFM0XBYTQ4s8cmpqDyWwzrfAopyNoAAAF5y4BrJQ"
data = {
    "grant_type": "authorization_code",
    "client_id": rest_api_key,
    "redirect_uri": redirect_uri,
    "code": authorize_code,
}

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)
print(tokens["access_token"])
