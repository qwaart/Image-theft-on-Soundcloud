# Soundcloud Artwork Downloader

An easy-to-use Python program for downloading high-quality track covers from SoundCloud.

---

### 🚀 Features

* Automatically extracts the URL of the track cover.
* Download images in the highest available quality (500x500 pixels).
* Automatically save images to a special folder.
* Generate file names based on the artist and track name.

### 🛠️ Requirements

* Python 3.8+
* Playwright
* Requests
* BeautifulSoup4

---

### 📥 Installation

1.  Clone the repository:
```bash
    git clone [https://github.com/qwaart/Image-theft-on-Soundcloud.git](https://github.com/qwaart/Image-theft-on-Soundcloud.git)
    cd /Image-theft-on-Soundcloud
    ```

2.  Install the necessary libraries:
```bash
pip install -r requirements.txt
```
This command will automatically install everything you need.

3.  Install the browser for Playwright:
```bash
playwright install
```

---

### 💡 Usage

1.  Run the program:
```bash
python main.py
```

2.  Enter the SoundCloud track link when prompted:
```
Your link: [https://soundcloud.com/user/track-name](https://soundcloud.com/user/track-name)
```
    
    The program will automatically download the cover art to the `Soundcloud_Artwork` folder.

---
