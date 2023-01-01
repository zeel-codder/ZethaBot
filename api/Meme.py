# importing the requests library
import requests


# const getLink = async () =>{
#     const data=await axios.get("https://meme-api.herokuapp.com/gimme")
#     const todoItems = data.data.preview[data.data.preview.length-1] as String;
#     return todoItems;
# }


def getMeme():

    try:
        URL = "https://meme-api.com/gimme"
        # sending get request and saving the response as response object
        r = requests.get(url=URL)
        # extracting data in json format
        data = r.json()
        res = data["preview"][-1]
        return res
    except Exception as e:
        return "https://preview.redd.it/h3rasqahn89a1.jpg?width=640&crop=smart&auto=webp&s=3244a8157fe91f20b8f4baa183f90066afc010db"


getMeme()
