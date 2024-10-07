import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Streamlit simple app')

page = st.sidebar.radio("Pilih Halaman", ["Dataset", "Visualisasi"])

if page == "Dataset":
    st.header("Halaman Dataset")

    # Load dataset
    data = pd.read_csv("pddikti_example.csv")
    st.write(data)

elif page == "Visualisasi":
    st.header("Halaman Visualisasi")

    # Load dataset
    data = pd.read_csv("pddikti_example.csv")

    # Dropdown to select university
    selected_university = st.selectbox("Pilih Universitas", data['universitas'].unique())
    filtered_data = data[data['universitas'] == selected_university]

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12,6))

    for prog_studi in filtered_data['program_studi'].unique():
        subset = filtered_data[filtered_data['program_studi'] == prog_studi]
        subset = subset.sort_values(by="id", ascending=False)

        # Plot each program on the axis
        ax.plot(subset['semester'], subset['jumlah'], label=prog_studi)

    ax.set_title(f"Visualisasi Data Untuk {selected_university}")
    ax.set_xlabel('Semester')
    ax.set_xticklabels(subset['semester'], rotation=90)
    ax.set_ylabel('Jumlah')
    ax.legend()

    # Pass the figure to st.pyplot()
    st.pyplot(fig)