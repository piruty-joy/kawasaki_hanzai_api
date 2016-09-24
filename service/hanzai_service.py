# coding: utf-8

from repository.hanzai_repository import HanzaiRepository


class HanzaiService:

    def __init__(self):
        pass

    def find_all_hanzai(self):
        hanzai_repository = HanzaiRepository()
        return hanzai_repository.find_all()

    def find_hanzai_between_dates(self, date_from, date_to):
        hanzai_repository = HanzaiRepository()
        return hanzai_repository.find_between_dates(date_from, date_to)

    def find_hanzai_monthly(self):
        hanzai_repository = HanzaiRepository()
        return hanzai_repository.find_monthly()
