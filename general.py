def checks_in_string(string, check_list):
    for check in check_list:
        if check in string:
            return True
    return False
