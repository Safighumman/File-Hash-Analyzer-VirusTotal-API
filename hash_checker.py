
---

## 🐍 `hash_checker.py` (Main Script)

```python
import hashlib
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("VT_API_KEY")
HEADERS = {"x-apikey": API_KEY}

VT_BASE_URL = "https://www.virustotal.com/api/v3/files"

def compute_hashes(file_path):
    hashes = {'md5': '', 'sha1': '', 'sha256': ''}
    with open(file_path, 'rb') as f:
        file_bytes = f.read()
        hashes['md5'] = hashlib.md5(file_bytes).hexdigest()
        hashes['sha1'] = hashlib.sha1(file_bytes).hexdigest()
        hashes['sha256'] = hashlib.sha256(file_bytes).hexdigest()
    return hashes

def check_virustotal(sha256):
    url = f"{VT_BASE_URL}/{sha256}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        stats = data["data"]["attributes"]["last_analysis_stats"]
        print(f"\n[⚠️] Detected by {stats['malicious']} of {sum(stats.values())} engines.")

        for engine, result in data["data"]["attributes"]["last_analysis_results"].items():
            if result["category"] == "malicious":
                print(f" - {engine}: {result['result']}")
    elif response.status_code == 404:
        print("\n[ℹ️] Hash not found on VirusTotal. Possibly a clean or unknown file.")
    else:
        print(f"\n[!] API error: {response.status_code} - {response.text}")

def main():
    print("=== File Hash Analyzer ===")
    file_path = input("Enter path to the file: ").strip()

    if not os.path.exists(file_path):
        print("[!] File not found.")
        return

    print(f"\n[🔍] Scanning {os.path.basename(file_path)}...")

    hashes = compute_hashes(file_path)
    print(f"\nSHA256: {hashes['sha256']}")
    check_virustotal(hashes['sha256'])

if __name__ == "__main__":
    main()
