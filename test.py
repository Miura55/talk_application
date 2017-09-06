#-*- coding: utf8 -*-
import pya3rt
import json

apikey = "K5bYil4Wyd3mYuPgdy1Zi9u42GhR68LA"
client = pya3rt.TalkClient(apikey)

while True:
    say = input("you: ")
    if say == 'end':
        print('seri: ではまた')
        break
    else:
        ans_json = client.talk(say)
        ans = ans_json['results'][0]['reply']
        print('seri:', ans)
