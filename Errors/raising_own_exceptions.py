#Why Raise exist -> Python can encounter the calculation and syntax related error but it can't encounter errors in app's custom rules (like this field cannot contain negetive numbers).
#raise Exception("message") -> This will manually trigger a custom error and take down the function if the user's input violate the rules.
#Early guard patter -> When you put raise in the function the first thing that happens is that it checks if the user's input or logic is correct.

def ssh_input_validation(hostname, port):
    if hostname == "":
        raise Exception("Hostname Can't be Empty!")
    if port < 1 or port > 65535:
        raise Exception("Invalid Port Number!")
    return f"{hostname} is Hostname and {port} is the Port number!!!"

try:
    print(ssh_input_validation("",22222212))
except Exception as e:
    print(e)