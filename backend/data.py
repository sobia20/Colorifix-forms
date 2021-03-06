import json

PATH = './'
FILE_NAME = 'data.json'
DATA_PATH = '%s%s' % (PATH, FILE_NAME)

class Data:
    def __init__(self):
        self.data = {}
        self.form_names = []
        self.load_data()

    def flush_cache(self):
        '''Initializes form_names and data as empty'''
        self.form_names = []
        self.data = {}

    def load_data(self):
        '''Loads the JSON config file'''
        self.flush_cache()
        with open(DATA_PATH, 'r') as fd:
            self.data = fd.read()
            self.data = json.loads(self.data)

    def get_all_form_names(self):
        '''Returns all available form names and labels'''
        if not self.form_names:
            for form in self.data['forms']:
                self.form_names.append({'name':form['name'],'label':form['label']})
        return self.form_names

    def get_specs(self, name):
        '''Returns all available form specifications'''
        for form in self.data['forms']:
            if form['name'] == name:
                return form
        return 'There is no form by that name'

data_model = Data()