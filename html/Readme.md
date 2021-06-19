# HTML从零开始



## 一、概念

HTML 指的是超文本标记语言 (**H**yper **T**ext **M**arkup **L**anguage)

HTML 标记标签通常被称为 HTML 标签 (HTML tag)。

```
HTML 标签是由尖括号包围的关键词，比如 <html>
HTML 标签通常是成对出现的，比如 <b> 和 </b>
标签对中的第一个标签是开始标签，第二个标签是结束标签
开始和结束标签也被称为开放标签和闭合标签
```

**HTML 文档 = 网页**

- HTML 文档描述网页
- HTML 文档包含 HTML 标签 和纯文本
- HTML 文档也被称为网页

```
<html> 与 </html> 之间的文本描述网页
<body> 与 </body> 之间的文本是可见的页面内容
<h1> 与 </h1> 之间的文本被显示为标题,通过 <h1> - <h6> 等标签进行定义的。
<p> 与 </p> 之间的文本被显示为段落
<a> 与 </a> 之间的文本定义链接，在 href 属性中指定链接的地址
<img   /> 之间的文本定义图像，图像的名称和尺寸是以属性的形式提供的
<br> 标签定义换行，在开始标签中添加斜杠，比如 <br />，是关闭空元素的正确方法
```



## 二、语法

#### 1.标签 & 元素

```
<html> 与 </html> 之间的文本描述网页
<body> 与 </body> 之间的文本是可见的页面内容
<h1> 与 </h1> 之间的文本被显示为标题,通过 <h1> - <h6> 等标签进行定义的。
<p> 与 </p> 之间的文本被显示为段落
<a> 与 </a> 之间的文本定义链接，在 href 属性中指定链接的地址
<img   /> 之间的文本定义图像，图像的名称和尺寸是以属性的形式提供的
<br> 标签定义换行，在开始标签中添加斜杠，比如 <br />，是关闭空元素的正确方法
```

图像的名称和尺寸是以属性的形式提供的

```
<img src="w3school.jpg" width="104" height="142" />
```



HTML 标签对大小写不敏感：<P> 等同于 <p>。许多网站都使用大写的 HTML 标签。

**HTML 元素**

HTML 元素指的是从开始标签（start tag）到结束标签（end tag）的所有代码。

| 开始标签                | 元素内容            | 结束标签 |
| ----------------------- | ------------------- | -------- |
| <p>                     | This is a paragraph | </p>     |
| <a href="default.htm" > | This is a link      | </a>     |
| <br />                  |                     |          |

注释：开始标签常被称为开放标签（opening tag），结束标签常称为闭合标签（closing tag）。

**HTML 元素语法**

- HTML 元素以开始标签起始
- HTML 元素以结束标签终止
- 元素的内容是开始标签与结束标签之间的内容
- 某些 HTML 元素具有空内容（empty content）
- 空元素在开始标签中进行关闭 （以开始标签的结束而结束）
- 大多数 HTML 元素可拥有属性