# 🔳 Advanced QR Code Generator in Python

![QR Code Preview](https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=https://example.com)

> A clean and powerful QR Code Generator built in Python 🐍 — with **custom color support**, **optional logo embedding**, **high error correction**, and **timestamped auto-saving**. Ideal for students, developers, creators, and small businesses.

---

## 📌 Features

✅ **Custom Fill & Background Colors**  
✅ **Optional Center Logo (Branding Support)**  
✅ **High Error Correction (H Level: 30%)**  
✅ **Saves with Timestamp to Avoid Overwrite**  
✅ **Instant Image Preview**  
✅ **Offline & Lightweight – No Internet Needed**

---

## 🧠 How It Works

```mermaid
flowchart TD
    A[Start: User Runs Script] --> B[Enter URL or Text]
    B --> C{Custom Colors?}
    C -->|Yes| D[Input Fill & Background Colors]
    C -->|No| E[Use Default Colors]
    D --> F[Generate QR Code]
    E --> F
    F --> G{Add Logo?}
    G -->|Yes| H[Check for logo.png]
    H -->|Found| I[Embed Logo in Center]
    H -->|Not Found| J[Skip Logo with Warning]
    G -->|No| J
    I --> K[Save QR Code with Timestamp]
    J --> K
    K --> L[Open QR Image Preview]
    L --> M[Done ✅]
