import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.title("매년 수능일 전국 지역별 날씨 웹앱")

# 예시 데이터 또는 API, 실제 수능일 데이터/지역 데이터 활용
years = list(range(2012, 2026))
regions = ['서울','부산','대구','인천','광주','대전','울산','세종','경기도','강원도','충청북도','충청남도','전라북도','전라남도','경상북도','경상남도','제주도']
exams = {year: f"{year}-11-3째 목요일" for year in years}  # 실제 수능일 데이터로 교체 권장

selected_year = st.selectbox("연도 선택", years)
selected_date = exams[selected_year]
selected_region = st.multiselect("지역 선택 (중복 선택 가능)", regions, default=['서울'])

st.write(f"수능일: {selected_date}")

# (예시) API 조회 또는 데이터프레임에서 가져오기
@st.cache_data
def get_weather(region, date):
    """예시: Open-Meteo API 코드. 실제 기상청 API 혹은 CSV 연동 가능"""
    url = f"https://api.open-meteo.com/v1/forecast?latitude=37.57&longitude=126.98&start_date={date}&end_date={date}&hourly=temperature_2m"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['hourly']['temperature_2m'][0]
        return temp
    else:
        return None

weather_results = []
for region in selected_region:
    # 여기에서 실제 지역별 위경도 추출 및 실제 API/데이터 연동 필요
    temp = get_weather(region, selected_date)
    weather_results.append({'지역': region, '수능일': selected_date, '기온(°C)': temp})

df = pd.DataFrame(weather_results)
st.table(df)

# 데이터 지도 시각화(Plotly, 예시)
if not df.empty:
    st.subheader("전국 지역 수능일 기온 지도")
    # 예제: 서울 경도/위도만 입력, 실제 전국 시/도 좌표 필요
    df['위도'] = [37.57 for _ in df['지역']]
    df['경도'] = [126.98 for _ in df['지역']]
    fig = px.scatter_mapbox(
        df, lat="위도", lon="경도", color="기온(°C)", hover_name="지역",
        mapbox_style="carto-positron", zoom=5)
    st.plotly_chart(fig)

st.caption("공공데이터포털, 오픈메테오, 혹은 WeatherAPI 활용")

