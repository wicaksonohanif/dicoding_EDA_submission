import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Title for the Dashboard
st.title("Bike Sharing Dashboard 🚲")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Pilih tipe visualisasi:", ["Home", "Visualization 1", "Visualization 2"])

df_hour = pd.read_csv("all_data.csv")

# Define visualizations
if options == "Home":
    st.write("Sistem penyewaan sepeda adalah evolusi modern dari penyewaan sepeda tradisional, di mana proses seperti pendaftaran, peminjaman, dan pengembalian dilakukan secara otomatis. Dataset ini menarik untuk penelitian karena data yang dihasilkan memungkinkan untuk menganalisis pola mobilitas di kota, seperti durasi perjalanan, lokasi keberangkatan, dan lokasi tujuan.")
    st.write("Dataset yang digunakan berisi log historis selama dua tahun (2011-2012) dari sistem Capital Bikeshare di Washington D.C., AS.")
    st.write("Visualisasi dibuat untuk menjawab 2 pertanyaan, yaitu, Kapan waktu peminjaman sepeda yang paling ramai? Dan bagaimana pengaruh kondisi cuaca dan musim terhadap jumlah sepeda yang disewa?")
elif options == "Visualization 1":
    st.subheader("Visualization 1: Jumlah penyewaan berdasarkan waktu")
    # Total Penyewaan Sepeda per Jam
    hourly_counts = df_hour.groupby(by="hr").cnt.sum()
    plt.figure(figsize=(10, 6))
    plt.plot(hourly_counts.index, hourly_counts.values, marker='o', linestyle='-', color='#72BCD4')
    plt.title("Total Penyewaan Sepeda per Jam", fontsize=16)
    plt.xlabel("Jam (hr)", fontsize=14)
    plt.ylabel("Jumlah Penyewaan (cnt)", fontsize=14)
    plt.grid(alpha=0.5)
    plt.xticks(range(0, 24))
    st.pyplot(plt)

    # Total Penyewaan Sepeda per Hari
    days = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    daily_counts = df_hour.groupby(by="weekday").cnt.sum()
    plt.figure(figsize=(10, 6))
    plt.plot(daily_counts.index, daily_counts.values, marker='o', linestyle='-', color='#72BCD4')
    plt.title("Total Penyewaan Sepeda per Hari", fontsize=16)
    plt.xlabel("Hari (weekday)", fontsize=14)
    plt.ylabel("Jumlah Penyewaan (cnt)", fontsize=14)
    plt.grid(alpha=0.5)
    plt.xticks(range(0, 7), labels=days)
    st.pyplot(plt)
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
