# decorator_menu.py
# author: Daniel Jauergui
# date: 3-31-2015


def request_answer_menu(function):
    def request_answer(*args):
        op = 999
        while op != 0:
            rest = function(op)
            #if op != 999:
            #    op = 0
            try:
                if op == 0:
                    break
                op = input("\n\nPlease select an option: ")
            except:
                op = 999
    return request_answer