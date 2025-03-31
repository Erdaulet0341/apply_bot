import time
from datetime import datetime

from bottools.integrations.gpt.client import Client


class GPTConnector:
    """
    Class for connecting to the OpenAI API and processing messages.
    """

    RUN_STATUS_COMPLETED = 'completed'
    RUN_STATUS_REQUIRES_ACTION = 'requires_action'
    RUN_STATUS_FAILED = 'failed'
    RUN_STATUS_CANCELLED = 'cancelled'

    def __init__(self):
        self.client = Client()

    def create_thread(self):
        return self.client.create_thread().id

    def _create_message(self, thread_id: str, content: str, role="user"):
        return self.client.create_message(thread_id=thread_id,
                                          content=content,
                                          role=role)

    def _list_messages(self, thread_id: str, limit=20):
        messages = self.client.list_messages(thread_id, limit)
        return messages

    def _create_run(self, thread_id: str, assistant_id: str):
        return self.client.create_run(thread_id=thread_id,
                                     assistant_id=assistant_id)

    def _cancel_run(self, thread_id: str, run_id: str):
        return self.client.cancel_run(thread_id=thread_id,
                                      run_id=run_id)

    def _retrieve_run(self, thread_id: str, run_id: str):
        return self.client.retrieve_run(thread_id=thread_id,
                                        run_id=run_id)

    def process_message(self, thread_id: str, assistant_id: str, content: str, model: str = "gpt-4o-mini"):
        content = f'"{content} \n\nCurrent time is: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"'

        try:
            openai_message = self._create_message(  # Create a message in the thread
                thread_id=thread_id,
                content=content
            )

            run = self._create_run(  # Create a run for the assistant
                thread_id=thread_id,
                assistant_id=assistant_id
            )

            while run.status != self.RUN_STATUS_COMPLETED:  # Wait for the run to complete
                run = self._retrieve_run(thread_id=thread_id, run_id=run.id)
                if run.status in [self.RUN_STATUS_FAILED, self.RUN_STATUS_CANCELLED]:
                    raise Exception(f"Run ended with status: {run.status}")

                time.sleep(0.5)

            messages = self._list_messages(thread_id=thread_id, limit=1)
            assistant_response = next((msg for msg in messages if msg.role == 'assistant'), None)

            answer = assistant_response.content[0].text.value if assistant_response else None  # Get the assistant's response
            return answer

        except Exception as e:

            if 'run' in locals() and run.status != self.RUN_STATUS_COMPLETED:
                try:
                    self._cancel_run(thread_id=thread_id, run_id=run.id)
                except Exception as er:
                    print(f'Failed to cancel run: {er}')

            print(f'Error processing message: {e}')

            return None
