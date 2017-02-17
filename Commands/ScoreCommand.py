
import abc
from .abstract import MessageCommand
from openpyxl import load_workbook

class ScoreCommand(MessageCommand.MessageCommand):

    def getMessage(self):
        wb = load_workbook('../files/info.xlsx')
        return "2 à 1 pour Optic";