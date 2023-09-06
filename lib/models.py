from pydantic import BaseModel
from utils import StrEnum


class GmailBaseModel(BaseModel):
    """Custom modifciations to the BaseModel class"""

    def dict(self, exclude_none=True, **kwargs):
        return super().dict(exclude_none=exclude_none, **kwargs)


class Header(GmailBaseModel):
    name: str | None
    value: str | None


class MessagePartBody(GmailBaseModel):
    attachmentId: str | None
    size: int | None
    data: str | None


class MessagePart(GmailBaseModel):
    partId: str | None
    mimeType: str | None
    filename: str | None
    headers: list[Header] | None
    body: MessagePartBody | None
    parts: list[dict] | None


class Message(GmailBaseModel):
    id: str
    threadId: str
    labelIds: list[str] | None
    snippet: str | None
    historyId: str | None
    internalDate: str | None
    payload: MessagePart | None
    sizeEstimate: int | None
    raw: str | None


class UserMessageList(GmailBaseModel):
    messages: list[Message] | None
    nextPageToken: str | None
    resultSizeEstimate: int | None


class MessageListVisibility(StrEnum):
    SHOW = "show"
    HIDE = "hide"


class LabelListVisibility(StrEnum):
    LABEL_SHOW = "labelShow"
    LABEL_HIDE = "labelHide"
    SHOW_IF_UNREAD = "labelShowIfUnread"


class Label(GmailBaseModel):
    id: str
    name: str
    messageListVisibility: MessageListVisibility
    labelListVisibility: LabelListVisibility
    type: str | None
    messagesTotal: int | None
    messagesUnread: int | None
    threadsTotal: int | None
    threadsUnread: int | None
    color: dict | None


class SizeComparison(StrEnum):
    LARGE = "larger"
    SMALL = "smaller"


class Criteria(GmailBaseModel):
    from_: str | None
    to: str | None
    subject: str | None
    query: str | None
    negatedQuery: str | None
    hasAttachment: bool | None
    excludeChats: bool | None
    size: int | None
    sizeComparison: SizeComparison | None


class Action(GmailBaseModel):
    addLabelIds: list[str] | None
    removeLabelIds: list[str] | None
    forward: str | None


class Filter(GmailBaseModel):
    id: str
    criteria: Criteria
    action: Action
