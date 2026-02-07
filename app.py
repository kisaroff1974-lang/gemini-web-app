import streamlit as st
import google.generativeai as genai

# Настройка страницы
st.set_page_config(page_title="My Custom AI App", layout="centered")

# Подключаем ключ
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# !!! ЗДЕСЬ ПЕРЕНОСИМ ЛОГИКУ ИЗ AI STUDIO !!!
# Добавь сюда тот текст, который у тебя в поле "System Instructions" в Studio
system_message = "Твоя системная инструкция из AI Studio здесь"

model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction=system_message # Это заставит модель вести себя как в твоем приложении
)

st.title("Название твоего приложения")

user_input = st.text_input("Введите данные:") # Или text_area для длинного текста

if st.button("Результат"):
    if user_input:
        # Можно добавить префикс к запросу, если в Studio были сложные поля
        full_prompt = f"Обработай этот текст: {user_input}"
        
        response = model.generate_content(full_prompt)
        st.write(response.text)
