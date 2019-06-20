"""Automata Bot is ready"""
import requests
import random

URL = "https://api.noopschallenge.com/automatabot/rules"
URL_challange ="https://api.noopschallenge.com/automatabot/challenges/new"

class AutomataBot:

    def __init__(self):
        self.download = self.fetch_rules()
        self.rules = random.choice(self.download)
        self.challenge = self.fetch_challange()
        self.challengepath = self.challenge['challengePath']

        self.name = self.challenge['challenge']['rules']['name']
        self.birth = self.challenge['challenge']['rules']['birth']
        self.survival = self.challenge['challenge']['rules']['survival']

        self.cells = self.challenge['challenge']['cells']
        self.generations = self.challenge['challenge']['generations']

        self.rows = len(self.cells)
        self.cols = len(self.cells[0])

    def __str__(self):
        return "Name: {}, Birth: {}, Survival: {}, Life Span: {}, \nCells: {}, Cols: {}, Rows: {}".format(
            self.name, self.birth, self.survival, self.generations, self.cells, self.rows, self.rows)

    @staticmethod
    def fetch_rules():
        req = requests.get(URL)
        result = req.json()
        return result

    def fetch_challange(self):
        req = requests.get(URL_challange)
        result = req.json()
        return result