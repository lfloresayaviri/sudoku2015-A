# decorator_menu.py

def request_answer_menu(function):
    def request_answer():
        op = 999
        while (op != 0):
            function(op)
            if (op!=999):
                op=0
            try:
                if (op==0):
                    break
                op = input("\n\nPlease select an option: ")
            except:
                op = 999
    return request_answer
