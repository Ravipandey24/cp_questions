DictX = { 'Dict1': {1: 'G', 2: 'F', 3: 'G', 'new': 'nothing'},
         'Dict2': {'Name': 'Geeks', 'class': {'gender': 'male', 'race': 'brown', 'stuff': {'car': 'tesla', 'vehicle': {'name': 'nothing'}}}},
         'Dict3': 'nigga'}
         
# recursive function to find path of a certain value in a nested dictionary.
def get_path(dic, val, path=''):
    for key, value in dic.items():
        if value == val:
            print(path, '>', key)
        if isinstance(value, dict):
            get_path(value, val, path=path+' > '+key)
        
get_path(DictX, 'nothing')