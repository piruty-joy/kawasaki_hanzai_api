# coding: utf-8

import pymysql.cursors


class HanzaiRepository:

    def __init__(self):
        self.conn = None

    def __make_connection(self):
        if self.conn is not None:
            return
        self.conn = pymysql.connect(
            user='username',  # change to your mysql user name
            password='password',  # change to your mysql password
            host='localhost',
            db='kawasaki_hanzai',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )

    def __close_connection(self):
        if self.conn is None:
            return
        self.conn.close()

    def find_all(self):
        self.__make_connection()
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM hanzai WHERE date BETWEEN 20150401 AND 20150431 ORDER BY date")
            hanzai_list = cursor.fetchall()
        self.__close_connection()
        return hanzai_list

    def find_between_dates(self, date_from, date_to):
        self.__make_connection()
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM hanzai WHERE date BETWEEN {} AND {} ORDER BY date".format(date_from, date_to))
            hanzai_list = cursor.fetchall()
        self.__close_connection()
        return hanzai_list

    def find_monthly(self):
        self.__make_connection()
        with self.conn.cursor() as cursor:
            sql = "SELECT cast(date as SIGNED) date,cast(sum(rojou) as SIGNED) rojou,cast(sum(hittakuri) as SIGNED) hittakuri,cast(sum(akisu) as SIGNED) akisu,cast(sum(shajou) as SIGNED) shajou,cast(sum(jitensha) as SIGNED) jitensha FROM (SELECT TRUNCATE(date / 100, 0) AS date,rojou,hittakuri,akisu,shajou,jitensha FROM hanzai) hanzai_monthly GROUP BY hanzai_monthly.date;"
            cursor.execute(sql)
            hanzai_list = cursor.fetchall()
        self.__close_connection()
        return hanzai_list
