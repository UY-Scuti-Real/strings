from .general import checks_in_string


def _remove_mode_both(string_to_check, inclusions, exclusions):
    # would have been nice if this worked, but alas
    # if *exclusions not in string_to_check:
    #     if *inclusions in string_to_check:
    return (checks_in_string(string_to_check, inclusions)
            and not checks_in_string(string_to_check, exclusions))


def _remove_mode_include(string_to_check, inclusions, exclusions):

    return checks_in_string(string_to_check, inclusions)


def _remove_mode_exclude(string_to_check, inclusions, exclusions):
    return (not checks_in_string(string_to_check, exclusions))


_remove_mode_map = {
    "both": _remove_mode_both,
    "include": _remove_mode_include,
    "exclude": _remove_mode_exclude
}


def _get_valid_remove_mode(mode_field):
    if type(mode_field) == str and mode_field in _remove_mode_map:
        return _remove_mode_map[mode_field]
    elif type(mode_field) == __func__:
        # test function to make sure the format is correct-ish
        mode_field("arb_string", [], [])
        return mode_field
    else:
        raise TypeError("mode field not valid, specify in-build or pass\
                         function")


def filter_strings(
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
    check_function = _get_valid_remove_mode(mode)

    output_list = []
    for string in input_list:
        if check_function(string, inclusions, exclusions):
            output_list.append(string)
    return output_list
