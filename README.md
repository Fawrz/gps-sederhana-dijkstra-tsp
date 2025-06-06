# GPS Sederhana: Implementasi Graf, Dijkstra, dan TSP

## 📜 Deskripsi Proyek

[cite_start]Proyek ini adalah implementasi tugas akhir mata kuliah **Struktur Data** yang bertujuan untuk membangun simulasi Peta dan GPS sederhana.  [cite_start]Program ini memodelkan jaringan 10 kota di Indonesia sebagai sebuah graf berbobot, di mana bobotnya adalah estimasi jarak antar kota. 

Aplikasi ini mengimplementasikan dua algoritma pathfinding utama:
1.  [cite_start]**Algoritma Dijkstra:** Untuk menemukan rute terpendek antara dua kota yang dipilih. 
2.  [cite_start]**Traveling Salesman Problem (TSP):** Menggunakan metode brute-force untuk menemukan rute paling efisien yang mengunjungi semua kota tepat satu kali. 

[cite_start]Proyek ini disusun oleh mahasiswa Program Studi D4 Manajemen Informatika, Fakultas Vokasi, Universitas Negeri Surabaya. 

## ✨ Fitur Utama

* [cite_start]**Representasi Graf:** Membangun graf dari 10 kota dan 30 jalur menggunakan **Adjacency List**. 
* [cite_start]**Pencarian Rute Terpendek (Dijkstra):** Menghitung jalur dengan total jarak minimum antara dua kota pilihan pengguna. 
* [cite_start]**Pencarian Tur Efisien (TSP):** Menemukan rute terpendek yang mengunjungi semua kota dari titik awal yang ditentukan (menggunakan brute-force). 
* **Antarmuka Berbasis Teks:** Menu interaktif yang memungkinkan pengguna memilih algoritma yang ingin dijalankan.
* [cite_start]**Visualisasi Graf:** Menampilkan peta jaringan kota secara visual menggunakan `networkx` dan `matplotlib`. 

## 🛠️ Teknologi yang Digunakan

* **Bahasa Pemrograman:** Python
* **Library:**
    * `heapq`: Untuk implementasi *priority queue* pada algoritma Dijkstra.
    * [cite_start]`itertools`: Untuk menghasilkan permutasi pada algoritma TSP. 
    * [cite_start]`networkx`: Sebagai alat bantu untuk visualisasi graf. 
    * [cite_start]`matplotlib`: Untuk menampilkan plot/gambar visualisasi graf. 
