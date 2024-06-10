Sure, here's a README for the File Sorter project:

---

# 📂 File Sorter

The File Sorter is a command-line utility designed to organize files in a directory based on their file extensions.

## Features

- Automatically sorts files into folders based on their extensions.
- Supports customization of destination folders.
- Handles duplicate files gracefully.
- Provides detailed logs for the sorting process.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SherhoneGrantMDS/file-sorter.git
   ```

2. Navigate to the project directory:

   ```bash
   cd file-sorter
   ```

3. Run the setup script:

   ```bash
   python setup.py install
   ```

## Usage

1. Open your terminal or command prompt.
2. Navigate to the directory containing the files you want to sort.
3. Run the following command:

   ```bash
   file-sorter
   ```

4. The File Sorter will organize the files into folders based on their extensions.

## Configuration

You can customize the destination folders by editing the `config.json` file. Add or modify entries to specify the desired folder for each file extension.

```json
{
  ".txt": "TextFiles",
  ".jpg": "Images",
  ".pdf": "Documents",
  ".mp3": "Music"
}
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Python: https://www.python.org/

---
