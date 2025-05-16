# app/routes/mqtt_routes.py

from flask import Blueprint, render_template, request, jsonify
from auth.decorators import login_required
from controllers.mqtt_controller import handle_get_mqtt_data, handle_publish_message

mqtt_routes_bp = Blueprint('mqtt_routes', __name__, template_folder="../views/templates")

@mqtt_routes_bp.route('/tempo_real')
@login_required
def tempo_real():
    values = handle_get_mqtt_data()
    return render_template("tr.html", values=values)

@mqtt_routes_bp.route('/publish')
@login_required
def publish():
    return render_template('publish.html')

@mqtt_routes_bp.route('/publish_message', methods=['POST'])
@login_required
def publish_message():
    request_data = request.get_json()
    result = handle_publish_message(request_data)
    return jsonify(result)
