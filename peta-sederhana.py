import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# 1. Buat Graph kosong (menggunakan NetworkX)
G = nx.Graph()

# 2. Tambah 10 vertex (kota nyata)
cities = [
    "Jakarta", "Surabaya", "Bandung", "Medan", "Semarang",
    "Makassar", "Palembang", "Batam", "Balikpapan", "Samarinda"
]
G.add_nodes_from(cities)

# 3. Daftar edge dan jarak nyata (km)
edges_with_distance = [
    ("Jakarta", "Bandung", 150),
    ("Jakarta", "Semarang", 450),
    ("Jakarta", "Surabaya", 780),
    ("Jakarta", "Palembang", 430),
    ("Jakarta", "Batam", 850),
    ("Bandung", "Semarang", 350),
    ("Bandung", "Surabaya", 690),
    ("Surabaya", "Semarang", 350),
    ("Surabaya", "Makassar", 1600),
    ("Surabaya", "Balikpapan", 1500),
    ("Semarang", "Balikpapan", 1200),
    ("Semarang", "Palembang", 800),
    ("Palembang", "Batam", 500),
    ("Palembang", "Medan", 1400),
    ("Batam", "Medan", 900),
    ("Medan", "Makassar", 2700),
    ("Makassar", "Balikpapan", 900),
    ("Makassar", "Samarinda", 1000),
    ("Balikpapan", "Samarinda", 115),
    ("Samarinda", "Medan", 3200),
    # Tambahan edge agar total 30 (acak, isi dengan estimasi)
    ("Bandung", "Batam", 1200),
    ("Bandung", "Palembang", 900),
    ("Surabaya", "Palembang", 1200),
    ("Semarang", "Batam", 1300),
    ("Jakarta", "Makassar", 1400),
    ("Jakarta", "Balikpapan", 1500),
    ("Bandung", "Makassar", 1600),
    ("Medan", "Balikpapan", 2500),
    ("Batam", "Makassar", 1800),
    ("Palembang", "Samarinda", 2200)
]

# Tambahkan edge ke graph
for city1, city2, distance in edges_with_distance:
    G.add_edge(city1, city2, weight=distance)

# 4. Simpan graph ke adjacency list (dictionary)
adjacency_list = {city: {} for city in cities}
for city1, city2, data in G.edges(data=True):
    distance = data['weight']
    adjacency_list[city1][city2] = distance
    adjacency_list[city2][city1] = distance  # karena graph tidak berarah

# (Opsional) Cetak adjacency list
print("Adjacency List (Jarak dalam KM):")
for city, neighbors in adjacency_list.items():
    print(f"{city}: {neighbors}")

# Gambar grafnya
pos = nx.circular_layout(G)
edge_labels = nx.get_edge_attributes(G, 'weight')

# Buat colormap dan mapping warna untuk setiap kota
color_map = plt.get_cmap('tab10', len(cities))
city_colors = {city: color_map(i) for i, city in enumerate(cities)}

# Buat list warna edge berdasarkan kota asal (city1)
edge_colors = []
for city1, city2 in G.edges():
    edge_colors.append(city_colors[city1])

plt.figure(figsize=(12, 9))
nx.draw(
    G, pos, with_labels=True, node_color='lightblue', node_size=2500,
    font_size=8, font_weight='bold', edge_color=edge_colors, width=2
)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Graf Kota Indonesia (10 Vertex, 30 Edge, Bobot = Jarak Tempuh KM)")
plt.axis('off')
plt.show()

import itertools
import heapq

### === A. DIJKSTRA === ###
def dijkstra(graph, start, goal):
    queue = [(0, start, [])]  # (total_weight, current_city, path_so_far)
    visited = set()

    while queue:
        (cost, city, path) = heapq.heappop(queue)

        if city in visited:
            continue
        visited.add(city)

        path = path + [city]

        if city == goal:
            return path, cost

        for neighbor in graph[city]:
            if neighbor not in visited:
                total_cost = cost + graph[city][neighbor]
                heapq.heappush(queue, (total_cost, neighbor, path))

    return None, float('inf')

# ==== Tes Dijkstra ====
print("\n=== DIJKSTRA ===")
src = input("Masukkan kota asal: ")
dst = input("Masukkan kota tujuan: ")

if src in adjacency_list and dst in adjacency_list:
    shortest_path, total_distance = dijkstra(adjacency_list, src, dst)
    print(f"Jalur tercepat dari {src} ke {dst}: {' -> '.join(shortest_path)}")
    print(f"Total jarak: {total_distance} km")
else:
    print("Nama kota tidak ditemukan!")



### === B. TRAVELING SALESMAN PROBLEM (Brute Force) === ###
def tsp_brute_force(graph, cities):
    min_path = None
    min_cost = float('inf')

    # semua kemungkinan rute (tidak perlu kembali ke awal)
    for perm in itertools.permutations(cities):
        cost = 0
        valid = True

        for i in range(len(perm) - 1):
            c1, c2 = perm[i], perm[i + 1]
            if c2 in graph[c1]:
                cost += graph[c1][c2]
            else:
                valid = False
                break

        if valid and cost < min_cost:
            min_cost = cost
            min_path = perm

    return min_path, min_cost

# ==== Tes TSP ====
print("\n=== TSP (Traveling Salesman Problem) ===")
best_path, best_cost = tsp_brute_force(adjacency_list, cities)
print("Rute terbaik untuk mengunjungi semua kota sekali:")
print(" -> ".join(best_path))
print(f"Total jarak tempuh: {best_cost} km")
