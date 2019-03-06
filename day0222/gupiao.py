import requests
import re
def poo():
    r = requests.get("http://quote.stockstar.com/stock/ranklist_a_3_1_1.html")
    con = r.text
    result = re.findall('<td class="align_center "><a href="//stock.quote.stockstar.com/\d{6}.shtml">(\d{6})</a></td><td class="align_center"><a href="//stock.quote.stockstar.com/\d{6}.shtml">(.*?)</a></td>',con)
    return result

def writhinfo():
    with open("content.txt","r",encoding="utf-8") as f:
        content = f.read()
        result = re.findall('<td class="align_center "><a href="//stock.quote.stockstar.com/\d{6}.shtml">(\d{6})</a></td><td class="align_center"><a href="//stock.quote.stockstar.com/\d{6}.shtml">(.*?)</a></td>',content)
        return result


def writefile():
    with open("week.txt","w",encoding="utf-8") as f:
        for i in poo():
            f.write(i[0]+"\t"+i[1])
            f.write("\n")


if __name__ == "__main__"  :
    writefile()
