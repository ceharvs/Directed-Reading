#!/usr/bin/env python
# Tutorial from: https://docs.djangoproject.com/en/1.4/intro/tutorial01/

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
