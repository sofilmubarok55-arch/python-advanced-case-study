# case-02-iot-generator/main.py
import random
import time

def sensor_suhu_generator(jumlah_data=10):
    """
    Generator function untuk mensimulasikan pembacaan suhu IoT secara bertahap.
    Menggunakan 'yield' agar memori tidak penuh menampung data sekaligus.
    """
    for _ in range(jumlah_data):
        # Menghasilkan angka desimal suhu acak antara 15.0 hingga 38.0 derajat Celcius
        suhu = round(random.uniform(15.0, 38.0), 1)
        
        # 'yield' menyerahkan nilai suhu satu per satu, lalu fungsi berhenti sejenak
        yield suhu

def kategorisasi_suhu(suhu):
    """Mengelompokkan status suhu berdasarkan aturan soal."""
    if suhu < 20.0:
        return "Dingin"
    elif 20.0 <= suhu <= 30.0:
        return "Normal"
    else:
        return "Panas"

def main():
    print("=== MONITORING STREAMING DATA SENSOR IOT ===")
    
    # 1. Inisialisasi generator (menyiapkan aliran data)
    stream_sensor = sensor_suhu_generator(12)

    # 2. Konsumsi data satu per satu sebanyak 10 kali putaran di terminal
    for i in range(1, 11):
        try:
            # Mengambil data suhu berikutnya dari generator menggunakan next()
            suhu_sekarang = next(stream_sensor)
            
            # Kategorikan suhunya
            status = kategorisasi_suhu(suhu_sekarang)
            
            # Tampilkan ke terminal dengan rapi
            print(f"Pembacaan ke-{i:02d} | Suhu: {suhu_sekarang}°C | Status: {status}")
            
            # Memberikan jeda waktu 0.3 detik agar terlihat seperti data streaming nyata
            time.sleep(0.3)
            
        except StopIteration:
            break

if __name__ == "__main__":
    main()