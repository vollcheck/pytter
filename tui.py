import npyscreen as n


class MessageBox(n.BoxTitle):
    def create(self, **kwargs):
        client = None  # TODO: Get the messages from Gitter API.
        self.buff = len(client.dialogs) * [None]


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


class App(n.NPSAppManaged):  # telegram tui has inherits the StandardApp
    def onStart(self):
        self.addForm("MAIN", MainForm)


if __name__ == '__main__':
    application = App()
    application.run()
