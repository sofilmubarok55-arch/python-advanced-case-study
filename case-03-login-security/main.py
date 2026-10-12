# case-03-login-security/main.py
import re
from datetime import datetime
from functools import wraps

def audit_log(func):
    """
    Decorator / Closure untuk mencatat riwayat audit trail login secara otomatis.
    Merekam waktu, nama user, dan status (berhasil/ditolak) tanpa mengubah fungsi utama.
    """
    @wraps(func)
    def wrapper(self, password_input, *args, **kwargs):
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        username_coba = self.username
        
        try:
            # Mencoba menjalankan fungsi login utama
            hasil = func(self, password_input, *args, **kwargs)
            print(f"[{waktu}] AUDIT: User '{username_coba}' - Status: BERHASIL")
            return hasil
        except ValueError as e:
            # Jika fungsi login error/menolak, catat alasan penolakannya
            print(f"[{waktu}] AUDIT: User '{username_coba}' - Status: DITOLAK | Alasan: {e}")
            raise e
            
    return wrapper

class User:
    def __init__(self, username, password):
        self.username = username  # Otomatis memicu setter property username
        self.password = password  # Otomatis memicu setter property password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        # RegEx: minimal 5 karakter, hanya huruf (a-z, A-Z) dan angka (0-9)[cite: 4]
        pattern = r"^[a-zA-Z0-9]{5,}$"
        if not re.match(pattern, value):
            raise ValueError("Username tidak valid (minimal 5 karakter, alfanumerik tanpa spasi/simbol)[cite: 4].")
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        # RegEx / Aturan: minimal 8 karakter dan wajib ada minimal 1 angka[cite: 4]
        if len(value) < 8 or not re.search(r"\d", value):
            raise ValueError("Password tidak valid (minimal 8 karakter dan harus mengandung minimal 1 angka)[cite: 4].")
        self._password = value

    @audit_log
    def login(self, password_input):
        """Fungsi login yang dibungkus oleh decorator audit_log."""
        if self.password == password_input:
            print("--> Akses Diberikan: Selamat datang di sistem!")
            return True
        else:
            raise ValueError("Password salah.")

def main():
    print("=== PENGUJIAN SISTEM KEAMANAN AKUN & AUDIT LOG ===")
    
    # Skenario 1: Login gagal akibat format username salah (mengandung simbol '!')[cite: 5]
    print("\n--- Skenario 1: Username Invalid ---")
    try:
        user1 = User("user!", "Password123")
    except ValueError as e:
        print(f"Error ditangkap: {e}")

    # Skenario 2: Login gagal akibat password terlalu pendek atau tidak ada angka[cite: 5]
    print("\n--- Skenario 2: Password Invalid ---")
    try:
        user2 = User("devpython", "rahasia")
    except ValueError as e:
        print(f"Error ditangkap: {e}")

    # Skenario 3: Akun valid dibuat, lalu diuji login sukses dan gagal (tercatat audit log)[cite: 5]
    print("\n--- Skenario 3: Uji Coba Login dengan Audit Trail ---")
    valid_user = User("coderpro", "SecurePass2026")
    
    # Percobaan 1: Password salah (Gagal)
    try:
        valid_user.login("SalahPassword")
    except ValueError:
        pass

    # Percobaan 2: Password benar (Berhasil)
    try:
        valid_user.login("SecurePass2026")
    except ValueError:
        pass

if __name__ == "__main__":
    main()