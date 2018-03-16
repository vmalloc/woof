# Woof

## What is it?

Woof is a small utility library to simplify notification support for system scripts. It is aimed at
minimizing the amount of configuration needed through code, and provides flexible ways to configure
your notifications.

## How to use it?

Given the following script (shown here using [fades](https://pypi.python.org/pypi/fades/) to
demonstrate zero-environment configuration):

```python
#! /usr/bin/env fades
from woof import notify
import shutil

if __name__ == "__main__":
    shutil.rmtree("/path/to/delete") # <-- takes time
    notify("Finished deleting!")
```

By default, running this script will do nothing since *woof* is lacking any configuration telling it
how to send notifications.

However, adding a notification backend is possible even without changing the code above. Let's add
notifications through telegram, for example:

```
$ WOOF_TELEGRAM_APIKEY=xx-xxx-xxx-xxxxx WOOF_TELEGRAM_CHAT_ID=1234 ./script.py
```

The above will make woof send the message through the Telegram backend!


## License

Woof is licensed under the MIT open source license
