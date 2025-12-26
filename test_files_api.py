import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("CLAUDE_API_KEY")
base_url = os.getenv("CLAUDE_BASE_URL", "https://api.anthropic.com/v1")

print(f"API Key: {api_key[:20]}...")
print(f"Base URL: {base_url}")

test_content = b"Hello, World!\nThis is a test file."

headers = {
    "x-api-key": api_key,
    "anthropic-version": "2023-06-01",
    "anthropic-beta": "files-api-2025-04-14"
}

files = {
    'file': ('test.txt', test_content, 'text/plain')
}

print("\n=== Testing Files API Upload ===")
print(f"URL: {base_url}/files")
print(f"Headers: {headers}")
print(f"File: test.txt, Size: {len(test_content)} bytes")

try:
    response = requests.post(
        f"{base_url}/files",
        headers=headers,
        files=files
    )
    
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}")
    print(f"Response Body: {response.text}")
    
    if response.status_code == 200:
        print("\n[SUCCESS] Upload successful!")
        data = response.json()
        print(f"File ID: {data.get('id')}")
        print(f"Filename: {data.get('filename')}")
        print(f"Type: {data.get('type')}")
    else:
        print("\n[FAILED] Upload failed!")
        
except Exception as e:
    print(f"\n[ERROR] Exception: {e}")
    if hasattr(e, 'response'):
        print(f"Response: {e.response.text}")
