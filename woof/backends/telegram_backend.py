import requests
from yarl import URL
from .base import Backend

class TelegramBackend(Backend):

    def __init__(self, apikey, chat_id):
        self.apikey = apikey
        self.chat_id = chat_id

    def notify(self, message):
        url = URL('https://api.telegram.org') / f'bot{self.apikey}' / 'sendMessage'
        url = url.with_query(chat_id=self.chat_id, text=message)
        requests.get(url).raise_for_status()
