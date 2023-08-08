#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django Not Found: It appears that Django is not properly installed or accessible on your PYTHONPATH environment variable. Please ensure that Django is installed and activated within your virtual environment. If you haven't set up a virtual environment, consider creating one to manage your project dependencies effectively."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
