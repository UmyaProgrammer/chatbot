from chatbot import Chatbot


def main():
    print(r"""
     __      __       .__                                  __              _____           __________        __         .__.__                
/  \    /  \ ____ |  |   ____  ____   _____   ____   _/  |_  ____     /     \_______   \______   \ _____/  |______  |__|  |   ___________ 
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \   /  \ /  \_  __ \   |       _// __ \   __\__  \ |  |  |  /  _ \_  __ \
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> ) /    Y    \  | \/   |    |   \  ___/|  |  / __ \|  |  |_(  <_> )  | \/
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/  \____|__  /__| /\   |____|_  /\___  >__| (____  /__|____/\____/|__|   
       \/       \/          \/            \/     \/                         \/     \/          \/     \/          \/                      
    """)
    print("\n\n")
    user_fname = input("What is your first name? ")
    user_lname = input("What is your last name? ")
    user_age = input("What is your age? ")
    print()

    return user_fname, user_lname, user_age


def ask_to_continue(f_name: str):
    response = input(f"Would you like to continue {f_name}? (y/n): ").strip().lower()
    while response not in ("y", "n"):
        response = input("Please enter (y/n): ").strip().lower()
    return response == 'y'


if __name__ == "__main__":
    user_fname, user_lname, user_age = main() 
    chatbot = Chatbot(fname=user_fname, lname=user_lname, age=user_age)
    # chatbot = Chatbot(fname="Usame", lname="Alan", age=17)
    chatbot.greet()
    chatbot.options_list()
    
    should_continue = chatbot.start_conversation()

    while should_continue:
        should_continue = chatbot.continue_conversation()


    chatbot.farewell()
    
    