NEAR_BY_PAYLOAD = "NEAR_BY_PAYLOAD"
RECOMMEND_ME_PAYLOAD = "RECOMMEND_ME_PAYLOAD"
LOCATION_NEGATIVE_PAYLOAD = "LOCATION_NEGATIVE_PAYLOAD"
QUESTIONS_PAYLOAD = "QUESTIONS_PAYLOAD"
CHECK_PP_PAYLOAD = "CHECK_PP_PAYLOAD"
ABOUT_PAYLOAD = "ABOUT_PAYLOAD"

ABOUT_PAGE_PAYLOAD = "ABOUT_PAGE_PAYLOAD"
PRIVACY_POLICY_PAYLOAD = "PRIVACY_POLICY_PAYLOAD"
DISCLAIMER_PAYLOAD = "DISCLAIMER_PAYLOAD"

CHECK_AGAIN_POSITIVE_PAYLOAD = "CHECK_AGAIN_POSITIVE_PAYLOAD"
CHECK_AGAIN_NEGATIVE_PAYLOAD = "CHECK_AGAIN_NEGATIVE_PAYLOAD"

# Quick Reply Templates
INITIAL_QUICK_REPLY = [
    {
        "content_type": "text",
        "title": "မေးခွန်းမေးမည်",
        "payload": QUESTIONS_PAYLOAD
    }, {
        "content_type": "text",
        "title": "စစ်မယ်",
        "payload": CHECK_PP_PAYLOAD
    },
    {
        "content_type": "text",
        "title": "အကြောင်း",
        "payload": ABOUT_PAYLOAD
    }

]

ABOUT_QUICK_REPLY = [
    {
        "content_type": "text",
        "title": "ကျွနု်ပ်တို့အကြောင်း",
        "payload": ABOUT_PAGE_PAYLOAD
    }, {
        "content_type": "text",
        "title": "ကိုယ်ရေးလုံခြုံမှု",
        "payload": PRIVACY_POLICY_PAYLOAD
    },
    {
        "content_type": "text",
        "title": "ကြေငြာချက်",
        "payload": DISCLAIMER_PAYLOAD
    }

]

RESTART_QUICK_REPLY = [
    {
        "content_type": "text",
        "title": "ပြန်စမယ်",
        "payload": CHECK_AGAIN_POSITIVE_PAYLOAD
    }, {
        "content_type": "text",
        "title": "စစ်တော့ဘူး",
        "payload": CHECK_AGAIN_NEGATIVE_PAYLOAD
    },
]

CHECK_AGAIN_QUICK_REPLY = [
    {
        "content_type": "text",
        "title": "ထပ်စစ်မည်",
        "payload": CHECK_AGAIN_POSITIVE_PAYLOAD
    }, {
        "content_type": "text",
        "title": "စစ်တော့ဘူး",
        "payload": CHECK_AGAIN_NEGATIVE_PAYLOAD
    },
]
