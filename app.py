import streamlit as st

st.set_page_config(page_title="Petrol Pump Management System", page_icon="⛽", layout="centered")

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
        .css-12w0qpk {
            background-color: #f5f5dc;
        }
        .stSidebar h2 {
            color: white;
        }
        .stSidebar {
            background-color: #4B4B4B;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <p style="font-size:20px; text-align:center; color:black; font-weight:bold; font-size:40px;">
    Petrol Pump Management System
    </p>
    """,
    unsafe_allow_html=True
)
import cv2

image = cv2.imread(r"C:\Users\ARSHAN\Desktop\g\image2.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = cv2.resize(image, (550, 400))  # Width x Height
st.image(image, caption="OpenCV Resized Image")

st.markdown(
    f"""
    
    <br>
    <p style="font-size:20px;">
    <span style="color:black;font-size:35px;">About This Web App</span><br>
    <span style="color:black;">This app is designed to streamline petrol pump management tasks.</span><br>
    <span style="color:black;">You can track fuel sales, monitor fuel stock, and generate daily reports.</span><br>
    <span style="color:black;">It also allows you to manage employees and record their attendance.</span><br>
    <span style="color:black;">A highly user-friendly platform for efficient fuel station management.</span><br>
    <span style="color:black;">Designed with simplicity and speed in mind.</span>
    </p>

    <br>
    <p style="font-size:20px;">
    <span style="color:black;font-size:35px;">User Guide</span><br>
    <span style="color:black;">1. Use the sidebar to navigate through different sections of the app.</span><br>
    <span style="color:black;">2. To add, delete, or update fuel stock, go to the 'Fuel Management' section.</span><br>
    <span style="color:black;">3. To manage employees and attendance, visit the 'Employee Management' section.</span><br>
    <span style="color:black;">4. Generate daily sales reports from the 'Sales Report' section.</span><br>
    <span style="color:black;">5. To take a printout of sales, use the 'Print Report' button under 'Sales Report'.</span><br>
    <span style="color:black;">6. Always ensure to update stock and attendance regularly.</span>
    </p>

    <br>
    <br>

    <p style="font-size:20px; text-align:center; color:black;">
    <span style="font-size:30px;">Contact Us</span><br><br>
    <span>Email: support@petrolpumpapp.com</span><br>
    <span>Phone: +91 98765 43210</span><br>
    <span>Website: www.petrolpumpapp.com</span><br><br>
    <span style="font-size:18px; font-style:italic;">"Fueling your business, one click at a time."</span>
    </p>
    """,
    unsafe_allow_html=True
)