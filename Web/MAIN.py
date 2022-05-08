from distutils.command.upload import upload
from fileinput import filename
from tkinter import Image
from numpy import imag
import streamlit as st
import os
from PIL import Image
import PIL 
import csv
from datetime import date
from sympy import false
import streamlit.components.v1 as components
from email_validator import validate_email, EmailNotValidError

#Upvote / Dislike
#Admin / backend
#Rediger opslag
#More likes show up first or newest
#Find total likes
#Score på profil ud fra likes 
#Min side
#Mail(IT-Sikkerhed)
#Søg i alt


# streamlit run MAIN.py


global User
User = "None"
AL = "1234567890qwertyuiopåasdfghjklæøzxcvbnm,.-_:;'?#!@%()"

#0 = Id     1 = Name     2 = Desc    3 = Date     4 = User      5 = likes

st.set_page_config(layout="centered",page_title="FoodHub",page_icon="logo.png")
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
body {
    text-align: center;
}
.big-font {
    font-size:50px !important;
    font-family: Arial, sans-serif;
    text-align: center;
}
.text {
    font-size:30px !important;
    font-family: Arial, sans-serif;
    text-align: center;
}
.texts {
    font-size:20px !important;
    font-family: Arial, sans-serif;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

#Sidebar kan også være radio
st.sidebar.title("Menu")
choice = st.sidebar.selectbox("",('New', 'Top', 'Upload', 'Login', 'Create account'))


def load_image(image_file):
    img = PIL.Image.open(image_file)
    return img


def liked(Filename, User):
    print("Like", Filename, User)
    #try:
    #    User = st.session_state.user
    #except:
    #    User = "None"
#
    #if User != "None":
    #    g = False
    #    Accounts= []
    #    ac = open('data.csv', 'r')
    #    reader = csv.reader(ac)
    #    for line in reader:
    #        Accounts.append(line)
#
    #    tem = 0
    #    with open('data.csv','w',newline='') as wr:
    #        writer = csv.writer(wr)
    #        for line in range(len(Accounts)):
    #            tmp = Accounts[line][4].strip()
    #            if tmp == User:
#
    #                for dt in Accounts[line][6:]:
    #                    tem +=1
    #                    print(dt)
    #                    if dt == Filename:
    #                        #Remove like
    #                        g = True
    #                        Accounts.remove([line][5+tem])
    #                        break
#
    #                if g == False:
    #                    #like
    #                    Accounts.append(User)
    #                    break
    #                
    #        writer.writerows(Accounts)
    #else:
    #    print(User)

        

def FP_load(FileName,ShowName,Desc,Date,User,Like):
    st.image(FileName+".png",  width=500,use_column_width="auto")    
    st.markdown(f'<p class="text">{ShowName}</p>', unsafe_allow_html=True)    
    st.markdown(f'<p class="texts">{Desc}</p>', unsafe_allow_html=True)
    st.markdown( f'<p class="texts">{Date}</p>', unsafe_allow_html=True)
    st.markdown( f'<p class="texts">{User}</p>', unsafe_allow_html=True)
    st.markdown( f'<p class="texts">{Like}</p>', unsafe_allow_html=True)
    
    TEMP = st.button("Like", key = FileName)
    if TEMP:
        liked(FileName,User)

    st.markdown("________________________________________________________________")      
    st.markdown("")    
    st.markdown("")    
def test_mail(mail):
    m_data = False
    while m_data == False:
        try:
            email = validate_email(mail, test_environment=True).email
            
            m_data=True
            
            return email
            
        except EmailNotValidError as e:
            st.write("Email does not exist")
            return False
                                         

if choice == "New":  
    st.markdown('<p class="big-font">FoodHub Newest</p>', unsafe_allow_html=True)
    path = os.getcwd()
    FP_search = st.text_input("Search:", value="")

    csvfile = open('data.csv', newline='')
    spamreader = csv.reader(csvfile, delimiter=',') 

    if FP_search == None or FP_search == "":
        for line in reversed(list(spamreader)):
            FP_load(line[0], line[1],line[2],line[3],line[4],line[5])
    else:
        for line in reversed(list(spamreader)):
            if FP_search.lower() in line[1].lower():
                FP_load(line[0], line[1],line[2],line[3],line[4],line[5])
            elif FP_search.lower() in line[2].lower():
                FP_load(line[0], line[1],line[2],line[3],line[4],line[5])
            elif FP_search.lower() in line[4].lower():
                FP_load(line[0], line[1],line[2],line[3],line[4],line[5])

elif choice == "Top":
    st.markdown('<p class="big-font">Top</p>', unsafe_allow_html=True)
    csvfile = open('data.csv', newline='')
    spamreader = csv.reader(csvfile, delimiter=',') 
    reader = csv.reader(csvfile)
    data = list(reader)
    row_count = sum(1 for row in csvfile)
    a = [0]
    b = [0] 
    for line in range(row_count):
        for x in range(len(a)):
            if int(spamreader[line, 5]) > int(a[x]):
                a.insert(x,spamreader[line, 5])
                b.insert(x,line)
    for k in b:
        temp = data[k]
        FP_load(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5])

elif choice == "Upload":
    try:
        User = st.session_state.user
    except:
        User = "None"
    st.markdown('<p class="big-font">Upload your images!</p>', unsafe_allow_html=True)
    if User != "None":
        UL_image = st.file_uploader("",type=["png","jpg","jpeg"])
        UL_tag = st.text_input("Name your image", value="", max_chars = 50)
        UL_Desc = st.text_input("Description", value="", max_chars = 320)

        if st.button("Upload") and UL_image != None and UL_tag != None:
            UL_END = st.image(load_image(UL_image),width=300)

            with open('data.txt', "r+") as f:
                lines = f.readlines()
                print(lines)
                f.seek(0)
                TEMP = int(lines[0])+1
                f.write(str(TEMP))
                f.close()

            with open('data.csv', 'a', newline='\n') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
                today = date.today()
                today = today.strftime("%m/%d/%y")

                a = [str(TEMP)+",", str(UL_tag)+",", str(UL_Desc),",",str(today)+",",str(User)+",","0"]
                spamwriter.writerow(a)                

            with open(os.path.join(str(TEMP)+".png"),"wb") as sa:
                sa.write((UL_image).getbuffer())  
                sa.close()

            image = Image.open(str(TEMP)+".png")
            if image.size[1] > image.size[0]*1.5:
                newimg = image.resize((600, 600))
                newimg.save(str(TEMP)+".png")

    elif User == "None":
        st.write("Please Login first")

elif choice == "Create account":
    ACC = open('Acc.csv', newline='')
    Accounts = csv.reader(ACC, delimiter=',')   
    st.markdown('<p class="big-font">Create Account</p>', unsafe_allow_html=True)
    L_Name_new = st.text_input("Username", value="")
    L_Pass_new = st.text_input("Password",type="password", value="")
    L_Mail = st.text_input("Email", value="")
    
    if st.button("Create account") and L_Name_new != None and L_Pass_new != None and test_mail(L_Mail) != False:
        cba = False
        
        for x in L_Name_new:
            if x not in AL:
                st.write("Only use letters and numbers please")
                cba = True
        for x in L_Pass_new:
            if x not in AL:
                st.write("Only use letters and numbers please")
                cba = True
        if cba == False:
            abc = False
            for x in Accounts:
                if x[0]==L_Name_new:
                    st.write("Username in use")
                    abc = True
                    break
                elif x[2] == L_Mail:
                    st.write("Email in use")
                    abc = True
                    break
            if abc == False:
                with open('Acc.csv', 'a', newline='\n') as create_acc:
                    spamwriter = csv.writer(create_acc, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow([L_Name_new+","+L_Pass_new+","+L_Mail])   
                st.write("Account created")

elif choice == "Login":
    option1 = True
    b = False
    ACC = open('Acc.csv', newline='')
    Accounts = csv.reader(ACC, delimiter=',') 
    st.markdown('<p class="big-font">Login</p>', unsafe_allow_html=True)
    L_Name = st.text_input("Username", value="")
    L_Pass = st.text_input("Password",type="password", value="")
    if st.button("Login") and L_Name != None and L_Pass != None:
        abc = False
        for x in Accounts:
            if x[0]==L_Name:
                if x[1] == L_Pass:
                    st.session_state['user']=L_Name
                    abc = True
                    st.write("Login Succes")
        if abc == False:
            
            st.write("We did not find an active account, but you can always make a new one!")


            ACC = open('Acc.csv', newline='')
            Accounts = csv.reader(ACC, delimiter=',')   
            st.markdown('<p class="big-font">Create Account</p>', unsafe_allow_html=True)
            L_Name_new = st.text_input("Username", value="", key="111")
            L_Pass_new = st.text_input("Password",type="password", value="", key="11111")
            L_Mail = st.text_input("Email", value="")
            
            if st.button("Create account") and L_Name_new != None and L_Pass_new != None and test_mail(L_Mail) != False:
                cba = False
                
                for x in L_Name_new:
                    if x not in AL:
                        st.write("Only use letters and numbers please")
                        cba = True
                for x in L_Pass_new:
                    if x not in AL:
                        st.write("Only use letters and numbers please")
                        cba = True
                if cba == False:
                    abc = False
                    for x in Accounts:
                        if x[0]==L_Name_new:
                            st.write("Username in use")
                            abc = True
                            break
                        elif x[2] == L_Mail:
                            st.write("Email in use")
                            abc = True
                            break
                    if abc == False:
                        with open('Acc.csv', 'a', newline='\n') as create_acc:
                            spamwriter = csv.writer(create_acc, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
                            spamwriter.writerow([L_Name_new+","+L_Pass_new+","+L_Mail])   
                        st.write("Account created")
    
