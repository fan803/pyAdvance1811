import requests
import re
def poo():
    with open("content.txt","r",encoding="utf-8") as f:
        content = f.read()
        result = re.findall('<td class=""><span class="red">(^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$)</span></td>',content)


        print(result)
poo()