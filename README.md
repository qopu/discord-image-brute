# Discord Image Bruteforce
This script **finds all images from a Discord channel or PM** by bruteforcing a `cdn.discordapp.com` link.

### How an image link is being formatted
![Link Format](https://i.imgur.com/YeYpglS.png)
As you can see, the only dynamic part of the link is the **Message ID**, which you can bruteforce using this script.

## Usage
- You can find all images from someone else's **Private Messages**
- You can export all images from a guild channel

## Requirements
- **Link of another image or channel ID**
- **Hi-CPU Server** (recommended for faster brute)

## Installation
> **[Python](https://www.python.org/) 3.9 or newer is required**

- **Clone GitHub repository**
  ```shell
  git clone https://github.com/qopu/discord-image-brute
  ```
- **Run program**
  ```shell
  python3 main.py
  ```