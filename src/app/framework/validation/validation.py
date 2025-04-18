from pydantic import ValidationError
import yaml
from loguru import logger

from framework.config_loader import IniConfigLoader
from framework.schemas import FullConfig


class ValidateConfig:
    """
    Класс для валидации конфигурационного файла.

    Attributes
    ----------
    cfg : IniConfigLoader
        Объект для загрузки и парсинга .ini файла конфигурации.

    Methods
    -------
    validate() -> bool
        Выполняет валидацию конфигурации, загруженной из .ini файла.

    """

    def __init__(self, ininame: str) -> None:
        """
        Инициализирует объект для валидации конфигурации.

        Parametrs
        ---------
        ininame : str
            Имя конфигурационного файла (без расширения .ini).

        """

        self.cfg = IniConfigLoader(ininame)


    def validate(self) -> bool:
        """
        Выполняет валидацию конфигурации, загруженной из .ini файла.
        
        Returns
        -------
        bool
            Возвращает True, если конфигурация прошла валидацию, иначе False.

        Exceptions
        ----------
        ValidationError
            Если данные не проходят валидацию по схеме.
        Exception
            Для неизвестных ошибок, которые могут возникнуть в процессе валидации.

        """

        try:
            logger.debug("Начало процесса валидации конфигурации ...")
            
            pars_data = self.cfg.parse_ini_cfg()

            logger.debug(
                f"Полученные данные для валидации:\n{yaml.dump(
                    pars_data,
                    allow_unicode=True,
                    sort_keys=False
                )}"
            )

            FullConfig(**pars_data)
            
            logger.info("Конфигурация прошла валидацию успешно")

            return True

        except ValidationError as e:
           logger.error(f"Ошибка валидации данных конфигурации: {e}")
           return False
        except Exception as e:
           logger.error(f"Неизвестная ошибка при валидации конфигурации: {e}")
           return False
