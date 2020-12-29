import os
from typing import List

from gitterpy.client import GitterClient
from npyscreen import BoxTitle

from message import Message


TOKEN = os.environ.get("TOKEN")
CHANNEL = os.environ.get("CHANNEL")


class Message:
    def __init__(self, data, **kwargs):
        try:
            # Valuable fields for now
            self.id = data["id"]
            self.text = data["text"]
            self.html = data["html"]
            self.sent = data["sent"]
            self.username = data["fromUser"]["username"]  # For now I just need only that field

            # Other
            self.unread = data["unread"]
            self.read_by = data["readBy"]
            self.urls = data["urls"]
            self.mentions = data["mentions"]
            self.issues = data["issues"]
            self.meta = data["meta"]
            self.v = data["v"]
        except KeyError as e:
            raise e


class MessageBox(BoxTitle):
    def get_messages(self) -> List[Message]:
        return [Message(m) for m in self.gitter.messages.list(self.channel)]

    def display_messages(self) -> None:
        self.gitter = GitterClient(TOKEN)
        self.channel = CHANNEL
        self.messages = self.get_messages()
        self.messages_buff = len(self. messages) * [None]

        # color_data = []
        # data = []
        # for i in range(len(messages) - 1, -1, -1):
        #     # replace empty char
        #     messages[i].message = messages[i].message.replace(chr(8203), '')

        #     data.append(messages[i].name + " " + messages[i].message)
        #     color_data.append(messages[i].color)

        # self.entry_widget.highlighting_arr_color_data = color_data

        self.values = [m.text for m in self.get_messages()]

        if len(self.messages) > self.height - 3:
            self.entry_widget.start_display_at = len(self.messages) - self.height + 3
        else:
            self.entry_widget.start_display_at = 0

        self.entry_widget.cursor_line = len(self.messages)

        self.name = self.channel
        # self.footer = client.online[current_user]  # the value that

        self.display()
