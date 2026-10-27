import streamlit as st
import requests

st.title("☀️ かんたん天気予報アプリ")

city = st.text_input("都市名（英語で入力してください、例: Tokyo）", "Tokyo")

if st.button("天気を調べる"):
    api_key = "7ee01e540038e7e4a2bc861ec121e319"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},jp&appid={api_key}&lang=ja&units=metric"
    
    try:
        response = requests.get(url).json()
        if response.get('cod') == 200:
            weather = response['weather'][0]['description']
            temp = response['main']['temp']
            humidity = response['main']['humidity']
            
            st.success(f"【 {city} の天気 】")
            st.write(f"- **天候:** {weather}")
            st.write(f"- **気温:** {temp} ℃")
            st.write(f"- **湿度:** {humidity} %")
        else:
            st.error("都市が見つかりませんでした。正しい英語名を入力してください。")
    except Exception as e:
        st.error("エラーが発生しました。")