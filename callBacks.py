from twilio.twiml.messaging_response import MessagingResponse
import setup as list
import utils as Ut
import api.Yt as YtApi
import api.Meme as Meme


def GreetingMessageHandler():
    resp = MessagingResponse()
    reply = resp.message()
    reply.body("hello!")
    return resp


def GetGfMessage():
    resp = MessagingResponse()
    reply = resp.message()
    reply.body(Ut.GetRanDom(list.DATALIST["GFMessages"]))
    return resp


def GetMeme():
    resp = MessagingResponse()
    reply1 = resp.message()
    reply1.body("Lo meme bus 😂😂")
    reply2 = resp.message()
    reply2.media(Meme.getMeme())
    return resp


def GetRandom():
    resp = MessagingResponse()
    reply = resp.message()
    reply.body(Ut.GetRanDom(list.DATALIST["Randoms"]))
    return resp


def GetYTLink():
    resp = MessagingResponse()
    reply1 = resp.message()
    reply1.body("Ye suno mast 🌚🫡😍")
    reply2 = resp.message()
    reply2.body(YtApi.get_latest_videos())
    return resp


def GetGali():
    resp = MessagingResponse()
    reply = resp.message()
    reply.body(Ut.GetRanDom(list.DATALIST["Galis"]))
    return resp


def TellAboutMe():
    resp = MessagingResponse()
    reply = resp.message()
    reply.body(list.DATALIST["AboutMe"])
    return resp


def AboutMe():
    resp = MessagingResponse()
    list = ["static/me/1.mp3", "static/me/2.mp3", "static/me/3.mp3", "static/me/4.mp3"]
    reply1 = resp.message()
    reply1.body("This is Zeel 🫡🫡")
    reply2 = resp.message()
    reply2.media(Ut.GetRanDom(list))
    return resp
