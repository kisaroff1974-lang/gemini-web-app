import streamlit as st
import google.generativeai as genai
import os

# 1. Настройка страницы
st.set_page_config(page_title="Gemini App", layout="centered")
st.title("🚀 Моё AI Приложение")

# 2. Получение ключа из секретов
api_key = st.secrets["GEMINI_API_KEY"]

if not api_key:
    st.error("API ключ не найден!")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # 3. Интерфейс
    user_input = st.text_area("Введите ваш запрос:", placeholder="Напиши что-нибудь...")

    if st.button("Запустить магию ✨"):
        if user_input:
            with st.spinner('Думаю...'):
                try:
                    response = model.generate_content(user_input)
                    st.subheader("Ответ Gemini:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Ошибка: {e}")
