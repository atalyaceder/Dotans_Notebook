import yaml
import logging

def get_subjects_from_config(selected_groups, config_path):
    """
    Loads subject IDs from specified groups in a YAML config.

    Parameters:
        selected_groups (list of str): Names of groups to include.
        config_path (str): Path to the YAML configuration file.

    Returns:
        list of str: Unique list of subject IDs from selected groups.
    """
    with open(config_path, 'r') as file:
        subjects_config = yaml.safe_load(file)

    subjects_list = []
    for group in selected_groups:
        if group not in subjects_config:
            logging.warning(f"Group '{group}' not found in config.")
            continue
        subjects_list.extend(subjects_config[group])

    return list(set(subjects_list))

