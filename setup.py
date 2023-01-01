import callBacks as cb

RES_JSON = [
    {"message": ["hi"], "callBack": cb.TellAboutMe},
    {"message": ["/send gf message"], "callBack": cb.GetGfMessage},
    {"message": ["/send meme"], "callBack": cb.GetMeme},
    {"message": ["/send yt link"], "callBack": cb.GetYTLink},
    {"message": ["/galid do muje"], "callBack": cb.GetGali},
    {"message": ["/about me"], "callBack": cb.TellAboutMe},
    {"message": ["/about my creator"], "callBack": cb.AboutMe},
]


DATALIST = {
    "AboutMe": """
Hi I am Zetha Bot, Baki You can call me zeel ka bhai.\n
I can Do this for you 🫡🫣🫠.\n
1. random chat (this will totally random send any meesage i will send any and maja karo. ChatGpt ka peisa nahi abi)
2. /send gf message (will send you message as i am your gf 🌚)
3. /send meme
4. /send yt link (will send you one song 🫣)
5. /gali do muje
6. /about me
7. /about my creator (zeel ke bare me kuch info 🌚)\n

How to use:
Just send me */send meme* buss

Baki bhai abhi naya naya peda hua hu to spam na kare free trial hai 🥲🙂
""",
    "GFMessages": [
        "I 🐳 always love you.🥰",
        "I’d love to cook you dinner. You know, if I knew how to cook. How do you feel about microwave burritos? 🥰",
        "I smile whenever I get a message from you 😊",
        "I promise to always be on your side. (You know, unless I’m under you, or on top, or we’re trying something weird and diagonal.) 😜",
        "You are amazing and perfect in every way. Damn, autocorrect. I mean good morning. 🥰",
        "I could totally go for some of you right now. 🥰",
        "Na bhai tumse na ho paye 🥰",
        "Kya bhai gf nahi he na 🫣🫣🫣🌚",
    ],
    "Galis": [
        "Na Me kyu gali du tume. you are the most cutest and best person in world 🌚🫡🫣🥰.",
        "Gandu.",
        "MC hai tu",
        "Bus bhai me nahi deta gali 👀",
    ],
    "Randoms": [
        "Kya hal hai sir 🌚",
        "Muje kya me to batka hu 👀",
        "Me hi hu tere sath 24x7 😍",
        "I could totally go for some of you right now. 🥰",
        "Na bhai tumse na ho paye 🥰",
        "mann ki chalakiya h sahab,\nbechari zindgi to nadan hi h",
        "aage ka sochkar ab nahi jee rahe ho,\njab has skte the tab hase nahi\naur ab aansu pee rahe ho",
        "Users cannot select more than one option at the same time from a list or button message, but they can go back and re-open a previous message.\nLo pura random",
        "Me nahi bat kar raha aub💀",
        "GN bhai 😍",
        "Tata 💀",
    ],
}
