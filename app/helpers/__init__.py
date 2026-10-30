"""Code the services use that is not business logic, in ``<topic>_helper.py``.

For example: ``auth_helper.py`` (token checks), ``file_helper.py`` (upload
validation), ``date_helper.py`` (formatting). A helper knows nothing about
HTTP requests or this service's business rules, so any service can reuse it.
"""

__all__: list[str] = []
