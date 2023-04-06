# -ChatGPT-AI-
零基础使用ChatGPT来帮助生成AI程序


https://m.okjike.com/originalPosts/63bedf6b5b351a0c1425c368?s=eyJ1IjoiNTk4YWY2YThjZjdjODYwMDEwZjk3OWI1IiwiZCI6NH0%3D&utm_source=wechat_session

1. 使用 ChatGPT 生成代码，描述需求，这个时候描述清楚你希望网页有哪些元素，同时每个元素的功能是什么，操作之后会发生什么诸如此类。

举例：「用 python + html 帮我写一个程序，名字内容是【作文生成器】，单独一行展示，第二行是一个标题“请输入作文主题”，另起一行是文字输入框，右边是“确认”按钮，点击确认后将“请以下列内容为主题生成一篇作文：\n\n”加上输入框的内容传到 openai 的接口，再另起一行是输出框，用于展示内容，将前面接口传过去后返回得到的内容展示在输出框。希望代码要中文注释，注释要清晰； 给我完整代码"」

2. 于是乎就得到了一堆 python 代码，和一份 html 的代码，如果发现不完整可以输入”继续“得到完整的代码。

3. 通过查阅 openai 的 api 文档和对比 python 代码可以发现我们需要有一个 key 调用接口才能正常获取内容。
生成 key 的网址，登录账号后使用 beta.openai.com

将下面注释中这段内的内容替换成自己生成的 key ，然后将代码保存成后缀为.py的文件这个程序就能正常本地使用了（如何运行也可以询问 AI ）。
# 设置 OpenAI API 密钥
openai.api_key = "XXXXXXXXXXXXXXXXXX"

4. 如果需要部署成网页前面也有生成对应的前端代码，将html代码保存为 index.html 文件并放入 templates 文件夹内，将 py 文件与这个文件夹保持同一级然后就能上传到服务器去运行这个程序了
