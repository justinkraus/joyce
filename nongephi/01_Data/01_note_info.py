from bs4 import BeautifulSoup, SoupStrainer
import requests
import pandas as pd

# url = "http://everynoise.com/everynoise1d.cgi?scope=all"

url_list = ['http://www.joyceproject.com/index.php?chapter=telem&notes=1',
'http://www.joyceproject.com/index.php?chapter=nestor&notes=1',  # noqa: E128
'http://www.joyceproject.com/index.php?chapter=proteus&notes=0',  # noqa: E128
'http://www.joyceproject.com/index.php?chapter=calypso&notes=0',  # noqa: E128
'http://www.joyceproject.com/index.php?chapter=lotus&notes=0',  # noqa: E128
'http://www.joyceproject.com/index.php?chapter=hades&notes=0',  # noqa: E128
'http://www.joyceproject.com/index.php?chapter=aeolus&notes=0',  # noqa: E128
'http://www.joyceproject.com/index.php?chapter=lestry&notes=0',  # noqa: E128
'http://www.joyceproject.com/index.php?chapter=scylla&notes=0',  # noqa: E128
'http://www.joyceproject.com/index.php?chapter=wrocks&notes=0',  # noqa: E128
'http://www.joyceproject.com/index.php?chapter=sirens&notes=0',  # noqa: E128
'http://www.joyceproject.com/index.php?chapter=cyclops&notes=0',  # noqa: E128
'http://www.joyceproject.com/index.php?chapter=nausicaa&notes=0',  # noqa: E128
'http://www.joyceproject.com/index.php?chapter=oxen&notes=0',  # noqa: E128
'http://www.joyceproject.com/index.php?chapter=circe&notes=0',  # noqa: E128
'http://www.joyceproject.com/index.php?chapter=eumaeus&notes=0',  # noqa: E128
'http://www.joyceproject.com/index.php?chapter=ithaca&notes=0',  # noqa: E128
'http://www.joyceproject.com/index.php?chapter=penelope&notes=0']  # noqa: E128

df = pd.DataFrame(columns=['href_url', 'link_id', 'page'])
ls = []

for url in url_list:
	page = requests.get(url)
	data = page.text
	soup = BeautifulSoup(data, features="html.parser")

	print(url)

	for link in soup.find_all('a'):
	    print(link.get('href'))
	    # df['href_url'] = link.get('href')
	    href = [link.get('href') for link in soup.find_all('a')]
	    # df['link_id'] = link.get('id')
	    link_id = [link.get('id') for link in soup.find_all('a')]
	    # df['page'] = url
	    text_string = [link.text for link in soup.find_all('a')]
	    df = pd.DataFrame({'href_url': href, 'link_id': link_id, 'text_string': text_string, 'page': url}, columns=['href_url', 'link_id', 'text_string', 'page'])

	df.to_csv('joyce_notes.csv', index=False, mode='a', sep='|')
