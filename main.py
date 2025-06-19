import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 데이터 파일 업로드
st.title("지역별 인구 구조 시각화")
uploaded_file = st.file_uploader("인구 데이터 CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='cp949')  # 인코딩은 데이터에 따라 변경
    regions = df['지역명'].unique()
    region = st.selectbox("지역을 선택하세요", regions)

    # 선택한 지역의 데이터 추출
    region_data = df[df['지역명'] == region].iloc[0, 3:]  # 연령별 컬럼만 추출
    ages = region_data.index
    population = region_data.values.astype(int)

    # Plotly 그래프
    fig = go.Figure()
    fig.add_trace(go.Bar(x=ages, y=population, marker_color='cornflowerblue'))
    fig.update_layout(
        title=f"{region} 인구 구조",
        xaxis_title="연령",
        yaxis_title="인구 수",
        template="plotly_white"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.write(f"선택한 지역: **{region}**")
else:
    st.info("CSV 파일을 먼저 업로드하세요.")
