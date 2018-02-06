def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		return None,0
	start_quote = page.find('"',start_link)
	end_quote = page.find('"',start_quote + 1)
	url = page[start_quote + 1:end_quote]
	return url,end_quote

url,endpos = get_next_target('some example<a href="https://github.com">valid ling</a>')

#print(get_next_target('some example<a href="https://github.com">valid ling</a>'))

def extract_all_links(page):
	all_links = []
	while True:
		url,endpos = get_next_target(page)
		if url:
			all_links.append(url)
			page = page[endpos:]
			print url
		else:
			break
	with open('all_links.txt','w') as linky:
		for i in all_links:
			linky.write('%s\n'%i)

extract_all_links('some example<a href="https://github.com">valid ling</a> another link <a href="https://inbox.google.com">assured</a>')
