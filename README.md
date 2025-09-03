# FastestHeicToJpg

Convert HEIC images to JPG easily with a simple graphical interface!

## Features

- Select individual HEIC files or an entire folder
- Choose where to save converted JPGs
- Fast batch conversion using [pillow-heif](https://github.com/carsales/pillow-heif) and [Pillow](https://python-pillow.org/)
- Modern, easy-to-use interface

## Requirements

- Python 3.8 or newer
- [pillow-heif](https://github.com/carsales/pillow-heif)
- [Pillow](https://python-pillow.org/)

## Installation

1. **Clone or download this repository**

    ```sh
    git clone https://github.com/yourusername/FastestHeicToJpg.git
    cd FastestHeicToJpg
    ```

2. **Install dependencies**

    ```sh
    pip install pillow pillow-heif
    ```

## Usage

1. **Run the app**

    ```sh
    python FastestHeicToJPG.py
    ```

2. **How to use**

    - Click **Select Files or Folders** to choose HEIC files or a folder containing HEIC images.
    - Click **Convert** and select the output folder for your JPG files.
    - Conversion progress and errors will appear in the log box.

## Notes

- This app works on macOS, Windows, and Linux (with Python and Tkinter installed).
- You cannot create a Windows `.exe` directly on macOS. Share the `.py` file for cross-platform use.
- For Mac users: You can create a `.app` using [py2app](https://py2app.readthedocs.io/en/latest/).
- For Windows users: You can create a `.exe` using [PyInstaller](https://pyinstaller.org/) on a Windows machine.

## License

MIT License

---

**Made with ❤️ by KNOOKSIK**
