# 🛰️ OctetHunter Networking Tool

A lightweight Python script to automate wireless NIC mode switching and initiate scanning with `airodump-ng`.

Kablosuz ağ kartınızı hızlıca `Monitor` moduna geçirip, pasif tarama başlatmak için hazırlanmış basit bir Python aracıdır.

---

## 🚀 Features / Özellikler

- 📡 Switch NIC to Monitor Mode automatically (Lazy Mode)
- 🧙 Manual mode: only switch to Monitor mode, you handle the rest
- 📴 Restore NIC back to Managed mode
- 📂 Automatic output directory creation
- 📝 Time-stamped scan results
- 🐧 Compatible with most Linux distros using `iwconfig` and `airodump-ng`

---

## 📦 Requirements / Gereksinimler

- Python 3.x
- `aircrack-ng` suite installed
- Root privileges (`sudo`)
- A wireless NIC that supports monitor mode

> **Note / Not:** `wlan1` interface is hardcoded. If your NIC uses another name (e.g., `wlan0`, `wlp3s0`), modify the script accordingly.

---

## 🛠️ Usage / Kullanım

```bash
python3 octethunter.py


Scenario Options / Senaryo Seçenekleri:



L - Lazy Mode
Full automation: switches to monitor mode and starts scanning.
Tam otomasyon: Monitor moda geçirir ve taramayı başlatır.




M - Manual Setup
Only sets monitor mode, you take over from there.
Sadece monitor moda alır, gerisini sen halledersin.




E - Exit / Restore
Reverts NIC back to Managed mode.
Ağ kartını tekrar yönetimli moda alır.







🗃️ Output Files / Çıktı Dosyaları

Scan results will be stored in the OctetHunterNetworkHub/ folder with a timestamped filename such as:

Scan_20250620_&H&M.cap




⚠️ Disclaimer / Yasal Uyarı


This tool is intended for educational and authorized network analysis purposes only.
Use it only on networks you own or have permission to test.




Bu araç sadece eğitim ve yetkili ağ testleri amacıyla kullanılmalıdır.
Sadece sahibi olduğunuz veya izinli olduğunuz ağlarda kullanınız.





📌 TODO


[ ] Interface detection instead of hardcoding wlan1

[ ] Support for multiple wireless chipsets

[ ] Add command-line arguments for automation

[ ] Real-time scanning visualization





👨‍💻 Author

OctetHunter Project
Hand-crafted by a caffeine-fueled mind.



📜 License

This project is licensed under the MIT License.