from loguru import logger

from framework.validation import ValidateConfig
from cli import parse_args

def main() -> None:
    """
    Главная функция для запуска процесса валидации конфигурационного файла.

    Эта функция создает объект для валидации конфигурации и выполняет проверку,
    выводя соответствующие сообщения в лог в зависимости от результата.

    """

    args = parse_args()

    validator = ValidateConfig(args.file)

    if validator.validate():
        logger.success("✅ Конфигурация прошла валидацию успешно.")
    else:
        logger.error("❌ Конфигурация не прошла валидацию.")


if __name__ == "__main__":
    main()
