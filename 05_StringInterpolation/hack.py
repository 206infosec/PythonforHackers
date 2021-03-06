"""
If else, elseif are supported, space delimited like the rest of python

Brutespray examples

Not in Brutespray but really needs to be
"""

protocols = {"postgressql":"sql",
             "pop3": "email"}

people_protocol = [["Steve", "postgressql"],
                   ["Alice", "pop3"],
                   ["Alice", "sql"]]

for person, protocol in people_protocol:
    if person == "Alice":

        # .format string formatting/interpolation. Use this instead of + signs
        print("Hacking {0} with {1} even harder".format(person, protocol))
    else:
        # Python 2 style, no longer fashionable
        print("Hacking %s with %s" % (person, protocol))
