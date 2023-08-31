from dataclasses import dataclass
from typing import Literal, Optional


@dataclass
class LoggerConfig:
    name: str
    level: Literal['NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']  # Log level
    stream: Optional[Literal['stdout', 'stderr']] = None  # Log stream if any
    file_path: Optional[str] = None  # Log file path if any
    format: Optional[str] = None  # Log format if any


@dataclass
class RedisConfig:
    host: str
    port: int
    db: str
    password: str
    logger: LoggerConfig


@dataclass
class DBConfig:
    host: str  # DBMS host
    port: int  # DBMS port
    user: str  # DBMS user
    password: str  # DBMS user password
    database: str  # Database name
    logger: LoggerConfig  # Logger config for database


@dataclass
class Config:
    redis: RedisConfig
    db: DBConfig
    # Extra configs if any
    logger: LoggerConfig  # Logger config for the app
