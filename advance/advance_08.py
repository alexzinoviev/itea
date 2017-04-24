class CSV:
    def load(self):
        print('CSV load')
        return {'Bill': 911}

    def save(self, d):
        print('CSV save')


class JSON:
    def load(self):
        print('JSON load')
        return {'Bill': 911}

    def save(self, d):
        print('JSON save')

CONFIG = {
    'dumper': 'CSV',
}

#-----------------
# if CONFIG['dumper'] == 'CSV':
#     phonebook = CSV().load()
# elif CONFIG['dumper'] == 'JSON':
#     phonebook = JSON().load()
#
#
# if CONFIG['dumper'] == 'CSV':
#     phonebook = CSV().save(phonebook)
# elif CONFIG['dumper'] == 'JSON':
#     phonebook = JSON().save(phonebook)
#------------------


if CONFIG['dumper'] == 'CSV':
    dumper = CSV()
elif CONFIG['dumper'] == 'JSON':
    dumper = JSON()

phonebook = dumper.load()

phonebook = dumper.save(phonebook)