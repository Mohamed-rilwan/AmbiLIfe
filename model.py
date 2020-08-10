import mongoengine as model
import uuid
import json

db = model.connect(host='mongodb+srv://m001-student:m001-mongodb-basics@cluster0-pkj8t.mongodb.net/Trial2?retryWrites=true&w=majority')

class TrafficLightPos(model.EmbeddedDocument):
    id = model.UUIDField(primary_key=True, binary=False)
    location = model.PointField()


class Places(model.EmbeddedDocument):
    id = model.UUIDField(primary_key=True, binary=False)
    name = model.StringField(required=True, max_length=120, unique=True)
    traffic_light_pos = model.ListField(model.EmbeddedDocumentField(TrafficLightPos))


class TraficLight(model.Document):
    city = model.StringField(required=True)
    places = model.ListField(model.EmbeddedDocumentField(Places))


# t1 = TrafficLightPos(id=uuid.uuid4(), location=[12.917306, 77.622176])
# t2 = TrafficLightPos(id=uuid.uuid4(), location=[12.917677, 77.623321])
# t3 = TrafficLightPos(id=uuid.uuid4(), location=[12.916599, 77.622922])

# p1 = Places(id=uuid.uuid4(), name="Silkboard", traffic_light_pos=[t1, t2, t3])

# T = TraficLight(city="Bangalore", places=[p1])

# T.save()

# T = TraficLight.objects.get(city="Bangalore").filter(name="Silkboard")

#----------------------------------------
# t1 = TrafficLightPos(id=uuid.uuid4(), location=[12.917306, 77.622176])
# t2 = TrafficLightPos(id=uuid.uuid4(), location=[12.917677, 77.623321])
# t3 = TrafficLightPos(id=uuid.uuid4(), location=[12.916599, 77.622922])
#
# p1 = Places(id=uuid.uuid4(), name="Silkboard", traffic_light_pos=[t1, t2, t3])
#
# T = TraficLight(city="Bangalore", places=[p1])
#
# T.save()

# T = TraficLight.objects.get(city="Bangalore").filter(name="Silkboard")