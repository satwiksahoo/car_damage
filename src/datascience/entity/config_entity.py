from dataclasses import dataclass
from pathlib import Path

@dataclass

class dataIngestionconfig:
    root_dir : Path
    source_url : str
    local_data_file : Path
    unzip_dir : Path


@dataclass

class datavalidationconfig:
    root_dir : Path
    unzip_data_dir : Path
    STATUS_FILE : str

    