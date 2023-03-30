import streamlit as st
import time


st.title("Streamlit 超入門")

st.write("プログレバーの表示")
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iterration {i + 1}")
    bar.progress(i + 1)
    time.sleep(0.01)

"Done....."



left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ1')
expander.write('問い合わせ内容1')

expander = st.expander('問い合わせ2')
expander.write('問い合わせ内容2')

expander = st.expander('問い合わせ3')
expander.write('問い合わせ内容3')

# test
