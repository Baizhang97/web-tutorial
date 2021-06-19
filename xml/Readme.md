



# XML从零开始



## 一、概念

**XML:extensiable markup language 被称作可扩展标记语言**

**HTML语言本身就有缺陷**：

- **标记都是固定的，不能自定义。HTML语言中有什么标记就只能用什么标记** 
- **HTML标签本身就缺少含义（tr标签里面什么内容都能放进去，不规范！!）**
- **HTML没有实现真正的国际化**



## 二、语法



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









#### 3. SAX解析

> SAX采用的是一种顺序的模式进行访问，是一种快速读取XML数据的方式。当使用SAX解析器进行操作时，会触发一系列事件SAX。采用事件处理的方式解析XML文件，利用 SAX 解析 XML 文档，涉及两个部分：**解析器和事件处理器**

**sax是一种推式的机制,你创建一个sax 解析器,解析器在发现xml文档中的内容时就告诉你(把事件推给你). 如何处理这些内容，由程序员自己决定。**

当解析器解析到`<?xml version="1.0" encoding="UTF-8" standalone="no"?>`声明头时，会触发事件。解析到`<china>`元素头时也会触发事件！也就是说：**当使用SAX解析器扫描XML文档(也就是Document对象)开始、结束，以及元素的开始、结束时都会触发事件，根据不同事件调用相对应的方法!**







#### 4. DOM和SAX解析的区别

**DOM解析读取整个XML文档，在内存中形成DOM树，很方便地对XML文档的内容进行增删改。但如果XML文档的内容过大，那么就会导致内存溢出！**

**SAX解析采用部分读取的方式，可以处理大型文件，但只能对文件按顺序从头到尾解析一遍，不支持文件的增删改操作**