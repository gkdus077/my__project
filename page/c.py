import streamlit as st
import sqlite3
conn=sqlite3.connect('db.db')
cursor= conn.cursor()





if "logged_in" not in st.session_state:
        st.session_state.logged_in = False


id=st.text_input("이름",placeholder='이름을 입력하세요')
pw=st.text_input("비밀번호",placeholder='비밀번호를 입력하세요')
btn=st.button("로그인")
if btn:
    cursor.execute(f"SELECT *FROM users WHERE username='{id}'")
    row=cursor.fetchone()
    if row:
        db_id=row[1]
        db_pw=row[2]
    else:
        db_id=''
        db_pw=''

    if db_id==id and db_pw==pw:
        st.write(f"{id}님 환영합니다")
        st.switch_page("./page/d.py")
               
    else:
        st.error("비밀번호 혹은 아이디가 일치하지 않습니다.")


