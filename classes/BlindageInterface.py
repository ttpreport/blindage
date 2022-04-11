from PyInquirer import prompt, Separator


class BlindageInterface:
    @staticmethod
    def print_good(data):
        print("\x1b[1;32m[+]\x1b[m " + data)

    @staticmethod
    def print_bad(data):
        print("\x1b[1;31m[-]\x1b[m " + data)

    @staticmethod
    def ask_checkbox(question_text, answer_choices):
        question = [
            {
                'type': 'checkbox',
                'name': 'result',
                'message': question_text,
                'choices': answer_choices
            }
        ]
        return prompt(question)['result']

    @staticmethod
    def ask_list(question_text, answer_choices):
        question = [
            {
                'type': 'list',
                'name': 'result',
                'message': question_text,
                'choices': answer_choices
            }
        ]
        return prompt(question)['result']

    @staticmethod
    def ask_text(question_text, default='', validate=None):
        if not default:
            default = ''

        question = [
            {
                'type': 'input',
                'name': 'result',
                'message': question_text,
                'default': default,
                'validate': validate
            }
        ]
        return prompt(question)['result']

    @staticmethod
    def ask_yesno(question_text):
        question = [
            {
                'type': 'confirm',
                'name': 'result',
                'message': question_text,
                'default': False
            }
        ]
        return prompt(question)['result']

    @staticmethod
    def get_separator(text):
        return Separator(text)
