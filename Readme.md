
# Phonepe Pulse Data Visualization

#### Phonepe became a leading digital payments company
- The Indian digital payments story has truly captured the world's imagination.
- From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and states-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government.
- Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. 
- PhonePe Pulse is our way of giving back to the digital payments ecosystem.

## Project Descriptions:
#### This app is build for Visualization of Phonepe Pulse Data 
In this project that visualizes transaction and user data to provide insights and trends of the PhonePe platform. It utilizes various data visualization techniques to present the data in an interactive and informative manner.

#### Data Sources
The data used in the PhonePe Pulse project is sourced from PhonePe's transaction and user records. The data is stored in CSV format and preprocessed before visualisations are used.

Dataset Link for [Download](https://github.com/PhonePe/pulse)

<h3 align="left">Languages and Tools:</h3>

<p align="left">
   <!-- Python -->
  <a href="https://www.python.org" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
  </a>
  
   <!-- Numpy -->
  <a href="https://pytorch.org/" target="_blank" rel="noreferrer">
    <img src="https://www.vectorlogo.zone/logos/numpy/numpy-ar21.svg" alt="Numpy" width="70" height="40"/>
  </a>

   <!-- Pandas -->
  <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/>
  </a>

   <!-- Git -->
  <a href="https://git-scm.com/" target="_blank" rel="noreferrer">
    <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/>
  </a>

   <!-- MySQL -->
  <a href="https://www.mysql.com/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/>
  </a>
  
   <!-- Streamlit -->
  <a href="https://streamlit.io/" target="_blank" rel="noreferrer">
    <img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" alt="streamlit" width="70" height="40"/>
  </a>

#### To run this app
`python -m streamlit run app.py` or `streamlit run app.py`

#### NOTE :- provide your sql user, database name, password.

## Basic Requirements:
- __[Python 3.10](https://docs.python.org/3/)__
- __[mysql_connector](https://dev.mysql.com/doc/connector-python/en/)__ 
- __[Pandas](https://pandas.pydata.org/docs/)__
- __[Streamlit](https://docs.streamlit.io/)__
- __[Numpy](https://numpy.org/doc/)__ 
- __[streamlit-option-menu](https://discuss.streamlit.io/t/streamlit-option-menu-is-a-simple-streamlit-component-that-allows-users-to-select-a-single-item-from-a-list-of-options-in-a-menu/20514)__ 

### Contact
- Name : Ajin B
- GITHUB : https://github.com/AJIN-B
- LINKEDIN: https://www.linkedin.com/in/ajin-b-0851191b0/
- Mail : ajin.b.edu@gmail.com

### **Local Setup**:

1. **Clone the Repository**:
```bash
git clone git@github.com:AJIN-B/Phonepe_Pulse_Data_Visualization.git
cd Phonepe_Pulse_Data_Visualization
```

2. **Set Up a Virtual Environment** (Optional but Recommended):
```bash
# For macOS and Linux:
python3 -m venv venv

# For Windows:
python -m venv venv
```

3. **Activate the Virtual Environment**:
```bash
# For macOS and Linux:
source venv/bin/activate

# For Windows:
.\venv\Scripts\activate
```

4. **Install Required Dependencies**:
```bash
pip install -r requirements.txt
```

5. **Set up the Environment Variables**:

```bash
# add the following Keys

HOST="Your HOST ID"

USER="Your USER ID"

PASSWORD="Your PASSWORD"

PORT="Your PORT"

DATABASE_NAME="Your DATABASE NAME"

```

6. **Run**:
```bash
python -m streamlit run app.py 
or 
streamlit run app.py
```

After running the command, Streamlit will provide a local URL (usually `http://localhost:8501/`) which you can open in your web browser to access application.
