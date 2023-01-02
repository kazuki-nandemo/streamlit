import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image 
import time

st.title("Streamkit 入門")
st.write('DataFrame')
df = pd.DataFrame(
    #縦20、横3のデータ
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon'])
# st.write(df)
# st.dataframe(df.style.highlight_max(axis=1),width=100,height=100)
# st.dataframe(df.style.highlight_max(axis=1))
# st.table(df.style.highlight_max(axis=1),width=100,height=100)
#線グラフ
# st.line_chart(df)
#èria グラフ
# st.area_chart(df)
#barグラフ
# st.bar_chart(df)
#mapグラフ
st.map(df)
st.write('Display Image')

st.write('progress bar')
'start'
latest_iteration = st.empty()
bar=st.progress(0)
for i in range(100):
    latest_iteration.text(f'iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.3)
'Done'

# st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
# )

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)
'あなたの好きな数字は、',option,'です。'

# option = st.text_input('あなた趣味を教えてください')
# 'あなたの趣味は、',option,'です。'
# condition = st.slider('あなたの今の調子は？',0,100,50)
# 'コンディション:',condition

left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

option = st.sidebar.text_input('あなた趣味を教えてください')
condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)
'あなたの趣味は、',option,'です。'
'コンディション:',condition


if st.checkbox('show Image'):
    img = Image.open(r'C:\Users\korok\Documents\programmingfile\files\18_streamlit\sample.jpg')
    st.image(img, caption='kaziki kurata',use_column_width=True)
#画像
#マークダウン
"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""
