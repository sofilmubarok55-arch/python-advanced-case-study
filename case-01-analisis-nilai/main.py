# case-01-analisis-nilai/main.py

# Data awal mahasiswa dengan tambahan 2 data baru
data_mahasiswa = [
    {"nama": "Aisyah", "nim": "230101", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Budi", "nim": "230102", "tugas": 70, "uts": 65, "uas": 75},
    {"nama": "Cantika", "nim": "230103", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Dedi", "nim": "230104", "tugas": 78, "uts": 82, "uas": 80},
    {"nama": "Eka", "nim": "230105", "tugas": 95, "uts": 90, "uas": 94}
]

def hitung_nilai_akhir(mhs):
    return (mhs["tugas"] * 0.3) + (mhs["uts"] * 0.3) + (mhs["uas"] * 0.4)

def main():
    # 1. Hitung Nilai Akhir menggunakan List Comprehension
    list_nilai = [
        {
            "nama": mhs["nama"],
            "nim": mhs["nim"],
            "nilai_akhir": round(hitung_nilai_akhir(mhs), 2)
        }
        for mhs in data_mahasiswa
    ]

    # 3. Pemeringkatan (Ranking) dari tinggi ke rendah menggunakan lambda
    ranking = sorted(list_nilai, key=lambda x: x["nilai_akhir"], reverse=True)

    print("=== PEMERINGKATAN MAHASISWA ===")
    for idx, mhs in enumerate(ranking, start=1):
        print(f"Peringkat {idx}: {mhs['nama']} (NIM: {mhs['nim']}) - Nilai Akhir: {mhs['nilai_akhir']}")

    # 2. Filter Mahasiswa Berprestasi (Nilai > 80) tanpa for loop bertingkat
    berprestasi = [mhs for mhs in ranking if mhs["nilai_akhir"] > 80]

    print("\n=== MAHASISWA BERPRESTASI (Nilai > 80) ===")
    for mhs in berprestasi:
        print(f"- {mhs['nama']} ({mhs['nilai_akhir']})")

    # 4. Mahasiswa Terbaik (Peringkat Pertama)
    terbaik = ranking[0]
    print(f"\n=== MAHASISWA TERBAIK ===")
    print(f"Selamat kepada {terbaik['nama']} (NIM: {terbaik['nim']}) dengan nilai akhir tertinggi: {terbaik['nilai_akhir']}")

if __name__ == "__main__":
    main()