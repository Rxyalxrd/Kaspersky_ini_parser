import argparse


def parse_args() -> argparse.Namespace:
    """
    Функция для парсинга аргументов командной строки.

    Returns
    -------
    argparse.Namespace
        Объект, содержащий значения аргументов командной строки.
    """
    parser = argparse.ArgumentParser(
        description="Парсер и валидатор конфигурационных файлов Kaspersky."
    )
    
    parser.add_argument(
        "-f", "--file",
        type=str,
        nargs="?",
        default="/var/opt/kaspersky/config.ini",
        help="Имя конфигурационного файла без расширения .ini (по умолчанию: /var/opt/kaspersky/config.ini)"
    )

    return parser.parse_args()
