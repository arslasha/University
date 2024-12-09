import os
import shutil
import zipfile


def create_filesystem():
    structure = {
        "file1.txt": "Hello, this is file1.\nIt contains a few lines of text.",
        "file2.txt": "This is file2.\nAnother example file.",
        "dir1/file3.txt": "File3 content goes here.",
        "dir1/file4.txt": "Some text in file4.",
        "dir3/subdir1/file5.txt": "File5 in a nested directory.",
        "dir3/subdir2/file6.txt": "File6 in another nested directory."
    }

    base_dir = "filesystem"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    for path, content in structure.items():
        full_path = os.path.join(base_dir, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w") as f:
            f.write(content)

    # Создаем архив
    with zipfile.ZipFile(f"{base_dir}.zip", "w") as zipf:
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, base_dir))

    # Удаляем временную файловую систему
    shutil.rmtree(base_dir)


create_filesystem()
