import json
from datetime import datetime, timezone
from collections import Counter


def load_ytd(path):
    with open(path, "r", encoding="utf-8-sig") as f:
        text = f.read().strip()

    starts = [i for i in (text.find("["), text.find("{")) if i != -1]
    if not starts:
        return []
    text = text[min(starts):]

    if text.endswith(";"):
        text = text[:-1].rstrip()

    return json.loads(text)


def parse_created_at(s):
    # X format: "Tue Oct 06 12:34:56 +0000 2020"
    try:
        return datetime.strptime(s, "%a %b %d %H:%M:%S %z %Y").astimezone(timezone.utc)
    except ValueError:
        # fallback if the cleaned data uses ISO format
        return datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(timezone.utc)


def snow_ms(tweet_id):
    return (int(tweet_id) >> 22) + 1288834974657


def snow_dt(tweet_id):
    return datetime.fromtimestamp(snow_ms(tweet_id) / 1000, tz=timezone.utc)


# ---------- Question 1 ----------
tweets = load_ytd("PATH/TO/tweets.js")              # change the path
rows = [t["tweet"] if "tweet" in t else t for t in tweets]
print(rows[0].keys())                               # check the field names

oct20 = []
for r in rows:
    dt = parse_created_at(r["created_at"])
    if dt.year == 2020 and dt.month == 10:
        oct20.append((dt, r))

print("a)", len(oct20))

text_key = "full_text" if "full_text" in rows[0] else "text"
print("b)", sum(1 for dt, r in oct20 if r[text_key].startswith("RT @")))

day_counts = Counter(dt.day for dt, r in oct20)
print("c)", day_counts.most_common(5))              # top one is the answer; check for ties


# ---------- Question 2 ----------
liked = snow_dt("1269920197139406848")
print("a)", liked.date())                           # already YYYY-MM-DD
print("b)", liked.hour)

likes = load_ytd("PATH/TO/like.js")                 # change the path
likes = [l["like"] if "like" in l else l for l in likes]
print(likes[0].keys())                              # check the ID field name

id_key = "tweetId" if "tweetId" in likes[0] else "tweet_id"
count = 0
for l in likes:
    d = snow_dt(l[id_key])
    if d.year == liked.year and d.month == liked.month:
        count += 1
print("c)", count)