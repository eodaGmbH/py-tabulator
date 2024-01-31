from shiny.session import Session, require_active_session


class TabulatorContext(object):
    def __init__(self, id: str, session: Session = None) -> None:
        self.id = id
        self._session = require_active_session(session)
        self._message_queue = []

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.render()

    async def render(self):
        await self._session.send_custom_message(
            f"tabulator-{self.id}", {"id": self.id, "calls": self._message_queue}
        )

    def add_call(self, method_name: str, *args) -> None:
        call = [method_name, args]
        self._message_queue.append(call)

    def trigger_download(self, type: str = "csv") -> None:
        self.add_call("download", type, f"tabulator-data.{type}")

    def add_row(self, row: dict = {}) -> None:
        self.add_call("addRow", row)

    def trigger_get_data(self) -> None:
        self.add_call("getData")


"""
async def tabulator_get_data(id: str, session: Session = None) -> None:
    await require_active_session(session).send_custom_message(
        f"tabulator-{id}", {"id": id, "call": "getData"}
    )
"""

"""
async def tabulator_trigger_download(id: str, session: Session = None) -> None:
    await require_active_session(session).send_custom_message(
        f"tabulator-{id}", {"id": id, "call": "triggerDownload"}
    )
"""
