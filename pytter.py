from pprint import pprint

from gitterpy.client import GitterClient

TOKEN = "63e45c87f9fa2a0fecab53fceb2776f33022f695"


def auth():
    # Once create instance
    gitter = GitterClient(TOKEN)

    # Check_my id
    print(gitter.auth.get_my_id)
    return gitter


def rooms(gitter):
    # Join into the room
    # gitter.rooms.join('gitterHQ/sandbox')

    # Leave from the room
    # gitter.rooms.leave('gitterHQ/sandbox')

    # List of rooms
    pprint(gitter.rooms.rooms_list)

    # Grab room
    # gitter.rooms.grab_room('gitterHQ/sandbox')

    # Room sub-resource
    # print(gitter.rooms.sub_resource('gitterHQ/sandbox'))

    # Update room topic
    # gitter.rooms.update('test-gitter/test1', 'My updated topic')

    # Delete the room
    # gitter.rooms.delete_room('test-gitter/test1') #  {'success': True}


def messages(gitter):
    # Send a message to #gitterHQ/sandbox room
    gitter.messages.send('Alex Bender', 'Okay, it works')

    # Message list
    pprint(gitter.messages.list('caveatemptor/community'))

    # Get single message by id
    # gitter.messages.get_message('gitterHQ/sandbox', '5903a16d6a471')


def groups(gitter):
    # List of groups
    gitter.groups.groups_list

    # Chat messages
    # Current user
    gitter.user.current_user #  [{'displayName': 'freshjelly', 'id': '3131', ...}]

    # User sub-resource
    gitter.user.sub_resource # [{'noindex': True, 'id': '3131', ...}]

    # User unread-items
    gitter.user.unread_items('gitterHQ/sandbox') # {'mention': [], 'chat': []}

    # Mark all messages in the room as read
    gitter.user.mark_as_read('test-gitter/Lobby') # {'success': True}

    # User orgs
    gitter.user.orgs # [{'name': 'bla bla', 'description': 'blabla', ...}]

    # User repos
    gitter.user.repos # [{'name': 'MichaelYusko/GitterPy', 'description': 'Python for the Gitter API', ...}]


def channels(gitter):
    # User channels
    pprint(gitter.user.channels)

    response = gitter.stream.chat_messages('Alex Bender')

    for stream_messages in response.iter_lines():
        if stream_messages:
            print(stream_messages)

def events(gitter):
    # Events
    pprint(gitter.stream.events('Alex Bender'))


# if __name__ == "__main__":
#     auth()

gitter = auth()
# rooms(gitter)
# messages(gitter)
channels(gitter)
# events(gitter)

# what is gitter.stream
