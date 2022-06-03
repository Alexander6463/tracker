from pathlib import Path

import click
from PyTrack.Experiment import Experiment


@click.command()
@click.option('--experiment-dir', help="Path to directory with your experiment")
@click.option('--visualize')
@click.option('--statistical-test')
def main(experiment_dir: str, visualize: bool, statistical_test: str) -> None:
    configure_json_path = str(Path(f"{experiment_dir}/{experiment_dir}.json").absolute())
    exp = Experiment(json_file=configure_json_path)

    exp.metaMatrixInitialisation()

    exp.analyse(parameter_list={"all"},
                between_factor_list=["Subject_type", "Gender"],
                within_factor_list=["Stimuli_type"],
                statistical_test=statistical_test,
                file_creation=True)

    if visualize:
        exp.visualizeData()


if __name__ == "__main__":
    main()