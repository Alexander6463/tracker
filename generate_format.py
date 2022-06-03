import shutil
from pathlib import Path

from PyTrack.formatBridge import generateCompatibleFormat

experiment_dir_name = "experiment"
experiment_path = str(Path(experiment_dir_name).absolute())

generateCompatibleFormat(
    exp_path=experiment_path,
    device="eyelink",
    start='start_trial',
    stop="stop_trial",
    eye='B'
)

shutil.move(
    src=Path(experiment_dir_name) / f"Data{experiment_dir_name}.db",
    dst=Path(experiment_dir_name) / "Data" / f"{experiment_dir_name}.db",
)
