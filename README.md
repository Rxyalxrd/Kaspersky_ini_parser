# 🛡️ Конфигурационный валидатор `.ini` файлов

Этот проект предоставляет утилиту для валидации конфигурационных файлов `.ini` с использованием схем `Pydantic`. Программа проверяет конфигурацию на наличие обязательных секций, правильность значений и форматирования.

## 🧰 Стек технологий
- 🐍 **Python 3.12+**
- 📦 **Pydantic v2** — валидация конфигураций
- ⚙️ **Pydantic Settings** — управление настройками
- 📄 **Loguru** — логирование
- 🧾 **PyYAML** — поддержка YAML (опционально)
- 🛠 **PyInstaller** — сборка проекта в исполняемый `.exe`
- 📦 **Poetry** — управление зависимостями и виртуальным окружением
- 🧪 **Pytest** — тестирование
- 🧹 **Ruff**, 🕵️ **MyPy** — линтинг и статический анализ

## 🚀 Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/Rxyalxrd/Kaspersky_ini_parser.git
   ```

2. Перейдите в каталог проекта:

   ```bash
   cd src/
   ```

3. Установите зависимости:

   ```bash
   poetry install
   ```

4. Компилируем проект в `.exe`:

   ```bash
   make compile
   ```

5. Запуск проекта:

   ```bash
   make run INI=valid_sample
   ```

6. Тестирование:

   ```bash
   make test
   ```

## ⚙️ Примеры использования

```bash
./dist/kaspersky_validator.exe -f valid_sample
```

## 📂 Пример конфигурационного файла

```ini
[General]
ScanMemoryLimit=8192
Locale=en_US.UTF-8

[Watchdog]
MaxMemory=70.5
PingInterval=3000
```

</details>

## ✅ Результат валидации

- 🟢 **Успех:** валидация проходит, выводится лог об успешной проверке.
- 🔴 **Ошибка:** Pydantic выводит подробные сообщения о недостающих или некорректных параметрах.

Пример ошибки:

```
Ошибка валидации данных конфигурации: 4 validation errors for FullConfig
General.ScanMemoryLimit
  Input should be greater than or equal to 1024 [type=greater_than_equal, input_value='999', input_type=str]
    For further information visit https://errors.pydantic.dev/2.11/v/greater_than_equal
General.PackageType
  Input should be 'rpm', 'deb', 'RPM' or 'DEB' [type=literal_error, input_value='unknown', input_type=str]
    For further information visit https://errors.pydantic.dev/2.11/v/literal_error
General.ExecArgMax
  Input should be less than or equal to 100 [type=less_than_equal, input_value='200', input_type=str]
    For further information visit https://errors.pydantic.dev/2.11/v/less_than_equal
General.AdditionalDNSLookup
  Input should be 'true', 'false', 'yes', 'no', 'TRUE', 'FALSE', 'YES' or 'NO' [type=literal_error, input_value='maybe', input_type=str]
    For further information visit https://errors.pydantic.dev/2.11/v/literal_error
```

## 📁 Структура проекта

- `app/framework/` — Основной код проекта, включая валидацию.
- `app/cli/` — Парсинг аргументов командной строки.
- `app/framework/config_loader.py` — Загрузка `.ini` конфигураций.
- `app/framework/schemas.py` — Схемы данных Pydantic.
- `app/framework/validation.py` — Логика валидации.
- `app/test/` — Тесты на Pytest.
- `configs/` — Примеры конфигурационных файлов.


## 📝 Лицензия

MIT © [Rxyalxrd](https://github.com/Rxyalxrd)
