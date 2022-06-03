from pathlib import Path

from PyTrack.Experiment import Experiment

# Creating an object of the Experiment class
experiment_dir = "experiment"
configure_json_path = str(Path(f"{experiment_dir}/{experiment_dir}.json").absolute())
exp = Experiment(json_file=configure_json_path)

exp.metaMatrixInitialisation()


exp.analyse(parameter_list={"all"},
            between_factor_list=["Subject_type", "Gender"],
            within_factor_list=["Stimuli_type"],
            statistical_test="anova",
            file_creation=True)

exp.visualizeData()
