from shiny.session import Session, require_active_session


class TabulatorContext(object):
    def __init__(self, id: str, session: Session = None) -> None:
        self.id = id
        self._session = require_active_session(session)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.render()

    async def render(self):
        await self._session.send_custom_message(
            f"tabulator-{self.id}", {"id": self.id, "data": {"Hello": "World"}}
        )


async def tabulator_get_data(id: str, session: Session = None) -> None:
    await require_active_session(session).send_custom_message(
        f"tabulator-{id}", {"id": id, "call": "getData"}
    )
