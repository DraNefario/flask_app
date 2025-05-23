from models.db import db
from models.iot.devices import Device

class Actuator(db.Model):
    __tablename__ = 'actuators'
    id= db.Column('id', db.Integer, primary_key=True)
    devices_id = db.Column( db.Integer, db.ForeignKey(Device.id))
    unit = db.Column(db.String(50))
    topic = db.Column(db.String(50))

    def save_actuator(name, brand, model, topic, unit, is_active):
        device = Device(name = name, brand = brand, model = model,
                        is_active = is_active)
        actuator = Actuator(devices_id = device.id, unit = unit, topic = topic)

        device.actuators.append(actuator)
        db.session.add(device)
        db.session.commit()

    def get_actuator():
      actuators = Actuator.query.join(Device, Device.id == Actuator.devices_id)\
                        .add_columns(Device.id, Device.name,
                                      Device.brand, Device.model,
                                        Device.is_active, Actuator.topic,
                                        Actuator.unit).all()
      return actuators