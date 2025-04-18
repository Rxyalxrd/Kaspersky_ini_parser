import pytest
from app.framework.config_loader import IniConfigLoader
from app.framework.schemas import FullConfig
from pydantic import ValidationError

def test_invalid_ini_config():
    """
    Тест на валидацию неправильной конфигурации.
    Ожидается ошибка валидации.
    """
    invalid_config_loader = IniConfigLoader("test_invalid_config")

    parsed_data = invalid_config_loader.parse_ini_cfg()

    with pytest.raises(ValidationError):
        FullConfig(**parsed_data)