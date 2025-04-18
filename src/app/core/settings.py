from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class PathConfigsSettings(BaseSettings):
    """
    Настройки путей к конфигурационным файлам.

    Attributes
    ----------
    ini_path : str
        Абсолютный путь к .ini-файлу конфигурации.

    """
    
    ini_path: str = "/var/opt/kaspersky/config.ini"



class Settings(PathConfigsSettings):
    """
    Основные настройки конфигурации приложения.

    Наследуется от `PathConfigsSettings` и добавляет поддержку переменных окружения.

    Attributes
    ----------
    model_config : SettingsConfigDict
        Конфигурация модели, включающая параметры.

    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
