from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/drive"]


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("drive", "v3", credentials=creds)

    # Call the Drive v3 API
    results = (
        service.files()
        .list(
            pageSize=20,
            fields="nextPageToken, files(id, name)",
        )
        .execute()
    )
    items = results.get("files", [])

    if not items:
        print("No files found.")
    else:
        print("Files:")
        for item in items:
            print(u"{0} ({1})".format(item["name"], item["id"]))

    #     # 단순 파일 업로드
    # file_metadata = {'name' : name}
    # ## mimeType을 설정해주어야 하지만, 웬만한 파일들은 자동으로 생성해준다.
    # media = MediaFileUpload('/path', resumable = True)
    # file = service.files().create(body = file_metadata, media_body=media, fields='id').execute()

    # 특정 폴더 내 파일 업로드
    ## parents에 업로드할 파일의 상위 폴더의 ID를 넣어주면 해당 폴더 안으로 업로드 된다.
    name = "cat2"
    # file_metadata = {"name": name, "parents": ["1Q9Hiy3cp2ewOZrJsq5E7RB_odPOPEEdx"]}
    # media = MediaFileUpload("C:/Dev/Github/Smart_Bell/project/test/cat2.jpg", resumable=True)
    # file = service.files().create(body=file_metadata, media_body=media, fields="id").execute()
    print(1)

    # test 용
    file_metadata = {"name": "photo.jpg", "parents": ["1aAdyOkkIrwiGr-Bqy_MOS5xbNHwjCvaR"]}
    media = MediaFileUpload("C:/Dev/Github/Smart_Bell/project/test/cat2.jpg", mimetype="image/jpeg")
    file = service.files().create(body=file_metadata, media_body=media, fields="id").execute()
    print(file)


if __name__ == "__main__":
    main()