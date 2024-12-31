import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Title for the Dashboard
st.title("Bike Sharing Dashboard 🚲")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Pilih tipe visualisasi:", ["Home", "Visualization 1", "Visualization 2"])

# Load the dataset
df_hour = pd.read_csv("all_data.csv")

# Viz 1
if options == "Visualization 1":
    st.subheader("Visualization 1: Jumlah penyewaan berdasarkan waktu dengan filter")
    
    year_filter = st.sidebar.selectbox("Pilih Tahun:", [2011, 2012])
    month_filter = st.sidebar.selectbox(
        "Pilih Bulan:", 
        ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
         "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    )
    
    month_mapping = {
        "Januari": 1, "Februari": 2, "Maret": 3, "April": 4, "Mei": 5, "Juni": 6,
        "Juli": 7, "Agustus": 8, "September": 9, "Oktober": 10, "November": 11, "Desember": 12
    }
    
    filtered_data = df_hour[(df_hour['yr'] == (year_filter - 2011)) & 
                            (df_hour['mnth'] == month_mapping[month_filter])]
    
    if filtered_data.empty:
        st.write("Tidak ada data untuk bulan dan tahun yang dipilih.")
    else:
        plt.figure(figsize=(12, 6))
        sns.barplot(
            x=filtered_data.groupby('hr')['cnt'].sum().index, 
            y=filtered_data.groupby('hr')['cnt'].sum().values, 
            palette="Blues_d"
        )
        plt.title(f"Jumlah Penyewaan Sepeda per Jam ({month_filter} {year_filter})", fontsize=16)
        plt.xlabel("Jam (hr)", fontsize=14)
        plt.ylabel("Jumlah Penyewaan (cnt)", fontsize=14)
        plt.xticks(range(0, 24))
        plt.grid(alpha=0.3)
        st.pyplot(plt)

# viz 2
elif options == "Visualization 2":
    st.subheader("Visualization 2: Jumlah penyewaan berdasarkan cuaca dan musim")
     # Penyewaan Berdasarkan Cuaca
    weathers = ['cerah', 'berawan', 'hujan/salju', 'badai']
    weatherly_counts = df_hour.groupby(by="weathersit").cnt.sum()
    plt.figure(figsize=(10, 6))
    weatherly_counts.plot(kind='bar', color='#72BCD4')
    plt.title('Jumlah penyewa berdasarkan cuaca')
    plt.xlabel('Cuaca (weathersit)', fontsize=14)
    plt.ylabel('Jumlah Penyewaan (cnt)', fontsize=14)
    for i, count in enumerate(weatherly_counts):
        plt.text(i, count + 1, str(count), ha='center', va='bottom')
    plt.xticks(range(0, 4), labels=weathers, rotation=0)
    plt.tight_layout()
    st.pyplot(plt)

    # Penyewaan Berdasarkan Musim
    seasons = ['semi', 'panas', 'gugur', 'dingin']
    seasonly_counts = df_hour.groupby(by="season").cnt.sum()
    plt.figure(figsize=(10, 6))
    seasonly_counts.plot(kind='bar', color='#72BCD4')
    plt.title('Jumlah penyewa berdasarkan musim')
    plt.xlabel('Musim (season)', fontsize=14)
    plt.ylabel('Jumlah Penyewaan (cnt)', fontsize=14)
    for i, count in enumerate(seasonly_counts):
        plt.text(i, count + 1, str(count), ha='center', va='bottom')
    plt.xticks(range(0, 4), labels=seasons, rotation=0)
    plt.tight_layout()
    st.pyplot(plt)