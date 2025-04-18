from typing import TypeAlias
import configparser
from pathlib import Path

from loguru import logger

from core import settings


ConfigDataType: TypeAlias = dict[str, str]


class IniConfigLoader:
    """
    Класс для загрузки и парсинга .ini конфигурационных файлов.

    Attributes
    ----------
    config : Path
        Путь к .ini файлу конфигурации.

    Methods
    -------
    parse_ini_cfg() -> dict[str, ConfigDataType]
        Парсит .ini файл и возвращает данные в виде словаря.

    """

    def __init__(self, ininame: str) -> None:
        """
        Инициализирует объект и загружает конфигурационный файл.

        Parametrs
        ---------
        ininame : str
            Имя конфигурационного файла (без расширения .ini).
        
        Exceptions
        ----------
        FileNotFoundError
            Если конфигурационный файл не найден по указанному пути.

        """
        
        logger.debug("Загружаем .ini файл ...")

        self.config = Path(settings.ini_path) / f"{ininame}.ini"

        if not self.config.exists():
            logger.error("Файл конфигурации не найден")
            raise FileNotFoundError("Файл конфигурации не найден")
        
        logger.info("Файл конфигурации загружен успешно.")

    def parse_ini_cfg(self) -> dict[str, ConfigDataType]:
        """
        Парсит .ini файл конфигурации и возвращает данные в виде словаря.

        Returns
        -------
        dict[str, ConfigDataType]
            Спаршенный .ini конфиг. 

        Exceptions
        ----------
        Exception
            Если произошла ошибка при чтении или обработке .ini файла.

        """

        logger.debug("Начинаем парсинг файла ...")

        try:
            parser = configparser.ConfigParser()
            parser.optionxform = str
            parser.read(self.config)

            logger.info("Предподготовка прошла успешно.")
        except Exception as e:
            logger.error("Ошибка в предподготовке.")
            raise e

        ret = {section: dict(parser[section]) for section in parser.sections()}

        logger.debug("Данные конфигурации успешно спаршены:")

        return ret
