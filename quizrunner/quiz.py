from abc import ABCMeta, abstractmethod
from collections import OrderedDict

WAITING_FOR_START = 'Waiting for Start'
WAITING_FOR_ANSWER = 'Waiting for Answer'
WAITING_FOR_ACKNOWLEDGEMENT = "Waiting for acknowledgement"
WAITING_TO_CHECK_ANSWER = 'Waiting to Check Answer'
PLAYING_A_ROUND = 'Playing'
CHECKING_IN = 'Checking In'


class Observable(metaclass=ABCMeta):
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def changed(self, aspect, *args):
        for observer in self._observers:
            observer.notify(self, aspect, args)


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def notify(self, observable, aspect, args):
        pass


class Quiz(Observable):
    def __init__(self):
        Observable.__init__(self)
        self._teams = OrderedDict()
        self._scores = OrderedDict()
        self._team_count = 0
        self._seen = set()
        self._state = WAITING_FOR_START

    def name_for(self, team_id):
        return self._teams[team_id]

    def add_new_team(self, team_id):
        self._scores[team_id] = 0
        team_name = 'Team %d' % (1 + len(self._teams))
        self._teams[team_id] = team_name
        teams = [self._teams[team_id] for team_id in self._teams]
        self.changed('teams', teams)

    def got_correct_answer_from(self, answering_team):
        self._scores[answering_team] += 1

    def scores(self):
        result = OrderedDict()
        for team_id in self._teams:
            result[self.name_for(team_id)] = self._scores[team_id]
        return result

    def start(self, team_count):
        self.state(CHECKING_IN)
        self._team_count = team_count

    def state(self, new_state):
        self._state = new_state
        self.changed('state', new_state)

    def accepts(self, team_id):
        if len(team_id) == 0:
            return False
        if team_id not in self._teams:
            self.add_new_team(team_id)
        return True
