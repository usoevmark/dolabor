   import sys
   import requests
   import pyperclip
   from plyer import notification

   def translate(text, target_language='en'):
       url = "https://translate.googleapis.com/translate_a/single"
       params = {
           "client": "gtx",
           "sl": "auto",
           "tl": target_language,
           "dt": "t",
           "q": text,
       }
       response = requests.get(url, params=params)
       if response.status_code == 200:
           result = response.json()
           return ''.join([item[0] for item in result[0]])
       return None

   if __name__ == "__main__":
       input_text = sys.stdin.read().strip()
       translated_text = translate(input_text)
       if translated_text:
           pyperclip.copy(translated_text)
           notification.notify(
               title="Translation Complete",
               message=translated_text,
               timeout=10
           )
           print(translated_text)
       else:
           print("Translation failed.")
   