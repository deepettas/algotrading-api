from typing import List
import json 
#Todo: Bad practice fix Decouple the response class -> Per object requests/responses.

class CrawledDataResponse(object):

    def __init__(self, cid: str, content: str, timestamp: float) -> None:
        self.cid = cid
        self.content = content
        self.timestamp = timestamp
    
    @classmethod
    def from_json(cls, data):
        return cls(**data)

    def serialize(self):
        return json.dumps(self.__dict__)
