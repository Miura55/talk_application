#-*- coding: utf8 -*-
import pya3rt

apikey = "K5bYil4Wyd3mYuPgdy1Zi9u42GhR68LA"
client = pya3rt.TalkClient(apikey)

def talk():
    say = input("you: ")
    if say == 'end':
        return('ではまた')
    else:
        ans_json = client.talk(say)
        ans = ans_json['results'][0]['reply']
        return(ans)

if __name__ == '__main__':
    while True:
        vo = talk()
        print('Seri:', vo)
        if vo == 'ではまた':
            break
