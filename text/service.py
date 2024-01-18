from text.enums import TXTActions
from text.rm_newln import run_rmln
from text.word_count import run_word_counter


def run_text_action(action: TXTActions):
    match action:
        case TXTActions.REMOVE_NEWLINES:
            run_rmln()
        case TXTActions.WORD_COUNT:
            run_word_counter()
