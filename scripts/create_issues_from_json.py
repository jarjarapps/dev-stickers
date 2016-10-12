import json
import requests
import time

category = ""
token = ""
repoOwner = "jarjarapps"
repoName = "dev-stickers"

def make_github_issue(title, body=None, assignee=None, milestone=None, labels=None):
    url = 'https://api.github.com/repos/%s/%s/issues?access_token=%s' % (repoOwner, repoName, token)
    issue = {'title': title,
             'body': body,
             'labels': labels}
    r = requests.post(url, json.dumps(issue))
    if r.status_code == 201:
        print('Successfully created Issue "%s"' % title)
    else:
        print('Could not create Issue "%s"' % title)
        print('Response:', r.content)


with open('svgporn.json') as data_file:    
    svgporn = json.load(data_file)

logos = list(filter(lambda item: category in item["categories"], svgporn["items"]))
for logo in logos:
	title = "Add "+ logo["name"] + " logo"
	body = "- [ ] Verify license at " + logo["url"] + "\n- [ ] Create PNG"
	labels = ['enhancement']
	make_github_issue(title, body, labels = labels)
	time.sleep(2)