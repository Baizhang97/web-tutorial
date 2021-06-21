from lxml import etree
tree = etree.parse("test.xml")

root = tree.getroot()
# etree.indent(root)
print(etree.tostring(tree,encoding='gb2312'))


def save_xml():
    tree.write('gen_test.xml',encoding=tree.docinfo.encoding,standalone=tree.docinfo.standalone)
