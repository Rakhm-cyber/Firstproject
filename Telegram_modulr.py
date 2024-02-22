import requests


class TeleModule:
    def set_token(self, Token):
        self.Token = Token

    def send_message(self, id, message):
        self.id = id
        self.message = message
        url = f"https://api.telegram.org/bot{self.Token}/sendMessage"
        params = {"chat_id": self.id, "text": self.message}
        response = requests.post(url, data=params)

    def get_message(self):
        url = f"https://api.telegram.org/bot{self.Token}/getUpdates"
        r = requests.get(url)
        data = r.json()

        if 'result' in data:
            for update in data['result']:
                message = update.get('message', {})
                user_id = message.get('from', {}).get('id')
                text = message.get('text', '')
                print(f"User ID: {user_id}")
                print(f"Message: {text}")

pt = TeleModule()
pt.set_token("6719205536:AAERrWNZMhCoCIwJAaFrhQV4SdQ3CdM1MKw")
pt.send_message(1045687610, "ИЗВИНИ, ПРОВЕРЯЛ РАБОТУ БОТА ЗАБЫЛ УБРАТЬ ТВОЙ АЙДИ И СООБЩЕНИЕ УЖЕ ДАВНО СТОИТ")
pt.get_message()
