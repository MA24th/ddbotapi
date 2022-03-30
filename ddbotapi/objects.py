# -*- coding: utf-8 -*-

"""
ddbotapi.objects
~~~~~~~~~~~~~~~~
This submodule provides a Discord Available Objects,
All types used in the Bot API responses are represented as JSON-objects,
that are also useful for external consumption.
"""

from .utils import *


class Application(JsonDeserializable):
    """
    This object represents an Application Structure
    """
    def __init__(self, uid, name, icon, description, rpc_origins, bot_public, bot_require_code_grant,
                 terms_of_service_url, privacy_policy_url, owner, summary, verify_key, team, guild_id, primary_sku_id,
                 slug, cover_image, flags):
        self.id = uid
        self.name = name
        self.icon = icon
        self.description = description
        self.rpc_origins = rpc_origins
        self.bot_public = bot_public
        self.bot_require_code_grant = bot_require_code_grant
        self.terms_of_service_url = terms_of_service_url
        self.privacy_policy_url = privacy_policy_url
        self.owner = owner
        self.summary = summary
        self.verify_key = verify_key
        self.team = team
        self.guild_id = guild_id
        self.primary_sku_id = primary_sku_id
        self.slug = slug
        self.cover_image = cover_image
        self.flags = flags

    @classmethod
    def de_json(cls, obj_type):
        obj = cls.check_type(obj_type)
        uid = None
        if 'id' in obj:
            uid = obj['id']
        name = None
        if 'name' in obj:
            name = obj['name']
        icon = None
        if 'icon' in obj:
            icon = obj['icon']
        description = None
        if 'description' in obj:
            description = obj['description']
        rpc_origins = None
        if 'rpc_origins' in obj:
            rpc_origins = obj['rpc_origins']
        bot_public = False
        if 'bot_public' in obj:
            bot_public = obj['bot_public']
        bot_require_code_grant = None
        if 'bot_require_code_grant' in obj:
            bot_require_code_grant = obj['bot_require_code_grant']
        terms_of_service_url = None
        if 'terms_of_service_url' in obj:
            terms_of_service_url = obj['terms_of_service_url']
        privacy_policy_url = None
        if 'privacy_policy_url' in obj:
            privacy_policy_url = obj['privacy_policy_url']
        owner = None
        if 'owner' in obj:
            owner = User.de_json(obj['owner'])
        summary = None
        if 'summary' in obj:
            summary = obj['summary']
        verify_key = None
        if 'verify_key' in obj:
            verify_key = obj['verify_key']
        team = None
        if 'team' in obj:
            team = obj['team']
        guild_id = None
        if 'guild_id' in obj:
            guild_id = obj['guild_id']
        primary_sku_id = None
        if 'primary_sku_id' in obj:
            primary_sku_id = obj['primary_sku_id']
        slug = None
        if 'slug' in obj:
            slug = obj['slug']
        cover_image = None
        if 'cover_image' in obj:
            cover_image = obj['cover_image']
        flags = None
        if 'flags' in obj:
            flags = obj['flags']
        return cls(uid, name, icon, description, rpc_origins, bot_public, bot_require_code_grant, terms_of_service_url,
                   privacy_policy_url, owner, summary, verify_key, team, guild_id, primary_sku_id, slug, cover_image,
                   flags)


class User(JsonDeserializable):
    """
    This object represents a User Structure
    """

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
        bot = False
        if 'bot' in obj:
            bot = True  # bot = obj['bot']
        system = False
        if 'system' in obj:
            system = True  # system = obj['system']
        mfa_enabled = False
        if 'mfa_enabled' in obj:
            mfa_enabled = True  # mfa_enabled = obj['mfa_enabled']
        banner = None
        if 'banner' in obj:
            banner = obj['banner']
        accent_color = None
        if 'accent_color' in obj:
            accent_color = obj['accent_color']
        locale = None
        if 'locale' in obj:
            locale = obj['locale']
        verified = False
        if 'verified' in obj:
            verified = True  # verified = obj['verified']
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


class Connection(JsonDeserializable):
    """
    This object represents user has attached
    """

    def __init__(self, uid, name, ttype, revoked, integration, verified, friend_sync, show_activity, visibility):
        self.id = uid
        self.name = name
        self.type = ttype
        self.revoked = revoked
        self.integration = integration
        self.verified = verified
        self.friend_sync = friend_sync
        self.show_activity = show_activity
        self.visibility = visibility

    @classmethod
    def de_json(cls, obj_type):
        obj = cls.check_type(obj_type)
        uid = None
        if 'id' in obj:
            uid = obj['id']
        name = None
        if 'name' in obj:
            name = obj['name']
        ttype = None
        if 'type' in obj:
            ttype = obj['type']
        revoked = False
        if 'revoked' in obj:
            revoked = True
        integrations = None
        if 'integrations' in obj:
            integrations = obj['integrations']
        verified = False
        if 'verified' in obj:
            verified = True
        friend_sync = False
        if 'friend_sync' in obj:
            friend_sync = True
        show_activity = False
        if 'show_activity' in obj:
            show_activity = True
        visibility = None
        if 'visibility' in obj:
            visibility = obj['visibility']
        return cls(uid, name, ttype, revoked, integrations, verified, friend_sync, show_activity, visibility)
