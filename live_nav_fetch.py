import requests
import pandas as pd
 
# Single Scheme (HDFC Top 100)
 
url = "https://api.mfapi.in/mf/125497"
res = requests.get(url).json()

df = pd.DataFrame(res.get("data", []))
df.to_csv("data/raw/HDFC_Top_100_nav.csv", index=False)

print("HDFC Top 100 data saved")

# Multiple Schemes
schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    res = requests.get(url).json()
    
    df = pd.DataFrame(res.get("data", []))
    df.to_csv(f"data/raw/{name}_nav.csv", index=False)
    
    print(f"{name} data saved")