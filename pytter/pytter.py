import npyscreen as n

from message_box import MessageBox


class MainForm(n.FormBaseNew):
    # def afterEditing(self):
    #     self.parentApp.setNextForm(None)

    def create(self):
        # Get the window size.
        y, x = self.useable_space()

        # UI creation.
        self.message_box = self.add(
            MessageBox,
            rely=2,
            relx=(x // 5) + 1,
            max_height=-5,
            editable=True,
            # custom_highlighting=True,
            # highlighting_arr_color_data=[0]
        )

        self.input_box = self.add(
            n.MultiLineEdit,
            name="Write a message",
            relx=(x // 5) + 1,
            rely=-7
        )

        # Initial data.
        self.message_box.display_messages()
        # self.chat_box.display_chat()  # TODO.


class Pytter(n.NPSAppManaged):  # Telegram TUI inherits the StandardApp.
    def onStart(self):
        self.addForm("MAIN", MainForm)


if __name__ == "__main__":
    pytter = Pytter()
    pytter.run()
