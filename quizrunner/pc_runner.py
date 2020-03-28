from guizero import App, ListBox, TextBox, PushButton

from quizrunner.quiz import Quiz
from quizrunner.quiz_app import QuizApp
from quizrunner.game_master import GameMaster
from quizrunner.reader import SerialReader

import pkg_resources



# TODO: add labels above team list, scores


class GuiApp(App, QuizApp):

    def __init__(self, reader):
        App.__init__(self, title='Quiz Runner', layout='grid')
        self._create_view()
        self._game_master = GameMaster(reader, Quiz(), self)
        self.repeat(100, self._game_master.check_reader)  # Schedule call to counter() every 100ms

    def _create_view(self):
        self._status_text = TextBox(self, grid=[1, 0, 2, 1], width=30)
        self._status_text.disable()
        self._team_list = ListBox(self, grid=[0, 0, 1, 2])
        self._score_list = ListBox(self, grid=[0, 2, 1, 2])
        self._next_button = PushButton(self, text='Next', command=self._next_message, grid=[1, 1])
        self._next_button.disable()
        self._done_button = PushButton(self, text='Done', command=self.start_round, grid=[2, 1])
        self._done_button.disable()
        self._ok_button = PushButton(self, image=pkg_resources.resource_filename('quizrunner','tick.png'), command=self._correct, grid=[1, 2])
        self._wrong_button = PushButton(self, image=pkg_resources.resource_filename('quizrunner','cross.png'), command=self._wrong, grid=[2, 2])
        self._hide_checks()

    def _correct(self):
        self._game_master.correct()
        self.start_round()

    def _wrong(self):
        self._team_list.clear()
        self._disable_checks()
        self._done_button.enable()
        self._game_master.wrong()

    def _hide_checks(self):
        self._ok_button.visible = False
        self._wrong_button.visible = False


    def _next_message(self):
        self._next_button.disable()
        self._game_master.wait_for_next_team()

    def _enable_checks(self):
        self._ok_button.visible = True
        self._ok_button.enable()
        self._wrong_button.visible = True
        self._wrong_button.enable()

    def _disable_checks(self):
        self._ok_button.disable()
        self._wrong_button.disable()

    # **PUBLIC methods start here**

    def start_round(self):
        self._team_list.clear()
        self._done_button.disable()
        self._disable_checks()
        self._next_button.disable()
        self._game_master.start_round()

    def show_status(self, status):
        self._status_text.value = status

    def waiting_for_acknowledgment(self, answering_team):
        self._team_list.append(answering_team)
        self._next_button.enable()
        self._done_button.enable()

    def waiting_for_answer_check(self, answering_team):
        self._team_list.append(answering_team)
        self._enable_checks()

    def add_team(self, team_name):
        self._team_list.append(team_name)

    def show_scores(self, scores):
        self._score_list.clear()
        for team_name in scores:
            self._score_list.append('%s: %d' % (team_name, scores[team_name]))

def main():
    app = GuiApp(SerialReader())
    app.display()

if __name__ == '__main__':
    main()
