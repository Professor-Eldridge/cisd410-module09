import streamlit as st
st.title('My first app')


Options = ["1","2","3"]
choose = st.selectbox("Pick an option:", Options)


if st.button('Classify'):
    st.write("You have clicked the button")


st.sidebar.write('This is the sidebar. You can put things like buttons and checkboxes here')
st.sidebar.button('New Button')
Options2 = ["4","5","6"]
st.sidebar.selectbox("Pick an option:", Options2)


st.write("Well Done")
st.write('Your first app') 
