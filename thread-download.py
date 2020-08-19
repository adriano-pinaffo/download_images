"""Download images from unsplash.com."""

import sys
import os
import requests
import time
import getopt
import concurrent.futures


def download_image(img):
    """Function to download image."""
    title = img['description'] if img['description'] is not None else img['id']
    title = title.replace('"', '').replace('’', '').replace('?', '').replace('/', '').replace('\n', '')
    title = title[:30] + '.jpg'
    url = img['urls']['raw']
    print(f'Image {title} download started...')

    img_blob = requests.get(url, timeout=5).content
    with open(destination + '/' + title, 'wb') as img_file:
        img_file.write(img_blob)
    return title


defopts = ['destination=', 'threads=', 'number=']
opts, args = getopt.getopt(sys.argv[1:], 'd:t:n:', defopts)
threads = 1
destination = os.path.realpath(os.curdir)
number = 20

base_url = 'https://unsplash.com'
search_uri = '/napi/search'
parameters = {'query': '', 'xp': '', 'per_page': 20}

if len(sys.argv) == 1:
    print('Enter the keyword')
    sys.exit(0)

for o, v in opts:
    if o in ['-d', '--destination']:
        destination = os.path.realpath(v)
    elif o in ['-t', '--threads']:
        threads = v
    elif o in ['-n', '--number']:
        number = v
    else:
        raise AssertionError('Unhandled option')

parameters['query'] = ' '.join(args)
parameters['per_page'] = number

start = time.perf_counter()

resp = requests.get(base_url + search_uri, params=parameters, timeout=5)
resp_dict = resp.json()

images = resp_dict['photos']['results']

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(download_image, img) for img in images]

    for t in concurrent.futures.as_completed(results):
        print(f'Image {t.result()} downloaded')

stop = time.perf_counter()

print(f'Finished in {stop-start} seconds')
