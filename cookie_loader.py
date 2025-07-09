def load_cookies_from_txt(file_path):
    cookies = []
    with open(file_path, "r") as f:
        for line in f:
            if not line.startswith("#") and line.strip():
                parts = line.strip().split("\t")
                if len(parts) == 7:
                    domain, flag, path, secure, expiry, name, value = parts
                    cookies.append({
                        "domain": domain,
                        "name": name,
                        "value": value,
                        "path": path,
                        "secure": secure == "TRUE",
                    })
    return cookies
