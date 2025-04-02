from pydantic import BaseModel

from typing import List, Optional, Dict, Any


class AttachmentPayload(BaseModel):
    url: str


class Attachment(BaseModel):
    type: str
    payload: AttachmentPayload


class QuickReply(BaseModel):
    payload: str


class AdsContextData(BaseModel):
    ad_title: str
    photo_url: str
    video_url: str


class Referral(BaseModel):
    ref: Optional[str]
    ad_id: Optional[str]
    source: Optional[str]
    type: Optional[str]
    ads_context_data: Optional[AdsContextData]


class ReplyToStory(BaseModel):
    url: str
    id: str


class ReplyTo(BaseModel):
    mid: Optional[str]
    story: Optional[ReplyToStory]


class Message(BaseModel):
    mid: str
    attachments: Optional[List[Attachment]]
    is_deleted: Optional[bool]
    is_echo: Optional[bool]
    is_unsupported: Optional[bool]
    quick_reply: Optional[QuickReply]
    referral: Optional[Referral]
    reply_to: Optional[ReplyTo]
    text: Optional[str]


class Messaging(BaseModel):
    sender: Dict[str, str]
    recipient: Dict[str, str]
    timestamp: int
    message: Message


class Entry(BaseModel):
    id: str
    time: int
    messaging: List[Messaging]

class InstagramPayload(BaseModel):
    object: str
    entry: List[Entry]



