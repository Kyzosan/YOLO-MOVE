# 🧠 YOLOv8 Object Detection (Interactive Menu)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange?style=for-the-badge&logo=ai)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8.0-blue?style=for-the-badge&logo=opencv)

Script deteksi objek canggih berbasis **YOLOv8** dengan interface menu interaktif yang user-friendly! 🎯

## ✨ Fitur Unggulan

<div align="center">

| 🖼️ Deteksi Gambar | 🎥 Deteksi Video | 📹 Live Camera |
|:---:|:---:|:---:|
| ✅ Format: JPG, PNG, JPEG | ✅ Format: MP4, AVI, MOV | ✅ Real-time detection |
| ✅ Multi-object detection | ✅ Frame-by-frame analysis | ✅ Smooth performance |
| ✅ High accuracy | ✅ Save processed video | ✅ Press 'q' to quit |

</div>

## 🚀 Quick Start

### 📥 Installasi Otomatis (Recommended)

```bash
git clone https://github.com/Kyzosan/YOLO-MOVE.git && cd YOLO-MOVE && chmod +x install.sh && ./install.sh && python3 main.py
```

<details>
<summary><strong>📦 Installasi Manual</strong></summary>

```bash
# Clone repository ini
git clone https://github.com/Kyzosan/YOLO-MOVE.git
cd YOLO-MOVE

# Install dependencies
pip install ultralytics opencv-python
```
</details>

## 🎮 Cara Penggunaan

Jalankan script dengan perintah:

```bash
python3 main.py
```

Akan muncul menu interaktif seperti ini:

```
🤖 YOLOv8 INTERACTIVE DETECTION
================================
Pilih mode deteksi:
1. 📁 Deteksi File (Gambar/Video)
2. 📹 Deteksi Langsung (Kamera)  
3. ❌ Keluar

Pilihan Anda [1-3]: 
```

### 🖼️ Mode 1: Deteksi File

```bash
# Contoh penggunaan
Masukkan path file (gambar/video): ./contoh.jpg
Model YOLO (default: yolov8n.pt): yolov8s.pt

✅ Deteksi berhasil! Hasil disimpan di: runs/detect/predict/contoh.jpg
```

### 📹 Mode 2: Deteksi Kamera

```bash
Camera ID (default: 0): 0
Model YOLO (default: yolov8n.pt): 

🎥 Kamera aktif! Tekan 'q' untuk keluar...
```

## 🎯 Model YOLOv8 yang Tersedia

| Model | Size | Speed | Accuracy | Use Case |
|:---|:---:|:---:|:---:|:---|
| **yolov8n.pt** | 🟢 Small | 🟢 Fast | 🟡 Medium | Default/Real-time |
| **yolov8s.pt** | 🟡 Small | 🟡 Medium | 🟡 Medium | Balanced |
| **yolov8m.pt** | 🟠 Medium | 🟠 Medium | 🟢 High | Recommended |
| **yolov8l.pt** | 🔴 Large | 🔴 Slow | 🟢 High | High Accuracy |
| **yolov8x.pt** | 🔴 X-Large | 🔴 Slow | 🟢 Best | Maximum Accuracy |

## 📁 Struktur Project

```
./
├── 📄 main.py          # Main script
├── 📄 install.sh              # Auto-install script
├── 📁 runs/detect/predict/    # Output directory
└── 📄 README.md              # Dokumentasi ini
```

## 🛠️ Troubleshooting

<details>
<summary><strong>🔧 Masalah Umum & Solusi</strong></summary>

### ❌ Error: "Module not found"
```bash
# Solution: Install ulang dependencies
pip install -r requirements.txt
```

### ❌ Error: "Camera not accessible"
```bash
# Solution: Ganti camera ID
Camera ID (default: 0): 1
```

### ❌ Error: "Model not found"
```bash
# Solution: Model akan otomatis di-download
# Atau download manual:
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
```
</details>

## 🤝 Contributing

Mari berkontribusi! 🎉

1. Fork project ini
2. Buat feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Developer

**Kyzo** - [GitHub Profile](https://github.com/kyzosan)

<div align="center"> 

**Happy Detecting!** 🚀🧠

</div>

---

<div align="center">

![YOLOv8](https://img.shields.io/badge/Powered%20by-YOLOv8-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python)

</div>
