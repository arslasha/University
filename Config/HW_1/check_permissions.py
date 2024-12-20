import os

def check_permissions(directory):
    """Проверяет права на чтение и запись в указанной директории."""
    can_read = os.access(directory, os.R_OK)  # Проверяем право на чтение
    can_write = os.access(directory, os.W_OK)  # Проверяем право на запись

    if can_read and can_write:
        return f"Директория {directory}: доступно для чтения и записи."
    elif can_read:
        return f"Директория {directory}: доступно только для чтения."
    elif can_write:
        return f"Директория {directory}: доступно только для записи."
    else:
        return f"Директория {directory}: нет доступа."

# Пример использования
directory_path = "./vfs"  # Укажите путь к вашей VFS
print(check_permissions(directory_path))
