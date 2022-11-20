from backend.dictionary import get_word



def option_button(num):
    game_frame.tkraise()
    get_word()
    print(get_word())
    num = len(get_word())
    return num


print(option_button())
