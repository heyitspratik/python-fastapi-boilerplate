"""Business logic, one class per feature in ``<feature>_service.py``.

Controllers handle HTTP only and call these. A service takes the clients it
needs in ``__init__``, so it never imports FastAPI and can be tested without
a request. Queries belong in ``app/db/services/``, and code that is not
business logic (parsing, formatting, calls to other systems) in
``app/helpers/``.

Example:
    class OrderService:
        def __init__(self, session: AsyncSession) -> None:
            self.session = session

        async def get_order(self, order_id: int) -> OrderResponse: ...

    # In the controller method:
    order_service = OrderService(session)
    order = await order_service.get_order(order_id)
"""

__all__: list[str] = []
