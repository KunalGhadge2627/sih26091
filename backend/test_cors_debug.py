from dotenv import load_dotenv
load_dotenv()
import os

_raw_origins = os.getenv("ALLOWED_ORIGINS", "")
_custom_origins = [o.strip() for o in _raw_origins.split(",") if o.strip()]
_dev_origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
allowed_origins = list(set(_custom_origins + _dev_origins)) if _custom_origins else _dev_origins
print("raw:", repr(_raw_origins))
print("custom:", _custom_origins)
print("allowed:", allowed_origins)
print("has http://localhost:3000:", "http://localhost:3000" in allowed_origins)
