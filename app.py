# coding: utf-8

from flask import Flask, jsonify, request
from flask.ext.cors import CORS
from service.hanzai_service import HanzaiService


app = Flask(__name__)
cors = CORS(app)


@app.route('/hanzai', methods=['GET'])
def find_all_hanzai():
    hanzai_service = HanzaiService()
    return jsonify(hanzai_service.find_all_hanzai())


@app.route('/hanzai_between_dates', methods=['GET'])
def find_hanzai_between_dates():
    date_from = request.args.get('from', '')
    date_to = request.args.get('to', '')
    date_from = '20130401' if date_from is None or date_from == '' else date_from
    date_to = '20160331' if date_to is None or date_to == '' else date_to
    hanzai_service = HanzaiService()
    return jsonify(hanzai_service.find_hanzai_between_dates(date_from, date_to))


@app.route('/hanzai_monthly', methods=['GET'])
def find_hanzai_monthly():
    hanzai_service = HanzaiService()
    return jsonify(hanzai_service.find_hanzai_monthly())


if __name__ == "__main__":
    app.run()
