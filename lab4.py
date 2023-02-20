import sys
import os
import re

def main():
    log_file = get_log_file_path_from_cmd_line()
    records = filter_log_by_regex(log_file, 'sshd', print_summary=True, print_records=True)

# Step 3
def get_log_file_path_from_cmd_line():
    num_params = len(sys.argv)-1
    if num_params >= 1:
        logfile_path = sys.argv[1]
        if os.path.isfile(logfile_path):
            return os.path.abspath(logfile_path)
        else:
            print("Error: Log file does not exists.")
            sys.exit(1)
    else:
        print("Error: Log file not found!")
        sys.exit(1)

# Steps 4-7
def filter_log_by_regex(log_file, regex, ignore_case=True, print_summary=False, print_records=False):
    """Gets a list of records in a log file that match a specified regex.

    Args:
        log_file (str): Path of the log file
        regex (str): Regex filter
        ignore_case (bool, optional): Enable case insensitive regex matching. Defaults to True.
        print_summary (bool, optional): Enable printing summary of results. Defaults to False.
        print_records (bool, optional): Enable printing all records that match the regex. Defaults to False.

    Returns:
        (list, list): List of records that match regex, List of tuples of captured data
    """

    records = []

    regex_flags = re.IGNORECASE if ignore_case else 0
    
    with open(log_file, 'r') as file:
        for line in file:
            match = re.search(regex, line)
            if match:
                records.append(line)

    if print_records is True: 
        print(*records,sep='')

    if print_summary is True:
        a = len(records)
        print(f'The log file contains {a} records that case-insensitive match the regex "{regex}".')

    return records

# TODO: Step 8
def tally_port_traffic(log_file):
    return

# TODO: Step 9
def generate_port_traffic_report(log_file, port_number):
    return

# TODO: Step 11
def generate_invalid_user_report(log_file):
    return

# TODO: Step 12
def generate_source_ip_log(log_file, ip_address):
    return

if __name__ == '__main__':
    main()