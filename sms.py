import requests'https://textbelt.com/text', {
  'phone': f'{phone}',
  'message': f'{text}',
  'key': 'textbelt',
})
   print(resp.json())

if __name__ == "__main__":
  msg = input()
  number = input()
  send_msg(number, msg)