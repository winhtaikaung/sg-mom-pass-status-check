NEAR_BY_PAYLOAD = "NEAR_BY_PAYLOAD"
RECOMMEND_ME_PAYLOAD = "RECOMMEND_ME_PAYLOAD"
LOCATION_NEGATIVE_PAYLOAD = "LOCATION_NEGATIVE_PAYLOAD"
QUESTIONS_PAYLOAD = "QUESTIONS_PAYLOAD"
CHECK_PP_PAYLOAD = "CHECK_PP_PAYLOAD"
ABOUT_MORE_PAYLOAD = "ABOUT_MORE_PAYLOAD"

ABOUT_PAGE_PAYLOAD = "ABOUT_PAGE_PAYLOAD"
PRIVACY_POLICY_PAYLOAD = "PRIVACY_POLICY_PAYLOAD"
LICENSE_PAYLOAD = "LICENSE_PAYLOAD"

CHECK_AGAIN_POSITIVE_PAYLOAD = "CHECK_AGAIN_POSITIVE_PAYLOAD"
CHECK_AGAIN_NEGATIVE_PAYLOAD = "CHECK_AGAIN_NEGATIVE_PAYLOAD"

# Quick Reply Templates
INITIAL_QUICK_REPLY = [
    {
        "content_type": "text",
        "title": "စစ်မယ်",
        "image_url": "https://image.flaticon.com/icons/png/128/148/148767.png",
        "payload": CHECK_PP_PAYLOAD
    },
    {
        "content_type": "text",
        "title": "ပိုမိုသိရှိရန်",
        "image_url": "https://image.flaticon.com/icons/png/128/189/189665.png",
        "payload": ABOUT_MORE_PAYLOAD
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
        "title": "Licenses",
        "payload": LICENSE_PAYLOAD
    }

]

RESTART_QUICK_REPLY = [
    {
        "content_type": "text",
        "title": "ပြန်စမယ်",
        "image_url":"https://image.flaticon.com/icons/png/128/426/426867.png",
        "payload": CHECK_AGAIN_POSITIVE_PAYLOAD
    }, {
        "content_type": "text",
        "title": "စစ်တော့ဘူး",
        "image_url":"https://image.flaticon.com/icons/png/128/334/334047.png",
        "payload": CHECK_AGAIN_NEGATIVE_PAYLOAD
    },
]

CHECK_AGAIN_QUICK_REPLY = [
    {
        "content_type": "text",
        "title": "ထပ်စစ်မည်",
        "image_url": "https://image.flaticon.com/icons/png/128/426/426867.png",
        "payload": CHECK_AGAIN_POSITIVE_PAYLOAD
    }, {
        "content_type": "text",
        "title": "စစ်တော့ဘူး",
        "image_url": "https://image.flaticon.com/icons/png/128/334/334047.png",
        "payload": CHECK_AGAIN_NEGATIVE_PAYLOAD
    },
]
