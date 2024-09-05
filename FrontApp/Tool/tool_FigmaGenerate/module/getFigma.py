import sys
sys.path.append("./")

import json
import os
import re
import requests
import io
from PIL import Image
import pprint


class get_Figma:
    def __init__(self):
        self.token = str(self.getlink()["token"]).strip()
        self.url = str(self.getlink()["url"]).strip()
        self.keyFile = re.search(r"https://www.figma.com/(file|design)/([0-9A-Za-z]+)",self.url).group(2).strip()
        

    def getlink(self):
        with open(f"{os.path.join(os.path.dirname(__file__),'..','asset','info_figma.json')}","r") as file:
            data_infoFigma = json.load(file)
        return data_infoFigma
    

    def getDesigned(self):
        api_endpoint_url = "https://api.figma.com/v1"
        link_getfile = f"{api_endpoint_url}/files/{self.keyFile}"
        link_header = {"X-FIGMA-TOKEN":self.token}
        response = requests.get(link_getfile,headers=link_header)
        return response.json()
        
    def getLinkImage(self,id):
        api_endpoint_url = "https://api.figma.com/v1"
        link_getfileImage = f"{api_endpoint_url}/images/{self.keyFile}?ids={id}&scale=2"
        link_header = {"X-FIGMA-TOKEN":self.token}
        response = requests.get(link_getfileImage,headers=link_header)
        link_image = response.json()["images"][id]
        return link_image


    def getImage(self,link_image,pathFile):
        response = requests.get(link_image)
        content = io.BytesIO(response.content)
        im = Image.open(content)
        im = im.resize((im.size[0] // 2, im.size[1] // 2), Image.LANCZOS)
        with open(pathFile,"wb") as file:
            im.save(file)
            print(f"download in {pathFile}")



