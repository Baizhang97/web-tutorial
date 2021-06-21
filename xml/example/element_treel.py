from lxml import etree


def save_xml(file_name: str, tree: etree._ElementTree):
    tree.write(file_name, encoding=tree.docinfo.encoding,
               standalone=tree.docinfo.standalone)
    print('Save xml OK !')


def load_xml(file_name: str):
    tree = etree.parse(file_name)
    return tree, tree.getroot()


def iterate():
    root = etree.Element("root")
    etree.SubElement(root, "child").text = "Child 1"
    etree.SubElement(root, "child").text = "Child 2"
    etree.SubElement(root, "another").text = "Child 3"
    """
    <root>
      <child>Child 1</child>
      <child>Child 2</child>
      <another>Child 3</another>
    </root>
    """
    etree.indent(root)
    print(etree.tostring(root, encoding='gb2312'))
    for element in root.iter():
        print("tag: %s - text: %s" % (element.tag, element.text))


xml_file = 'test.xml'
tree, root = load_xml(xml_file)
# etree.indent(root)
# print(etree.tostring(tree,encoding='gb2312'))
suffix = '.xml'

xp = root.xpath('/data/country')

for i in range(1):

    for country in root.iter('country'):
        # 获得该元素的属性名称对应的属性值
        name = country.get('name')
        print('country: ',name)

        # 更改 text 内容
        if name == 'Singapore':
            print()
            for year in country.iter('year'):
                year.text = 'nianfen'
            for neighbour in country.iter('neighbor'):
                n_name = neighbour.get('name')
                print("neighbor: ", n_name)
                attr = neighbour.attrib
                print("attr: ",attr)

                if n_name == 'Malaysia':
                    # 更改属性值
                    attr['direction']='al;skdfh'

    file_name = str(i) + suffix
    save_xml(file_name, tree)
