from xml.etree import ElementTree as ET
import pdb
pdb.set_trace()
'''
root = ET.Element('root',{'age':'18'})

son=ET.SubElement(root,'root',{'age':'18'})
ET.SubElement(son,'haha',{'bb':'fhfhf'})

tree = ET.ElementTree(root)
tree.write('aha.xml')

tree = ET.ElementTree()
#tree = ET.parse('pic_Z4RYDR8G_1518019046_1524.xml') 
tree.parse('pic_Z4RYDR8G_1518019046_1524.xml') 
root = tree.getroot()
print root
'''

updateTree = ET.parse('pic_Z4RYDR8G_1518019046_1524.xml')
root = updateTree.getroot()
objs = root.findall('object')
root.remove(objs[-1])
newEle = ET.Element("NewElement")
newEle.attrib = {"name":"NewElement","age":"20"}
newEle.text = "This is a new element"
newEle.tail = '\n'
root.append(newEle)
print root.find('NewElement')

updateTree.write('updatedXml.xml')
