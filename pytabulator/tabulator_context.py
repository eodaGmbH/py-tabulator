from typing import Literal

from shiny.session import Session, require_active_session


class TabulatorContext(object):
    """Table context"""

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

    def trigger_download(
        self, type: Literal["csv", "json"] = "csv", file_name: str = None
    ) -> None:
        """Trigger download"""
        if not file_name:
            file_name = f"tabulator-data.{type}"

        self.add_call("download", type, file_name)

    def add_row(self, row: dict = {}) -> None:
        """Add a row to the bottom of the table"""
        self.add_call("addRow", row)

    def delete_row(self, row_number: int) -> None:
        """Delete a row from the table"""
        self.add_call("deleteRow", row_number)

    def delete_selected_rows(self) -> None:
        """Delete selected rows from table"""
        self.add_call("deleteSelectedRows")

    def undo(self) -> None:
        self.add_call("undo")

    def redo(self) -> None:
        self.add_call("redo")

    def trigger_get_data(self) -> None:
        """Trigger sending data"""
        self.add_call("getData")
