# Call history

class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        call_string = f"{other_phone.phone_number} called"
        print(call_string)
        self.call_history.append(call_string)

    def show_call_history(self):
        print(f"Call history on {self.phone_number}")
        for number in self.call_history:
            print(number)

    def send_message(self, other_phone, content):
        message = {}
        message['from'] = self.phone_number
        message['to'] = other_phone.phone_number
        message['content'] = content
        self.messages.append(message)
        other_phone.messages.append(message)

    def show_outgoing_messages(self):
        print("Outgoing messages")
        for item in self.messages:
            print(f"to: {item['to']}, message: {item['content']}")

    def show_incoming_messages(self):
        print("Incoming messages")
        for item in self.messages:
            if item['to'] == self.phone_number:
                print(f"from: {item['from']}, message: {item['content']}")

    def show_messages_from(self, phone):
        print(f"Show messages from {phone}")
        for item in self.messages:
            if item["from"] == phone:
                print(f"{item['content']}")



my_phone = Phone("0700450844")
his_phone = Phone("0689763456")

my_phone.call(his_phone)
my_phone.call(his_phone)
my_phone.call(his_phone)
my_phone.call(his_phone)
my_phone.call(his_phone)

my_phone.show_call_history()

my_phone.send_message(his_phone, "Hello world" )
my_phone.send_message(his_phone, "I send message" )
my_phone.send_message(his_phone, "This is a new message" )
his_phone.send_message(his_phone, "How are you doing?" )
# print(his_phone.messages)
my_phone.show_outgoing_messages()
his_phone.show_incoming_messages()

his_phone.show_messages_from(my_phone.phone_number)