from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True) #frozen=true means it won't be accpeting any other if you add something it won't be accpeting
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path