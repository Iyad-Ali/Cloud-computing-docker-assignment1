from urllib.request import urlopen
from bs4 import BeautifulSoup

def html_to_text (url):

    url = url
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    for script in soup(["script", "style"]):
        script.extract()    

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text
    

book1 = html_to_text("https://www.hplovecraft.com/writings/texts/fiction/bws.aspx").lower()
book2 = html_to_text("https://www.gutenberg.org/files/1342/1342-h/1342-h.htm").lower()


words1 = book1.split()
words2 = book2.split()


print(list(set(words1) & set(words2)))
