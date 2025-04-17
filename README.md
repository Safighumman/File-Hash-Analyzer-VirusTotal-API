# 🧬 File Hash Analyzer (VirusTotal API)

This Python tool allows you to scan file hashes (MD5, SHA1, SHA256) against VirusTotal to see if the file has been flagged as malicious by antivirus engines.

Built for learning malware detection basics and interacting with public threat intelligence APIs.

---

## 💡 Features

- Accepts any file type and auto-computes multiple hash types
- Queries VirusTotal for hash reputation
- Shows:
  - Total scan count
  - Detection count
  - Specific engines that flagged the file

---

## 🚀 Quick Start

### 1. Clone the Repository

    ```bash
git clone https://github.com/yourusername/file-hash-analyzer.git
cd file-hash-analyzer


### 2. Install Dependencies

pip install -r requirements.txt

### 3. Add Your API Key
Create a .env file with:
    VT_API_KEY=your_virustotal_api_key_here
---

## 🔬 How to Use
Run the tool and provide a file path:

    python3 hash_checker.py

Example:
    Enter file path: suspicious_file.exe


---
## 📸 Sample Output

[🔍] Scanning suspicious_file.exe...

SHA256: e3b0c44298fc1c149afbf4c8996...

[⚠️] Detected by 5 of 71 engines.
 - BitDefender: Gen:Trojan.Heur.FU.zq0@a2v2kcm
 - ESET-NOD32: a variant of Win32/Spy.Agent.A
 - Kaspersky: Trojan-Downloader.Win32.Agent

[✅] File is known and flagged as suspicious.

---
## ⚠️ Important Notes
VirusTotal does not allow scanning the file itself unless you're a premium user. This tool submits the hash only.

If the hash is unknown to VirusTotal, you’ll be informed.

---
## 🧠 Educational Value
Learn how malware is tracked via hashes

Explore antivirus engine results

Practice secure API use and hash algorithms

---
## 🌟 Like this project?
Give it a ⭐ and follow for more cybersecurity tools.
