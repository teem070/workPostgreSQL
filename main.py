from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/prepods', methods=['GET'])
def get_prepods():
    # Список всех преподавателей, проводящих занятия в семестре
    return 0

@app.route('/groups', methods=['GET'])
def get_groups():
    # Список всех групп, проводящих занятия в семестре
    return 0

@app.route('/predmets', methods=['GET'])
def get_predmets():
    # Список всех дисциплин, запланированных в аудитории lab

    # Получаем параметр 'lab' из запроса
    lab = request.args.get('lab')

    return 0

@app.route('/pair', methods=['GET'])
def get_pair():
    # Список всех пар, запланированных в аудитории lab на дату date

    # Получаем параметры "date" и 'lab' из запроса
    date = request.args.get('date', default='2023-05-22')
    lab = request.args.get('lab')

    return 0

if __name__ == '__main__':
    app.run()