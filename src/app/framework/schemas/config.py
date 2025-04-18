from typing import (
    Literal,
    TypeAlias,
)
from uuid import UUID
import re

from pydantic import (
    BaseModel,
    Field,
    field_validator,
)


BoolStr: TypeAlias = Literal["true", "false", "yes", "no", "TRUE", "FALSE", "YES", "NO"]
PackageType: TypeAlias = Literal["rpm", "deb", "RPM", "DEB"]


class GeneralSection(BaseModel):
    """
    Секция конфигурации, содержащая общие параметры.

    Attributes
    ----------
    ScanMemoryLimit : int
        Лимит памяти для сканирования.
    PackageType : PackageType
        Тип пакета.
    ExecArgMax : int
        Максимальное количество аргументов для выполнения.
    AdditionalDNSLookup : BoolStr
        Указывает, нужно ли выполнять дополнительный DNS-запрос.
    CoreDumps : BoolStr
        Указывает, нужно ли создавать дампы памяти.
    RevealSensitiveInfoInTraces : BoolStr
        Указывает, нужно ли раскрывать чувствительную информацию в трассировках.
    ExecEnvMax : int
        Максимальное количество env окружений для выполнения.
    MaxInotifyWatches : int
        Максимальное количество наблюдателей inotify.
    CoreDumpsPath : str
        Путь к файлам дампов памяти.
    UseFanotify : BoolStr
        Указывает, нужно ли использовать fanotify.
    KsvlaMode : BoolStr
        Указывает, нужно ли использовать режим Ksvla.
    MachineId : UUID
        Идентификатор машины (UUID).
    StartupTraces : BoolStr
        Указывает, нужно ли записывать traces.
    MaxInotifyInstances : int
        Максимальное количество экземпляров inotify.
    Locale : str
        Encoding системы, определенном в RFC 3066.

    Methods
    -------
    check_path_exists(cls, v: str) -> str
        Проверяет, является ли путь к дампам абсолютным.
    validate_locale(cls, v: str) -> str
        Проверяет encoding, определенном в RFC 3066.

    """

    ScanMemoryLimit: int = Field(..., ge=1024, le=8192)
    PackageType: PackageType
    ExecArgMax: int = Field(..., ge=10, le=100)
    AdditionalDNSLookup: BoolStr
    CoreDumps: BoolStr
    RevealSensitiveInfoInTraces: BoolStr
    ExecEnvMax: int = Field(..., ge=10, le=100)
    MaxInotifyWatches: int = Field(..., ge=1000, le=1_000_000)
    CoreDumpsPath: str
    UseFanotify: BoolStr
    KsvlaMode: BoolStr
    MachineId: UUID
    StartupTraces: BoolStr
    MaxInotifyInstances: int = Field(..., ge=1024, le=8192)
    Locale: str

    @field_validator("CoreDumpsPath")
    def check_path_exists(cls, v: str) -> bool:
        """
        Проверяет, является ли путь к дампам абсолютным.

        Parametrs
        ---------
        v : str
            Путь к файлу дампа.

        Returns
        -------
        bool
            Возвращает путь, если он абсолютный.

        """

        return v.startswith('/')
    
    @field_validator("Locale")
    def validate_locale(cls, v: str) -> str:
        """
        Проверяет правильность encoding RFC 3066.

        Parametrs
        ---------
        v : str
            Encoding.

        Returns
        -------
        str
            Возвращает локаль, если она соответствует нужному формату.

        Exceptions
        ----------
        ValueError
            Если encoding не соответствует RFC 3066.

        """

        pattern = r"^[a-zA-Z]{2}_[A-Z]{2}(\.UTF-8)?$"

        if not re.match(pattern, v):
            raise ValueError("Locale должен выглядеть как en_US.UTF-8.")

        return v


class WatchdogSection(BaseModel):
    """
    Секция конфигурации для параметров watchdog.

    Attributes
    ----------
    ConnectTimeout : str
        Тайм-аут подключения в формате 'Xm'.
    MaxVirtualMemory : float | Literal["off", "auto", "OFF", "AUTO"]
        Максимальный объем виртуальной памяти или одно из значений: "off", "auto".
    MaxMemory : float | Literal["off", "auto", "OFF", "AUTO"]
        Максимальный объем памяти или одно из значений: "off", "auto".
    PingInterval : int
        Интервал пинга.

    Methods
    -------
    validate_connect_timeout(cls, v: str) -> str
        Проверяет корректность значения тайм-аута подключения.

    """

    ConnectTimeout: str
    MaxVirtualMemory: float | Literal["off", "auto", "OFF", "AUTO"]
    MaxMemory: float | Literal["off", "auto", "OFF", "AUTO"]
    PingInterval: int = Field(..., ge=100, le=10_000)

    @field_validator("ConnectTimeout")
    def validate_connect_timeout(cls, v: str) -> str:
        """
        Проверяет корректность значения тайм-аута подключения.

        Parametrs
        ---------
        v : str
            Тайм-аут подключения в формате 'Xm' (например, '30m').

        Returns
        -------
        str
            Возвращает значение, если оно корректно.

        Exceptions
        ----------
        ValueError
            Если значение не соответствует формату или выходит за пределы.

        """

        if not v.endswith("m"):
            raise ValueError("ConnectTimeout должен оканчиваться на 'm' (пример: '30m')")
        try:
            number = int(v[:-1])
            if not (1 <= number <= 120):
                raise ValueError("ConnectTimeout должен быть от 1 до 120 (пример: '30m')")
        except ValueError:
            raise ValueError("ConnectTimeout должен быть с 'm' (пример: '30m')")
        return v


class FullConfig(BaseModel):
    """
    Полная конфигурация, включающая секции General и Watchdog.

    Attributes
    ----------
    General : GeneralSection
        Секция с общими параметрами.
    Watchdog : WatchdogSection
        Секция с параметрами для watchdog.

    """

    General: GeneralSection
    Watchdog: WatchdogSection
