from loguru import logger

from framework.validation import ValidateConfig


def main() -> None:
    validator = ValidateConfig("valid_sample")

    if validator.validate():
        logger.success("✅ Конфигурация прошла валидацию успешно.")
    else:
        logger.error("❌ Конфигурация не прошла валидацию.")


if __name__ == "__main__":
    main()
