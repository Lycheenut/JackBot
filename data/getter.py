import urllib.request
import json
import os


class DataGetter:
    def __init__(self, url):
        self.url = url

    def download(self, file):
        """
        Recursively download a file or all files in a directory
        :param file: an object in the form of {'path': string, 'type': string, 'filename': string}
        :return: void
        """
        if file['type'] == 'directory':
            os.mkdir(file['filename'])
            os.chdir(file['filename'])
            response = urllib.request.urlopen(self.url + file['path'])
            body = json.load(response)
            response_data = body['response_data']
            for sub_file in response_data:
                self.download(sub_file)
            os.chdir('..')

        elif file['type'] == 'image':
            response = urllib.request.urlopen(self.url + file['path'])
            fo = open(file['filename'], 'wb')
            out_bytes = response.read()
            fo.write(out_bytes)

    def download_all(self):
        file = {
            'path': '/assets/jp/res',
            'type': 'directory',
            'filename': 'res'
        }
        self.download(file)
