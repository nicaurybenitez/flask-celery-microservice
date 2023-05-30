from flask import Blueprint, request, jsonify
from celery.result import AsyncResult
from app.tasks import report

bp = Blueprint('report', __name__, url_prefix='/report')

@bp.route('/', methods=['POST'])
def generate_report():
    async_result = report.delay()
    return jsonify({"report_id": async_result.id})

@bp.route('/<report_id>')
def get_report(report_id):
    res = AsyncResult(report_id, app=bp.celery)
    return jsonify({"id": res.id, "result": res.result})

def register_routes(app):
    app.register_blueprint(bp)
    return app

app = register_routes(app)
