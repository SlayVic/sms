import requests

def send_msg(phone, text):
   resp = requests.post('https://textbelt.com/text', {
  'phone': f'{phone}',
  'message': f'{text}',
  'key': 'textbelt',
})
   print(resp.json())

if __name__ == "__main__":
  msg = input('Write msg')
  number = input('write number')
  send_msg(number, msg)