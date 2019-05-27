class Schema(object):
    def __init__(self, schema_dict):
        self.key = schema_dict['Property']
        self.type = schema_dict['Type']

    def __str__(self):
        print("key: {}\ntype: {}".format(self.key, self.type))

    def __repr__(self):
        return "key: {}, type: {}".format(self.key, self.type)
