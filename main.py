from pytube import  YouTube
a=input("Enter the Url")
vd=YouTube(a)
st=vd.streams.get_highest_resolution()
st.download()