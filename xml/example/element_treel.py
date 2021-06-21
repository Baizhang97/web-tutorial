from lxml import etree


def save_xml(file_name: str, tree: etree._ElementTree):
    tree.write(file_name, encoding=tree.docinfo.encoding,
               standalone=tree.docinfo.standalone)
    print('Save xml OK !')




tree = etree.parse("test.xml")

root = tree.getroot()
# etree.indent(root)
print(etree.tostring(tree,encoding='gb2312'))

suffix = '.xml'
for i in range(1):
    file_name = str(i) + suffix
    save_xml(file_name, tree)
















