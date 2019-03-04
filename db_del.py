from app import db
from app.models import Question, Option, Weight, Faction

Weight.query.delete()
Option.query.delete()
Question.query.delete()


