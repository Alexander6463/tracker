from typing import Union
import json

from pathlib import Path


def create_experiment_structure(
        experiment_directory_name: str,
        experiment_json_config_path: str
) -> None:
    with open(experiment_json_config_path) as f:
        experiment_json_config = json.load(f)
    experiment_json_config['Experiment_name'] = experiment_dir
    experiment_json_config['Path'] = experiment_dir
    Path(experiment_directory_name).mkdir()
    (Path(experiment_directory_name) / "Data").mkdir()
    (Path(experiment_directory_name) / "Stimuli").mkdir()
    with open(Path(experiment_directory_name) / f"{experiment_directory_name}.json", "w") as f:
        json.dump(experiment_json_config, f)


def preprocessing_experiment_data(
        input_data_path: Union[str, Path],
        output_data_path: Union[str, Path]
) -> None:

    for data_file in Path(input_data_path).iterdir():
        print(f"Preprocessing file {data_file.name}")
        with open(Path(output_data_path) / data_file.name, "w") as f2:
            with open(data_file, "r") as f:
                text = f.readline()
                f2.write(text)
                while text:
                    text = f.readline()
                    if 'graphics/VC_' in text:
                        els = text.split()
                        f2.write((els[0] + "\t" + els[1] + " start_trial\n"))
                        continue
                    if 'END' in text:
                        sample_number = int(text.split()[1]) - 1
                        f2.write(f"MSG\t{sample_number} stop_trial\n")
                        f2.write(text)
                        continue
                    f2.write(text)


if __name__ == "__main__":
    experiment_dir = "experiment"
    experiment_json_config = "experiment.json"
    input_path = Path("input_files")
    output_path = Path(experiment_dir) / "Data"
    create_experiment_structure(
        experiment_directory_name=experiment_dir,
        experiment_json_config_path=experiment_json_config
    )
    preprocessing_experiment_data(
        input_data_path=input_path,
        output_data_path=output_path
    )
