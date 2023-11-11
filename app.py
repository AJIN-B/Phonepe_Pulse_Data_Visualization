

from streamlit_option_menu import option_menu 
import mysql.connector as my_sql 
from dotenv import load_dotenv
import streamlit as st 
from PIL import Image
import pandas as pd
import os 

load_dotenv()

Root = os.getcwd()
mydb = my_sql.connect(host=os.getenv('HOST'),user=os.getenv('USER'),
                      port=os.getenv('PORT'),password=os.getenv('PASSWORD'),database =os.getenv('DATABASE_NAME')) 

def sql_get_data(query):
    cursor = mydb.cursor() 
    cursor.execute(query)
    dd = cursor.fetchall() 
    mydb.commit()     
    return dd


short_state = {'andaman-&-nicobar-islands':'AN', 'assam':"AS",'bihar':"BR", 
               'andhra-pradesh':"AP", 'arunachal-pradesh':"AR",'goa':"GA",
               'chandigarh':'CH', 'chhattisgarh':"CG",'delhi':"DL",
               'dadra-&-nagar-haveli-&-daman-&-diu':"DH-DD", 'gujarat':"GJ",
               'haryana':"HR", 'himachal-pradesh':"HP", 'jammu-&-kashmir':"JK",
               'jharkhand':"JH",'karnataka':"KA", 'kerala':"KL",'ladakh':"LDK",
               'lakshadweep':"LD", 'madhya-pradesh':"MP",'maharashtra':"MH",
               'manipur':"MN", 'meghalaya':"ML", 'mizoram':"MZ",'nagaland':"NL",
               'odisha':"OR",'puducherry':"PY",'punjab':"PB", 'rajasthan':"RJ",
               'sikkim':"SK",'tamil-nadu':"TN",'telangana':"TL",'tripura':"TR",
               'uttar-pradesh':"UP",'uttarakhand':"UK", 'west-bengal':"WB"}


st.set_page_config(page_title = 'PhonePe Data plus Harvesting and Analysis' , layout='wide'
                   ,menu_items={'About': """### This app is created by *AJIN B*"""})

col11,col21 = st.columns([5,15])

with col11:
    st.image(Image.open(os.path.join(Root,"images\\phonepe.png")),width = 250)

with col21:
        st.title(' :violet[PhonePe Pulse Data Visualization and Exploration]') 


st.markdown("***")

SELECT = option_menu( menu_title = None,orientation="horizontal",
                     options = ["Home","Basic insights","Contact"],
                     icons =["house","bar-chart","at"],default_index=0,
                     styles={"container": {"padding": "0!important", "background-color": "white","size":"cover", "width": "100%"},
                             "icon": {"color": "black", "font-size": "20px"},
                             "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
                             "nav-link-selected": {"background-color": "#6F36AD"}})


if SELECT == "Basic insights":
    
    st.write("----")
    st.subheader("Let's know some basic insights about the data")
    options = ["--select--",
               "Top 10 states based on transaction amount",
               "Top 10 states based on transaction Count",
               "Top 10 Districts based on transaction amount",
               "Top 10 Districts based on transaction Count",
               "Top 10 States based on RegisteredUsers",
               "Top 10 Districts based on RegisteredUsers",]
               
    select = st.selectbox("Select the option",options)
    
    if select in ["Top 10 States based on RegisteredUsers","Top 10 Districts based on RegisteredUsers"]:
        
        coly,colq,colty = st.columns(3)     
        with coly:
            Year = st.selectbox('select the Year',
                                ('None','2018', '2019', '2020','2021','2022'))
        with colq:
            Quarter = st.selectbox('select the Quarter',
                                   ('None','1', '2', '3','4')) 
        with colty:
            Type_ = st.selectbox( 'select the Type', ['None'])

    else:
        coly,colq,colty = st.columns(3)     
        with coly:
            Year = st.selectbox('select the Year',
                                ('None','2018', '2019', '2020','2021','2022'))
        with colq:
            Quarter = st.selectbox('select the Quarter',
                                   ('None','1', '2', '3','4')) 
        with colty:
            Type_ = st.selectbox( 'select the Type',
                                 ['None','Recharge & bill payments',
                                  'Peer-to-peer payments','Merchant payments', 
                                  'Financial Services', 'Others'])
        
    
    st.markdown("---")
    
    if select == "Top 10 states based on transaction amount" :
        q1 = [ "SELECT States, SUM(Transaction_Amount) as Total FROM dats ", 
              " GROUP BY States ORDER BY Total DESC LIMIT 10"] 
        tit = "##### Total Transaction Amount by States"
        col = ['States','Total Amount']
    
    if select == "Top 10 states based on transaction Count" :
        q1 = [ "SELECT States, SUM(Transaction_Count) as Total FROM dats ", 
              " GROUP BY States ORDER BY Total DESC LIMIT 10"]
        tit = "##### Total Transaction Count by States"
        col = ['States','Total Count']
    
    if select == "Top 10 Districts based on transaction amount" :
        q1 = [ "SELECT District, SUM(Transaction_Amount) AS Counts, States FROM dmts ", 
              " GROUP BY States,District ORDER BY Counts DESC LIMIT 10"]
        tit = "##### Total Transaction Amount by District"
        col = ['Districts','Total Amount','States']
    
    if select == "Top 10 Districts based on transaction Count" :
        q1 = [ "SELECT District, SUM(Transaction_Count) AS Counts, States FROM dmts ", 
              " GROUP BY States,District ORDER BY Counts DESC LIMIT 10"]
        tit = "##### Total Transaction Count by District"
        col = ['Districts','Total Count','States']
    
    if select == "Top 10 States based on RegisteredUsers" :
        q1 = [ "SELECT States, SUM(registeredUsers) AS Counts  FROM dmus ", 
              " GROUP BY States ORDER BY Counts DESC LIMIT 10"]
        tit = "##### Total Registered Users by States"
        col = ['States','registeredUsers']
    
    if select == "Top 10 Districts based on RegisteredUsers" :
        q1 = [ "SELECT District, SUM(registeredUsers) AS Counts, States  FROM dmus ", 
              " GROUP BY States,District ORDER BY Counts DESC LIMIT 10"]
        tit = "##### Total Registered Users by District"
        col = ['Districts','registeredUsers','States']
    
    if Year in ['2018', '2019', '2020','2021','2022'] and Quarter in ['1', '2', '3','4'] and \
        Type_ in ['Recharge & bill payments', 'Peer-to-peer payments','Merchant payments', 
                  'Financial Services', 'Others']:
        year=int(Year)
        quarter=int(Quarter)
        type_ = Type_
        
        quey = q1[0] + f"WHERE Transaction_Year={year} AND Quarters={quarter} AND Name='{type_}'" + q1[1]
        
        dd = sql_get_data(quey)
        df = pd.DataFrame(dd,columns=col,index=list(range(1,len(dd)+1)))   
        
        tit = tit + f" on Year = {year} , Quarter = {quarter} , Type = {type_}"
        st.write(tit)
        st.write('')
        
        if df.dtypes[1] != 'float64':
            df[col[1]] = df[col[1]].astype("float64")
        
        col1,col11 = st.columns(2)
        with col1:
            st.dataframe(df, width=500, height=250)
        with col11:
            st.bar_chart(data=df, y=col[1], x=col[0])
    
    elif Year in ['2018', '2019', '2020','2021','2022'] and Quarter in ['1', '2', '3','4']:
        
        year=int(Year)
        quarter=int(Quarter)

        quey = q1[0] + f"WHERE Transaction_Year={year} AND Quarters={quarter}" + q1[1]
        
        dd = sql_get_data(quey)
        df = pd.DataFrame(dd,columns=col,index=list(range(1,len(dd)+1)))   
        
        tit = tit + f" on Year = {year} , Quarter = {quarter}"
        st.write(tit)
        st.write('')
        
        if df.dtypes[1] != 'float64':
            df[col[1]] = df[col[1]].astype("float64")
        
        col1,col11 = st.columns(2)
        with col1:
            st.dataframe(df, width=500, height=250)
        with col11:
            st.bar_chart(data=df, y=col[1], x=col[0])
    
    elif Year in ['2018', '2019', '2020','2021','2022'] and Type_ in ['Recharge & bill payments', 
                                                                      'Peer-to-peer payments',
                                                                      'Merchant payments',
                                                                      'Financial Services',
                                                                      'Others']:
        
        year=int(Year)
        type_ = Type_
        
        quey = q1[0] + f"WHERE Transaction_Year={year} AND Name='{type_}'" + q1[1]
        
        dd = sql_get_data(quey)
        df = pd.DataFrame(dd,columns=col,index=list(range(1,len(dd)+1)))   
        
        tit = tit + f" on Year = {year} , Type = {type_}"
        st.write(tit)
        st.write('')
        
        if df.dtypes[1] != 'float64':
            df[col[1]] = df[col[1]].astype("float64")
            
        col1,col11 = st.columns(2)
        with col1:
            st.dataframe(df, width=500, height=250)
        with col11:
            st.bar_chart(data=df, y=col[1], x=col[0])
    
    elif Quarter in ['1', '2', '3','4'] and Type_ in ['Recharge & bill payments', 
                                                      'Peer-to-peer payments',
                                                      'Merchant payments',
                                                      'Financial Services',
                                                      'Others']:
        type_ = Type_
        quarter=int(Quarter)

        quey = q1[0] + f"WHERE Name='{type_}' AND Quarters={quarter}" + q1[1]
        
        dd = sql_get_data(quey)
        df = pd.DataFrame(dd,columns=col,index=list(range(1,len(dd)+1)))   
        
        tit = tit + f" on Quarter = {quarter} , Type = {type_}"
        st.write(tit)
        st.write('')
        
        if df.dtypes[1] != 'float64':
            df[col[1]] = df[col[1]].astype("float64")
              
        col1,col11 = st.columns(2)
        with col1:
            st.dataframe(df, width=500, height=250)
        with col11:
            st.bar_chart(data=df, y=col[1], x=col[0])
    
    
    elif Year in ['2018', '2019', '2020','2021','2022'] :
        
        year=int(Year)
        quey = q1[0] + f"WHERE Transaction_Year={year}" + q1[1]
        
        dd = sql_get_data(quey)
        df = pd.DataFrame(dd,columns=col,index=list(range(1,len(dd)+1)))   
        
        tit = tit + f" on Year = {year}"
        st.write(tit)
        st.write('')
        
        if df.dtypes[1] != 'float64':
            df[col[1]] = df[col[1]].astype("float64")
              
        col1,col11 = st.columns(2)
        with col1:
            st.dataframe(df, width=500, height=250)
        with col11:
            st.bar_chart(data=df, y=col[1], x=col[0])
    
    elif Quarter in ['1', '2', '3','4']:
        
        quarter=int(Quarter)
        quey = q1[0] + f"WHERE Quarters={quarter}" + q1[1]
        
        dd = sql_get_data(quey)
        df = pd.DataFrame(dd,columns=col,index=list(range(1,len(dd)+1)))   
        
        tit = tit + f" on Quarter = {quarter}"
        st.write(tit)
        st.write('')
        
        if df.dtypes[1] != 'float64':
            df[col[1]] = df[col[1]].astype("float64")
                
        col1,col11 = st.columns(2)
        with col1:
            st.dataframe(df, width=500, height=250)
        with col11:
            st.bar_chart(data=df, y=col[1], x=col[0])
    
    
    elif Year not in ['2018', '2019', '2020','2021','2022'] and Quarter not in ['1', '2', '3','4'] and \
        Type_ not in ['Recharge & bill payments', 'Peer-to-peer payments','Merchant payments', 'Financial Services', 'Others'] and\
            select != "--select--":
                
                quey = q1[0] + q1[1][1:]
                dd = sql_get_data(quey)
                df = pd.DataFrame(dd,columns=col,index=list(range(1,len(dd)+1)))   
                
                if df.dtypes[1] != 'float64':
                    df[col[1]] = df[col[1]].astype("float64")
                
                st.write(tit)
                st.write('')

                col1,col11 = st.columns(2)
                with col1:
                    st.dataframe(df, width=500, height=250)
                with col11:
                    st.bar_chart(data=df, y=col[1], x=col[0])
                
    
    else:
        dd = sql_get_data("""SELECT Transaction_Year, SUM(Transaction_Amount) as Total FROM datt 
              GROUP BY Transaction_Year ORDER BY Transaction_Year""")
        df = pd.DataFrame(dd,columns=['Year','Total Amount'],index=list(range(1,len(dd)+1)))   
        df['Year'] = df['Year'].astype("string")
        
        col1,col11 = st.columns(2)
        with col1:
            st.markdown("##### Year wise Total Transaction Amount")
            st.dataframe(df, width=500, height=250)
        with col11:
            st.bar_chart(data=df, y="Total Amount", x="Year")
        

#----------------Home-----------------------#

if SELECT == "Home":
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Phonepe became a leading digital payments company")
        st.image(Image.open(os.path.join(Root,"images/top.jpeg")),width = 500)
    with col2:
        st.image(Image.open(os.path.join(Root,"images/phonepe.png")),width = 500)
        st.write("---")
        st.subheader("The Indian digital payments story has truly captured the world's imagination."
                 " From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and states-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government."
                 " Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. "
                 "PhonePe Pulse is our way of giving back to the digital payments ecosystem.")
    st.write("---")
    st.image(Image.open(os.path.join(Root,"images/report.jpeg")),width = 800)

if SELECT == "Contact":
    col1, col2= st.columns([1,7])
    with col2:
        st.markdown("<h1 style='text-align: center;'>Hi 👋, I'm Ajin</h1>", unsafe_allow_html=True)
        st.markdown("- ### I'm currently working as a Assitant Programmer (python,Machine learning,Deep Learning).")
        st.markdown("- ### Currently learning more about Machine learning, Deep Learning, computer vision and LLM.")
        st.markdown("- ### Eagerly to learn and grow in the field of data science and working towards becoming a professional the field.")
        st.markdown("- ### You can find me on [LinkedIn](https://www.linkedin.com/in/ajin-b-0851191b0/).")
        st.markdown("- ### You can reach out to me at ajin.b.edu@gmail.com.")
        st.markdown("- ### Know about my [experiences](https://docs.google.com/document/d/14__rAIziYlwmE9QPHz9pM05GEBXuiKYj2VHBbQr05WY/edit?usp=sharing).")
        st.markdown("- ### Actively seeking opportunities to apply my data science skills to contribute to meaningful projects and make a positive impact.")

    