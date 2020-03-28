WAITING_FOR_ANSWER = 'Waiting for Answer'
WAITING_FOR_ACKNOWLEDGEMENT = "Waiting for acknowledgement"
WAITING_TO_CHECK_ANSWER = 'Waiting to Check Answer'
PLAYING_A_ROUND = 'Playing'
CHECKING_IN = 'Checking In'


class GameMaster():
    def __init__(self, reader, quiz, app):
        self._answering_team = None
        self._reader = reader
        self._app = app
        self._quiz = quiz
        self._round = 0
        self._message_queue = []
        self._replied = set()
        self.set_status(CHECKING_IN)

    def has_seen(self, team_id):
        return team_id in self._replied

    def check_reader(self):
        line = self._reader.readline().strip()
        if len(line) > 0:
            self._message_queue.append(line)
        for team_id in self._message_queue:
            if self.has_seen(team_id):
                self._message_queue.remove(team_id)
        if len(self._message_queue) > 0:
            self.handle_message()

    def add_new_team(self, team_id):
        self._quiz.add_new_team(team_id)
        return self.got_answer_from(team_id)

    def got_answer_from(self, team_id):
        self._answering_team = team_id
        self._replied.add(team_id)
        return self._quiz.name_for(team_id)

    def start_round(self):
        self._round += 1
        self._replied = set()
        self.set_status(PLAYING_A_ROUND)
        self._app.show_scores(self._quiz.scores())

    def status(self):
        return self._status

    def set_status(self, new_status):
        self._status = new_status
        self._app.show_status(self.extended_status())

    def extended_status(self):
        extension =  '' if self._round == 0 else ' - round %d' % self._round
        return self._status + extension

    def handle_message(self):
        if self._status == CHECKING_IN:
            team_name = self.add_new_team(self.next_answering_team())
            self.set_status(WAITING_FOR_ACKNOWLEDGEMENT)
            self._app.waiting_for_acknowledgment(team_name)
        if self._status == PLAYING_A_ROUND:
            team_name = self.got_answer_from(self.next_answering_team())
            self.set_status(WAITING_TO_CHECK_ANSWER)
            self._app.waiting_for_answer_check(team_name)

    def next_answering_team(self):
        return self._message_queue.pop(0)

    def correct(self):
        self._quiz.got_correct_answer_from(self._answering_team)

    def wrong(self):
        self.set_status(PLAYING_A_ROUND)

    def wait_for_next_team(self):
        self.set_status(CHECKING_IN)