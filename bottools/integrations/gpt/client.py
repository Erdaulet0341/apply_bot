from typing import List

from openai import OpenAI
from openai.types.beta import Thread
from openai.types.beta.threads import Message

from bottools.helpers.utils import get_env


class Client:
    def __init__(self):
        self.client = OpenAI(api_key=get_env('OPENAI_API_KEY'))

    def create_thread(self) -> Thread:
        return self.client.beta.threads.create()

    def create_message(self, thread_id: str, content: str, role) -> Message:
        return self.client.beta.threads.messages.create(
            thread_id=thread_id,
            role=role,
            content=content
        )

    def list_messages(self, thread_id: str, limit: int) -> List[Message]:
        res = self.client.beta.threads.messages.list(
            thread_id=thread_id,
            order="desc",
            limit=limit
        )
        return res.data

    def create_run(self, thread_id: str, assistant_id: str, ):
        run = self.client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id)
        return run

    def cancel_run(self, thread_id: str, run_id: str):
        return self.client.beta.threads.runs.cancel(
            thread_id=thread_id,
            run_id=run_id
        )

    def retrieve_run(self, thread_id: str, run_id: str):
        return self.client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )
