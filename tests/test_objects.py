import unittest
from ddbotapi.objects import *


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
