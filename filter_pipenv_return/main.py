def filter_return(message):
    if 'WARNING' in message:
        modified_message = message.split('WARNING')[0][1:-2].split(', ')
        return [" ".join(modified_message[i:i+2]) for i in range(0, len(modified_message), 2)]
    else:
        modified_message = message[1:-1].split(', ')
        return [" ".join(modified_message[i:i+2]) for i in range(0, len(modified_message), 2)]


list_with_warning = filter_return("[{\"name\": \"axe-selenium-python\", \"version\": \"2.1.6\"}, {\"name\": \"click\", \"version\": \"7.1.2\"}, {\"name\": \"Faker\", \"version\": \"4.14.0\"}, {\"name\": \"pip\", \"version\": \"20.1.1\"}, {\"name\": \"pydantic\", \"version\": \"1.7.1\"}, {\"name\": \"pyfiglet\", \"version\": \"0.8.post1\"}, {\"name\": \"pytest-parallel\", \"version\": \"0.1.0\"}, {\"name\": \"pytest-reportportal\", \"version\": \"5.0.5\"}, {\"name\": \"pytest-xdist\", \"version\": \"2.1.0\"}, {\"name\": \"setuptools\", \"version\": \"47.1.0\"}, {\"name\": \"webdriver-manager\", \"version\": \"3.2.2\"}]\nWARNING: You are using pip version 20.1.1; however, version 20.2.4 is available.\nYou should consider upgrading via the '/Users/gleek/Downloads/pyleniumio-master/venv/bin/python3 -m pip install --upgrade pip' command.")
list_no_warning = filter_return("[{\"name\": \"axe-selenium-python\", \"version\": \"2.1.6\"}, {\"name\": \"click\", \"version\": \"7.1.2\"}, {\"name\": \"Faker\", \"version\": \"4.14.0\"}, {\"name\": \"pip\", \"version\": \"20.1.1\"}, {\"name\": \"pydantic\", \"version\": \"1.7.1\"}, {\"name\": \"pyfiglet\", \"version\": \"0.8.post1\"}, {\"name\": \"pytest-parallel\", \"version\": \"0.1.0\"}, {\"name\": \"pytest-reportportal\", \"version\": \"5.0.5\"}, {\"name\": \"pytest-xdist\", \"version\": \"2.1.0\"}, {\"name\": \"setuptools\", \"version\": \"47.1.0\"}, {\"name\": \"webdriver-manager\", \"version\": \"3.2.2\"}]")

print(list_with_warning[0])
print(list_no_warning[0])
