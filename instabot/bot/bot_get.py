"""
    All methods must return media_ids that can be
    passed into e.g. like() or comment() functions.
"""

from tqdm import tqdm

# STORY


def get_user_stories(self, user_id):
    self.api.get_user_stories(user_id)
    try:
        if int(self.api.last_json["reel"]["media_count"]) > 0:
            list_image = []
            list_video = []
            for item in self.api.last_json["reel"]["items"]:
                if int(item["media_type"]) == 1:  # photo
                    img = item["image_versions2"]["candidates"][0]["url"]
                    list_image.append(img)
                elif int(item["media_type"]) == 2:  # video
                    video = item["video_versions"][0]["url"]
                    list_video.append(video)
            return list_image, list_video
        else:
            return [], []
    except Exception as e:
        self.logger.error(str(e))
        return [], []


def get_self_story_viewers(self, story_id):
    self.api.get_self_story_viewers(story_id)
    return self.api.last_json


def get_user_reel(self, user_id):
    self.api.get_user_reel(user_id)
    return self.api.last_json

def get_media_owner(self, media_id):
    self.api.media_info(media_id)
    try:
        return str(self.api.last_json.get("items")[0]["user"]["pk"])
    except Exception as ex:
        self.logger.error("Error: get_media_owner(%s)\n%s", media_id, ex)
        return False


def get_user_tags_medias(self, user_id):
    self.api.get_user_tags(user_id)
    return [str(media["pk"]) for media in self.api.last_json["items"]]


def get_popular_medias(self):
    self.api.get_popular_feed()
    return [str(media["id"]) for media in self.api.last_json["items"]]


def get_your_medias(self, as_dict=False):
    self.api.get_self_user_feed()
    if as_dict:
        return self.api.last_json.get("items")
    return self.filter_medias(self.api.last_json.get("items"), False)


def get_archived_medias(self, as_dict=False):
    self.api.get_archive_feed()
    if as_dict:
        return self.api.last_json.get("items")
    return self.filter_medias(self.api.last_json.get("items"), False)


def get_timeline_medias(self, filtration=True):
    if not self.api.get_timeline_feed():
        self.logger.warning("Error while getting timeline feed.")
        return []

    feed_items = [
        item["media_or_ad"]
        for item in self.api.last_json["feed_items"]
        if item.get("media_or_ad")
    ]
    return self.filter_medias(feed_items, filtration)


def get_user_medias(self, user_id, filtration=True, is_comment=False):
    user_id = self.convert_to_user_id(user_id)
    self.api.get_user_feed(user_id)
    if self.api.last_json["status"] == "fail":
        self.logger.warning("This is a closed account.")
        return []
    return self.filter_medias(
        self.api.last_json.get("items"), filtration, is_comment=is_comment
    )


def get_total_user_medias(self, user_id):
    user_id = self.convert_to_user_id(user_id)
    medias = self.api.get_total_user_feed(user_id)
    if self.api.last_json["status"] == "fail":
        self.logger.warning("This is a closed account.")
        return []
    return self.filter_medias(medias, filtration=False)


def get_last_user_medias(self, user_id, amount):
    user_id = self.convert_to_user_id(user_id)
    medias = self.api.get_last_user_feed(user_id, amount)
    if self.api.last_json["status"] == "fail":
        self.logger.warning("This is a closed account.")
        return []
    return self.filter_medias(medias, filtration=False)


def get_user_likers(self, user_id, media_count=10):
    your_likers = set()
    media_items = self.get_user_medias(user_id, filtration=False)
    if not media_items:
        self.logger.warning("Can't get %s medias." % user_id)
        return []
    for media_id in tqdm(
        media_items[:media_count], desc="Getting %s media likers" % user_id
    ):
        media_likers = self.get_media_likers(media_id)
        your_likers |= set(media_likers)
    return list(your_likers)
	
def get_users_commented(self, user_id, media_count=10):
    your_users = set()
    media_items = self.get_user_medias(user_id, filtration=False)
    if not media_items:
        self.logger.warning("Can't get %s medias." % user_id)
        return []
    for media_id in tqdm(media_items[:media_count],
                         desc="Getting %s media likers" % user_id):
        media_user_commented = self.get_media_commenters(media_id)
        your_users |= set(media_user_commented)
    return list(your_users)


def get_hashtag_medias(self, hashtag, filtration=True):
    if not self.api.get_hashtag_feed(hashtag):
        self.logger.warning("Error while getting hashtag feed.")
        return []
    return self.filter_medias(self.api.last_json.get("items"), filtration)


def get_total_hashtag_medias(self, hashtag, amount=100, filtration=False):
    medias = self.api.get_total_hashtag_feed(hashtag, amount)

    return self.filter_medias(medias, filtration=filtration)


def get_geotag_medias(self, geotag, filtration=True):
    # TODO: returns list of medias from geotag
    pass


def get_locations_from_coordinates(self, latitude, longitude):
    self.api.search_location(lat=latitude, lng=longitude)
    all_locations = self.api.last_json.get("items")
    filtered_locations = []

    for location in all_locations:
        location_lat = location["location"]["lat"]
        location_lng = location["location"]["lng"]

        if int(location_lat) == int(latitude) and int(location_lng) == int(longitude):
            filtered_locations.append(location)

    return filtered_locations


def get_media_info(self, media_id):
    if isinstance(media_id, dict):
        return media_id
    self.api.media_info(media_id)
    if "items" not in self.api.last_json:
        self.logger.info("Media with %s not found." % media_id)
        return []
    return self.api.last_json.get("items")


def get_timeline_users(self):
    if not self.api.get_timeline_feed():
        self.logger.warning("Error while getting timeline feed.")
        return []
    if "items" in self.api.last_json:
        return [
            str(i["user"]["pk"]) for i in self.api.last_json["items"] if i.get("user")
        ]
    elif "feed_items" in self.api.last_json:
        return [
            str(i["media_or_ad"]["user"]["pk"])
            for i in self.api.last_json["feed_items"]
            if i.get("media_or_ad", {}).get("user")
        ]
    self.logger.info("Users for timeline not found.")
    return []


def get_hashtag_users(self, hashtag):
    if not self.api.get_hashtag_feed(hashtag):
        self.logger.warning("Error while getting hashtag feed.")
        return []
    return [str(i["user"]["pk"]) for i in self.api.last_json["items"]]


def get_geotag_users(self, geotag):
    # TODO: returns list user_ids who just posted on this geotag
    pass


def get_user_id_from_username(self, username):
    if username not in self._usernames:
        self.api.search_username(username)
        self.very_small_delay()
        if "user" in self.api.last_json:
            self._usernames[username] = str(self.api.last_json["user"]["pk"])
        else:
            return None
    return self._usernames[username]


def get_username_from_user_id(self, user_id):
    user_info = self.get_user_info(user_id)
    if user_info and "username" in user_info:
        return str(user_info["username"])
    return None  # Not found


def get_user_info(self, user_id, use_cache=True):
    user_id = self.convert_to_user_id(user_id)
    if not use_cache or user_id not in self._user_infos:
        self.api.get_username_info(user_id)
        last_json = self.api.last_json
        if last_json is None or "user" not in last_json:
            return False
        user_info = last_json["user"]
        self._user_infos[user_id] = user_info
    return self._user_infos[user_id]


def get_user_followers(self, user_id, nfollows):
    user_id = self.convert_to_user_id(user_id)
    followers = self.api.get_total_followers(user_id, nfollows)
    return [str(item["pk"]) for item in followers][::-1] if followers else []


def get_user_following(self, user_id, nfollows=None):
    user_id = self.convert_to_user_id(user_id)
    following = self.api.get_total_followings(user_id, nfollows)
    return [str(item["pk"]) for item in following][::-1] if following else []


def get_comment_likers(self, comment_id):
    self.api.get_comment_likers(comment_id)
    if "users" not in self.api.last_json:
        self.logger.info("Comment with %s not found." % comment_id)
        return []
    return list(map(lambda user: str(user["pk"]), self.api.last_json["users"]))


def get_media_likers(self, media_id):
    self.api.get_media_likers(media_id)
    if "users" not in self.api.last_json:
        self.logger.info("Media with %s not found." % media_id)
        return []
    return list(map(lambda user: str(user["pk"]), self.api.last_json["users"]))


def get_media_comments(self, media_id, only_text=False):
    self.api.get_media_comments(media_id)
    if "comments" not in self.api.last_json:
        return []
    if only_text:
        return [str(item["text"]) for item in self.api.last_json["comments"]]
    return self.api.last_json["comments"]


def get_media_comments_all(self, media_id, only_text=False, count=False):
    has_more_comments = True
    max_id = ""
    comments = []

    while has_more_comments:
        self.api.get_media_comments(media_id, max_id=max_id)
        for comment in self.api.last_json["comments"]:
            comments.append(comment)
        has_more_comments = self.api.last_json["has_more_comments"]
        if count and len(comments) >= count:
            comments = comments[:count]
            has_more_comments = False
            self.logger.info("Getting comments stopped by count (%s)." % count)
        if has_more_comments:
            max_id = self.api.last_json["next_max_id"]

    if only_text:
        return [
            str(item["text"])
            for item in sorted(
                comments, key=lambda k: k["created_at_utc"], reverse=False
            )
        ]
    return sorted(comments, key=lambda k: k["created_at_utc"], reverse=False)


def get_media_commenters(self, media_id):
    self.get_media_comments(media_id)
    if "comments" not in self.api.last_json:
        return []
    return [str(item["user"]["pk"]) for item in self.api.last_json["comments"]]


def search_users(self, query):
    self.api.search_users(query)
    if "users" not in self.api.last_json:
        self.logger.info("Users with %s not found." % query)
        return []
    return [str(user["pk"]) for user in self.api.last_json["users"]]


def get_comment(self):
    try:
        return self.comments_file.random().strip()
    except IndexError:
        return "Wow!"
def get_comment1(self):
    try:
        return self.comments_file1.random().strip()
    except IndexError:
        return "Wow!"
def get_comment2(self):
    try:
        return self.comments_file2.random().strip()
    except IndexError:
        return "Wow!"
def get_comment3(self):
    try:
        return self.comments_file3.random().strip()
    except IndexError:
        return "Wow!"
def get_comment4(self):
    try:
        return self.comments_file4.random().strip()
    except IndexError:
        return "Wow!"
def get_comment5(self):
    try:
        return self.comments_file5.random().strip()
    except IndexError:
        return "Wow!"
def get_comment6(self):
    try:
        return self.comments_file6.random().strip()
    except IndexError:
        return "Wow!"
def get_comment7(self):
    try:
        return self.comments_file7.random().strip()
    except IndexError:
        return "Wow!"
def get_comment8(self):
    try:
        return self.comments_file8.random().strip()
    except IndexError:
        return "Wow!"
def get_comment9(self):
    try:
        return self.comments_file9.random().strip()
    except IndexError:
        return "Wow!"
def get_comment10(self):
    try:
        return self.comments_file10.random().strip()
    except IndexError:
        return "Wow!"
def get_comment11(self):
    try:
        return self.comments_file11.random().strip()
    except IndexError:
        return "Wow!"
def get_comment12(self):
    try:
        return self.comments_file12.random().strip()
    except IndexError:
        return "Wow!"
def get_comment13(self):
    try:
        return self.comments_file13.random().strip()
    except IndexError:
        return "Wow!"
def get_comment14(self):
    try:
        return self.comments_file14.random().strip()
    except IndexError:
        return "Wow!"
def get_comment15(self):
    try:
        return self.comments_file15.random().strip()
    except IndexError:
        return "Wow!"
def get_comment16(self):
    try:
        return self.comments_file16.random().strip()
    except IndexError:
        return "Wow!"
def get_comment17(self):
    try:
        return self.comments_file17.random().strip()
    except IndexError:
        return "Wow!"
def get_comment18(self):
    try:
        return self.comments_file18.random().strip()
    except IndexError:
        return "Wow!"
def get_comment19(self):
    try:
        return self.comments_file19.random().strip()
    except IndexError:
        return "Wow!"
def get_comment20(self):
    try:
        return self.comments_file20.random().strip()
    except IndexError:
        return "Wow!"
def get_comment21(self):
    try:
        return self.comments_file21.random().strip()
    except IndexError:
        return "Wow!"
def get_comment22(self):
    try:
        return self.comments_file22.random().strip()
    except IndexError:
        return "Wow!"
def get_comment23(self):
    try:
        return self.comments_file23.random().strip()
    except IndexError:
        return "Wow!"
def get_comment24(self):
    try:
        return self.comments_file24.random().strip()
    except IndexError:
        return "Wow!"
def get_comment25(self):
    try:
        return self.comments_file25.random().strip()
    except IndexError:
        return "Wow!"
def get_comment26(self):
    try:
        return self.comments_file26.random().strip()
    except IndexError:
        return "Wow!"
def get_comment27(self):
    try:
        return self.comments_file27.random().strip()
    except IndexError:
        return "Wow!"
def get_comment28(self):
    try:
        return self.comments_file28.random().strip()
    except IndexError:
        return "Wow!"
def get_comment29(self):
    try:
        return self.comments_file29.random().strip()
    except IndexError:
        return "Wow!"
def get_comment30(self):
    try:
        return self.comments_file30.random().strip()
    except IndexError:
        return "Wow!"
def get_comment31(self):
    try:
        return self.comments_file31.random().strip()
    except IndexError:
        return "Wow!"
def get_comment32(self):
    try:
        return self.comments_file32.random().strip()
    except IndexError:
        return "Wow!"
def get_comment33(self):
    try:
        return self.comments_file33.random().strip()
    except IndexError:
        return "Wow!"
def get_comment34(self):
    try:
        return self.comments_file34.random().strip()
    except IndexError:
        return "Wow!"
def get_comment35(self):
    try:
        return self.comments_file35.random().strip()
    except IndexError:
        return "Wow!"
def get_comment36(self):
    try:
        return self.comments_file36.random().strip()
    except IndexError:
        return "Wow!"
def get_comment37(self):
    try:
        return self.comments_file37.random().strip()
    except IndexError:
        return "Wow!"
def get_comment38(self):
    try:
        return self.comments_file38.random().strip()
    except IndexError:
        return "Wow!"
def get_comment39(self):
    try:
        return self.comments_file39.random().strip()
    except IndexError:
        return "Wow!"
def get_comment40(self):
    try:
        return self.comments_file40.random().strip()
    except IndexError:
        return "Wow!"
def get_comment41(self):
    try:
        return self.comments_file41.random().strip()
    except IndexError:
        return "Wow!"
def get_comment42(self):
    try:
        return self.comments_file42.random().strip()
    except IndexError:
        return "Wow!"
def get_comment43(self):
    try:
        return self.comments_file43.random().strip()
    except IndexError:
        return "Wow!"
def get_comment44(self):
    try:
        return self.comments_file44.random().strip()
    except IndexError:
        return "Wow!"
def get_comment45(self):
    try:
        return self.comments_file45.random().strip()
    except IndexError:
        return "Wow!"
def get_comment46(self):
    try:
        return self.comments_file46.random().strip()
    except IndexError:
        return "Wow!"
def get_comment47(self):
    try:
        return self.comments_file47.random().strip()
    except IndexError:
        return "Wow!"
def get_comment48(self):
    try:
        return self.comments_file48.random().strip()
    except IndexError:
        return "Wow!"
def get_comment49(self):
    try:
        return self.comments_file49.random().strip()
    except IndexError:
        return "Wow!"
def get_comment50(self):
    try:
        return self.comments_file50.random().strip()
    except IndexError:
        return "Wow!"
def get_comment51(self):
    try:
        return self.comments_file51.random().strip()
    except IndexError:
        return "Wow!"
def get_comment52(self):
    try:
        return self.comments_file52.random().strip()
    except IndexError:
        return "Wow!"
def get_comment53(self):
    try:
        return self.comments_file53.random().strip()
    except IndexError:
        return "Wow!"
def get_comment54(self):
    try:
        return self.comments_file54.random().strip()
    except IndexError:
        return "Wow!"
def get_comment55(self):
    try:
        return self.comments_file55.random().strip()
    except IndexError:
        return "Wow!"
def get_comment56(self):
    try:
        return self.comments_file56.random().strip()
    except IndexError:
        return "Wow!"
def get_comment57(self):
    try:
        return self.comments_file57.random().strip()
    except IndexError:
        return "Wow!"
def get_comment58(self):
    try:
        return self.comments_file58.random().strip()
    except IndexError:
        return "Wow!"
def get_comment59(self):
    try:
        return self.comments_file59.random().strip()
    except IndexError:
        return "Wow!"
def get_comment60(self):
    try:
        return self.comments_file60.random().strip()
    except IndexError:
        return "Wow!"
def get_comment61(self):
    try:
        return self.comments_file61.random().strip()
    except IndexError:
        return "Wow!"
def get_comment62(self):
    try:
        return self.comments_file62.random().strip()
    except IndexError:
        return "Wow!"
def get_comment63(self):
    try:
        return self.comments_file63.random().strip()
    except IndexError:
        return "Wow!"
def get_comment64(self):
    try:
        return self.comments_file64.random().strip()
    except IndexError:
        return "Wow!"
def get_comment65(self):
    try:
        return self.comments_file65.random().strip()
    except IndexError:
        return "Wow!"
def get_comment66(self):
    try:
        return self.comments_file66.random().strip()
    except IndexError:
        return "Wow!"
def get_comment67(self):
    try:
        return self.comments_file67.random().strip()
    except IndexError:
        return "Wow!"
def get_comment68(self):
    try:
        return self.comments_file68.random().strip()
    except IndexError:
        return "Wow!"
def get_comment69(self):
    try:
        return self.comments_file69.random().strip()
    except IndexError:
        return "Wow!"
def get_comment70(self):
    try:
        return self.comments_file70.random().strip()
    except IndexError:
        return "Wow!"
def get_comment71(self):
    try:
        return self.comments_file71.random().strip()
    except IndexError:
        return "Wow!"
def get_comment72(self):
    try:
        return self.comments_file72.random().strip()
    except IndexError:
        return "Wow!"
def get_comment73(self):
    try:
        return self.comments_file73.random().strip()
    except IndexError:
        return "Wow!"
def get_comment74(self):
    try:
        return self.comments_file74.random().strip()
    except IndexError:
        return "Wow!"
def get_comment75(self):
    try:
        return self.comments_file75.random().strip()
    except IndexError:
        return "Wow!"
def get_comment76(self):
    try:
        return self.comments_file76.random().strip()
    except IndexError:
        return "Wow!"
def get_comment77(self):
    try:
        return self.comments_file77.random().strip()
    except IndexError:
        return "Wow!"
def get_comment78(self):
    try:
        return self.comments_file78.random().strip()
    except IndexError:
        return "Wow!"
def get_comment79(self):
    try:
        return self.comments_file79.random().strip()
    except IndexError:
        return "Wow!"
def get_comment80(self):
    try:
        return self.comments_file80.random().strip()
    except IndexError:
        return "Wow!"
def get_comment81(self):
    try:
        return self.comments_file81.random().strip()
    except IndexError:
        return "Wow!"
def get_comment82(self):
    try:
        return self.comments_file82.random().strip()
    except IndexError:
        return "Wow!"
def get_comment83(self):
    try:
        return self.comments_file83.random().strip()
    except IndexError:
        return "Wow!"
def get_comment84(self):
    try:
        return self.comments_file84.random().strip()
    except IndexError:
        return "Wow!"
def get_comment85(self):
    try:
        return self.comments_file85.random().strip()
    except IndexError:
        return "Wow!"
def get_comment86(self):
    try:
        return self.comments_file86.random().strip()
    except IndexError:
        return "Wow!"
def get_comment87(self):
    try:
        return self.comments_file87.random().strip()
    except IndexError:
        return "Wow!"
def get_comment88(self):
    try:
        return self.comments_file88.random().strip()
    except IndexError:
        return "Wow!"
def get_comment89(self):
    try:
        return self.comments_file89.random().strip()
    except IndexError:
        return "Wow!"
def get_comment90(self):
    try:
        return self.comments_file90.random().strip()
    except IndexError:
        return "Wow!"
def get_comment91(self):
    try:
        return self.comments_file91.random().strip()
    except IndexError:
        return "Wow!"
def get_comment92(self):
    try:
        return self.comments_file92.random().strip()
    except IndexError:
        return "Wow!"
def get_comment93(self):
    try:
        return self.comments_file93.random().strip()
    except IndexError:
        return "Wow!"
def get_comment94(self):
    try:
        return self.comments_file94.random().strip()
    except IndexError:
        return "Wow!"
def get_comment95(self):
    try:
        return self.comments_file95.random().strip()
    except IndexError:
        return "Wow!"
def get_comment96(self):
    try:
        return self.comments_file96.random().strip()
    except IndexError:
        return "Wow!"
def get_comment97(self):
    try:
        return self.comments_file97.random().strip()
    except IndexError:
        return "Wow!"
def get_comment98(self):
    try:
        return self.comments_file98.random().strip()
    except IndexError:
        return "Wow!"
def get_comment99(self):
    try:
        return self.comments_file99.random().strip()
    except IndexError:
        return "Wow!"
def get_comment100(self):
    try:
        return self.comments_file100.random().strip()
    except IndexError:
        return "Wow!"
def get_comment101(self):
    try:
        return self.comments_file101.random().strip()
    except IndexError:
        return "Wow!"
def get_comment102(self):
    try:
        return self.comments_file102.random().strip()
    except IndexError:
        return "Wow!"
def get_comment103(self):
    try:
        return self.comments_file103.random().strip()
    except IndexError:
        return "Wow!"


def get_media_id_from_link(self, link):
    if "instagram.com/p/" not in link:
        self.logger.error("Unexpected link")
        return False
    link = link.split("/")
    code = link[link.index("p") + 1]

    alphabet = {
        "-": 62,
        "1": 53,
        "0": 52,
        "3": 55,
        "2": 54,
        "5": 57,
        "4": 56,
        "7": 59,
        "6": 58,
        "9": 61,
        "8": 60,
        "A": 0,
        "C": 2,
        "B": 1,
        "E": 4,
        "D": 3,
        "G": 6,
        "F": 5,
        "I": 8,
        "H": 7,
        "K": 10,
        "J": 9,
        "M": 12,
        "L": 11,
        "O": 14,
        "N": 13,
        "Q": 16,
        "P": 15,
        "S": 18,
        "R": 17,
        "U": 20,
        "T": 19,
        "W": 22,
        "V": 21,
        "Y": 24,
        "X": 23,
        "Z": 25,
        "_": 63,
        "a": 26,
        "c": 28,
        "b": 27,
        "e": 30,
        "d": 29,
        "g": 32,
        "f": 31,
        "i": 34,
        "h": 33,
        "k": 36,
        "j": 35,
        "m": 38,
        "l": 37,
        "o": 40,
        "n": 39,
        "q": 42,
        "p": 41,
        "s": 44,
        "r": 43,
        "u": 46,
        "t": 45,
        "w": 48,
        "v": 47,
        "y": 50,
        "x": 49,
        "z": 51,
    }

    result = 0
    for char in code:
        result = result * 64 + alphabet[char]
    return result


def get_link_from_media_id(self, media_id):
    alphabet = {
        "-": 62,
        "1": 53,
        "0": 52,
        "3": 55,
        "2": 54,
        "5": 57,
        "4": 56,
        "7": 59,
        "6": 58,
        "9": 61,
        "8": 60,
        "A": 0,
        "C": 2,
        "B": 1,
        "E": 4,
        "D": 3,
        "G": 6,
        "F": 5,
        "I": 8,
        "H": 7,
        "K": 10,
        "J": 9,
        "M": 12,
        "L": 11,
        "O": 14,
        "N": 13,
        "Q": 16,
        "P": 15,
        "S": 18,
        "R": 17,
        "U": 20,
        "T": 19,
        "W": 22,
        "V": 21,
        "Y": 24,
        "X": 23,
        "Z": 25,
        "_": 63,
        "a": 26,
        "c": 28,
        "b": 27,
        "e": 30,
        "d": 29,
        "g": 32,
        "f": 31,
        "i": 34,
        "h": 33,
        "k": 36,
        "j": 35,
        "m": 38,
        "l": 37,
        "o": 40,
        "n": 39,
        "q": 42,
        "p": 41,
        "s": 44,
        "r": 43,
        "u": 46,
        "t": 45,
        "w": 48,
        "v": 47,
        "y": 50,
        "x": 49,
        "z": 51,
    }
    result = ""
    while media_id:
        media_id, char = media_id // 64, media_id % 64
        result += list(alphabet.keys())[list(alphabet.values()).index(char)]
    return "https://instagram.com/p/" + result[::-1] + "/"


def get_messages(self):
    if self.api.get_inbox_v2():
        return self.api.last_json
    else:
        self.logger.info("Messages were not found, something went wrong.")
        return None


def convert_to_user_id(self, x):
    x = str(x)
    if not x.isdigit():
        x = x.lstrip("@")
        x = self.get_user_id_from_username(x)
    # if type is not str than it is int so user_id passed
    return x


def get_pending_follow_requests(self):
    self.api.get_pending_friendships()
    if self.api.last_json.get("users"):
        return self.api.last_json.get("users")
    else:
        self.logger.info("There isn't any pending request.")
        return []


def get_pending_thread_requests(self):
    self.api.get_pending_inbox()
    threads = self.api.last_json["inbox"]["threads"]
    if not threads:
        self.logger.info("There isn't any pending thread request.")
    return threads