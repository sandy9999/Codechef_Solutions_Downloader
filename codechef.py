from bs4 import BeautifulSoup as bs
import requests
import os
import time
import re
from conf import codechef_handle, codechef_pass

#a pull request fromssssssssssssssssss from meiven
headers = {
    'user-agent': 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

with requests.Session() as s:
    try:
        directory = "codechef_solutions"
        parent_dir = "."
        path = os.path.join(parent_dir, directory)
        if not os.path.exists(path):
            os.mkdir(path)
        directory = codechef_handle
        parent_dir = "./codechef_solutions"
        path = os.path.join(parent_dir, directory)
        if not os.path.exists(path):
            os.mkdir(path)
        url = "https://www.codechef.com"
        r = s.get(url + '/', headers=headers)
        soup = bs(r.content, 'html5lib')

        login_data = {
            'name': codechef_handle,
            'pass': codechef_pass,
            'form_id': 'new_login_form',
            'op': 'Login'
        }
        login_data['form_build_id'] = soup.find('input', attrs={'name': 'form_build_id'})['value']
        r = s.post(url, data=login_data, headers=headers)
        print("Logged in successfully")
        r = s.get(url + '/users/' + codechef_handle, headers=headers)
        soup = bs(r.content, 'html5lib')
        prob_table = soup.find('section', class_ = 'rating-data-section problems-solved')
        
        link = prob_table.findAll('a')
        prob_links = []
        for l in link:
            prob_links.append([str(l['href']), l.text])
        for l in prob_links:
            r = s.get(url + l[0], headers = headers)
            soup = bs(r.content, 'html5lib')        
            while not soup.find('table', class_ = 'dataTable'):
                time.sleep(10)
                r = s.get(url + l[0], headers = headers)
                soup = bs(r.content, 'html5lib')
            soln_link = url + soup.find('table', class_ = 'dataTable').find('tbody').findAll('tr')[0].findAll('a')[1]['href']
            soln_link = re.sub(r"viewsolution","viewplaintext", soln_link)
            r = s.get(soln_link, headers=headers)
            soup = bs(r.content, 'html5lib')
            code = soup.find('pre').prettify(formatter=None)
            code = re.sub(r"<pre>","", code)
            code = re.sub(r"</pre>","", code)
            parent_dir = "./codechef_solutions/" + codechef_handle
            filename = l[1]
            print(filename)
            path = os.path.join(parent_dir, filename)
            code_file = open(path, 'w+')
            code_file.write(code)
            code_file.close()

        r = s.get(url + '/logout/', headers=headers)
        print("Logged out")
    except:
        r = s.get(url + '/logout/', headers=headers)
        print("Logged out")
        s.close()
