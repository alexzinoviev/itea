"""
xml
"""
import pprint
from xml.etree import ElementTree as et

pprint.pprint(dir(et))

root = et.Element('tasks')
print(root)

day = et.SubElement(root, 'day') # в тег tasks вложен элемент day
day.set('date', '01.01.2018')
print(day)

task1 = et.SubElement(day, 'task')
task1.text = 'Wake up'
task2 = et.SubElement(day, 'task')
task2.text = 'Make coffee'
tree = et.ElementTree(root)

print(tree)

tree.write('tasks.xml')