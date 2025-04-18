import pytest
from app.framework.config_loader import IniConfigLoader
from app.framework.schemas import FullConfig
from pydantic import ValidationError

@pytest.fixture
def valid_config_loader():
    # Фикстура для инициализации IniConfigLoader с валидным конфигом
    return IniConfigLoader('test_valid_config')

def test_valid_ini_config(valid_config_loader: IniConfigLoader):
    """
    Тест на правильную загрузку и парсинг конфигурации.
    """
    parsed_data = valid_config_loader.parse_ini_cfg()

    assert parsed_data is not None
    assert "General" in parsed_data
    assert "ScanMemoryLimit" in parsed_data["General"]
    assert parsed_data["General"]["ScanMemoryLimit"] == "2048"

def test_valid_config_validation(valid_config_loader: IniConfigLoader):
    """
    Тест на валидацию правильного конфигурационного файла.
    """
    parsed_data = valid_config_loader.parse_ini_cfg()

    try:
        FullConfig(**parsed_data)
    except ValidationError as e:
        pytest.fail(f"Конфигурация не прошла валидацию: {e}")