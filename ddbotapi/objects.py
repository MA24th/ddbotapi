# -*- coding: utf-8 -*-

"""
ddbotapi.objects
~~~~~~~~~~~~~~~~
This submodule provides a Discord Available Objects,
All types used in the Bot API responses are represented as JSON-objects,
that are also useful for external consumption.
"""

from .utils import *


class User(JsonDeserializable):
    def __init__(self, uid, username, discriminator, avatar, bot, system, mfa_enabled, banner, accent_color, locale,
                 verified, email, flags, premium_type, public_flags):
        self.id = uid
        self.username = username
        self.discriminator = discriminator
        self.avatar = avatar
        self.bot = bot
        self.system = system
        self.mfa_enabled = mfa_enabled
        self.banner = banner
        self.accent_color = accent_color
        self.locale = locale
        self.verified = verified
        self.email = email
        self.flags = flags
        self.premium_type = premium_type
        self.public_flags = public_flags

    @classmethod
    def de_json(cls, obj_type):
        obj = cls.check_type(obj_type)
        uid = None
        if 'id' in obj:
            uid = obj['id']
        username = None
        if 'username' in obj:
            username = obj['username']
        discriminator = None
        if 'discriminator' in obj:
            discriminator = obj['discriminator']
        avatar = None
        if 'avatar' in obj:
            avatar = obj['avatar']
        bot = None
        if 'bot' in obj:
            bot = obj['bot']
        system = None
        if 'system' in obj:
            system = obj['system']
        mfa_enabled = None
        if 'mfa_enabled' in obj:
            mfa_enabled = obj['mfa_enabled']
        banner = None
        if 'banner' in obj:
            banner = obj['banner']
        accent_color = None
        if 'accent_color' in obj:
            accent_color = obj['accent_color']
        locale = None
        if 'locale' in obj:
            locale = obj['locale']
        verified = None
        if 'verified' in obj:
            verified = obj['verified']
        email = None
        if 'email' in obj:
            email = obj['email']
        flags = None
        if 'flags' in obj:
            flags = obj['flags']
        premium_type = None
        if 'premium_type' in obj:
            premium_type = obj['premium_type']
        public_flags = None
        if 'public_flags' in obj:
            public_flags = obj['public_flags']
        return cls(uid, username, discriminator, avatar, bot, system, mfa_enabled, banner, accent_color, locale,
                   verified, email, flags, premium_type, public_flags)
