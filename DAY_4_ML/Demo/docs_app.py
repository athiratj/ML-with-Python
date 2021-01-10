import streamlit as st

# Title
#st.title("Streamlit demo ")
# Header
st.header("Icfoss")
# Subheader
#st.subheader("Language&Technology")

# Text
#st.text("Machine Learning Course")

# Markdown
#st.markdown("### Streamlit  ")


# Adding A Link
url_link = "https://icfoss.in/"
#st.markdown(url_link)

#st.markdown("[Google](https://google.com)")




# Error text
#st.success("Successful")

#st.info("This is an info alert ")

#st.warning("This is a warning ")

#st.error("This shows an error ")

#st.exception("NameError('name not defined')")

# Getting Help Info From Python
#st.help(range)

# Writing Text/Super Fxn
#st.write("Text with write")

st.write("Python Range with write",range(10))

## MEDIA
# Images
from PIL import Image 
img = Image.open("ICFOSS_logo.png")
#st.image(img,width=300,caption='Streamlit Images')

# Videos
video_file = open("video.mp4",'rb')
video_bytes = video_file.read()
#st.video(video_bytes)

# Videos From URL(Youtube)
yt_url ='https://www.youtube.com/watch?v=PyRDe6p1N7c'
#st.video(yt_url)

# # Audio
#st.write("MP3 SONG")
audio_file = open("demo.mp3",'rb')
audio_bytes = audio_file.read()
#st.audio(audio_bytes,format='audio/mp3')


# Widget
# Checkbox
#if st.checkbox("Show/Hide"):
#	st.text("Showing or Hiding Widget")

# Radio Button
#status = st.radio("What is your status",('Active','Inactive'))
#if status == 'Active':
#	st.text("Status is Active")
else:
#	st.warning("Not Active Yet")

# SelectBox
#occupation = st.selectbox("Your Occupation",['Data Scientist','Programmer','Doctor','Businessman'])
#st.write("You selected this option",occupation)

# MultiSelect
#location = st.multiselect("Where do you stay",("London","New York","Accra","Kiev","Berlin","New Delhi"))
#st.write("You selected",len(location),"location")


# Slider
#salary = st.slider("What is your salary",1000,10000)

# Buttons
#st.button("Simple Button")


# Text Input
#name = st.text_input("Enter Name","Type Here...")
#if st.button('Submit'):
 #   result = name.title()
 #   st.success(result)
#else:
#    st.write("Press the above button..")

# Text Area
#c_text = st.text_area("Enter Text","Type Here...")
#if st.button('Analyze'):
 #   c_result = c_text.title()
 #   st.success(c_result)
#else:
#    st.write("Press the above button..")


# Number Input
#number = st.number_input('Enter Number')
#st.write("The Number was",number)

# With Limits
#level = st.number_input('Enter Level',5,10)
#st.write("You are in level",level)


#  Date Input
#import datetime,time
#today = st.date_input("Today is",datetime.datetime.now())


# Time Input
#t = st.time_input("The time now is",datetime.time(10,00))
#st.write("The time will be",t)

# SIDE Bar
#st.sidebar.header("Side Bar Header")
#st.sidebar.text("Hello")


# Balloons
#st.balloons()

