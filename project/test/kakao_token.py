url = "https://kauth.kakao.com/oauth/token"
rest_api_key = "ae26094c86e9e55680461930e4d16e13"
redirect_uri = "http://localhost:5000/oauth"  # APP에서 등록한 redirect_url
authorize_code = "위 방법으로 얻은 code 값"

data = {
    "grant_type": "authorization_code",
    "client_id": rest_api_key,
    "redirect_uri": redirect_uri,
    "code": authorize_code,
}

response = requests.post(url, data=data)
tokens = response.json()
print(tokens["access_token"])

http://kauth.kakao.com/oauth/authorize?client_id=ae26094c86e9e55680461930e4d16e13&redirect_uri=https://example.com/oauth&response_type=code
http://kauth.kakao.com/oauth/authorize?client_id={"ae26094c86e9e55680461930e4d16e13"}&redirect_uri={"https://example.com/oauth"}&response_type=code
/oauth/authorize?client_id=ae26094c86e9e55680461930e4d16e13&redirect_uri=https://example.com/oauth&response_type=code