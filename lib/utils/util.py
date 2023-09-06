import os
import os.path
from concurrent.futures import TimeoutError

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


def credentials_and_token():
    """Gets credentials from the credentials.json file"""
    # If modifying these scopes, delete the file token.json.
    # This scope gives you full access to your gmail.
    # If you feel you would like to restrict this app you can do so here:
    SCOPES = [
        "https://mail.google.com/",
        "https://www.googleapis.com/auth/gmail.settings.basic",
    ]

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def service():
    """Returns a Gmail service object"""
    creds = credentials_and_token()
    # Call the Gmail API
    service = build("gmail", "v1", credentials=creds)
    return service
