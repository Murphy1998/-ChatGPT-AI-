import openai
import streamlit as st

# 设置 OpenAI API 密钥
openai.api_key = "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"

# 初始化 Streamlit 页面
st.set_page_config(page_title="作文生成器")

# 显示页面标题
st.write("# 作文生成器")

# 显示作文主题输入框
title = st.text_input("请输入作文主题")

# 如果确认按钮被点击
if st.button("确认"):

    # 设置 OpenAI API 请求参数
    prompt = "请以下列内容为主题生成一篇作文：\n\n" + title
    model = "text-davinci-002"
    temperature = 0.5
    max_tokens = 1024

    # 请求 OpenAI API 生成作文
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    # 显示作文生成结果
    st.write("## 作文生成结果")
    st.write(response.choices[0].text)
