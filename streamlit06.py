import streamlit as st
from datetime import datetime

st.title('Clock')

# 시간 표시를 위한 빈 플레이스홀더 생성
clock = st.empty()

# 시간을 지속적으로 업데이트하기 위한 무한 루프
while True:
    time = datetime.now().strftime('%H:%M:%S')
    
    # 플레이스홀더에 현재 시간 표시
    clock.info(f'**Current time:** {time}')
    
    if time > '10:17:15':
        # 알람 조건이 충족되면 시간 표시를 지우고 알람 표시
        clock.empty()
        st.warning('Alarm!!')
        break

import streamlit as st
import requests

# 진행 텍스트를 위한 빈 플레이스홀더 생성
progress_text = st.empty()

# 진행 표시줄 위젯 생성, 초기값은 0%
progress_bar = st.progress(0)

def download_file(url, filename):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    with open(filename, "wb") as f:
        downloaded = 0
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
                downloaded += len(chunk)
                percent = int(downloaded * 100 / total_size) if total_size else 0
                
                # 진행 텍스트와 진행 표시줄 업데이트
                progress_text.subheader(f'Progress: {percent}%')
                progress_bar.progress(percent)
    
    progress_bar.progress(100)
    st.success('다운로드 완료!!')
    return filename

# 사용자 정의 진행 표시줄을 사용하여 requests로 파일 다운로드
download_file('https://buly.kr/5UKBJv8', 'oracle11xe_win64.zip')