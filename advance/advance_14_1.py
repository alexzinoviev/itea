# import pprint
# from xml.etree import ElementTree as et
#
# tree = et.parse('tasks.xml')
#
# print(tree)
#
# t1 = tree.findall('.//day')
#
# print(t1)
#
# t2 = tree.findall('.//task')
# print(t2)


#-----------------------------
# from xml.dom import minidom
#
# tree = minidom.parse('tasks.xml')
#
# print(tree)
#
# for el in tree.firstChild.firstChild.childNodes:
#     print(el.firstChild.wholeText)
#

#-----------------------------
# from xml.dom import pulldom
#
# doc = pulldom.parse('tasks.xml')
# for event, node in doc:
#     if event == pulldom.START_ELEMENT and node.localName == 'task':
#         doc.expandNode(node)
#         print(node.toxml())
#         print(node.firstChild.wholeText)
#
#-----------------------------

from xml import sax

class TasksHandler(sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.is_task = False

    def startElement(self, name, attrs):
        if name == 'task':
            self.is_task = True

    def endElement(self, name):
        if name == 'task':
            self.is_task = False

    def characters(self, content):
        if self.is_task:
            print(content)

parser = sax.make_parser()
parser.setContentHandler(TasksHandler())
parser.parse(open('tasks.xml', 'rt'))