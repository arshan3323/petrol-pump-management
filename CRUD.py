
import streamlit as st
import mysql.connector
import pandas as pd

from create import *
from database import *
from delete import *
from read import *
from update import *


# Add custom CSS with forced text color override
# st.markdown("""
#     <style>
#         /* Main background with light gradient */
#         .stApp {
#             background: linear-gradient(135deg, #f5f7fa 0%, #e4e8f0 100%);
#         }
        
#         /* FORCE ALL TEXT to be black/dark for maximum visibility */
#         .stMarkdown, .stMarkdown p, .stText, .stText p, 
#         label, .stTextInput label, .stTextArea label, .stSelectbox label,
#         h1, h2, h3, h4, h5, h6, p, div span, .stTitle {
#             color: #000000 !important; /* Force black text everywhere */
#             font-weight: 500 !important; /* Make text slightly bolder */
#         }
        
#         /* Force input text to be black */
#         input, textarea, select, .stSelectbox > div > div > div {
#             color: #000000 !important;
#         }
        
#         /* Header styling */
#         .stTitle {
#             font-size: 2.5rem !important;
#             text-align: center !important;
#             margin-bottom: 1.5rem !important;
#             padding: 0.5rem !important;
#             border-bottom: 3px solid #3b82f6 !important;
#             color: #000000 !important; /* Ensure title is black */
#             font-weight: 800 !important;
#         }
        
#         /* Subheader styling */
#         h2, h3, .stSubheader {
#             border-left: 4px solid #3b82f6 !important;
#             padding-left: 10px !important;
#             margin-top: 1.5rem !important;
#             color: #000000 !important; /* Ensure headers are black */
#             font-weight: 600 !important;
#         }
        
#         /* Sidebar styling - dark with white text */
#         .stSidebar {
#             background-color: #1e3a8a !important;
#         }
        
#         /* Sidebar text */
#         .stSidebar label, .stSidebar .stSelectbox label,
#         .stSidebar h2, .stSidebar p, .stSidebar div, .stSidebar span {
#             color: #ffffff !important; /* Force WHITE text in sidebar */
#         }
        
#         /* Sidebar header */
#         .stSidebar h2 {
#             border-left: none !important;
#             text-align: center !important;
#             padding-bottom: 10px !important;
#             border-bottom: 2px solid #60a5fa !important;
#             color: #ffffff !important; /* Ensure sidebar header is white */
#         }
        
#         /* Button styling */
#         .stButton > button {
#             background-color: #1e3a8a !important;
#             color: #ffffff !important; /* White text on buttons */
#             border: none !important;
#             border-radius: 5px !important;
#             padding: 0.5rem 1rem !important;
#             font-weight: 600 !important;
#             transition: all 0.3s ease !important;
#         }
        
#         .stButton > button:hover {
#             background-color: #3b82f6 !important;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
#             transform: translateY(-2px) !important;
#         }
        
#         /* Table styling */
#         .dataframe {
#             border-collapse: collapse !important;
#             width: 100% !important;
#             border-radius: 10px !important;
#             overflow: hidden !important;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05) !important;
#         }
        
#         .dataframe th {
#             background-color: #1e3a8a !important;
#             color: #ffffff !important; /* White text in table headers */
#             padding: 12px !important;
#             text-align: left !important;
#         }
        
#         .dataframe td {
#             padding: 10px !important;
#             border-bottom: 1px solid #e5e7eb !important;
#             color: #000000 !important; /* Black text in table cells */
#         }
        
#         /* Card-like containers for content */
#         .card {
#             background-color: white !important;
#             border-radius: 10px !important;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05) !important;
#             padding: 20px !important;
#             margin-bottom: 20px !important;
#         }
        
#         /* Status indicators with forced colors */
#         .status-success {
#             color: #10b981 !important; /* Green */
#             font-weight: 600 !important;
#         }
        
#         .status-warning {
#             color: #f59e0b !important; /* Amber */
#             font-weight: 600 !important;
#         }
        
#         .status-error {
#             color: #ef4444 !important; /* Red */
#             font-weight: 600 !important;
#         }
        
#         /* Footer text */
#         .footer {
#             color: #374151 !important; /* Darker gray for better contrast */
#             font-weight: 500 !important;
#         }
      
#     </style>
# """, unsafe_allow_html=True)


# st.markdown(
#     """
#     <style>
#     textarea, input[type="text"], input[type="number"], select {
#         color: orange !important;
#     }

#     textarea::placeholder, input::placeholder {
#         color: #aaa;
#     }

#     textarea:focus, input:focus {
#         border: 2px solid orange;
#         outline: none;
#         color: orange;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

st.markdown(
    """
    <style>
    body {
        background-color:#2f2f2f; /* Very light yellow background */
    }
    .stApp {
        background-color: #2f2f2f; /* Very light yellow background */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    .css-1d391kg { /* Title style */
        color: #4CAF50;
        font-size: 36px;
    }
    .css-1kyxreq { /* Sidebar */
        background-color: #f4f4f4;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
    }
    /* Custom styles for three dots dropdown menu */
    .stActionButton > button {
        background-color: yellow;
        color: black;
        border-radius: 5px;
        border: none;
    }
    .stActionButton > button:hover {
        background-color: yellow;
        color: black;
    }
    .stActionButton > div[role="menu"] {
        background-color: #ffffe0;
        color: black;
    }
    .stActionButton > div[role="menu"] div[role="menuitem"] {
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
   st.title("Petrol Pump Management System")
   menu = ["PetrolPump", "Owners", "Employee", "Customer","Invoice", "Tanker","Query"]
   choice = st.sidebar.selectbox("Tables", menu)

   create_table()
   
   if choice == "PetrolPump":
      menu = ["Add", "View", "Update", "remove"]
      choice2 = st.sidebar.selectbox("CRUD Operations", menu)
      if choice2 == "Add":
         st.subheader("Enter Petrolpump Details:")
         create_for_Petrolpump()
      elif choice2 == "View":
         st.subheader("View the Petrolpump details:")
         read_for_Petrolpump()
      elif choice2 == "Update":
         st.subheader("Updated petrolpump  tasks")
         update_for_Petrolpump()
      elif choice2 == "remove":
         st.subheader("Deleted petrolpump  tasks")
         delete_for_Petrolpump()

   elif choice == "Owners":
      menu = ["Add", "View", "Update", "Remove"]
      choice2 = st.sidebar.selectbox("CRUD Operations", menu)
      if choice2 == "Add":
            st.subheader("Enter Owners Details:")
            create_for_Owners()
      elif choice2 == "View":
            st.subheader("View Owners details:")
            read_for_Owners()
      elif choice2 == "Update":
            st.subheader("Update created tasks")
            update_for_Owners()
      elif choice2 == "Remove":
            st.subheader("Delete created tasks")
            delete_for_Owners()

   elif choice == "Employee":
      menu = ["Add", "View", "Update", "Remove"]
      choice2 = st.sidebar.selectbox("CRUD Operations", menu)
      if choice2 == "Add":
         st.subheader("Enter Employee Details:")
         create_for_Employee()
      elif choice2 == "View":
         st.subheader("View the Employee details:")
         read_for_Employee()
      elif choice2 == "Update":
         st.subheader("Update created tasks")
         update_for_Employee()
      elif choice2 == "Remove":
         st.subheader("Delete created tasks")
         delete_for_Employee()

   elif choice == "Customer":
     menu = ["Add", "View", "Update", "Remove"]
     choice2 = st.sidebar.selectbox("CRUD Operations", menu)
     if choice2 == "Add":
         st.subheader("Enter trainer Details:")
         create_for_Customer()
     elif choice2 == "View":
         st.subheader("View the trainer details:")
         read_for_Customer()
     elif choice2 == "Update":
         st.subheader("Update created tasks")
         update_for_Customer()
     elif choice2 == "Remove":
         st.subheader("Delete created tasks")
         delete_for_Customer()

   elif choice == "Invoice":
     menu = ["Add", "View", "Update", "Remove"]
     choice2 = st.sidebar.selectbox("CRUD Operations", menu)
     if choice2 == "Add":
         st.subheader("Enter Invoice Details:")
         create_for_Invoice()
     elif choice2 == "View":
         st.subheader("View the Invoice details:")
         read_for_Invoice()
     elif choice2 == "Update":
         st.subheader("Update created tasks")
         update_for_Invoice()
     elif choice2 == "Remove":
         st.subheader("Delete created tasks")
         delete_for_Invoice()

   elif choice == "Tanker":
     menu = ["Add", "View", "Update", "Remove"]
     choice2 = st.sidebar.selectbox("CRUD Operations", menu)
     if choice2 == "Add":
         st.subheader("Enter Tanker Details:")
         create_for_Tanker()
     elif choice2 == "View":
         st.subheader("View the Tanker details:")
         read_for_Tanker()
     elif choice2 == "Update":
         st.subheader("Update created tasks")
         update_for_Tanker()
     elif choice2 == "Remove":
         st.subheader("Delete created tasks")
         delete_for_Tanker()


   elif choice == "Query":
      menu = ["Custom Query","Function"]
      choice2 = st.sidebar.selectbox("Query", menu)
      if choice2 == "Custom Query":
         query = st.text_input("Enter Your Query:")
         if st.button("Run Query"):
            c.execute(query)
            data = c.fetchall()
            st.dataframe(data)
      elif choice2 == "Function":
         net_value()

   else:
      st.subheader("About tasks")

def net_value():
   tanker_id = st.text_input("Enter Tanker ID:")
   result = TOTAL_Amount(tanker_id)
   if st.button("RUN Function"):
      df2=pd.DataFrame(result, columns = ["Total Amount"])
      st.dataframe(df2)

if __name__ == '__main__':
   main()
