# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech
Submission Pertama: Menyelesaikan Permasalahan Human Resources Perusahan JAYA JAYA MAJU

## Business Understanding

### Latar Belakang Bisnis
Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

Untuk mencegah hal ini semakin parah, manajer departemen HR ingin meminta bantuan Anda mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, ia juga meminta Anda untuk membuat business dashboard untuk membantunya memonitori berbagai faktor tersebut. Selain itu, mereka juga telah menyediakan dataset yang dapat Anda unduh melalui tautan berikut: [Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee).

### Permasalahan Bisnis

Berdasarkan latar belakang yang telah dijelaskan, terdapat beberapa permasalahan bisnis utama yang perlu diselesaikan:

1. **Tingginya Attrition Rate**  
   Persentase karyawan yang keluar dari perusahaan melebihi 10%, yang dapat berdampak negatif terhadap stabilitas operasional dan efisiensi kerja.

2. **Minimnya Pemahaman terhadap Faktor-Faktor Penyebab Attrition**  
   HR Department belum memiliki gambaran yang jelas tentang variabel apa saja yang paling berpengaruh terhadap keputusan karyawan untuk keluar, seperti tingkat kepuasan kerja, gaji, jarak ke tempat kerja, atau beban kerja.

3. **Tidak Tersedianya Sistem Monitoring Berbasis Data**  
   Saat ini tidak ada *business dashboard* yang bisa digunakan oleh manajer HR untuk memantau faktor-faktor risiko yang berkontribusi terhadap *attrition* secara *real-time* atau periodik.

4. **Kesulitan Mengambil Keputusan Strategis Berbasis Data**  
   Tanpa adanya *insight* yang akurat, HR akan kesulitan dalam merancang strategi retensi karyawan yang efektif dan berbasis data (*data-driven decision-making*).


### Cakupan Proyek

Untuk menyelesaikan permasalahan di atas, proyek ini akan memiliki cakupan sebagai berikut:

1. **Eksplorasi dan Analisis Data**  
   - Mengunduh dan memahami struktur dataset yang disediakan.  
   - Membersihkan data (*data cleaning*) dari nilai yang hilang atau tidak konsisten.  
   - Melakukan analisis eksploratif (*EDA*) untuk mengidentifikasi pola dan hubungan antar fitur terhadap *attrition*.

2. **Identifikasi Faktor Penyebab Tingginya Attrition**  
   - Menggunakan teknik statistik dan visualisasi untuk mengukur korelasi fitur-fitur dengan *attrition*.

3. **Pembuatan Business Dashboard Interaktif**  
   - Mendesain dashboard menggunakan **Metabase** dan menyambungkannya dengan **Supabase** sebagai basis data.  
   - Dashboard akan menampilkan metrik-metrik penting seperti tingkat *attrition* per divisi, tren kepuasan kerja, rata-rata gaji, dan beban kerja.

4. **Pembuatan Model Prediksi Attrition**  
   - Mengembangkan model *machine learning* untuk memprediksi kemungkinan seorang karyawan akan keluar dari perusahaan.  
   - Melakukan pelatihan dan evaluasi model.

### Persiapan

**Sumber data**: Dataset disediakan oleh perusahaan Jaya Jaya Maju dan dapat diakses melalui tautan berikut:  
[https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

---

**Setup Environment**:

1. **Buat virtual environment** (opsional tapi disarankan):

    ```bash
         python -m venv venv
    ```
2. **Aktifkan virtual environment**:

    Windows:
    
    ```bash
    .\venv\Scripts\activate
    ```
    macOS/Linux:
    
    ```
    source venv/bin/activate
    ```

3. **Instal semua dependensi dari requirements.txt**:
  ```
  pip install -r requirements.txt
  ```
4. **Jalankan Notebook Analisis**:

  Buka file hr_attrition_notebook.ipynb menggunakan Jupyter Notebook atau VSCode Jupyter, lalu jalankan seluruh sel untuk melakukan eksplorasi dan analisis data.

5. **Deploy Model Menggunakan Gradio**:

Tersedia file bernama gradio_deployment.py yang dapat dijalankan untuk menyajikan model prediksi dalam antarmuka web sederhana berbasis Gradio.

Jalankan dengan:

```
python gradio_deployment.py
```

Koneksi ke Dashboard Metabase:

Proyek ini juga dilengkapi dengan dashboard interaktif menggunakan Metabase, yang menyimpan konfigurasinya dalam file metabase.db.mv. Untuk masuk ke Metabase, gunakan kredensial berikut:

> Email: mrizki135790@gmail.com

> Password: dG8M@BWcewxUtxc
---
## Business Dashboard
# 📈 HR Attrition Monitoring Dashboard

Dashboard ini dirancang untuk memantau dan menganalisis tingkat **attrition** (perpindahan atau pengunduran diri karyawan) dari berbagai perspektif, seperti departemen, usia, pendidikan, status pernikahan, dan frekuensi perjalanan bisnis.

## 🔍 Highlight Utama
- **Total Karyawan:** 1.058 orang  
- **Total Attrition:** 179 orang  
- **Tingkat Attrition Keseluruhan:** 16,92%  
- **Rata-rata Masa Kerja:** 7 tahun  
- **Pendapatan Bulanan Rata-rata:** $6.625,95  

## 📊 Visualisasi & Analisis Data

### 1. Distribusi Attrition per Departemen
- Departemen **R&D** mencatat jumlah attrition tertinggi (**107 orang**).
- Disusul oleh **Sales (66 orang)** dan **Human Resources (6 orang)**.

### 2. Distribusi Usia Karyawan
- Sebagian besar karyawan berada di rentang usia **30–39 tahun**, diikuti oleh usia **40–49 tahun**.

### 3. Tingkat Attrition Berdasarkan Bidang Pendidikan
- Lulusan dengan **Technical Degree** memiliki tingkat attrition tertinggi (**24,2%**).
- Disusul oleh bidang **Marketing (19,8%)**.

### 4. Distribusi Bidang Pendidikan
- Mayoritas karyawan berlatar belakang **Life Sciences** dan **Marketing**.

### 5. Attrition Berdasarkan Status Pernikahan
- Karyawan dengan status **Single** dan **Divorced** memiliki tingkat attrition lebih tinggi dibandingkan yang **Married**.

### 6. Tingkat Attrition Berdasarkan Frekuensi Perjalanan Bisnis
- Karyawan yang sering bepergian (**Travel Frequently**) cenderung memiliki risiko attrition lebih tinggi.

## 🤖 Ringkasan Akhir – Pipeline Machine Learning

🎉 **Proses Machine Learning Selesai dengan Sukses!**

### 🔬 Hasil Evaluasi Model:
- **Model Terbaik:** *Logistic Regression*  
- **F1-Score:** 0.5714 → menggambarkan keseimbangan antara presisi dan recall  
- **Akurasi:** 87,26% → menunjukkan ketepatan model dalam memprediksi attrition  
- **ROC-AUC:** 0.8205 → menunjukkan kemampuan model membedakan antara attrition dan non-attrition

### 💾 Output Disimpan di Folder:
`hr_attrition_results_[timestamp]/`
- Model terlatih  
- Hasil prediksi dan probabilitas  
- Metode evaluasi performa  
- Laporan evaluasi lengkap 

### 🚀 Langkah Selanjutnya:
1. Tinjau laporan evaluasi model secara rinci  
2. Analisis fitur yang berpengaruh terhadap attrition  
3. Terapkan model untuk prediksi pada data karyawan aktif  
4. Siapkan sistem monitoring & jadwal retraining berkala  
5. Buat strategi retensi bagi karyawan berisiko tinggi  

✅ **Analisis Selesai!**

---

## 🧾 Kesimpulan

Proyek ini berhasil membangun **dashboard interaktif** dan **pipeline machine learning** yang mampu:
- Memberikan gambaran menyeluruh terkait karakteristik karyawan yang mengundurkan diri
- Mengidentifikasi faktor-faktor utama penyebab attrition
- Memprediksi karyawan dengan risiko tinggi untuk mendukung pengambilan keputusan HR

Dengan tingkat akurasi sebesar **87,26%**, model prediktif ini bisa menjadi alat bantu dalam **strategi retensi karyawan jangka panjang**.

---

## ✅ Rekomendasi Tindak Lanjut

- 🧪 **Investigasi Departemen R&D:** Lakukan survei atau interview mendalam untuk mengetahui penyebab tingginya attrition.  
- 🧘‍♀️ **Perbaiki Work-Life Balance:** Terutama untuk karyawan yang sering melakukan perjalanan dinas.  
- ❤️ **Program Retensi untuk Karyawan Single & Divorced:** Ciptakan lingkungan kerja yang lebih suportif.  
- 📈 **Evaluasi Benefit Lulusan Technical Degree:** Tawarkan peluang pengembangan karir yang lebih baik.  
- 🧠 **Gunakan Model Prediktif:** Terapkan hasil prediksi untuk identifikasi dan intervensi karyawan berisiko tinggi sebelum mereka mengundurkan diri.  

---

> 🧩 *Catatan:* Proyek ini dapat dikembangkan lebih lanjut dengan integrasi **dashboard real-time**, **automasi retraining model**, dan **penggunaan feedback loop dari tim HR**.

