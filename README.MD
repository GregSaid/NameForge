# 🟢 7Miner - Minecraft Username Checker
[![Releases](https://img.shields.io/github/v/release/GregSaid/7Miner?label=latest%20release)](https://github.com/GregSaid/7Miner/releases)

**7Miner** is an advanced and automated tool developed in Python that checks the availability of Minecraft usernames. It allows for efficient, anonymous (via proxies), and even real-time queries, with Discord integration for automatic alerts.

---

## 📌 Index

- [📌 Index](#-index)
- [📦 About the Project](#-about-the-project)
- [🚀 Features](#-features)
- [🔧 How to Install](#-how-to-install)
- [⚙️ Requirements](#️-requirements)
- [💡 How to Use](#-how-to-use)
- [📡 Discord Webhook (Optional)](#-discord-webhook-optional)
- [📜 Mojang Terms and Policy](#-mojang-terms-and-policy)
- [⚖️ License of Use](#%EF%B8%8F-license-of-use)
- [🤝 Credits](#-developed-with--by-gregsaid)

---

## 📦 About the Project

7Miner was created to make it easier to search for unique and rare Minecraft usernames. Whether to reclaim a nostalgic name, grab a common word, or create something aesthetic, 7Miner makes the process simple and efficient. No need to check one by one anymore!

- ✔️ Uses proxies for anonymity and to avoid rate-limits.  
- ✔️ Supports automatic name generation or custom name lists.  
- ✔️ Smart cache that avoids duplicate checks.  
- ✔️ Fully free and open-source.  

---

## 🚀 Features

- ✅ Checks name availability directly via Mojang's official API.  
- ✅ Automatically generates usernames using filters.  
- ✅ Reads names from a custom `names.txt` list.  
- ✅ Local cache to save requests (`debug/cache.txt`).  
- ✅ Discord integration via Webhook (`webhook.txt`).  
- ✅ Supports HTTP/S proxies (`proxies.txt`).  
- ✅ Interactive system with real-time logging.  

---

## 🔧 How to Install

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/7Miner.git
   cd 7Miner
   ```

2. **Install the required libraries**:

   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Requirements

- Python 3.9 or higher  
- Internet connection  
- Optional: `proxies.txt` file for increased anonymity

---

## 💡 How to Use

### 1. Open the file '7Miner.py' / '7Miner.exe'

#### 1.1 How to open the '7Miner.**py**' file?
![1](https://media.discordapp.net/attachments/1358169758658334821/1358628021808009246/image.png?ex=67f48872&is=67f336f2&hm=cec2489662cf669f2e3c65c7902da56d34af4cd227f079e46606defa1abb0eba&=&format=webp&quality=lossless)

![2](https://media.discordapp.net/attachments/1358169758658334821/1358628379565494494/image.png?ex=67f488c7&is=67f33747&hm=a3786c1f90b654ba97d7b1935177cf3437bd7ad2bad4a63109247ae271ffe584&=&format=webp&quality=lossless)

![3](https://media.discordapp.net/attachments/1358169758658334821/1358628819468156988/image.png?ex=67f48930&is=67f337b0&hm=68e4e90d5523eee1685cede05d93510e0d8cb41d32d8117f191a37d05cb89e16&=&format=webp&quality=lossless)

![4](https://media.discordapp.net/attachments/1358169758658334821/1358629540758290604/image.png?ex=67f489dc&is=67f3385c&hm=2961829293a6d1404a1c526b1682f7f1f37f87c84175202c254f35ecb28c6a3b&=&format=webp&quality=lossless)

![5](https://media.discordapp.net/attachments/1358169758658334821/1358630587778207886/image.png?ex=67f48ad6&is=67f33956&hm=6f3376e272fa2622360c973b5555c445b2acb46df9b4a4e4e9ac87b31af58259&=&format=webp&quality=lossless)

#### 1.2 How to open the '7Miner.**exe**' file?
- A: Just double-click the `.exe` file.

#### 1.3 After running the '7Miner.py' or '7Miner.exe' file for the first time, important folders and files will be created.
- ![Files/Folders](https://media.discordapp.net/attachments/1358169758658334821/1358636955113357363/68747470733a2f2f6d656469612e646973636f72646170702e6e65742f6174746163686d656e74732f313335383136393735383635383333343832312f313335383633343836313133323531373536362f696d6167652e706e673f65783d3637663438656431266973_1.png?ex=67f490c4&is=67f33f44&hm=a16d6f879fde02d5b79ba875feb84d5a6d859219dd57686bb0b9f9ae1a997390&=&format=webp&quality=lossless)

### 2. How to use 'names.txt'?

Put one name per line:
- ![name.txt](https://media.discordapp.net/attachments/1358169758658334821/1358637799032750144/image.png?ex=67f4918d&is=67f3400d&hm=514adfc378e7c31cbe8fd140a637a180711e43d947b473ee4cf439e2520f842b&=&format=webp&quality=lossless)

### 3. How to use 'proxies.txt'?

Put one proxy per line (Proxy format: `user:pass@ip:port`):
- ![proxies.txt](https://media.discordapp.net/attachments/1358169758658334821/1358638609124560977/image.png?ex=67f4924e&is=67f340ce&hm=231031dd3de785ba74b7b4e353116b9ca86bb672d53405c536517ad93d9b89b0&=&format=webp&quality=lossless)

### 4. How to use 'webhook.txt'?

Use only one Webhook. Paste your Webhook in the first line:
- ![webhook.txt](https://media.discordapp.net/attachments/1358638810921177258/1358639905143783544/image.png?ex=67f49383&is=67f34203&hm=6d36c43937787fe6a8e53738c2bac8e91185347d0891474dd4a60e76b360e7e4&=&format=webp&quality=lossless)

---

## 📡 Discord Webhook (Optional)

If you want to receive notifications directly in a Discord channel:

1. Create a webhook on your Discord server.  
2. Paste the URL into the file `webhook.txt`.  
3. Done! All available usernames found will be sent automatically to your Discord channel.

---

## 📜 Mojang Terms and Policy

This project **does not perform automatic purchases** of usernames, **does not violate Mojang's Terms of Use**,  
and only **queries the public API**, which any user can access.

> **Mojang allows the use of its public API to check usernames, provided that:**
> 
> - “The usage is done responsibly (no flooding or abuse).”
> - “Access does not attempt to bypass protection systems or automate acquisition.”
> - “It does not interfere with other players' experience.”
> 
> **This project respects these guidelines and encourages all users to do the same.**

🔗 **Official reference:**  
- [Terms of Service](https://www.minecraft.net/en-us/terms)  
- [API Guidelines](https://wiki.vg/Mojang_API)

---

## ⚖️ License of Use

Copyright © 2025 GregSaid

This project is provided for free **strictly for personal and educational use only**. Any commercial use, including but not limited to:

- Resale,  
- Paid distribution,  
- Integration into commercial products,  
- Or direct or indirect monetization of the software  

**requires the author's explicit written permission.**

---

### ❌ Restrictions

You are **NOT** allowed, without the author's consent, to:

- Copy, modify, merge, publish, distribute, sublicense, or sell copies of this software;  
- Make public or redistribute modified versions;  
- Use the software for profit or within for-profit organizations.

---

### ✅ Permitted

- Personal, local, and non-commercial use;  
- Study, testing, and use as a support tool in individual projects;  
- Sharing the project with intact credits and without modifications for educational purposes.

---

### ⚠️ Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY.

---

### 📬 Contact

For commercial use requests or questions, contact the author via GitHub or another official channel listed in the repository.

---

<h3 align="center">👨🏽‍💻 Developed with 🧠 by <strong>GregSaid</strong></h3>
<p align="center">☕ Made with focus, dedication and a few sleepless nights!</p>