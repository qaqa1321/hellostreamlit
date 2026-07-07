import streamlit as st
from datetime import date  # 현재 날짜를 사용하기 위해 임포트

# 피드백 폼 생성
with st.form('feedback_form'):
    st.header('Feedback Form')

    # 폼 입력을 컬럼으로 정리
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input('Please enter your name', placeholder='Your full name')
        rating = st.slider('Rate this app (0 = Worst, 10 = Best)', 0, 10, 5)
        
    with col2:
        dob = st.date_input('Enter your date of birth')
        recommend = st.radio('Would you recommend this app to others?', ('Yes', 'No'))
        
    # 제출 버튼
    submit_button = st.form_submit_button('Submit')

# 폼 제출 처리
if submit_button:
    # 이름이 비어 있는지 확인
    if not name.strip():
        st.error('Name cannot be empty. Please provide your name.')
    # 생년월일이 유효한지 확인
    elif dob > date.today():
        st.error('Date of birth cannot be in the future.')
    else:
        st.success('Thank you for your feedback!')
        st.write('**Name:**', name)
        st.write('**Date of Birth:**', dob)
        st.write('**Rating:**', rating)
        st.write('**Would Recommend?:**', recommend)

        import streamlit as st

# 이름을 표시하는 함수
def display_name(name):
    st.info(f'**Name:** {name}')

# 이름 입력
name = st.text_input('Please enter your name')

# 유효성 검사: 이름이 입력되면 정보 표시, 아니면 오류 메시지 표시
if name:
    display_name(name)
else:
    st.error('No name entered')

    import streamlit as st

# 입력을 위한 컬럼 생성
col1, col2 = st.columns(2)

with col1:
    number_1 = st.number_input('Please enter the first number', value=0, step=1)
with col2:
    number_2 = st.number_input('Please enter the second number', value=0, step=1)
try:
    st.info(f'**{number_1}/{number_2}=** {number_1/number_2}')
except Exception as e:
    st.error(f'Error: {e}')

import streamlit as st
import pandas as pd
import numpy as np

# 재현성을 위해 시드 설정
np.random.seed(0)

# 무작위 데이터로 데이터프레임 생성
df = pd.DataFrame(
    np.random.randn(4, 3),
    columns=('Column 1', 'Column 2', 'Column 3')
)

# 원본 데이터프레임 표시
st.subheader('Original DataFrame')
st.dataframe(df)

# 데이터프레임 필터링 (변형)
df = df[df['Column 1'] > 1]

# 변형된 데이터프레임 표시
st.subheader('Mutated DataFrame')
st.dataframe(df)


import streamlit as st
import pandas as pd
import numpy as np

# 재현성을 위해 시드 설정
np.random.seed(0)

# 난수로 데이터프레임 생성
df = pd.DataFrame(
    np.random.randn(4, 3),
    columns=('Column 1', 'Column 2', 'Column 3')
)

# 원본 데이터프레임 표시
st.subheader('Original DataFrame')
st.dataframe(df)  # 상호작용을 위해 st.dataframe 사용

# 특정 컬럼을 선택하여 데이터프레임 변형
df = df[['Column 1', 'Column 2']]

# 변형된 데이터프레임 표시
st.subheader('Mutated DataFrame')
st.dataframe(df)  # 상호작용을 위해 st.dataframe 사용

import streamlit as st
import pandas as pd
import numpy as np

# 재현성을 위해 시드 설정
np.random.seed(0)

# 난수로 데이터프레임 생성
df = pd.DataFrame(
    np.random.randn(4, 3),
    columns=('Column 1', 'Column 2', 'Column 3')
)

# 원본 데이터프레임 표시
st.subheader('Original DataFrame')
st.dataframe(df)  # 대화형 표시를 위해 st.dataframe 사용

# 'Column 1'을 기준으로 정렬하여 데이터프레임 변형
df = df.sort_values(by='Column 1', ascending=True)

# 변형된 데이터프레임 표시
st.subheader('Mutated DataFrame')
st.dataframe(df)  # 대화형 표시를 위해 st.dataframe 사용

import streamlit as st
import pandas as pd
import numpy as np

# 재현성을 위해 시드 설정
np.random.seed(0)

# 난수로 데이터프레임 생성
df = pd.DataFrame(
    np.random.randn(4, 3),
    columns=('Column 1', 'Column 2', 'Column 3')
)

# 원본 데이터프레임 표시
st.subheader('Original DataFrame')
st.dataframe(df)

# 'Column 1'을 기반으로 새 컬럼 'Column 4' 생성
df = df.assign(Column_4 = lambda x: x['Column 1'] * 2)

# 변형된 데이터프레임 표시
st.subheader('Mutated DataFrame')
st.dataframe(df)

import streamlit as st
import pandas as pd
import numpy as np

# 0과 100 사이의 임의의 정수로 데이터프레임 생성
df = pd.DataFrame(
    np.random.randint(0, 101, size=(6, 3)),
    columns=('Exam 1', 'Exam 2', 'Exam 3')
)

# 'Name'과 'Category' 컬럼 직접 할당
df['Name'] = ['John', 'Jessica', 'Jessica', 'John', 'John', 'Jessica']
df['Category'] = ['B', 'A', 'A', 'B', 'A', 'B']

# 원본 데이터프레임 표시
st.subheader('Original DataFrame')
st.dataframe(df)

# 'Name'과 'Category'로 그룹화하고 각 그룹의 첫 번째 행 가져오기
# df_grouped = df.groupby(['Name', 'Category']).first()
df_grouped = df.groupby(['Category', 'Name']).first()

# 그룹화 후 변형된 데이터프레임 표시
st.subheader('Mutated DataFrame')
st.dataframe(df_grouped)

import streamlit as st
import pandas as pd

# 첫 번째 데이터프레임 생성 (df1)
df1 = pd.DataFrame(data={'Name': ['Jessica', 'John'],
                         'Exam 1': [77, 56]})

# 두 번째 데이터프레임 생성 (df2)
df2 = pd.DataFrame(data={'Name': ['Jessica', 'John'],
                         'Exam 2': [76, 97]})

# 세 번째 데이터프레임 생성 (df3)
df3 = pd.DataFrame(data={'Name': ['Jessica', 'John'],
                         'Exam 3': [87, 95]})

# 원본 데이터프레임 표시
st.subheader('Original DataFrames')
st.dataframe(df1)
st.dataframe(df2)
st.dataframe(df3)

# 'Name' 컬럼을 기준으로 내부 조인(inner join)을 사용하여 데이터프레임 병합
df_merged = df2.merge(df3, how='inner', on='Name')
df_merged = df1.merge(df_merged, how='inner', on='Name')

# 병합 후 변형된 데이터프레임 표시
st.subheader('Mutated DataFrame')
st.dataframe(df_merged)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터프레임 생성
df = pd.DataFrame(data={'Name': ['Jessica', 'John'],
                        'Exam 1': [77, 56],
                        'Exam 2': [76, 97],
                        'Exam 3': [87, 95]})

# 'Name' 컬럼을 인덱스로 설정하고 막대 차트 그리기
df.set_index('Name').plot(kind='line', stacked=False, xlabel='Name', ylabel='Exam', subplots=True)

# 스트림릿을 사용하여 플롯 표시
st.pyplot(plt)

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 데이터프레임 생성
df = pd.DataFrame(data={
    'Exam': ['Exam 1', 'Exam 2', 'Exam 3'],
    'Jessica': [77, 76, 87],
    'John': [56, 97, 95]
})

# 선 플롯으로 플로틀리 피규어 생성
fig = go.Figure(data=[
    go.Scatter(name='Jessica', x=df['Exam'], y=df['Jessica'], mode='lines+markers'),
    go.Scatter(name='John', x=df['Exam'], y=df['John'], mode='lines+markers')
])

# 레이아웃 업데이트
fig.update_layout(
    xaxis_title='Exam',
    yaxis_title='Score',
    legend_title='Name',
)

# 선택 기능이 활성화된 상태로 스트림릿을 사용하여 플롯 표시
event = st.plotly_chart(fig, on_select='rerun')

# 선택된 포인트 접근
if event and event.selection:
    selected_data = []
    for point in event.selection.points:
        selected_data.append({
            'Exam': point['x'],
            'Student': point['curve_number'],
            'Score': point['y']
        })
    # curveNumber를 학생 이름으로 매핑
    for item in selected_data:
        item['Student'] = fig.data[item['Student']].name
    st.write('Selected Exam Scores:')
    st.dataframe(selected_data)

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 대학 위치 데이터
df = pd.DataFrame(data={'university': ['Harvard University', 'Yale University', 'Princeton University',
                        'Columbia University', 'Brown University', 'Dartmouth University',
                         'University of Pennsylvania', 'Cornell University'],
                'latitude': [42.3770, 41.3163, 40.3573, 40.8075, 41.8268, 43.7044, 39.9522, 42.4534],
                'longitude': [-71.1167, -72.9223, -74.6672, -73.9626, -71.4025, -72.2887, -75.1932, -76.4735]
                })

# scattergeo 플롯 생성
fig = go.Figure(data=go.Scattergeo(
    lon=df['longitude'],
    lat=df['latitude'],
    text=df['university'],
    mode='markers',
    marker=dict(size=10, color='red', opacity=0.7)
))

# 미국에 초점을 맞추도록 레이아웃 업데이트 및 추가 지도 속성 설정
fig.update_layout(
    geo_scope='usa',
    geo=dict(
        projection_type='albers usa',
        showland=True,
        landcolor='lightgray',
        subunitwidth=1,
    ))

# 스트림릿을 사용하여 지도 표시
st.plotly_chart(fig)