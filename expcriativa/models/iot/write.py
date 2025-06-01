from models.db import db
from models.iot.actuators import Actuator
from models.iot.devices import Device
from datetime import datetime

class Write(db.Model):
    __tablename__ = 'write'
    id = db.Column('id', db.Integer, nullable = False, primary_key = True)
    write_datetime = db.Column(db.DateTime(), nullable = False)
    actuators_id = db.Column(db.Integer, db.ForeignKey(Actuator.id), nullable = False)
    value = db.Column(db.String(255), nullable=True)



    def save_write(topic, value):
        print(f"save_write called with topic={topic}, value={value}")
        actuator = Actuator.query.filter(Actuator.topic == topic).first()
        if actuator is None:
            print("Actuator not found for topic:", topic)
            return
        device = Device.query.filter(Device.id == actuator.devices_id).first()
        if device is None:
            print("Device not found for actuator's device id:", actuator.devices_id)
            return
        print(f"Found actuator id={actuator.id}, device is_active={device.is_active}")
        if device.is_active:
            try:
                write = Write(write_datetime=datetime.now(), actuators_id=actuator.id, value=str(value))
                db.session.add(write)
                db.session.commit()
                print("Write saved successfully")
            except Exception as e:
                print("Error saving write:", e)
        else:
            print("Device is not active, skipping write")

    
    def get_write(device_id, start, end):
        actuator = Actuator.query.filter(Actuator.devices_id == device_id).first()
        write = Write.query.filter(Write.actuators_id == actuator.id, Write.write_datetime > start, Write.write_datetime < end).all()
        return write