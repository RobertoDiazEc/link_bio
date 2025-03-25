import asyncio
import reflex as rx


class ProgressState(rx.State):
    value: int = 0

    @rx.event(background=True)
    async def start_progress(self):
        async with self:
            self.value = 0
        while self.value < 100:
            await asyncio.sleep(0.1)
            async with self:
                self.value += 1


def live_progress():
    return rx.box(
        rx.hstack(
                rx.progress(value=ProgressState.value),
                rx.button(
            "Start", on_click=ProgressState.start_progress
                ),
                width="50%",
            ),
        border_radius="10px",
        background_color="var(--gray-2)",
        padding="3em",
        position="fixed",
        bottom="10px",
        z_index="1000",
        width="80%",
        overflow="auto" 
)