from __future__ import annotations

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
        """Add a method call that is executed on the table instance

        Args:
            method_name (str): The name of the method to be executed.
            *args (any): The arguments to be passed to the table method.
        """
        call = [method_name, args]
        self._message_queue.append(call)

    def trigger_download(
        self, type: Literal["csv", "json"] = "csv", file_name: str = None
    ) -> None:
        """Trigger download

        Args:
            type (str): The data type of file to be downloaded.
            file_name (str): The file name.
        """
        if not file_name:
            file_name = f"tabulator-data.{type}"

        self.add_call("download", type, file_name)

    def add_row(self, row: dict = {}) -> None:
        """Add a row to the table

        Args:
            row (dict): Row data to add.
        """
        self.add_call("addRow", row)

    def delete_row(self, index: int | str) -> None:
        """Delete a row from the table

        Args:
            index: The index of the row to delete.
        """
        self.add_call("deleteRow", index)

    def delete_selected_rows(self) -> None:
        """Delete selected rows from table"""
        self.add_call("deleteSelectedRows")

    def undo(self) -> None:
        """Trigger undo"""
        self.add_call("undo")

    def redo(self) -> None:
        """Trigger redo"""
        self.add_call("redo")

    def trigger_get_data(self) -> None:
        """Trigger sending data"""
        self.add_call("getData")
