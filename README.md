# Gmail

Automated handling of email requests coming in through various sources. 📬

## Setup

- `pipenv install` if you want some helpful tools `pipenv install --dev`
- `pipenv shell` to enter the virtual environment
- Make sure you have your google token and credentials for your project from google cloud. You can follow the steps [here](https://developers.google.com/gmail/api/quickstart/python) to get started.

## gmail.py

Quick overview of the methods:

| Name                 | Description                                                                                                                                                                |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| list_labels          | List of labels (returns a dict)                                                                                                                                            |
| create_label         | Creates a label                                                                                                                                                            |
| update_label         | Updates a label                                                                                                                                                            |
| delete_label         | Deletes a label                                                                                                                                                            |
| label_by_id          | Gets a label by id                                                                                                                                                         |
| label_by_name        | Gets a label by name                                                                                                                                                       |
| mark_read            | Marks an eamil as read by id                                                                                                                                               |
| mark_all_read        | Marks all emails as read given a label or sender or both                                                                                                                   |
| mark_unread          | Marks an email as unread by id                                                                                                                                             |
| list_messages        | List of messages                                                                                                                                                           |
| send_message         | Sends a message that can have with or without an attachment. If provided a threadId it will also reply within the email thread chain.                                      |
| download_attachment  | Downloads an attachment and puts it in the attachments directory. Returns the path of the attachment. Also marks the email as read                                         |
| download_attachments | Download attachments from a list of messages using a ThreadPool and puts it in the attachments directory. Returns the path of the attachment. Also marks the email as read |
| list_filters         | List of filters                                                                                                                                                            |
| get_filter           | Get a filter by id                                                                                                                                                         |
| create_filter        | Creates a filter                                                                                                                                                           |
| update_filter        | Updates a filter                                                                                                                                                           |
| delete_filter        | Deletes a filter                                                                                                                                                           |
