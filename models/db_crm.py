# -*- coding: utf-8 -*-

db.define_table(
    "states",
    Field("state_name", notnull=True, requires=IS_IN_SET(["Colorado", "Washington", "Alask", "Oregon", "Washington D.C.", "California", "Maine", "Massachusetts", "Nevada", "Michigan", "Vermont", "Illinois", "Arizona"])),
format="%(state_name)s"
)


db.define_table(
    "companies",
    Field("company_id", notnull=True),
    Field("company_name", notnull=True),
    Field("address", notnull=True),
    Field("state", "reference states", notnull=True),
    Field("industry", notnull=True),
    Field("website", requires=IS_URL()),
    Field("linkedin"),
    Field("phone_number"),
    format="%(company_name)s"
)

db.define_table(
    "persons",
    Field("person_id", notnull=True),
    Field("company_id", "reference companies", notnull=True),
    Field("first_name", notnull=True),
    Field("last_name", notnull=True),
    Field("title"),
    Field("work_phone", requires=IS_MATCH("[\d\-\(\) ]+")),
    Field("cell_phone", requires=IS_MATCH("[\d\-\(\) ]+")),
    Field("email", requires=IS_EMAIL()),
    Field("birthday", requires=IS_DATE(format=T("%Y-%m-%d"))),
    Field("company_type", requires=IS_IN_SET(["Customer", "Vendor"])),
    Field("comm_type", requires=IS_IN_SET(["Web", "Phone", "Email", "In person"])),
    Field("comments", "text"),
    Field("created_by", "reference auth_user", default=auth.user_id),
    Field("created_on", "datetime", default=request.now),
    format="%(person_name)s"
)

db.define_table(
    "events",
    Field("user_id", "reference auth_user"),
    Field("person_name", "reference persons"),
    Field("comm_type", requires=IS_IN_SET(["Phone", "Email", "In person"])),
    Field("event_date", requires=IS_DATETIME()),
    Field("event_time", requires=IS_TIME()),
    Field("status", requires=IS_IN_SET(["Open", "Closed", "Canceled"])),
    Field("event_type", requires=IS_IN_SET(["Meeting", "Call", "Email", "Lunch", "Dinner", "Breakfast", "Other"])),
    Field("comments", "text"),
    format="%(person_name)s"
)
