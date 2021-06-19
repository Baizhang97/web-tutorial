



# json从零开始



## 一、概念

JSON：**JavaScript Object Notation** 【JavaScript 对象表示法】

JSON 是存储和交换文本信息的语法。类似 XML。

**JSON 比 XML 更小、更快，更易解析**。

- javaScript原生支持JSON，解析速度会很快
- XML解析成DOM对象的时候，浏览器【IE和fireFox】会有差异
- 使用JSON会更简单

![这里写图片描述](https://segmentfault.com/img/remote/1460000013279259?w=1304&h=720)

**更加容易创建JavaScript对象**

```
var p = {'city':['北京','上海','广州','深圳']};
for(var i=0;i<p.city.length;i++){
    document.write(p.city[i]+"<br/>");
}
```





## 二、JSON语法

**客户端与服务端的交互数据无非就是两种**

- **数组**
- **对象**

于是乎，JSON所表示的数据要么就是对象，要么就是数据

JSON语法是javaScript语法的子集，**javaScript用[]中括号来表示数组，用{}大括号来表示对象，JSON亦是如此**



#### 1.JSON数组

```
    var employees = [
    { "firstName":"Bill" , "lastName":"Gates" },
    { "firstName":"George" , "lastName":"Bush" },
    { "firstName":"Thomas" , "lastName": "Carter" }
    ];
```



#### 2.JSON对象

```
        var obj = {

            age: 20,
            str: "zhongfucheng",
            method: function () {
                alert("我爱学习");
            }

        };
```

**数组可以包含对象，在对象中也可以包含数组**

#### 3.解析JSON

javaScript原生支持JSON的，**我们可以使用eval()函数来解析JSON，把JSON文本数据转换成一个JavaScript对象。**

```
        function test() {
            //在写JOSN的时候，记得把带上逗号
            var txt = "{a:123," +
                    "b:'zhongfucheng'}";

            //使用eval解析JSON字符串，需要增添()
            var aa = eval("(" + txt + ")");
            alert(aa);

        }
```



![这里写图片描述](https://segmentfault.com/img/remote/1460000013279260?w=283&h=169)

#### 总结

![这里写图片描述](https://segmentfault.com/img/remote/1460000013279261)