user_url = input("Enter a website URL: ").strip().lower()

# Check protocol
if user_url.startswith("https://"):
    print("🔐 Secure website")
elif user_url.startswith("http://"):
    print("⚠️ Not secure website")
else:
    print("🤔 Unknown or missing protocol")

# Check domain type
if user_url.endswith(".com"):
    print("🌐 This is a commercial website (.com)")
elif user_url.endswith(".org"):
    print("📘 This is an organization website (.org)")
else:
    print("🔎 Other or unknown domain type")

