# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AndroidMetadata(models.Model):
    locale = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'android_metadata'


class AnnouncementPublicInfo(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    phone_number = models.TextField(unique=True)
    latest_message_id = models.TextField(blank=True, null=True)
    classification = models.IntegerField(blank=True, null=True)
    imsi = models.TextField(blank=True, null=True)
    sim_slot = models.IntegerField(blank=True, null=True)
    announcement_name = models.TextField(blank=True, null=True)
    logo_url = models.TextField(blank=True, null=True)
    plugin_type = models.IntegerField(blank=True, null=True)
    operator_type = models.IntegerField(blank=True, null=True)
    timestamp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'announcement_public_info'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlockFilter(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    filter_type = models.IntegerField(blank=True, null=True)
    filter = models.TextField(blank=True, null=True)
    criteria = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'block_filter'


class BotMenus(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    service_id = models.TextField()
    button_id = models.TextField()
    app_link = models.TextField(blank=True, null=True)
    web_link = models.TextField(blank=True, null=True)
    app_link_action = models.TextField(blank=True, null=True)
    app_link_uri = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bot_menus'


class BotRelatedBots(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    service_id = models.TextField()
    related_bot_id = models.TextField()
    title = models.TextField()
    image = models.TextField()

    class Meta:
        managed = False
        db_table = 'bot_related_bots'


class BotServiceIdSmsNumber(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    service_id = models.TextField()
    sms_number = models.TextField()

    class Meta:
        managed = False
        db_table = 'bot_service_id_sms_number'


class Bots(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    name = models.TextField()
    service_id = models.TextField()
    email = models.TextField(blank=True, null=True)
    sms = models.TextField(blank=True, null=True)
    phone_number = models.TextField(blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    tc_page = models.TextField(blank=True, null=True)
    icon_url = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_my_bot = models.IntegerField(blank=True, null=True)
    has_confirmed_chat = models.IntegerField(blank=True, null=True)
    has_confirmed_location = models.IntegerField(blank=True, null=True)
    has_confirmed_device_info = models.IntegerField(blank=True, null=True)
    addr_uri = models.TextField(blank=True, null=True)
    bg_img_url = models.TextField(blank=True, null=True)
    sub_title = models.TextField(blank=True, null=True)
    sub_image = models.TextField(blank=True, null=True)
    sub_number = models.TextField(blank=True, null=True)
    sub_description = models.TextField(blank=True, null=True)
    brand_link = models.TextField(blank=True, null=True)
    persistent_menu = models.TextField(blank=True, null=True)
    map_address = models.TextField(blank=True, null=True)
    category_list = models.TextField(blank=True, null=True)
    is_hidden_brand_home = models.IntegerField(blank=True, null=True)
    is_hidden_search = models.IntegerField(blank=True, null=True)
    bot_type = models.IntegerField(blank=True, null=True)
    latest_success_imsi = models.TextField(blank=True, null=True)
    raw_string = models.TextField(blank=True, null=True)
    bot_expires_ms = models.IntegerField(blank=True, null=True)
    bot_provider = models.TextField(blank=True, null=True)
    is_verified = models.IntegerField(blank=True, null=True)
    verification_expires = models.IntegerField(blank=True, null=True)
    verified_by = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bots'


class Categories(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    name = models.TextField()
    remote_id = models.IntegerField(blank=True, null=True)
    is_enable = models.IntegerField(blank=True, null=True)
    order_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Cmas(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    message_id = models.IntegerField(blank=True, null=True)
    conversation_id = models.IntegerField(blank=True, null=True)
    service_category = models.IntegerField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    response_type = models.IntegerField(blank=True, null=True)
    severity = models.IntegerField(blank=True, null=True)
    urgency = models.IntegerField(blank=True, null=True)
    certainty = models.IntegerField(blank=True, null=True)
    identifier = models.IntegerField(blank=True, null=True)
    alert_handling = models.IntegerField(blank=True, null=True)
    expires = models.IntegerField(blank=True, null=True)
    language = models.IntegerField(blank=True, null=True)
    expired = models.IntegerField(blank=True, null=True)
    using_mode = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmas'


class CmcCommands(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    msg_action = models.IntegerField(blank=True, null=True)
    gio_action = models.IntegerField(blank=True, null=True)
    state_action = models.IntegerField(blank=True, null=True)
    remote_id = models.IntegerField(blank=True, null=True)
    local_id = models.IntegerField(blank=True, null=True)
    conversation_id = models.IntegerField(blank=True, null=True)
    sim_slot = models.IntegerField(blank=True, null=True)
    conversation_type = models.IntegerField(blank=True, null=True)
    message_type = models.IntegerField(blank=True, null=True)
    information_message_type = models.IntegerField(blank=True, null=True)
    event_timestamp = models.IntegerField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    creator = models.TextField(blank=True, null=True)
    cmc_prop = models.TextField(blank=True, null=True)
    data_type = models.TextField(blank=True, null=True)
    request_type = models.TextField(blank=True, null=True)
    correlation_tag = models.TextField(blank=True, null=True)
    correlation_id = models.TextField(blank=True, null=True)
    chat_id = models.TextField(blank=True, null=True)
    object_id = models.TextField(blank=True, null=True)
    recipients_list = models.TextField(blank=True, null=True)
    byte_data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmc_commands'


class ConversationCategories(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    conversation_id = models.IntegerField()
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conversation_categories'


class ConversationRecipients(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    conversation_id = models.IntegerField()
    recipient_id = models.IntegerField()
    conv_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conversation_recipients'


class Conversations(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    smsmms_thread_id = models.IntegerField(blank=True, null=True)
    im_thread_id = models.IntegerField(blank=True, null=True)
    sort_timestamp = models.IntegerField()
    created_timestamp = models.IntegerField()
    snippet = models.TextField(blank=True, null=True)
    unread_count = models.IntegerField(blank=True, null=True)
    information_message_count = models.IntegerField(blank=True, null=True)
    conversation_type = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    latest_message_id = models.IntegerField(blank=True, null=True)
    is_mute = models.IntegerField()
    is_to_be_deleted = models.IntegerField()
    latest_msg_content_uri = models.TextField(blank=True, null=True)
    latest_msg_content_type = models.TextField(blank=True, null=True)
    latest_msg_width = models.IntegerField(blank=True, null=True)
    latest_msg_height = models.IntegerField(blank=True, null=True)
    latest_msg_orientation = models.IntegerField(blank=True, null=True)
    latest_msg_status = models.IntegerField(blank=True, null=True)
    latest_msg_box_type = models.IntegerField(blank=True, null=True)
    latest_msg_recipient_detail = models.TextField(blank=True, null=True)
    pin_to_top = models.IntegerField()
    is_opened = models.IntegerField(blank=True, null=True)
    is_safe = models.IntegerField(blank=True, null=True)
    using_mode = models.IntegerField(blank=True, null=True)
    classification = models.IntegerField(blank=True, null=True)
    from_address = models.TextField(blank=True, null=True)
    message_count = models.IntegerField(blank=True, null=True)
    notification_count = models.IntegerField(blank=True, null=True)
    reply_all = models.IntegerField(blank=True, null=True)
    alert_type = models.IntegerField(blank=True, null=True)
    alert_expired = models.IntegerField(blank=True, null=True)
    attach_count = models.IntegerField(blank=True, null=True)
    group_nick_name = models.TextField(blank=True, null=True)
    group_leader = models.TextField(blank=True, null=True)
    group_remark = models.TextField(blank=True, null=True)
    profile_image_uri = models.TextField(blank=True, null=True)
    notification_channel_id = models.TextField(blank=True, null=True)
    rcs_read_confirmation = models.IntegerField(blank=True, null=True)
    composer_background_uri = models.TextField(blank=True, null=True)
    composer_background_brightness = models.IntegerField(blank=True, null=True)
    is_link_sharing = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conversations'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Messages(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    conversation_id = models.IntegerField(blank=True, null=True)
    message_type = models.IntegerField()
    recipients = models.TextField(blank=True, null=True)
    message_box_type = models.IntegerField()
    message_status = models.IntegerField()
    subject = models.TextField(blank=True, null=True)
    created_timestamp = models.IntegerField(blank=True, null=True)
    sent_timestamp = models.IntegerField(blank=True, null=True)
    scheduled_timestamp = models.IntegerField(blank=True, null=True)
    remote_message_uri = models.TextField(blank=True, null=True)
    message_size = models.IntegerField(blank=True, null=True)
    is_read = models.IntegerField(blank=True, null=True)
    is_seen = models.IntegerField(blank=True, null=True)
    is_locked = models.IntegerField(blank=True, null=True)
    error_code = models.IntegerField(blank=True, null=True)
    is_hidden = models.IntegerField(blank=True, null=True)
    is_spam = models.IntegerField(blank=True, null=True)
    is_request_delivery_report = models.IntegerField(blank=True, null=True)
    is_read_report_requested = models.IntegerField(blank=True, null=True)
    is_mms_auto_download = models.IntegerField(blank=True, null=True)
    mms_transaction_id = models.TextField(blank=True, null=True)
    transaction_id = models.TextField(blank=True, null=True)
    mms_expiry_timestamp = models.IntegerField(blank=True, null=True)
    retry_start_timestamp = models.IntegerField(blank=True, null=True)
    retry_index = models.IntegerField(blank=True, null=True)
    sim_slot = models.IntegerField(blank=True, null=True)
    sim_imsi = models.TextField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    group_type = models.IntegerField(blank=True, null=True)
    delivered_timestamp = models.IntegerField(blank=True, null=True)
    information_message_type = models.IntegerField(blank=True, null=True)
    session_id = models.TextField(blank=True, null=True)
    imdn_message_id = models.TextField(blank=True, null=True)
    remote_db_id = models.IntegerField(blank=True, null=True)
    im_db_id = models.IntegerField(blank=True, null=True)
    reason_code = models.IntegerField(blank=True, null=True)
    preferred_line = models.TextField(blank=True, null=True)
    user_alias = models.TextField(blank=True, null=True)
    displayed_counter = models.IntegerField(blank=True, null=True)
    device_name = models.TextField(blank=True, null=True)
    delivery_report_status = models.IntegerField(blank=True, null=True)
    delivery_report_received_count = models.IntegerField(blank=True, null=True)
    read_report_status = models.IntegerField(blank=True, null=True)
    updated_timestamp = models.IntegerField(blank=True, null=True)
    using_mode = models.IntegerField(blank=True, null=True)
    roam_pending = models.IntegerField(blank=True, null=True)
    svc_cmd = models.IntegerField(blank=True, null=True)
    svc_cmd_content = models.TextField(blank=True, null=True)
    is_safe = models.IntegerField(blank=True, null=True)
    teleservice_id = models.IntegerField(blank=True, null=True)
    link_url = models.TextField(blank=True, null=True)
    is_spam_reported = models.IntegerField(blank=True, null=True)
    is_favorite = models.IntegerField(blank=True, null=True)
    is_secret = models.IntegerField(blank=True, null=True)
    announcements_subtype = models.IntegerField(blank=True, null=True)
    suggestion_id = models.IntegerField(blank=True, null=True)
    display_notification_status = models.IntegerField(blank=True, null=True)
    is_broadcast_msg = models.IntegerField(blank=True, null=True)
    callback_number = models.TextField(blank=True, null=True)
    creator = models.TextField(blank=True, null=True)
    cmas_channel = models.TextField(blank=True, null=True)
    ft_mech = models.IntegerField(blank=True, null=True)
    protocol = models.IntegerField(blank=True, null=True)
    remote_creator = models.TextField(blank=True, null=True)
    req_app_id = models.IntegerField(blank=True, null=True)
    req_msg_id = models.IntegerField(blank=True, null=True)
    from_address = models.TextField(blank=True, null=True)
    mms_message_id = models.TextField(blank=True, null=True)
    mms_content_location = models.TextField(blank=True, null=True)
    mms_read_status = models.IntegerField(blank=True, null=True)
    correlation_tag = models.TextField(blank=True, null=True)
    object_id = models.TextField(blank=True, null=True)
    ft_expiry_timestamp = models.IntegerField(blank=True, null=True)
    cmc_prop = models.TextField(blank=True, null=True)
    is_bot = models.IntegerField(blank=True, null=True)
    view_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'


class MmsAddr(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    message_id = models.IntegerField(blank=True, null=True)
    contact_id = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    charset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mms_addr'


class MyChannels(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    channel_id = models.IntegerField(blank=True, null=True)
    channel_name = models.TextField(blank=True, null=True)
    is_checked = models.IntegerField(blank=True, null=True)
    sim_slot = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_channels'


class Parts(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    conversation_id = models.IntegerField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    content_uri = models.TextField(blank=True, null=True)
    content_type = models.TextField(blank=True, null=True)
    thumbnail_uri = models.TextField(blank=True, null=True)
    file_name = models.TextField(blank=True, null=True)
    sticker_id = models.TextField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    bytes_transferred = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    orientation = models.IntegerField(blank=True, null=True)
    webpreview_title = models.TextField(blank=True, null=True)
    webpreview_image = models.TextField(blank=True, null=True)
    webpreview_description = models.TextField(blank=True, null=True)
    webpreview_url = models.TextField(blank=True, null=True)
    webpreview_status = models.IntegerField(blank=True, null=True)
    antiphishing_urls_risks = models.TextField(blank=True, null=True)
    sef_type = models.IntegerField(blank=True, null=True)
    search_text = models.TextField(blank=True, null=True)
    field_data = models.TextField(db_column='_data', blank=True, null=True)  # Field renamed because it started with '_'.
    view_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parts'


class PluginAction(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    is_on = models.IntegerField(blank=True, null=True)
    package_name = models.TextField()
    type = models.IntegerField(blank=True, null=True)
    title_res_id = models.IntegerField(blank=True, null=True)
    icon_res_id = models.IntegerField(blank=True, null=True)
    run_type = models.IntegerField(blank=True, null=True)
    run_intent_class = models.TextField(blank=True, null=True)
    run_intent_category = models.TextField(blank=True, null=True)
    run_intent_action = models.TextField(blank=True, null=True)
    run_intent_launch_mode = models.IntegerField(blank=True, null=True)
    run_content_uri = models.TextField(blank=True, null=True)
    sales_code = models.TextField(blank=True, null=True)
    content_type = models.IntegerField(blank=True, null=True)
    input_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plugin_action'


class PluginActionMenu(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    action_id = models.IntegerField(blank=True, null=True)
    title_res_id = models.IntegerField(blank=True, null=True)
    icon_res_id = models.IntegerField(blank=True, null=True)
    run_type = models.IntegerField(blank=True, null=True)
    run_intent_class = models.TextField(blank=True, null=True)
    run_intent_category = models.TextField(blank=True, null=True)
    run_intent_action = models.TextField(blank=True, null=True)
    run_intent_launch_mode = models.IntegerField(blank=True, null=True)
    run_content_uri = models.TextField(blank=True, null=True)
    sales_code = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plugin_action_menu'


class PluginStickerPackages(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    plugin_pkg_name = models.TextField()
    pkg_name = models.TextField()
    type = models.TextField(blank=True, null=True)
    cost = models.TextField(blank=True, null=True)
    content_name = models.TextField(blank=True, null=True)
    cp_name = models.TextField(blank=True, null=True)
    title_static = models.BinaryField(blank=True, null=True)
    title_dynamic = models.BinaryField(blank=True, null=True)
    tray_on_image = models.BinaryField(blank=True, null=True)
    tray_off_image = models.BinaryField(blank=True, null=True)
    creator = models.TextField(blank=True, null=True)
    expire_timestamp = models.IntegerField(blank=True, null=True)
    initial_order = models.IntegerField(blank=True, null=True)
    arranged_order = models.IntegerField(blank=True, null=True)
    extra_1 = models.TextField(blank=True, null=True)
    content_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plugin_sticker_packages'


class PluginStickerRecents(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    plugin_pkg_name = models.TextField()
    pkg_name = models.TextField()
    type = models.TextField(blank=True, null=True)
    cost = models.TextField(blank=True, null=True)
    content_name = models.TextField(blank=True, null=True)
    cp_name = models.TextField(blank=True, null=True)
    item_file_name = models.TextField(blank=True, null=True)
    item_preview_image = models.BinaryField(blank=True, null=True)
    content_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plugin_sticker_recents'


class Recipients(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    address = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipients'


class Sessions(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    conversation_id = models.TextField(blank=True, null=True)
    sim_slot = models.IntegerField(blank=True, null=True)
    sim_imsi = models.TextField(blank=True, null=True)
    session_id = models.TextField(blank=True, null=True)
    service_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessions'


class Suggestions(models.Model):
    field_id = models.AutoField(db_column='_id', primary_key=True, blank=True, null=True)  # Field renamed because it started with '_'.
    conversation_id = models.IntegerField()
    text = models.TextField()
    content_type = models.TextField()
    is_read = models.IntegerField()
    created_timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'suggestions'
