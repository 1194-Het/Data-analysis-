import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

st.set_page_config(layout="wide")

st.markdown("""
<style>
[data-testid="stFileUploader"] {
    width: 200px;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("Dynamic Chart")
message = st.empty()
message.subheader("WELCOME TO MY WEBSITE")
time.sleep(5)
message.empty()

file = st.sidebar.file_uploader("Upload CSV", type="csv")

if file:
    st.header("DATA ANALYSIS PLATFORM")
    df = pd.read_csv(file, encoding="latin1")

    column = st.selectbox("Select column", df.columns)

    data = df[column].value_counts()

    st.write(data)

    if st.button("Submit"):
        with st.spinner("wait for it......."):
         time.sleep(2)
         st.snow()

         st.success("Sucessfully deployed the data.")

        # Pie Chart
        fig1, ax1 = plt.subplots(figsize=(2,2))
        ax1.pie(
            data.values,
            labels=data.index,
            autopct="%1.1f%%",
            textprops={"fontsize": 8}
        )
        ax1.set_title("Pie Chart")
        st.pyplot(fig1)

        # Bar Chart
        fig2, ax2 = plt.subplots(figsize=(2,2))
        ax2.bar(data.index, data.values)
        ax2.set_title("Bar Chart",fontsize= 10)
        ax2.set_xlabel("column",fontsize=6)
        ax2.set_ylabel("Count",fontsize=6)
        plt.xticks(rotation=90)

        st.pyplot(fig2)