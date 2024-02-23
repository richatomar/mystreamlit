import streamlit as st
st.set_page_config(page_title='MyStreamlit',page_icon='random')
mymenu=st.sidebar.selectbox('My menu',('Home','FillForm','Downloads'))
st.image('https://onleitechnologies.com/wp-content/uploads/2021/12/cropped-Untitled_design__6_-removebg-preview-1.png')
st.title('Onlie Technologies')
st.header('By Richa Tomar')
st.text('This is a tutorial on streamlit library')
st.image('https://onleitechnologies.com/wp-content/uploads/2021/12/kisspng-python-programming-language-computer-programming-language-5acfdc365292a6.6915108915235717663382.png')
if(mymenu=='Home'):
    st.markdown('<center><h1>WELCOME</h1></center>',unsafe_allow_html=True)
    st.video('https://www.youtube.com/watch?v=aGu0fbkHhek')
elif(mymenu=='FillForm'):
    with st.form('My Form'):
        name=st.text_input('Enter Name')
        dob=st.date_input("choose date of birth")
        marks=st.slider('Choose Marks')
        k=st.form_submit_button("Submit Form")
        if k:
            st.write('Name=',name,'DOB:',dob,'Marks:',marks)
            
elif(mymenu=='Downloads'):
    st.header("Downloads")
    st.download_button('Download Now','hello this is the downloaded data','onlie.txt')
    
