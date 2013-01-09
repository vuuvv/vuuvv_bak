import datetime
from flask import url_for
from vuuvv import db

METHOD = ('GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'TRACE', 'ALL')

class Permission(db.EmbeddedDocument):
    view = db.StringField(max_length=255, required=True)
    methods = db.ListField(
        db.StringField(max_length=10, required=True, choices=METHOD),
        default=['GET']
    )

class Role(db.Document):
    name = db.StringField(max_length=255, required=True)
    permissions = db.ListField(db.EmbeddedDocumentField(Permission))
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)

class User(db.Document):
    username = db.StringField(max_length=255, required=True)
    password = db.StringField(max_length=255, required=True)
    email = db.StringField(max_length=255, required=True)
    permissions = db.ListField(db.EmbeddedDocumentField(Permission))
    roles = db.ListField(db.ReferenceField(Role, dbref=True))
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)

