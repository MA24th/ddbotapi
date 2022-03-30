import unittest
from ddbotapi.objects import *


class TestApplication(unittest.TestCase):
    with open('schema/Application.json') as f:
        data = f.read()

    object = Application.de_json(data)

    def test_application(self):
        app = self.object
        self.assertEqual(app.id, '172150183260323840')
        self.assertEqual(app.name, 'Baba O-Riley')
        self.assertEqual(app.icon, None)
        self.assertEqual(app.description, 'Test')
        self.assertEqual(app.rpc_origins, None)
        self.assertEqual(app.bot_public, True)
        self.assertEqual(app.bot_require_code_grant, False)
        self.assertEqual(app.terms_of_service_url, None)
        self.assertEqual(app.privacy_policy_url, None)
        # app.owner -> test_app_owner()
        self.assertEqual(app.summary, 'This is a game')
        self.assertEqual(app.verify_key, '1e0a356058d627ca38a5c8c9648818061d49e49bd9da9e3ab17d98ad4d6bg2u8')
        # app.team -> test_app_team()
        self.assertEqual(app.guild_id, '290926798626357260')
        self.assertEqual(app.primary_sku_id, '172150183260323840')
        self.assertEqual(app.slug, 'test')
        self.assertEqual(app.cover_image, '31deabb7e45b6c8ecfef77d2f99c81a5')
        self.assertEqual(app.flags, None)

    def test_app_owner(self):
        user = self.object.owner
        self.assertEqual(user.id, '172150183260323840')
        self.assertEqual(user.username, 'i own a bot')
        self.assertEqual(user.discriminator, '1738')
        self.assertEqual(user.avatar, None)
        self.assertEqual(user.bot, False)
        self.assertEqual(user.system, False)
        self.assertEqual(user.mfa_enabled, False)
        self.assertEqual(user.banner, None)
        self.assertEqual(user.accent_color, None)
        self.assertEqual(user.locale, None)
        self.assertEqual(user.verified, False)
        self.assertEqual(user.email, None)
        self.assertEqual(user.flags, 1024)
        self.assertEqual(user.premium_type, None)
        self.assertEqual(user.public_flags, None)

class TestUser(unittest.TestCase):
    with open('schema/User.json') as f:
        data = f.read()

    object = User.de_json(data)

    def test_user(self):
        user = self.object
        self.assertEqual(user.id, '80351110224678912')
        self.assertEqual(user.username, 'Nelly')
        self.assertEqual(user.discriminator, '1337')
        self.assertEqual(user.avatar, '8342729096ea3675442027381ff50dfe')
        self.assertEqual(user.bot, False)
        self.assertEqual(user.system, False)
        self.assertEqual(user.mfa_enabled, False)
        self.assertEqual(user.banner, '06c16474723fe537c283b8efa61a30c8')
        self.assertEqual(user.accent_color, 16711680)
        self.assertEqual(user.locale, None)
        self.assertEqual(user.verified, True)
        self.assertEqual(user.email, 'nelly@discord.com')
        self.assertEqual(user.flags, 64)
        self.assertEqual(user.premium_type, 1)
        self.assertEqual(user.public_flags, 64)


class TestConnection(unittest.TestCase):
    with open('schema/Connection.json') as f:
        data = f.read()

    object = Connection.de_json(data)

    def test_connection(self):
        connection = self.object
        self.assertEqual(connection.id, '80351110224678912')
        self.assertEqual(connection.name, 'Nelly')
        self.assertEqual(connection.type, '1337')
        self.assertEqual(connection.revoked, True)
        self.assertEqual(connection.integration, [])
        self.assertEqual(connection.verified, True)
        self.assertEqual(connection.friend_sync, True)
        self.assertEqual(connection.show_activity, True)
        self.assertEqual(connection.visibility, 1)
