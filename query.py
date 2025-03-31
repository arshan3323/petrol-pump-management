import streamlit as st
import mysql.connector

st.set_page_config(page_title="Custom Query", page_icon="📊", layout="centered")

# Apply some custom CSS for a modern and aesthetic UI
st.markdown(
    """
    <style>
        .stApp {
            background-color: #f5f5dc;
        }
        .css-1d391kg {
            text-align: center;
        }
        .stMarkdown p {
            font-size: 1.1rem;
            color: #374151;
        }
        .stButton > button {
            background-color: #1e3a8a;
            color: white;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            font-size: 1rem;
            font-weight: bold;
            border: none;
        }
        .stButton > button:hover {
            background-color: #3b82f6;
            transform: scale(1.05);
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("<h2 style='text-align:center; color:black;'>Run Custom SQL Query</h2>", unsafe_allow_html=True)
import cv2
image = cv2.imread(r"C:\Users\ARSHAN\Desktop\g\oko.webp")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = cv2.resize(image, (400, 300))  # Width x Height

st.image(image, caption="OpenCV Resized Image")



# Connect to MySQL Server and directly use petrolpump_management database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bADBOY$1",
    database="petrolpump_management"
)
c = conn.cursor()

# Query Input
query = st.text_area("Enter Your SQL Query:")

# Execute Query
if st.button("Run Query"):
    try:
        c.execute(query)
        data = c.fetchall()
        st.dataframe(data)
    except Exception as e:
        st.error(f"An error occurred: {e}")

st.markdown("<h3 style='text-align:center; color:black;'>OR</h3>", unsafe_allow_html=True)

# Pre-defined Function
if st.button("Run net_value() Function"):
    def net_value():
       pass

conn.commit()
conn.close()

