### 基于Django的在线学习网站  
  
这个项目主要针对**基于类的视图和使用`Mixins`**的练习。使用用户分为教师Instructer和学生Student，教师可以更新课程、模块、内容（文字、图片、文档、视频），学生可以报名课程、浏览参与课程，同时提供`RESTful API`。  
   
**课程模型如下：**
```
Subject 1                                 #学科
    Course 1                              #课程
        Module 1                          #模块
            Content 1 (images)            #内容
            Content 3 (text) 
        Module 2 
            Content 4 (text) 
            Content 5 (file) 
            Content 6 (video) 
            ...
Subject 2
    ...
```
**项目特点**  
1. 使用基于类的视图和Mixins  
- 课程`course`的操作基于`ListView, CreateView, UpdateView, DeleteView, DetailView`等， 模块`module`和内容`content`的操作基于`TemplateResponseMixin`和`View`。  
- 使用`django-braces mixins`实现权限访问控制（项目基于django 1.8.6）。  
2. 模型设计  
- 定制模型字段`OrderField`，字段继承自`PositiveIntegerField`可实现自动按列分片计数，位置`courses.fields.py`。  
- 使用**抽象模型**，内容`content`模型分四类子模型。
- 使用formset编辑module模型。  
3. RESTful API  
