



# XML从零开始



## 一、概念

**XML:extensiable markup language 被称作可扩展标记语言**

**HTML语言本身就有缺陷**：

- **标记都是固定的，不能自定义。HTML语言中有什么标记就只能用什么标记** 
- **HTML标签本身就缺少含义（tr标签里面什么内容都能放进去，不规范！!）**
- **HTML没有实现真正的国际化**



## 二、语法

#### 0.DTD规范文档

**DTD的基本结构**

DTD是用来规范XML文件的格式，必须出现在头文件中，一遍XML校验器在一开始便可以得到XML文件的格式定义。DTD是一套关于标记符的语法规则，它定义了可用在文档中的元素、属性和实体，以及这些内容之间的关系。



###### DTD的基本结构

DTD语法格式如下：

```
<!DOCTYPE 根元素名称[
<!ELEMENT 子元素名称(#PCDATA)>
]>
```

参数说明：

- `<!DOCTYPE`：文档类型声明的起始定界符；
- `根元素名称[`：一个XML文档只有一个根元素，如果XML文档使用DTD，那么根元素的名称就在这里指定；
- `<!ELEMENT子元素名称(#PCDATA)>`：用来定义出现在文档中的元素；
- `]>`：文档类型声明的结束界定符。









#### １.文档声明

- **XML声明放在XML的第一行**
- **version----版本**
- **encoding--编码**
- **standalone--独立使用--默认是no。standalone表示该xml是不是独立的，如果是yes，则表示这个XML文档时独立的，不能引用外部的DTD规范文件；如果是no，则该XML文档不是独立的，表示可以引用外部的DTD规范文档。**
- **正确的文档声明格式，属性的位置不能改变！**

```
    <?xml version="1.0" encoding="utf-8" standalone="no"?>
```

![image-20210619143939485](img/image-20210619143939485.png)



#### ２.元素／标签

**在XML中元素和标签指的是同一个东西**

**元素中需要值得注意的地方**：

- **XML元素中的出现的空格和换行都会被当做元素内容进行处理**
- **每个XML文档必须有且只有一个根元素**
- **元素必须闭合**
- **大小写敏感**
- **不能交叉嵌套**
- **不能以数字开头**

**XML的语法是规范的！不要随意乱写！**



#### ３.属性

**属性是作为XML元素中的一部分的，命名规范也是和XML元素一样的！**

```
    <!--属性名是name，属性值是china-->
    <中国 name="china">

    </中国>
```



#### ４.注释

**注释和HTML的注释是一样的**

```
    <!---->
    <!-- This is a comment --> 
```

#### ５.CDATA

**在编写XML文件时，有些内容可能不想让解析引擎解析执行，而是当作原始内容处理。遇到此种情况，可以把这些内容放在CDATA区里，对于CDATA区域内的内容，XML解析程序不会处理，而是直接原封不动的输出**

语法：

```
    <![CDATA[
        ...内容
    ]]>
```



#### ６.转义字符(实体引用)

**对于一些单个字符，若想显示其原始样式，也可以使用转义的形式予以处理。**

![img](https://segmentfault.com/img/remote/1460000013252691?w=512&h=490)



在 XML 中，一些字符拥有特殊的意义。

如果你把字符 "<" 放在 XML 元素中，会发生错误，这是因为解析器会把它当作新元素的开始。

这样会产生 XML 错误：

```
<message>if salary < 1000 then</message>
```

为了避免这个错误，请用*实体引用*来代替 "<" 字符：

```
<message>if salary &lt; 1000 then</message> 
```

在 XML 中，有 5 个预定义的实体引用：

| &lt;   | <    | 小于   |
| ------ | ---- | ------ |
| &gt;   | >    | 大于   |
| &amp;  | &    | 和号   |
| &apos; | '    | 单引号 |
| &quot; | "    | 引号   |

注释：在 XML 中，只有字符 "<" 和 "&" 确实是非法的。大于号是合法的，但是用实体引用来代替它是一个好习惯。



#### ７.处理指令

**处理指令，简称PI （processing instruction）。处理指令用来指挥解析引擎如何解析XML文档内容。**

例如：

**在XML文档中可以使用xml-stylesheet指令，通知XML解析引擎，应用css文件显示xml文档内容。**

```
    <?xml-stylesheet type="text/css" href="1.css"?>
```

- **XML代码：**

```
    <?xml version="1.0" encoding="UTF-8" ?>
    <?xml-stylesheet type="text/css" href="1.css"?>
    
    <china>
        <guangzhou>
            广州
        </guangzhou>
        <shenzhen>
            深圳
        </shenzhen>
    </china>
```

- **CSS代码：**

```
    guangzhou{
        font-size: 40px;
    }
```

- 效果：

![img](https://segmentfault.com/img/remote/1460000013252692?w=877&h=293)



## 三、解析



#### 1. XML解析方式

XML解析方式分为两种：

**①：dom(Document Object Model)文档对象模型，是W3C组织推荐解析XML的一种方式**

**②：sax(Simple API For XML)，它是XML社区的标准，几乎所有XML解析器都支持它！**

![img](https://segmentfault.com/img/remote/1460000013252693?w=833&h=240)

从上面的图很容易发现，**应用程序不是直接对XML文档进行操作的，而是由XML解析器对XML文档进行分析，然后应用程序通过XML解析器所提供的DOM接口或者SAX接口对分析结果进行操作，从而间接地实现了对XML文档的访问！**

#### 2. DOM解析操作

> DOM解析是一个基于对象的API，它把XML的内容加载到内存中，生成与XML文档内容对应的模型！当解析完成，内存中会生成与XML文档的结构与之对应的DOM对象树，这样就能够根据树的结构，以节点的形式对文档进行操作！

简单来说：**DOM解析会把XML文档加载到内存中，生成DOM树的元素都是以对象的形式存在的！我们操作这些对象就能够操作XML文档了！**



**在DOM解析中有几个核心的操作接口：**

- **Document【代表整个XML文档，通过Document节点可以访问XML文件中所有的元素内容！】**
- **Node【Node节点几乎在XML操作接口中几乎相当于普通Java类的Object，很多核心接口都实现了它，在下面的关系图可以看出！】**
- **NodeList【代表着一个节点的集合，通常是一个节点中子节点的集合！】**
- NameNodeMap【表示一组节点和其唯一名称对应的一一对应关系，主要用于属性节点的表示（书上说是核心的操作接口，但我好像没用到！呃呃呃，等我用到了，我再来填坑！）】

**节点之间的关系图：**

![img](https://segmentfault.com/img/remote/1460000013252696?w=406&h=225)

- **XML文档代码**

```
    <?xml version="1.0" encoding="UTF-8" ?>
    <china>
        <guangzhou >广州</guangzhou>
        <shenzhen>深圳</shenzhen>
        <beijing>北京</beijing>
        <shanghai>上海</shanghai>
    </china>
```



##### 1)获取解析器

根据XML解析的流程图，**我们先要获取到解析器对象！**

```java
    public class DomParse {
    
        public static void main(String[] args) throws ParserConfigurationException, IOException, SAXException {
    
            //API规范：需要用一个工厂来造解析器对象，于是我先造了一个工厂！
            DocumentBuilderFactory documentBuilderFactory = DocumentBuilderFactory.newInstance();
    
            //获取解析器对象
            DocumentBuilder documentBuilder = documentBuilderFactory.newDocumentBuilder();
    
            //获取到解析XML文档的流对象
            InputStream inputStream = DomParse.class.getClassLoader().getResourceAsStream("city.xml");
    
            //解析XML文档，得到了代表XML文档的Document对象！
            Document document = documentBuilder.parse(inputStream);
            
        }
    }
```



##### 2)遍历

- **可能我们会有两种想法**：
  - **①：从XML文档内容的上往下看，看到什么就输出什么！【这正是SAX解析的做法】**
  - **②：把XML文档的内容分成两部分，一部分是有子节点的，一部分是没有子节点的（也就是元素节点！）。首先我们判断是否为元素节点，如果是元素节点就输出，不是元素节点就获取到子节点的集合，再判断子节点集合中的是否是元素节点，如果是元素节点就输出，如果不是元素节点获取到该子节点的集合....好的，一不小心就递归了...**

- **我们来对XML文档遍历一下吧，为了更好地重用，就将它写成一个方法吧（也是能够更好地用递归实现功能）**！

```java
    public class DomParse {
    
        public static void main(String[] args) throws ParserConfigurationException, IOException, SAXException {
    
            //API规范：需要用一个工厂来造解析器对象，于是我先造了一个工厂！
            DocumentBuilderFactory documentBuilderFactory = DocumentBuilderFactory.newInstance();
    
            //获取解析器对象
            DocumentBuilder documentBuilder = documentBuilderFactory.newDocumentBuilder();
    
            //获取到解析XML文档的File对象
            InputStream inputStream = DomParse.class.getClassLoader().getResourceAsStream("city.xml");
    
            //解析XML文档，得到了代表XML文档的Document对象！
            Document document = documentBuilder.parse(inputStream);
    
            //把代表XML文档的document对象传递进去给list方法
            list(document);
    
        }
    
    
        //我们这里就接收Node类型的实例对象吧！多态！！！
        private static void list(Node node) {
    
            //判断是否是元素节点，如果是元素节点就直接输出
            if (node.getNodeType() == Node.ELEMENT_NODE) {
                System.out.println(node.getNodeName());
            }
    
            //....如果没有进入if语句，下面的肯定就不是元素节点了，所以获取到子节点集合
            NodeList nodeList = node.getChildNodes();
    
            //遍历子节点集合
            for (int i = 0; i < nodeList.getLength(); i++) {
    
                //获取到其中的一个子节点
                Node child = nodeList.item(i);
    
                //...判断该子节点是否为元素节点，如果是元素节点就输出，不是元素节点就再获取到它的子节点集合...递归了
    
                list(child);
            }
            
        }
    }
```

- 效果：

![img](https://segmentfault.com/img/remote/1460000013252698?w=538&h=218)



##### 3)查询

**现在我要做的就是：读取guangzhou这个节点的文本内容！**

​        

```java
    private static void read(Document document) {

        //获取到所有名称为guangzhou节点
        NodeList nodeList = document.getElementsByTagName("guangzhou");
        
        //取出第一个名称为guangzhou的节点
        Node node = nodeList.item(0);
        
        //获取到节点的文本内容
        String value = node.getTextContent();

        System.out.println(value);

    }
```



##### 4)增加

现在我想多增加一个城市节点(杭州)，我需要这样做：

```java
    private static void add(Document document) {

        //创建需要增加的节点
        Element element = document.createElement("hangzhou");

        //向节点添加文本内容
        element.setTextContent("杭州");

        //得到需要添加节点的父节点
        Node parent = document.getElementsByTagName("china").item(0);

        //把需要增加的节点挂在父节点下面去
        parent.appendChild(element);

    }
```

- **做到这里，我仅仅在内存的Dom树下添加了一个节点，要想把内存中的Dom树写到硬盘文件中，需要转换器**！
- **获取转换器也十分简单**：

​        

```java
        //获取一个转换器它需要工厂来造，那么我就造一个工厂
        TransformerFactory transformerFactory = TransformerFactory.newInstance();
        
        //获取转换器对象
        Transformer transformer = transformerFactory.newTransformer();
```

- **把内存中的Dom树更新到硬盘文件中的transform()方法就稍稍有些复杂了**！

![img](https://segmentfault.com/img/remote/1460000013252700?w=881&h=300)

- **它需要一个Source实例对象和Result的实例对象，这两个接口到底是什么玩意啊？**
- 于是乎，**我就去查API，发现DomSource实现了Source接口，我们使用的不正是Dom解析吗，再看看构造方法，感觉就是它了！**

![img](https://segmentfault.com/img/remote/1460000013252701?w=1641&h=912)

- **而SteamResult实现了Result接口，有人也会想，DomResult也实现了Result接口啊，为什么不用DomResult呢？我们现在做的是把内存中的Dom树更新到硬盘文件中呀，当然用的是StreamResult啦！**
- 完整代码如下：

​                

```java
    private static void add(Document document) throws TransformerException {

        //创建需要增加的节点
        Element element = document.createElement("hangzhou");

        //向节点添加文本内容
        element.setTextContent("杭州");

        //得到需要添加节点的父节点
        Node parent = document.getElementsByTagName("china").item(0);

        //把需要增加的节点挂在父节点下面去
        parent.appendChild(element);

        //获取一个转换器它需要工厂来造，那么我就造一个工厂
        TransformerFactory transformerFactory = TransformerFactory.newInstance();

        //获取转换器对象
        Transformer transformer = transformerFactory.newTransformer();

        //把内存中的Dom树更新到硬盘中
        transformer.transform(new DOMSource(document),new StreamResult("city.xml"));
    }
```

**指定增加节点的在beijing节点之前**，是这样做的：

​        

```java
    private static void add2(Document document) throws TransformerException {

        //获取到beijing节点
        Node beijing = document.getElementsByTagName("beijing").item(0);

        //创建新的节点
        Element element = document.createElement("guangxi");

        //设置节点的文本内容
        element.setTextContent("广西");

        //获取到要创建节点的父节点，
        Node parent = document.getElementsByTagName("china").item(0);

        //将guangxi节点插入到beijing节点之前！
        parent.insertBefore(element, beijing);

        //将内存中的Dom树更新到硬盘文件中
        TransformerFactory transformerFactory = TransformerFactory.newInstance();
        Transformer transformer = transformerFactory.newTransformer();
        transformer.transform(new DOMSource(document), new StreamResult("city.xml"));
        
    }
```



##### 5)删除

现在我要删除的是beijing这个节点！

```java
    private static void delete(Document document) throws TransformerException {

        //获取到beijing这个节点
        Node node = document.getElementsByTagName("beijing").item(0);

        //获取到父节点，然后通过父节点把自己删除了
        node.getParentNode().removeChild(node);

        //把内存中的Dom树更新到硬盘文件中
        TransformerFactory transformerFactory = TransformerFactory.newInstance();
        Transformer transformer = transformerFactory.newTransformer();
        transformer.transform(new DOMSource(document), new StreamResult("city.xml"));


    }
```



##### 5)修改

将guangzhou节点的文本内容修改成广州你好

```java
    private static void update(Document document) throws TransformerException {

        //获取到guangzhou节点
        Node node = document.getElementsByTagName("guangzhou").item(0);

        node.setTextContent("广州你好");

        //将内存中的Dom树更新到硬盘文件中
        TransformerFactory transformerFactory = TransformerFactory.newInstance();
        Transformer transformer = transformerFactory.newTransformer();
        transformer.transform(new DOMSource(document), new StreamResult("city.xml"));


    }
```

##### 6)操作属性

XML文档是可能带有属性值的，现在我们要guangzhou节点上的属性

```java
    private static void updateAttribute(Document document) throws TransformerException {

        //获取到guangzhou节点
        Node node = document.getElementsByTagName("guangzhou").item(0);

        //现在node节点没有增加属性的方法，所以我就要找它的子类---Element
        Element guangzhou = (Element) node;

        //设置一个属性，如果存在则修改，不存在则创建！
        guangzhou.setAttribute("play", "gzchanglong");

        //如果要删除属性就用removeAttribute()方法


        //将内存中的Dom树更新到硬盘文件中
        TransformerFactory transformerFactory = TransformerFactory.newInstance();
        Transformer transformer = transformerFactory.newTransformer();
        transformer.transform(new DOMSource(document), new StreamResult("city.xml"));


    }
```

- 效果：

![img](https://segmentfault.com/img/remote/1460000013252706?w=1182&h=322)



#### 3. SAX解析

> SAX采用的是一种顺序的模式进行访问，是一种快速读取XML数据的方式。当使用SAX解析器进行操作时，会触发一系列事件SAX。采用事件处理的方式解析XML文件，利用 SAX 解析 XML 文档，涉及两个部分：**解析器和事件处理器**

**sax是一种推式的机制,你创建一个sax 解析器,解析器在发现xml文档中的内容时就告诉你(把事件推给你). 如何处理这些内容，由程序员自己决定。**

当解析器解析到`<?xml version="1.0" encoding="UTF-8" standalone="no"?>`声明头时，会触发事件。解析到`<china>`元素头时也会触发事件！也就是说：**当使用SAX解析器扫描XML文档(也就是Document对象)开始、结束，以及元素的开始、结束时都会触发事件，根据不同事件调用相对应的方法!**







#### 4. DOM和SAX解析的区别

DOM解析读取整个XML文档，在内存中形成DOM树，很方便地对XML文档的内容进行增删改。但如果XML文档的内容过大，那么就会导致内存溢出！

SAX解析采用部分读取的方式，可以处理大型文件，但只能对文件按顺序从头到尾解析一遍，不支持文件的增删改操作



参考：

https://segmentfault.com/a/1190000013252686





## 四、python读写

test.xml

```xml
<?xml version="1.0" encoding="gb2312" standalone="yes"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>年份 2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
```



#### 1.lxml 模块

Element Tree

[`xml.etree.ElementTree`](https://docs.python.org/zh-cn/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree) 模块实现了一个简单高效的API，用于解析和创建XML数据。

[`ElementTree`](https://docs.python.org/zh-cn/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree) 将整个XML文档表示为一个树， [`Element`](https://docs.python.org/zh-cn/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element) 表示该树中的单个节点。 与整个文档的交互（读写文件）通常在 [`ElementTree`](https://docs.python.org/zh-cn/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree) 级别完成。 与单个 XML 元素及其子元素的交互是在 [`Element`](https://docs.python.org/zh-cn/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element) 级别完成的。

```
import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
```



xml数据集里除了utf-8格式还有gb2312格式，parse方法并不支持gb2312格式

因此使用 **lxml模块**

 lxml是python的一个解析库，支持HTML和XML的解析，支持XPath解析方式，而且解析效率非常高

```
pip install lxml
```

https://lxml.de/tutorial.html



##### 1)元素类 The Element class

###### 1>创建元素

变量的标签值即元素名称

 Elements are easily created through the `Element` factory，

The XML tag name of elements is accessed through the `tag` property:

```
from lxml import etree
root = etree.Element("root")
print(root.tag)
```



###### 2>创建子节点元素

Elements are organised in an XML tree structure. To create child elements and add them to a parent element, you can use the `append()` method:

However, this is so common that there is a shorter and much more efficient way to do this: the `SubElement` factory. It accepts the same arguments as the `Element` factory, but additionally requires the parent as first argument:

To see that this is really XML, you can serialise the tree you have created:

```
root.append( etree.Element("child1") )
child2 = etree.SubElement(root, "child2")
child3 = etree.SubElement(root, "child3")
print(etree.tostring(root, pretty_print=True))
"""
<root>
  <child1/>
  <child2/>
  <child3/>
</root>
"""
```



###### 3>element 与 list 类似

To make the access to these subelements easy and straight forward, elements mimic the behaviour of normal Python lists as closely as possible:

```python
>>> child = root[0]
>>> print(child.tag)
child1

>>> print(len(root))
3

>>> root.index(root[1]) # lxml.etree only!
1

>>> children = list(root)

>>> for child in root:
...     print(child.tag)
child1
child2
child3

>>> root.insert(0, etree.Element("child0"))
>>> start = root[:1]
>>> end   = root[-1:]

>>> print(start[0].tag)
child0
>>> print(end[0].tag)
child3
```

There is another important case where the behaviour of Elements in lxml (in 2.0 and later) deviates from that of lists and from that of the original ElementTree (prior to version 1.3 or Python 2.7/3.2)

删除子节点：

```
>>> for child in root:
...     print(child.tag)
child0
child1
child2
child3
>>> root[0] = root[-1]  # this moves the element in lxml.etree!
>>> for child in root:
...     print(child.tag)
child3
child1
child2
```



###### 4>属性 Elements carry attributes as a dict

XML elements support attributes. You can create them directly in the Element factory:

Attributes are just unordered name-value pairs, so a very convenient way of dealing with them is through the dictionary-like interface of Elements:

```
root = etree.Element("root", interesting="totally")
etree.tostring(root)

print(root.get("interesting"))
print(root.get("hello"))
root.set("hello", "Huhu")
print(root.get("hello"))
etree.tostring(root)
for name, value in sorted(root.items()):
	print('%s = %r' % (name, value))


"""
b'<root interesting="totally"/>'
totally
b'<root interesting="totally" hello="Huhu"/>'
hello = 'Huhu'
interesting = 'totally'
"""
```

For the cases where you want to do item lookup or have other reasons for getting a 'real' dictionary-like object, e.g. for passing it around, you can use the `attrib` property:

```
attributes = root.attrib
attributes["hello"] = "Guten Tag"
print(attributes["hello"])
"""
Guten Tag
"""
```

###### 5>文本Elements contain text

```
root = etree.Element("root")
root.text = "TEXT"
etree.tostring(root)

"""
b'<root>TEXT</root>'
"""
```

However, if XML is used for tagged text documents such as (X)HTML, text can also appear between different elements, right in the middle of the tree:

```
<html><body>Hello<br/>World</body></html>
```

Here, the `<br/>` tag is surrounded by text. This is often referred to as *document-style* or *mixed-content* XML. Elements support this through their `tail` property. It contains the text that directly follows the element, up to the next element in the XML tree:

```
>>> html = etree.Element("html")
>>> body = etree.SubElement(html, "body")
>>> body.text = "TEXT"

>>> etree.tostring(html)
b'<html><body>TEXT</body></html>'

>>> br = etree.SubElement(body, "br")
>>> etree.tostring(html)
b'<html><body>TEXT<br/></body></html>'

>>> br.tail = "TAIL"
>>> etree.tostring(html)
b'<html><body>TEXT<br/>TAIL</body></html>'
```

The two properties `.text` and `.tail` are enough to represent any text content in an XML document. This way, the ElementTree API does not require any [special text nodes](http://www.w3.org/TR/DOM-Level-3-Core/core.html#ID-1312295772) in addition to the Element class, that tend to get in the way fairly often (as you might know from classic [DOM](http://www.w3.org/TR/DOM-Level-3-Core/core.html) APIs).

However, there are cases where the tail text also gets in the way. For example, when you serialise an Element from within the tree, you do not always want its tail text in the result (although you would still want the tail text of its children). For this purpose, the `tostring()` function accepts the keyword argument `with_tail`:

```
>>> etree.tostring(br)
b'<br/>TAIL'
>>> etree.tostring(br, with_tail=False) # lxml.etree only!
b'<br/>'
```

If you want to read *only* the text, i.e. without any intermediate tags, you have to recursively concatenate all `text` and `tail` attributes in the correct order. Again, the `tostring()` function comes to the rescue, this time using the `method` keyword:

```
>>> etree.tostring(html, method="text")
b'TEXTTAIL'
```



###### 6>Using XPath to find text



###### 7>Tree iteration



###### 8>Serialisation







##### 2)The ElementTree class

tree = etree.ElementTree(root)

- **tree.docinfo.doctype**

- **tree.docinfo.xml_version**
- **etree.tostring(tree)**
- **etree.tostring(tree.getroot())**



An `ElementTree` is mainly a document wrapper around a tree with a root node. It provides a couple of methods for serialisation and general document handling.

```
>>> root = etree.XML('''\
... <?xml version="1.0"?>
... <!DOCTYPE root SYSTEM "test" [ <!ENTITY tasty "parsnips"> ]>
... <root>
...   <a>&tasty;</a>
... </root>
... ''')

>>> tree = etree.ElementTree(root)
>>> print(tree.docinfo.xml_version)
1.0
>>> print(tree.docinfo.doctype)
<!DOCTYPE root SYSTEM "test">

>>> tree.docinfo.public_id = '-//W3C//DTD XHTML 1.0 Transitional//EN'
>>> tree.docinfo.system_url = 'file://local.dtd'
>>> print(tree.docinfo.doctype)
<!DOCTYPE root PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "file://local.dtd">
```

An `ElementTree` is also what you get back when you call the `parse()` function to parse files or file-like objects (see the parsing section below).

One of the important differences is that the `ElementTree` class serialises as a complete document, as opposed to a single `Element`. This includes top-level processing instructions and comments, as well as a DOCTYPE and other DTD content in the document:

```
>>> print(etree.tostring(tree))  # lxml 1.3.4 and later
<!DOCTYPE root PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "file://local.dtd" [
<!ENTITY tasty "parsnips">
]>
<root>
  <a>parsnips</a>
</root>
```

In the original xml.etree.ElementTree implementation and in lxml up to 1.3.3, the output looks the same as when serialising only the root Element:

```
>>> print(etree.tostring(tree.getroot()))
<root>
  <a>parsnips</a>
</root>
```

This serialisation behaviour has changed in lxml 1.3.4. Before, the tree was serialised without DTD content, which made lxml lose DTD information in an input-output cycle.





##### 3)解析字符串 & 文件Parsing from strings and files



- **fromstring() function**

```
some_xml_data = "<root>data</root>"
root = etree.fromstring(some_xml_data)
etree.tostring(root)

"""
b'<root>data</root>'
"""
```





- **XML() function**

```
>>> root = etree.XML("<root>data</root>")
>>> print(root.tag)
root
>>> etree.tostring(root)
b'<root>data</root>'

>>> root = etree.HTML("<p>data</p>")
>>> etree.tostring(root)
b'<html><body><p>data</p></body></html>'
```



- **parse() function**

`parse()` function is used to parse from files and file-like objects.Note that `parse()` returns an ElementTree object, not an Element object as the string parser functions:

```
```





##### 4)写入xml文件

![image-20210621113112352](img/image-20210621113112352.png)

```python
from lxml import etree
tree = etree.parse("test.xml")

root = tree.getroot()
# etree.indent(root)
print(etree.tostring(tree,encoding='gb2312'))

tree.write('gen_test.xml',encoding=tree.docinfo.encoding,standalone=tree.docinfo.standalone)
```





#### 2.DOM解析



python中用xml.dom.minidom来解析xml文件，实例如下：







## 五、与 json 对比



**XML的优点**

- A.格式统一，符合标准；
- B.容易与其他系统进行远程交互，数据共享比较方便

**XML的缺点**

- A.XML文件庞大，文件格式复杂，传输占带宽；
- B.服务器端和客户端都需要花费大量代码来解析XML，导致服务器端和客户端代码变得异常复杂且不易维护；
- C.客户端不同浏览器之间解析XML的方式不一致，需要重复编写很多代码；
- D.服务器端和客户端解析XML花费较多的资源和时间。

**JSON的优点**

- A.数据格式比较简单，易于读写，格式都是压缩的，占用带宽小；
- B.易于解析，客户端JavaScript可以简单的通过eval_r()进行JSON数据的读取；
- C.支持多种语言，包括ActionScript, C, C#, ColdFusion, Java, JavaScript, Perl, PHP, Python, Ruby等服务器端语言，便于服务器端的解析；
- D.因为JSON格式能直接为服务器端代码使用，大大简化了服务器端和客户端的代码开发量，且完成任务不变，并且易于维护

**JSON的缺点**

- A.没有XML格式这么推广的深入人心和喜用广泛，没有XML那么通用性；
- B.JSON片段的创建和验证过程比一般的XML稍显复杂。







