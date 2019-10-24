_remove_mode_map = {
    "both": remove_mode_both,
    "include": remove_mode_include,
    "exclude": remove_mode_exclude
}


def checks_in_string(string, check_list):
    for check in check_list:
        if check in string:
            return True
    return False


def remove_mode_both(string_to_check, inclusions, exclusions):
    # would have been nice if this worked, but alas
    # if *exclusions not in string_to_check:
    #     if *inclusions in string_to_check:
    return (checks_in_string(string_to_check, inclusions)
            and not checks_in_string(string_to_check, exclusions))


def remove_mode_include(string_to_check, inclusions, exclusions):
    return checks_in_string(string_to_check, inclusions)


def remove_mode_exclude(string_to_check, inclusions, exclusions):
    return (not checks_in_string(string_to_check, exclusions))


def get_valid_remove_mode(mode_field):
    if type(mode_field) == str and mode_field in _remove_mode_map:
        return _remove_mode_map[mode_field]
    elif type(mode_field) == __func__:
        # test function to make sure the format is correct-ish
        mode_field("arb_string", [], [])
        return mode_field
    else:
        raise TypeError("mode field not valid, specify in-build or pass\
                         function")


def remove_irrelevant_strings(
        input_list, inclusions=[], exclusions=[], mode="both"
):
    """
    takes a list of strings and removes entries as specified by inclusions,
    exclusions and mode.

    built-in modes:
    "both", "include", "exclude"

    "both" requires the string to have the inclusions and not have the
    exclustions

    "include" will include all the strings that contain any inclusions,
    regardless of exclusion presence

    "exclude" will exclude all that contain exclusions, but include
    everthing else.

    mode functions can be passed. mode functions requires the following args:
    string_to_check: str, inclusions: list, exclusions: list

    must return True if the string is to be kept, and false if not.
    """
    check_function = get_valid_remove_mode(mode)

    output_list = []
    for file_name in input_list:
        if check_function(file_name):
            output_list.append(file_name)
    return output_list
