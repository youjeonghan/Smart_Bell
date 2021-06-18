#-*-coding: utf-8-*-
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
from decorator import time_chek


SCOPES = ["https://www.googleapis.com/auth/drive"] # scopes 수정시 token.pickle 지워야함

@time_chek
def file_upload(file_name):
    """
    구글Drive v3 API
    음성 or 이미지 업로드하는 함수
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists("/home/jeongran/Project/token.pickle"):
        with open("/home/jeongran/Project/token.pickle", "rb") as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # credentials 저장
            flow = InstalledAppFlow.from_client_secrets_file("/home/jeongran/Project/credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("/home/jeongran/Project/token.pickle", "wb") as token:
            pickle.dump(creds, token)

    service = build("drive", "v3", credentials=creds)

    # 이미지 저장 (.jpg)
    file_metadata1 = {"name": file_name+".jpg", "parents": ["15C_6mNCIAXlmKnBPMDuz4UynLLxVXIxC"]} # 저장명, 저장폴더id
    media1 = MediaFileUpload("/home/jeongran/Project/Image/picture_"+file_name+".jpg", mimetype="image/jpeg")    # 업로드할 파일 경로 및 타입
    file1 = service.files().create(body=file_metadata1, media_body=media1, fields="id").execute()
    
    # 녹음 저장 (.wav)
    file_metadata2 = {"name": file_name+".wav", "parents": ["1uRvhgCvOPUjEpNVedCJW8zXbBPReSKjO"]}
    media2 = MediaFileUpload("/home/jeongran/Project/record/record_"+file_name+".wav", mimetype="audio/wav")
    file2 = service.files().create(body=file_metadata2, media_body=media2, fields="id").execute()
    return file1["id"], file2["id"]

if __name__ == "__main__":
    file_upload("123123")