# File Organizer CLI

[[PyPI - Version](https://img.shields.io/pypi/v/file-organizer-cli)](https://pypi.org/project/file-organizer-cli/)  
[[License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple, yet powerful command-line utility to **automatically organize your files** into categorized subdirectories based on their file extensions. Clean up your messy Downloads, Documents, or any other directory with ease!

## ✨ Features

* **Automatic Categorization:** Organizes files into sensible categories like `Images`, `Documents`, `Videos`, `etc.`
* **Recursive Scan:** Processes files within subdirectories.
* **Dry Run Mode:** Preview changes before actually moving any files, ensuring peace of mind.
* **Verbose Output:** Get detailed information about what files are being processed and where they're going.
* **Lightweight & Fast:** Built with Python, designed for efficiency.

## 🚀 Installation

You can install `file-organizer-cli` directly from PyPI using `pip`:

```bash
pip install file-organizer-cli
```

## 💡 Usage

Once installed, you can use the `organize-files` command directly from your terminal.

### Basic Usage

To organize files in a directory, simply provide the path to that directory:

```bash
organize-files /path/to/your/messy_folder
```

For example, to organize your Downloads folder:

```bash
organize-files ~/Downloads
```

(On Windows, this might be `organize-files C:\Users\YourUser\Downloads`)

### Dry Run (Recommended First Step!)

Always use the `--dry-run` flag first to see exactly what changes will be made without actually moving any files. This is a great way to verify the tool's behavior before committing to changes.

```bash
organize-files /path/to/your/messy_folder --dry-run
```

### Verbose Output

Use the `-v` or `--verbose` flag to get detailed information about each file being processed and its destination.

```bash
organize-files /path/to/your/messy_folder -v
```

### Combining Options

You can combine options. For instance, to see a verbose dry run:

```bash
organize-files /path/to/your/messy_folder --dry-run -v
```

## 🗂️ Categories

Files are moved into subdirectories based on their extensions. Here's a general idea of the default categories:

- **Images:** .jpg, .jpeg, .png, .gif, .bmp, .tiff, .webp
- **Documents:** .pdf, .doc, .docx, .txt, .rtf, .odt, .xls, .xlsx, .ppt, .pptx
- **Videos:** .mp4, .mov, .avi, .mkv, .flv, .wmv
- **Audio:** .mp3, .wav, .flac, .aac, .ogg
- **Archives:** .zip, .rar, .7z, .tar, .gz
- **Code:** .py, .cpp, .h, .java, .js, .html, .css
- **Others:** Any file with an unrecognized extension or no extension will go here.

## 🤝 Contributing

Contributions are welcome! If you have ideas for new features, bug fixes, or improvements to existing logic, please feel free to:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Write tests for your changes.
5. Commit your changes (`git commit -m 'Add new feature'`).
6. Push to the branch (`git push origin feature/your-feature-name`).
7. Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

If you have any questions or feedback, feel free to open an issue on the GitHub repository or reach out to [Your Name/Your Email Address].

### How to Use This `README.md` Content:

1. **Create `README.md`:** Save the content above into a file named `README.md` in the **root directory** of your project (`file_organizer_cli/README.md`).
2. **Customize:**
    - Replace `[Your Name/Your Email Address]` in the "Contact" section.
    - Consider adding a link to your GitHub repository if it's hosted there.
    - If you have a `LICENSE` file, ensure it's present in your root directory.
    - Update the PyPI version badge if you change your project's version.

With a solid test suite and a comprehensive `README.md`, your project will be much more robust and user-friendly!