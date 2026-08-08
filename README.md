# EviltechHackZz - Multi-Platform Ban Checker

![Version](https://img.shields.io/badge/version-1.0-red)
![Author](https://img.shields.io/badge/author-SavageHackZz-lightgrey)

A powerful multi-platform account ban checker written in Python. Check if accounts are banned, suspended, or active across **WhatsApp**, **Facebook**, **Twitter/X**, **Instagram**, **TikTok**, **Telegram** (username + phone), **Discord**, and **Snapchat**.

---

## 🚀 Features

| # | Platform   | Method                | Input Type      |
|---|------------|-----------------------|-----------------|
| 1 | WhatsApp   | Meta Web API lookup   | Phone number    |
| 2 | Facebook   | Profile page scraping | Username        |
| 3 | Twitter/X  | Profile page scraping | Username        |
| 4 | Instagram  | Profile page scraping | Username        |
| 5 | TikTok     | Profile page scraping | Username        |
| 6 | Telegram   | Web profile lookup    | Username (@)    |
| 7 | Telegram   | **MTProto API**       | **Phone number**|
| 8 | Discord    | User ID lookup        | User ID         |
| 9 | Snapchat   | Profile page scraping | Username        |

---

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Internet connection

### Steps

```bash
# 1. Clone or download the project
cd SavageHackZz

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create a .env file with your Telegram API credentials (see below)

# 4. Run the tool
python main.py
```

### Requirements
- `colorama` — Colored terminal output
- `httpx` — HTTP requests for web scraping
- `python-dotenv` — Load environment variables
- `telethon` — Telegram MTProto client (for phone number check)

---

## 🔑 Configure Telegram API Keys (Mandatory for Telegram Phone Checker)

The **Telegram Phone Check** (option 9) uses Telegram's MTProto protocol via `Telethon`. This requires your own `API_ID` and `API_HASH`.

### Step 1: Get your API credentials
1. Visit **[my.telegram.org](https://my.telegram.org/)**
2. Log in with your phone number
3. Go to **"API development tools"**
4. Create a new application (e.g., `SavageCheck`)
5. Copy your `api_id` and `api_hash`

### Step 2: Set up environment variables
Create a `.env` file in the project root directory:

```env
API_ID=12345678
API_HASH=your_api_hash_here
```

> ⚠️ **Security Note**: Never share your `API_ID` and `API_HASH`. They are tied to your Telegram account. The `.env` file is kept local and should not be committed to version control.

---

## 🎮 Usage

```bash
python main.py
```

### Main Menu
```
 [1]  WHATSAPP       [2]  FACEBOOK
 [3]  TWITTER/X      [4]  INSTAGRAM
 [5]  TIKTOK         [6]  TELEGRAM
 [7]  DISCORD        [8]  SNAPCHAT
 [9]  TELEGRAM PHONE
 [0]  QUIT
 SavageHack@root/home ~#>>
```

### Platform Details

#### WhatsApp (Option 1)
- **Input**: Phone number with country code (e.g., `+33612345678`)
- **Method**: Checks via Meta Web API gateway

#### Facebook (Option 2)
- **Input**: Username (e.g., `therock`)
- **Method**: Scrapes `facebook.com/{username}`

#### Twitter/X (Option 3)
- **Input**: Username (e.g., `elonmusk`)
- **Method**: Scrapes `twitter.com/{username}`

#### Instagram (Option 4)
- **Input**: Username (e.g., `leomessi`)
- **Method**: Scrapes `instagram.com/{username}/`

#### TikTok (Option 5)
- **Input**: Username (e.g., `billieeilish`)
- **Method**: Scrapes `tiktok.com/@{username}`

#### Telegram (Option 6 — Username)
- **Input**: Username with or without `@` (e.g., `@username` or `username`)
- **Method**: Scrapes `t.me/{username}`

#### Discord (Option 7)
- **Input**: Discord User ID (numeric)
- **Method**: User ID lookup

#### Snapchat (Option 8)
- **Input**: Username (e.g., `snapchat`)
- **Method**: Profile page check

#### Telegram Phone (Option 9 — New!)
- **Input**: Phone number with country code (e.g., `+33612345678`)
- **Method**: MTProto API via Telethon (requires API_ID/API_HASH)
- **Detection results**:
  - `ACTIVE / CLEAN` — Number is registered and not banned
  - `BANNED` — Number is permanently banned from Telegram
  - `INVALID NUMBER` — Format incorrect or number doesn't exist
  - `RATE LIMIT / FLOOD WAIT` — Too many requests, must wait

---

## 📁 Project Structure

```
Project/
├── main.py                  # Main entry point with menu
├── config.py                # Environment variables loader
├── requirements.txt         # Python dependencies
├── .env                     # Your Telegram API keys (create this)
├── README.md
└── handlers/
    ├── whatsapp.py          # WhatsApp checker
    ├── facebook.py          # Facebook checker
    ├── twitter.py           # Twitter/X checker
    ├── instagram.py         # Instagram checker
    ├── tiktok.py            # TikTok checker
    ├── telegram.py          # Telegram username checker
    ├── telegram2.py         # Telegram phone number checker (Telethon)
    ├── discord.py           # Discord checker
    └── snapchat.py          # Snapchat checker
```

---

## ⚠️ Disclaimer

This tool is for **educational purposes only**. The detection methods rely on publicly available information and API behaviors. Use responsibly and in accordance with each platform's Terms of Service.

- Some platforms may change their frontend code, causing false results.
- Rate limiting may apply (especially for Telegram phone check).
- The accuracy of ban detection depends on the platform's response patterns.

---

## 🛠️ Technical Notes

- **Telegram Phone Check** uses `Telethon` to send a code request. A `.session` file (`savage_check_session.session`) is created locally — this is normal.
- Web scrapers use common User-Agent headers to simulate a browser.
- All HTTP requests have a 10-second timeout.

---

**Author: SavageHackZz** | Version 1.0

**Network** : {
    **Telegram**: **"https://t.me/Savage_HackzzzzzzZ"**,
    **Channel Telegram**: **"https://t.me/SavageHackZzzzzzzzzzzzzzzzzz777"**
}
