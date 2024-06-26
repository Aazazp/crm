# -*- coding: utf-8 -*-

db.define_table(
    "states",
    Field("statename", notnull=True, requires=IS_IN_SET(sorted(["Colorado", "Washington", "Alask", "Oregon", "Washington D.C.", "California", "Maine", "Massachusetts", "Nevada", "Michigan", "Vermont", "Illinois", "Arizona", "Montana", "New Jersey", "New York", "Virginia", "New Mexico", "Connecticut", "Rhode Island", "Maryland", "Missouri", "Delaware", "Minnesota", "Ohio"]))),
format="%(statename)s"
)


db.define_table(
    "companies",
    Field("company_id", notnull=True),
    Field("company_name", notnull=True),
    Field("address", notnull=True),
    Field("statename", "reference states", notnull=True),
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
    format="%(first_name)s %(last_name)s"
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

db.define_table(
    "products",
    Field("product_name", notnull=True),
    Field("category", requires=IS_IN_SET(["Flower", "Edible", "Concentrate", "Pre-roll", "Topical", "Accessory"])),
    Field("description", "text"),
    Field("thc_content", "double", requires=IS_FLOAT_IN_RANGE(0, 100)),  # THC content in percentage
    Field("cbd_content", "double", requires=IS_FLOAT_IN_RANGE(0, 100)),  # CBD content in percentage
    Field("price", "double", requires=IS_FLOAT_IN_RANGE(0)),  # Price per unit
    Field("stock_quantity", "integer", default=0),  # Current stock quantity
    Field("supplier", notnull=True),  # Supplier of the product
    Field("created_by", "reference auth_user", default=auth.user_id),
    Field("created_on", "datetime", default=request.now),
    format="%(product_name)s"
)
