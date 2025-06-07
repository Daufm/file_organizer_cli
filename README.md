# File Organizer CLI

A simple Python command-line tool to organize files in a directory into categorized subfolders based on their file extensions.

---

## 🚀 Features

- **Automatic categorization:** Moves files into folders like `Images`, `Documents`, `Videos`, `Audio`, `Archives`, `Code`, and `Others`.
- **Dry run mode:** Preview what will happen before making changes.
- **Verbose output:** See detailed information about each operation.
- **Easy to use:** Just point it at a folder and go!

---

## 📦 Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/file-organizer-cli.git
cd file-organizer-cli
```

(Optional but recommended) Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies (if any):

```bash
pip install -r requirements.txt
```

---

## 🛠 Usage

From the project root, run:

```bash
PYTHONPATH=src python3 -m file_organizer.cli /path/to/your/folder
```

**Options:**

- `--dry-run` : Show what would be done, but don’t move any files.
- `-v` or `--verbose` : Enable detailed output.

**Examples:**

Preview what would happen in your Downloads folder:
```bash
PYTHONPATH=src python3 -m file_organizer.cli ~/Downloads --dry-run -v
```

Actually organize your Downloads folder:
```bash
PYTHONPATH=src python3 -m file_organizer.cli ~/Downloads -v
```

---

## 🗂 Categories

Files are sorted into these folders by default:

- **Images:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.webp`
- **Documents:** `.pdf`, `.doc`, `.docx`, `.txt`, `.rtf`, `.odt`, `.xls`, `.xlsx`, `.ppt`, `.pptx`
- **Videos:** `.mp4`, `.mov`, `.avi`, `.mkv`, `.flv`, `.wmv`
- **Audio:** `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`
- **Archives:** `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
- **Code:** `.py`, `.cpp`, `.h`, `.java`, `.js`, `.html`, `.css`
- **Others:** Anything else

---

## 🤝 Contributing

Pull requests and suggestions are welcome!  
Feel free to open an issue or submit a PR.

---

## 📄 License

This project is licensed under the MIT License.

---

## 📬 Contact

Questions or suggestions?  
Open an issue or contact [yourusername](https://github.com/yourusername).
