import shutil
from pathlib import Path

import click
from PyTrack.formatBridge import generateCompatibleFormat


@click.command()
@click.option('--experiment-dir', help="Path to directory with your experiment")
def main(experiment_dir):
    experiment_path = str(Path(experiment_dir).absolute())

    generateCompatibleFormat(
        exp_path=experiment_path,
        device="eyelink",
        start='start_trial',
        stop="stop_trial",
        eye='B'
    )

    shutil.move(
        src=Path(experiment_dir) / f"Data{experiment_dir}.db",
        dst=Path(experiment_dir) / "Data" / f"{experiment_dir}.db",
    )


if __name__ == "__main__":
    main()
