from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload


SCOPES = ["https://www.googleapis.com/auth/drive"] # scopes 수정시 token.pickle 지워야함


def file_upload(type):
    """
    구글Drive v3 API
    음성 or 이미지 업로드하는 함수
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # credentials 저장
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("drive", "v3", credentials=creds)

    # Call the Drive v3 API 테스트 코드
    # results = (
    #     service.files()
    #     .list(
    #         pageSize=20,
    #         fields="nextPageToken, files(id, name)",
    #     )
    #     .execute()
    # )
    # items = results.get("files", [])

    # if not items:
    #     print("No files found.")
    # else:
    #     print("Files:")
    #     for item in items:
    #         print(u"{0} ({1})".format(item["name"], item["id"]))


    if type=="image":
        # 이미지 저장 (.jpg)
        file_metadata = {"name": "test.jpg", "parents": ["15C_6mNCIAXlmKnBPMDuz4UynLLxVXIxC"]} # 저장명, 저장폴더id
        media = MediaFileUpload("C:/Dev/Github/Smart_Bell/project/test/test.jpg", mimetype="image/jpeg")    # 업로드할 파일 경로 및 타입
        
    elif type=="wav":
        # 녹음 저장 (.wav)
        file_metadata = {"name": "test.wav", "parents": ["1uRvhgCvOPUjEpNVedCJW8zXbBPReSKjO"]}
        media = MediaFileUpload("C:/Dev/Github/Smart_Bell/project/test/test.wav", mimetype="audio/wav")
    file = service.files().create(body=file_metadata, media_body=media, fields="id").execute()  # gdrive에 파일 저장
    return file["id"]

if __name__ == "__main__":
    file_upload("image")