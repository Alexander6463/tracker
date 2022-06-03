#!/bin/make -f
EXPERIMENT_DIR=experiment
EXPERIMENT_JSON_CONFIG=experiment.json
INPUT_PATH=input_files
VISUALIZE=true
STATISTICAL_TEST=anova

run_all:
	python3 preprocessing.py --experiment-dir ${EXPERIMENT_DIR} \
	--experiment-json-config ${EXPERIMENT_JSON_CONFIG} --input-path ${INPUT_PATH}
	python3 generate_format.py --experiment-dir ${EXPERIMENT_DIR}
	python3 analyze.py --experiment-dir ${EXPERIMENT_DIR} --visualize ${VISUALIZE} \
--statistical-test ${STATISTICAL_TEST}


run_preprocessing:
	python3 preprocessing.py --experiment-dir ${EXPERIMENT_DIR} \
	--experiment-json-config ${EXPERIMENT_JSON_CONFIG} --input-path ${INPUT_PATH}

run_generate_format:
	python3 generate_format.py --experiment-dir ${EXPERIMENT_DIR}

run_analyze:
	python3 analyze.py --experiment-dir ${EXPERIMENT_DIR} --visualize ${VISUALIZE} \
--statistical-test ${STATISTICAL_TEST}