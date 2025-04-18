from loguru import logger

from framework.validation import ValidateConfig


def main() -> None:
    """
    Главная функция для запуска процесса валидации конфигурационного файла.

    Эта функция создает объект для валидации конфигурации и выполняет проверку,
    выводя соответствующие сообщения в лог в зависимости от результата.

    """

    validator = ValidateConfig("valid_sample")

    if validator.validate():
        logger.success("✅ Конфигурация прошла валидацию успешно.")
    else:
        logger.error("❌ Конфигурация не прошла валидацию.")


if __name__ == "__main__":
    main()
