from typing import Union
import json
from pathlib import Path

import click


def create_experiment_structure(
        experiment_directory_name: str,
        experiment_json_config_path: str
) -> None:
    with open(experiment_json_config_path) as f:
        experiment_json_config = json.load(f)
    experiment_json_config['Experiment_name'] = experiment_directory_name
    experiment_json_config['Path'] = experiment_directory_name
    Path(experiment_directory_name).mkdir(exist_ok=True)
    (Path(experiment_directory_name) / "Data").mkdir(exist_ok=True)
    (Path(experiment_directory_name) / "Stimuli").mkdir(exist_ok=True)
    with open(Path(experiment_directory_name) / f"{experiment_directory_name}.json", "w") as f:
        json.dump(experiment_json_config, f)


def preprocessing_experiment_data(
        input_data_path: Union[str, Path],
        output_data_path: Union[str, Path]
) -> None:
    flag = 0
    for data_file in Path(input_data_path).iterdir():
        counter = 0
        print(f"Preprocessing file {data_file.name}")
        with open(Path(output_data_path) / data_file.name, "w") as f2:
            with open(data_file, "r") as f:
                text = f.readline()
                f2.write(text)
                while text:
                    text = f.readline()
                    if ".\t   .\t    0.0" in text and flag == 1:
                        counter += 1
                        continue
                    elif flag == 1 and "DISPLAY_video" in text:
                        ...
                    elif flag == 1 and "EBLINK R" in text:
                        ...
                    else:
                        flag = 0
                    if 'graphics/VC_' in text:
                        flag = 1
                        els = text.split()
                        f2.write((els[0] + "\t" + els[1] + " start_trial\n"))
                        continue
                    if 'END' in text:
                        sample_number = int(text.split()[1]) - 1
                        f2.write(f"MSG\t{sample_number} stop_trial\n")
                        f2.write(text)
                        continue
                    f2.write(text)
        print(counter)


@click.command()
@click.option('--experiment-dir', help="Path to directory with your experiment")
@click.option('--experiment-json-config', help="Path to your config")
@click.option('--input-path', help="Path to your input asc files")
def main(experiment_dir, experiment_json_config, input_path):
    output_path = Path(experiment_dir) / "Data"
    create_experiment_structure(
        experiment_directory_name=experiment_dir,
        experiment_json_config_path=experiment_json_config
    )
    preprocessing_experiment_data(
        input_data_path=input_path,
        output_data_path=output_path
    )


if __name__ == "__main__":
    main()
    #preprocessing_experiment_data(input_data_path="input_10", output_data_path="output_10")
