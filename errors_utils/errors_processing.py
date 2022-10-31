def gen_errors_list(errors_dict: dict) -> list:
    errors_list = []

    for k, v in errors_dict.items():
        for error in v:
            for error_text in error:
                errors_list.append(error_text)

    return errors_list
