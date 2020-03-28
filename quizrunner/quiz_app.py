from abc import abstractmethod, ABCMeta


class QuizApp(metaclass=ABCMeta):
    @abstractmethod
    def show_scores(self, scores):
        pass

    @abstractmethod
    def show_status(self, status):
        pass

    @abstractmethod
    def waiting_for_acknowledgment(self, team_name):
        pass

    @abstractmethod
    def waiting_for_answer_check(self, team_name):
        pass
