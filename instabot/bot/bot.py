import os
import atexit
import datetime
import random
import signal
import time
import requests
import json

from .. import utils
from ..api import API
from .bot_archive import archive, archive_medias, unarchive_medias
from .bot_block import block, block_bots, block_users, unblock, unblock_users
from .bot_checkpoint import load_checkpoint, save_checkpoint
from .bot_comment import (comment, comment_geotag, comment_hashtag, comment_hashtag1,comment_hashtag2,comment_hashtag3,comment_hashtag4,comment_hashtag5,comment_hashtag6,comment_hashtag7,comment_hashtag8,comment_hashtag9,comment_hashtag10,comment_hashtag11,comment_hashtag12,comment_hashtag13,comment_hashtag14,comment_hashtag15,comment_hashtag16,comment_hashtag17,comment_hashtag18,comment_hashtag19,comment_hashtag20,comment_hashtag21,comment_hashtag22,comment_hashtag23,comment_hashtag24,comment_hashtag25,comment_hashtag26,comment_hashtag27,comment_hashtag28,comment_hashtag29,comment_hashtag30,comment_hashtag31,comment_hashtag32,comment_hashtag33,comment_hashtag34,comment_hashtag35,comment_hashtag36,comment_hashtag37,comment_hashtag38,comment_hashtag39,comment_hashtag40,comment_hashtag41,comment_hashtag42,comment_hashtag43,comment_hashtag44,comment_hashtag45,comment_hashtag46,comment_hashtag47,comment_hashtag48,comment_hashtag49,comment_hashtag50,comment_hashtag51,comment_hashtag52,comment_hashtag53,comment_hashtag54,comment_hashtag55,comment_hashtag56,comment_hashtag57,comment_hashtag58,comment_hashtag59,comment_hashtag60,comment_hashtag61,comment_hashtag62,comment_hashtag63,comment_hashtag64,comment_hashtag65,comment_hashtag66,comment_hashtag67,comment_hashtag68,comment_hashtag69,comment_hashtag70,comment_hashtag71,comment_hashtag72,comment_hashtag73,comment_hashtag74,comment_hashtag75,comment_hashtag76,comment_hashtag77,comment_hashtag78,comment_hashtag79,comment_hashtag80,comment_hashtag81,comment_hashtag82,comment_hashtag83,comment_hashtag84,comment_hashtag85,comment_hashtag86,comment_hashtag87,comment_hashtag88,comment_hashtag89,comment_hashtag90,comment_hashtag91,comment_hashtag92,comment_hashtag93,comment_hashtag94,comment_hashtag95,comment_hashtag96,comment_hashtag97,comment_hashtag98,comment_hashtag99,comment_hashtag100,comment_hashtag101,comment_hashtag102,comment_hashtag103,
                          comment_medias,comment_medias1,comment_medias2,comment_medias3,comment_medias4,comment_medias5,comment_medias6,comment_medias7,comment_medias8,comment_medias9,comment_medias10,comment_medias11,comment_medias12,comment_medias13,comment_medias14,comment_medias15,comment_medias16,comment_medias17,comment_medias18,comment_medias19,comment_medias20,comment_medias21,comment_medias22,comment_medias23,comment_medias24,comment_medias25,comment_medias26,comment_medias27,comment_medias28,comment_medias29,comment_medias30,comment_medias31,comment_medias32,comment_medias33,comment_medias34,comment_medias35,comment_medias36,comment_medias37,comment_medias38,comment_medias39,comment_medias40,comment_medias41,comment_medias42,comment_medias43,comment_medias44,comment_medias45,comment_medias46,comment_medias47,comment_medias48,comment_medias49,comment_medias50,comment_medias51,comment_medias52,comment_medias53,comment_medias54,comment_medias55,comment_medias56,comment_medias57,comment_medias58,comment_medias59,comment_medias60,comment_medias61,comment_medias62,comment_medias63,comment_medias64,comment_medias65,comment_medias66,comment_medias67,comment_medias68,comment_medias69,comment_medias70,comment_medias71,comment_medias72,comment_medias73,comment_medias74,comment_medias75,comment_medias76,comment_medias77,comment_medias78,comment_medias79,comment_medias80,comment_medias81,comment_medias82,comment_medias83,comment_medias84,comment_medias85,comment_medias86,comment_medias87,comment_medias88,comment_medias89,comment_medias90,comment_medias91,comment_medias92,comment_medias93,comment_medias94,comment_medias95,comment_medias96,comment_medias97,comment_medias98,comment_medias99,comment_medias100,comment_medias101,comment_medias102,comment_medias103, comment_user, comment_users,	
                          is_commented, reply_to_comment
)
from .bot_delete import delete_comment, delete_media, delete_medias
from .bot_direct import (send_hashtag, send_like, send_media, send_medias,
                         send_message, send_messages, send_profile, send_photo,
                         approve_pending_thread_requests
)
from .bot_filter import (check_media, check_not_bot, check_user, filter_medias)
from .bot_follow import (follow, follow_followers, follow_following,
                         follow_users, approve_pending_follow_requests, reject_pending_follow_requests)
from .bot_get import (convert_to_user_id, get_archived_medias, get_comment, get_comment1, get_comment2,get_comment3,get_comment4,get_comment5,get_comment6,get_comment7,get_comment8,get_comment9,get_comment10,get_comment11,get_comment12,get_comment13,get_comment14,get_comment15,get_comment16,get_comment17,get_comment18,get_comment19,get_comment20,get_comment21,get_comment22,get_comment23,get_comment24,get_comment25,get_comment26,get_comment27,get_comment28,get_comment29,get_comment30,get_comment31,get_comment32,get_comment33,get_comment34,get_comment35,get_comment36,get_comment37,get_comment38,get_comment39,get_comment40,get_comment41,get_comment42,get_comment43,get_comment44,get_comment45,get_comment46,get_comment47,get_comment48,get_comment49,get_comment50,get_comment51,get_comment52,get_comment53,get_comment54,get_comment55,get_comment56,get_comment57,get_comment58,get_comment59,get_comment60,get_comment61,get_comment62,get_comment63,get_comment64,get_comment65,get_comment66,get_comment67,get_comment68,get_comment69,get_comment70,get_comment71,get_comment72,get_comment73,get_comment74,get_comment75,get_comment76,get_comment77,get_comment78,get_comment79,get_comment80,get_comment81,get_comment82,get_comment83,get_comment84,get_comment85,get_comment86,get_comment87,get_comment88,get_comment89,get_comment90,get_comment91,get_comment92,get_comment93,get_comment94,get_comment95,get_comment96,get_comment97,get_comment98,get_comment99,get_comment100,get_comment101,get_comment102,get_comment103,
                      get_comment_likers, get_geotag_medias, get_geotag_users,
                      get_hashtag_medias, get_hashtag_users,
                      get_last_user_medias, get_locations_from_coordinates,
                      get_media_commenters, get_media_comments,
                      get_media_comments_all, get_media_id_from_link,
                      get_link_from_media_id, get_media_info, get_media_likers,
                      get_media_owner, get_messages, get_popular_medias,
                      get_timeline_medias, get_timeline_users,
                      get_total_hashtag_medias, get_total_user_medias,
                      get_user_followers, get_user_following,
                      get_user_id_from_username, get_user_info,
                      get_user_likers, get_user_medias, get_user_tags_medias,
                      get_username_from_user_id, get_your_medias, search_users,
                      get_user_stories, get_user_reel, get_self_story_viewers,
                      get_pending_follow_requests, get_pending_thread_requests, get_users_commented)
from .bot_like import (like, like_comment, like_followers, like_following,
                       like_geotag, like_hashtag, like_media_comments,
                       like_medias, like_timeline, like_user, like_users, like_location_feed)
from .bot_photo import download_photo, download_photos, upload_photo
from .bot_stats import save_user_stats
from .bot_support import (check_if_file_exists, console_print, extract_urls,
                          read_list_from_file)
from .bot_unfollow import (unfollow, unfollow_everyone, unfollow_non_followers,
                           unfollow_users, unfollow_non_followers_followed_by_bot)
from .bot_unlike import (unlike, unlike_comment, unlike_media_comments,
                         unlike_medias, unlike_user)
from .bot_video import upload_video, download_video
from .bot_story import download_stories, upload_story_photo, watch_users_reels


class Bot(object):
    def __init__(self,
                 whitelist_file='whitelist.txt',
                 blacklist_file='blacklist.txt',
                 comments_file='comments.txt',
				 comments_file1='comment/comment1.txt',
				 comments_file2='comment/comment2.txt',
				 comments_file3='comment/comment3.txt',
				 comments_file4='comment/comment4.txt',
				 comments_file5='comment/comment5.txt',
				 comments_file6='comment/comment6.txt',
				 comments_file7='comment/comment7.txt',
				 comments_file8='comment/comment8.txt',
				 comments_file9='comment/comment9.txt',
				 comments_file10='comment/comment10.txt',
				 comments_file11='comment/comment11.txt',
				 comments_file12='comment/comment12.txt',
				 comments_file13='comment/comment13.txt',
				 comments_file14='comment/comment14.txt',
				 comments_file15='comment/comment15.txt',
				 comments_file16='comment/comment16.txt',
				 comments_file17='comment/comment17.txt',
				 comments_file18='comment/comment18.txt',
				 comments_file19='comment/comment19.txt',
				 comments_file20='comment/comment20.txt',
				 comments_file21='comment/comment21.txt',
				 comments_file22='comment/comment22.txt',
				 comments_file23='comment/comment23.txt',
				 comments_file24='comment/comment24.txt',
				 comments_file25='comment/comment25.txt',
				 comments_file26='comment/comment26.txt',
				 comments_file27='comment/comment27.txt',
				 comments_file28='comment/comment28.txt',
				 comments_file29='comment/comment29.txt',
				 comments_file30='comment/comment30.txt',
				 comments_file31='comment/comment31.txt',
				 comments_file32='comment/comment32.txt',
				 comments_file33='comment/comment33.txt',
				 comments_file34='comment/comment34.txt',
				 comments_file35='comment/comment35.txt',
				 comments_file36='comment/comment36.txt',
				 comments_file37='comment/comment37.txt',
				 comments_file38='comment/comment38.txt',
				 comments_file39='comment/comment39.txt',
				 comments_file40='comment/comment40.txt',
				 comments_file41='comment/comment41.txt',
				 comments_file42='comment/comment42.txt',
				 comments_file43='comment/comment43.txt',
				 comments_file44='comment/comment44.txt',
				 comments_file45='comment/comment45.txt',
				 comments_file46='comment/comment46.txt',
				 comments_file47='comment/comment47.txt',
				 comments_file48='comment/comment48.txt',
				 comments_file49='comment/comment49.txt',
				 comments_file50='comment/comment50.txt',
				 comments_file51='comment/comment51.txt',
				 comments_file52='comment/comment52.txt',
				 comments_file53='comment/comment53.txt',
				 comments_file54='comment/comment54.txt',
				 comments_file55='comment/comment55.txt',
				 comments_file56='comment/comment56.txt',
				 comments_file57='comment/comment57.txt',
				 comments_file58='comment/comment58.txt',
				 comments_file59='comment/comment59.txt',
				 comments_file60='comment/comment60.txt',
				 comments_file61='comment/comment61.txt',
				 comments_file62='comment/comment62.txt',
				 comments_file63='comment/comment63.txt',
				 comments_file64='comment/comment64.txt',
				 comments_file65='comment/comment65.txt',
				 comments_file66='comment/comment66.txt',
				 comments_file67='comment/comment67.txt',
				 comments_file68='comment/comment68.txt',
				 comments_file69='comment/comment69.txt',
				 comments_file70='comment/comment70.txt',
				 comments_file71='comment/comment71.txt',
				 comments_file72='comment/comment72.txt',
				 comments_file73='comment/comment73.txt',
				 comments_file74='comment/comment74.txt',
				 comments_file75='comment/comment75.txt',
				 comments_file76='comment/comment76.txt',
				 comments_file77='comment/comment77.txt',
				 comments_file78='comment/comment78.txt',
				 comments_file79='comment/comment79.txt',
				 comments_file80='comment/comment80.txt',
				 comments_file81='comment/comment81.txt',
				 comments_file82='comment/comment82.txt',
				 comments_file83='comment/comment83.txt',
				 comments_file84='comment/comment84.txt',
				 comments_file85='comment/comment85.txt',
				 comments_file86='comment/comment86.txt',
				 comments_file87='comment/comment87.txt',
				 comments_file88='comment/comment88.txt',
				 comments_file89='comment/comment89.txt',
				 comments_file90='comment/comment90.txt',
				 comments_file91='comment/comment91.txt',
				 comments_file92='comment/comment92.txt',
				 comments_file93='comment/comment93.txt',
				 comments_file94='comment/comment94.txt',
				 comments_file95='comment/comment95.txt',
				 comments_file96='comment/comment96.txt',
				 comments_file97='comment/comment97.txt',
				 comments_file98='comment/comment98.txt',
				 comments_file99='comment/comment99.txt',
				 comments_file100='comment/comment100.txt',
				 comments_file101='comment/comment101.txt',
				 comments_file102='comment/comment102.txt',
				 comments_file103='comment/comment103.txt',
                 followed_file='followed.txt',
                 unfollowed_file='unfollowed.txt',
                 skipped_file='skipped.txt',
                 friends_file='friends.txt',
                 base_path='',
                 proxy=None,
                 max_likes_per_day=1000,
                 max_unlikes_per_day=1000,
                 max_follows_per_day=350,
                 max_unfollows_per_day=350,
                 max_comments_per_day=100,
                 max_blocks_per_day=100,
                 max_unblocks_per_day=100,
                 max_likes_to_like=100,
                 min_likes_to_like=20,
                 max_messages_per_day=300,
                 filter_users=True,
                 filter_private_users=True,
                 filter_users_without_profile_photo=True,
                 filter_previously_followed=False,
                 filter_business_accounts=True,
                 filter_verified_accounts=True,
                 max_followers_to_follow=2000,
                 min_followers_to_follow=10,
                 max_following_to_follow=2000,
                 min_following_to_follow=10,
                 max_followers_to_following_ratio=10,
                 max_following_to_followers_ratio=2,
                 min_media_count_to_follow=3,
                 max_following_to_block=2000,
                 like_delay=10,
                 unlike_delay=10,
                 follow_delay=30,
                 unfollow_delay=30,
                 comment_delay=60,
                 block_delay=30,
                 unblock_delay=30,
                 message_delay=60,
                 stop_words=('shop', 'store', 'free'),
                 blacklist_hashtags=['#shop', '#store', '#free'],
                 blocked_actions_protection=True,
                 verbosity=True,
                 device=None
                 ):
        self.api = API(device=device, base_path=base_path)
        self.base_path = base_path

        self.total = {'likes': 0,
                      'unlikes': 0,
                      'follows': 0,
                      'unfollows': 0,
                      'comments': 0,
                      'blocks': 0,
                      'unblocks': 0,
                      'messages': 0,
                      'archived': 0,
                      'unarchived': 0,
					  'stories_viewed': 0
					  }

        self.start_time = datetime.datetime.now()

        self.delays = {'like': like_delay,
                       'unlike': unlike_delay,
                       'follow': follow_delay,
                       'unfollow': unfollow_delay,
                       'comment': comment_delay,
                       'block': block_delay,
                       'unblock': unblock_delay,
                       'message': message_delay}

        self.last = {key: 0 for key in self.delays.keys()}

        # limits - follow
        self.filter_users = filter_users
        self.filter_private_users = filter_private_users
        self.filter_users_without_profile_photo = filter_users_without_profile_photo
        self.filter_business_accounts = filter_business_accounts
        self.filter_verified_accounts = filter_verified_accounts
        self.filter_previously_followed = filter_previously_followed

        self.max_per_day = {'likes': max_likes_per_day,
                            'unlikes': max_unlikes_per_day,
                            'follows': max_follows_per_day,
                            'unfollows': max_unfollows_per_day,
                            'comments': max_comments_per_day,
                            'blocks': max_blocks_per_day,
                            'unblocks': max_unblocks_per_day,
                            'messages': max_messages_per_day}

        self.blocked_actions_protection = blocked_actions_protection

        self.blocked_actions = {'likes': False,
                                'unlikes': False,
                                'follows': False,
                                'unfollows': False,
                                'comments': False,
                                'blocks': False,
                                'unblocks': False,
                                'messages': False}

        self.max_likes_to_like = max_likes_to_like
        self.min_likes_to_like = min_likes_to_like
        self.max_followers_to_follow = max_followers_to_follow
        self.min_followers_to_follow = min_followers_to_follow
        self.max_following_to_follow = max_following_to_follow
        self.min_following_to_follow = min_following_to_follow
        self.max_followers_to_following_ratio = max_followers_to_following_ratio
        self.max_following_to_followers_ratio = max_following_to_followers_ratio
        self.min_media_count_to_follow = min_media_count_to_follow
        self.stop_words = stop_words
        self.blacklist_hashtags = blacklist_hashtags

        # limits - block
        self.max_following_to_block = max_following_to_block

        # current following and followers
        self._following = None
        self._followers = None
        self._user_infos = {}  # User info cache
        self._usernames = {}  # `username` to `user_id` mapping

        # Adjust file paths
        followed_file = os.path.join(base_path, followed_file)
        unfollowed_file = os.path.join(base_path, unfollowed_file)
        skipped_file = os.path.join(base_path, skipped_file)
        friends_file = os.path.join(base_path, friends_file)
        comments_file = os.path.join(base_path, comments_file)
        blacklist_file = os.path.join(base_path, blacklist_file)
        whitelist_file = os.path.join(base_path, whitelist_file)

        # Database files
        self.followed_file = utils.file(followed_file)
        self.unfollowed_file = utils.file(unfollowed_file)
        self.skipped_file = utils.file(skipped_file)
        self.friends_file = utils.file(friends_file)
        self.comments_file = utils.file(comments_file)
        self.comments_file1= utils.file(comments_file1)
        self.comments_file2= utils.file(comments_file2)
        self.comments_file3= utils.file(comments_file3)
        self.comments_file4= utils.file(comments_file4)
        self.comments_file5= utils.file(comments_file5)
        self.comments_file6= utils.file(comments_file6)
        self.comments_file7= utils.file(comments_file7)
        self.comments_file8= utils.file(comments_file8)
        self.comments_file9= utils.file(comments_file9)
        self.comments_file10= utils.file(comments_file10)
        self.comments_file11= utils.file(comments_file11)
        self.comments_file12= utils.file(comments_file12)
        self.comments_file13= utils.file(comments_file13)
        self.comments_file14= utils.file(comments_file14)
        self.comments_file15= utils.file(comments_file15)
        self.comments_file16= utils.file(comments_file16)
        self.comments_file17= utils.file(comments_file17)
        self.comments_file18= utils.file(comments_file18)
        self.comments_file19= utils.file(comments_file19)
        self.comments_file20= utils.file(comments_file20)
        self.comments_file21= utils.file(comments_file21)
        self.comments_file22= utils.file(comments_file22)
        self.comments_file23= utils.file(comments_file23)
        self.comments_file24= utils.file(comments_file24)
        self.comments_file25= utils.file(comments_file25)
        self.comments_file26= utils.file(comments_file26)
        self.comments_file27= utils.file(comments_file27)
        self.comments_file28= utils.file(comments_file28)
        self.comments_file29= utils.file(comments_file29)
        self.comments_file30= utils.file(comments_file30)
        self.comments_file31= utils.file(comments_file31)
        self.comments_file32= utils.file(comments_file32)
        self.comments_file33= utils.file(comments_file33)
        self.comments_file34= utils.file(comments_file34)
        self.comments_file35= utils.file(comments_file35)
        self.comments_file36= utils.file(comments_file36)
        self.comments_file37= utils.file(comments_file37)
        self.comments_file38= utils.file(comments_file38)
        self.comments_file39= utils.file(comments_file39)
        self.comments_file40= utils.file(comments_file40)
        self.comments_file41= utils.file(comments_file41)
        self.comments_file42= utils.file(comments_file42)
        self.comments_file43= utils.file(comments_file43)
        self.comments_file44= utils.file(comments_file44)
        self.comments_file45= utils.file(comments_file45)
        self.comments_file46= utils.file(comments_file46)
        self.comments_file47= utils.file(comments_file47)
        self.comments_file48= utils.file(comments_file48)
        self.comments_file49= utils.file(comments_file49)
        self.comments_file50= utils.file(comments_file50)
        self.comments_file51= utils.file(comments_file51)
        self.comments_file52= utils.file(comments_file52)
        self.comments_file53= utils.file(comments_file53)
        self.comments_file54= utils.file(comments_file54)
        self.comments_file55= utils.file(comments_file55)
        self.comments_file56= utils.file(comments_file56)
        self.comments_file57= utils.file(comments_file57)
        self.comments_file58= utils.file(comments_file58)
        self.comments_file59= utils.file(comments_file59)
        self.comments_file60= utils.file(comments_file60)
        self.comments_file61= utils.file(comments_file61)
        self.comments_file62= utils.file(comments_file62)
        self.comments_file63= utils.file(comments_file63)
        self.comments_file64= utils.file(comments_file64)
        self.comments_file65= utils.file(comments_file65)
        self.comments_file66= utils.file(comments_file66)
        self.comments_file67= utils.file(comments_file67)
        self.comments_file68= utils.file(comments_file68)
        self.comments_file69= utils.file(comments_file69)
        self.comments_file70= utils.file(comments_file70)
        self.comments_file71= utils.file(comments_file71)
        self.comments_file72= utils.file(comments_file72)
        self.comments_file73= utils.file(comments_file73)
        self.comments_file74= utils.file(comments_file74)
        self.comments_file75= utils.file(comments_file75)
        self.comments_file76= utils.file(comments_file76)
        self.comments_file77= utils.file(comments_file77)
        self.comments_file78= utils.file(comments_file78)
        self.comments_file79= utils.file(comments_file79)
        self.comments_file80= utils.file(comments_file80)
        self.comments_file81= utils.file(comments_file81)
        self.comments_file82= utils.file(comments_file82)
        self.comments_file83= utils.file(comments_file83)
        self.comments_file84= utils.file(comments_file84)
        self.comments_file85= utils.file(comments_file85)
        self.comments_file86= utils.file(comments_file86)
        self.comments_file87= utils.file(comments_file87)
        self.comments_file88= utils.file(comments_file88)
        self.comments_file89= utils.file(comments_file89)
        self.comments_file90= utils.file(comments_file90)
        self.comments_file91= utils.file(comments_file91)
        self.comments_file92= utils.file(comments_file92)
        self.comments_file93= utils.file(comments_file93)
        self.comments_file94= utils.file(comments_file94)
        self.comments_file95= utils.file(comments_file95)
        self.comments_file96= utils.file(comments_file96)
        self.comments_file97= utils.file(comments_file97)
        self.comments_file98= utils.file(comments_file98)
        self.comments_file99= utils.file(comments_file99)
        self.comments_file100= utils.file(comments_file100)
        self.comments_file101= utils.file(comments_file101)
        self.comments_file102= utils.file(comments_file102)
        self.comments_file103= utils.file(comments_file103)
        self.blacklist_file = utils.file(blacklist_file)
        self.whitelist_file = utils.file(whitelist_file)

        self.proxy = proxy
        self.verbosity = verbosity

        self.logger = self.api.logger
        self.logger.info('Instabot Started')

    @property
    def user_id(self):
        # For compatibility
        return self.api.user_id

    @property
    def username(self):
        # For compatibility
        return self.api.username

    @property
    def password(self):
        # For compatibility
        return self.api.password

    @property
    def last_json(self):
        # For compatibility
        return self.api.last_json

    @property
    def blacklist(self):
        # This is a fast operation because `get_user_id_from_username` is cached.
        return [self.convert_to_user_id(i) for i in self.blacklist_file.list
                if i is not None]

    @property
    def whitelist(self):
        # This is a fast operation because `get_user_id_from_username` is cached.
        return [self.convert_to_user_id(i) for i in self.whitelist_file.list
                if i is not None]

    @property
    def following(self):
        now = time.time()
        last = self.last.get('updated_following', now)
        if self._following is None or now - last > 7200:
            self.console_print('`bot.following` is empty, will download.', 'green')
            self._following = self.get_user_following(self.user_id)
            self.last['updated_following'] = now
        return self._following

    @property
    def followers(self):
        now = time.time()
        last = self.last.get('updated_followers', now)
        if self._followers is None or now - last > 7200:
            self.console_print('`bot.followers` is empty, will download.', 'green')
            self._followers = self.get_user_followers(self.user_id)
            self.last['updated_followers'] = now
        return self._followers

    def version(self):
        try:
            from pip._vendor import pkg_resources
        except ImportError:
            import pkg_resources
        return next((p.version for p in pkg_resources.working_set if p.project_name.lower() == 'instabot'), "No match")

    def logout(self, *args, **kwargs):
        save_checkpoint(self)
        self.api.logout()
        self.logger.info("Bot stopped. "
                         "Worked: %s", datetime.datetime.now() - self.start_time)
        self.print_counters()

    def login(self, **args):
        if self.proxy:
            args['proxy'] = self.proxy
        if self.api.login(**args) is False:
            return False
        self.prepare()
        signal.signal(signal.SIGTERM, self.logout)
        atexit.register(self.logout)
        return True

    def prepare(self):
        storage = load_checkpoint(self)
        if storage is not None:
            self.total, self.blocked_actions, self.api.total_requests, self.start_time = storage

    def print_counters(self):
        for key, val in self.total.items():
            if val > 0:
                self.logger.info("Total {}: {}{}".format(key, val,
                                                         "/" + str(self.max_per_day[key]) if self.max_per_day.get(key) else ""))
        for key, val in self.blocked_actions.items():
            if val:
                self.logger.info("Blocked {}".format(key))
        self.logger.info("Total requests: {}".format(self.api.total_requests))
		

		
       

    def delay(self, key):
        """Sleep only if elapsed time since `self.last[key]` < `self.delay[key]`."""
        last_action, target_delay = self.last[key], self.delays[key]
        elapsed_time = time.time() - last_action
        if elapsed_time < target_delay:
            t_remaining = target_delay - elapsed_time
            time.sleep(t_remaining * random.uniform(0.25, 1.25))
        self.last[key] = time.time()

    def error_delay(self):
        time.sleep(10)

    def small_delay(self):
        time.sleep(random.uniform(0.75, 3.75))

    def very_small_delay(self):
        time.sleep(random.uniform(0.175, 0.875))

    def reached_limit(self, key):
        current_date = datetime.datetime.now()
        passed_days = (current_date.date() - self.start_time.date()).days
        if passed_days > 0:
            self.reset_counters()
        return self.max_per_day[key] - self.total[key] <= 0

    def reset_counters(self):
        for k in self.total:
            self.total[k] = 0
        for k in self.blocked_actions:
            self.blocked_actions[k] = False
        self.start_time = datetime.datetime.now()

    # getters
    def get_user_stories(self, user_id):
        """
        Returns array of stories links
        """
        return get_user_stories(self, user_id)

    def get_user_reel(self, user_id):
        return get_user_reel(self, user_id)

    def get_self_story_viewers(self, story_id):
        return get_self_story_viewers(self, story_id)

    def get_pending_follow_requests(self):
        return get_pending_follow_requests(self)

    def get_your_medias(self, as_dict=False):
        """
        Returns your media ids. With parameter as_dict=True returns media as dict.
        :type as_dict: bool
        """
        return get_your_medias(self, as_dict)

    def get_archived_medias(self, as_dict=False):
        """
        Returns your archived media ids. With parameter as_dict=True returns media as dict.
        :type as_dict: bool
        """
        return get_archived_medias(self, as_dict)

    def get_timeline_medias(self):
        return get_timeline_medias(self)

    def get_popular_medias(self):
        return get_popular_medias(self)

    def get_user_medias(self, user_id, filtration=True, is_comment=False):
        return get_user_medias(self, user_id, filtration, is_comment)

    def get_total_user_medias(self, user_id):
        return get_total_user_medias(self, user_id)

    def get_last_user_medias(self, user_id, count):
        """
        Returns the last number of posts specified in count in media ids array.
        :type count: int
        :param count: Count of posts
        :return: array
        """
        return get_last_user_medias(self, user_id, count)

    def get_hashtag_medias(self, hashtag, filtration=True):
        return get_hashtag_medias(self, hashtag, filtration)

    def get_total_hashtag_medias(self, hashtag, amount=100, filtration=False):
        return get_total_hashtag_medias(self, hashtag, amount, filtration)

    def get_geotag_medias(self, geotag, filtration=True):
        return get_geotag_medias(self, geotag, filtration)

    def get_locations_from_coordinates(self, latitude, longitude):
        return get_locations_from_coordinates(self, latitude, longitude)

    def get_media_info(self, media_id):
        return get_media_info(self, media_id)

    def get_timeline_users(self):
        return get_timeline_users(self)

    def get_hashtag_users(self, hashtag):
        return get_hashtag_users(self, hashtag)

    def get_geotag_users(self, geotag):
        return get_geotag_users(self, geotag)

    def get_user_id_from_username(self, username):
        return get_user_id_from_username(self, username)

    def get_user_tags_medias(self, user_id):
        return get_user_tags_medias(self, user_id)
		
    def get_users_commented(self, user_id, media_count=10):
        return get_users_commented(self, user_id, media_count)

    def get_username_from_user_id(self, user_id):
        return get_username_from_user_id(self, user_id)

    def get_user_info(self, user_id, use_cache=True):
        return get_user_info(self, user_id, use_cache)

    def get_user_followers(self, user_id, nfollows=None):
        return get_user_followers(self, user_id, nfollows)

    def get_user_following(self, user_id, nfollows=None):
        return get_user_following(self, user_id, nfollows)

    def get_comment_likers(self, comment_id):
        return get_comment_likers(self, comment_id)

    def get_media_likers(self, media_id):
        return get_media_likers(self, media_id)

    def get_media_comments(self, media_id, only_text=False):
        return get_media_comments(self, media_id, only_text)

    def get_media_comments_all(self, media_id, only_text=False, count=False):
        return get_media_comments_all(self, media_id, only_text, count)

    def get_comment(self):
        return get_comment(self)
    def get_comment1(self):
        return get_comment1(self)
    def get_comment2(self):
        return get_comment2(self)
    def get_comment3(self):
        return get_comment3(self)
    def get_comment4(self):
        return get_comment4(self)
    def get_comment5(self):
        return get_comment5(self)
    def get_comment6(self):
        return get_comment6(self)
    def get_comment7(self):
        return get_comment7(self)
    def get_comment8(self):
        return get_comment8(self)
    def get_comment9(self):
        return get_comment9(self)
    def get_comment10(self):
        return get_comment10(self)
    def get_comment11(self):
        return get_comment11(self)
    def get_comment12(self):
        return get_comment12(self)
    def get_comment13(self):
        return get_comment13(self)
    def get_comment14(self):
        return get_comment14(self)
    def get_comment15(self):
        return get_comment15(self)
    def get_comment16(self):
        return get_comment16(self)
    def get_comment17(self):
        return get_comment17(self)
    def get_comment18(self):
        return get_comment18(self)
    def get_comment19(self):
        return get_comment19(self)
    def get_comment20(self):
        return get_comment20(self)
    def get_comment21(self):
        return get_comment21(self)
    def get_comment22(self):
        return get_comment22(self)
    def get_comment23(self):
        return get_comment23(self)
    def get_comment24(self):
        return get_comment24(self)
    def get_comment25(self):
        return get_comment25(self)
    def get_comment26(self):
        return get_comment26(self)
    def get_comment27(self):
        return get_comment27(self)
    def get_comment28(self):
        return get_comment28(self)
    def get_comment29(self):
        return get_comment29(self)
    def get_comment30(self):
        return get_comment30(self)
    def get_comment31(self):
        return get_comment31(self)
    def get_comment32(self):
        return get_comment32(self)
    def get_comment33(self):
        return get_comment33(self)
    def get_comment34(self):
        return get_comment34(self)
    def get_comment35(self):
        return get_comment35(self)
    def get_comment36(self):
        return get_comment36(self)
    def get_comment37(self):
        return get_comment37(self)
    def get_comment38(self):
        return get_comment38(self)
    def get_comment39(self):
        return get_comment39(self)
    def get_comment40(self):
        return get_comment40(self)
    def get_comment41(self):
        return get_comment41(self)
    def get_comment42(self):
        return get_comment42(self)
    def get_comment43(self):
        return get_comment43(self)
    def get_comment44(self):
        return get_comment44(self)
    def get_comment45(self):
        return get_comment45(self)
    def get_comment46(self):
        return get_comment46(self)
    def get_comment47(self):
        return get_comment47(self)
    def get_comment48(self):
        return get_comment48(self)
    def get_comment49(self):
        return get_comment49(self)
    def get_comment50(self):
        return get_comment50(self)
    def get_comment51(self):
        return get_comment51(self)
    def get_comment52(self):
        return get_comment52(self)
    def get_comment53(self):
        return get_comment53(self)
    def get_comment54(self):
        return get_comment54(self)
    def get_comment55(self):
        return get_comment55(self)
    def get_comment56(self):
        return get_comment56(self)
    def get_comment57(self):
        return get_comment57(self)
    def get_comment58(self):
        return get_comment58(self)
    def get_comment59(self):
        return get_comment59(self)
    def get_comment60(self):
        return get_comment60(self)
    def get_comment61(self):
        return get_comment61(self)
    def get_comment62(self):
        return get_comment62(self)
    def get_comment63(self):
        return get_comment63(self)
    def get_comment64(self):
        return get_comment64(self)
    def get_comment65(self):
        return get_comment65(self)
    def get_comment66(self):
        return get_comment66(self)
    def get_comment67(self):
        return get_comment67(self)
    def get_comment68(self):
        return get_comment68(self)
    def get_comment69(self):
        return get_comment69(self)
    def get_comment70(self):
        return get_comment70(self)
    def get_comment71(self):
        return get_comment71(self)
    def get_comment72(self):
        return get_comment72(self)
    def get_comment73(self):
        return get_comment73(self)
    def get_comment74(self):
        return get_comment74(self)
    def get_comment75(self):
        return get_comment75(self)
    def get_comment76(self):
        return get_comment76(self)
    def get_comment77(self):
        return get_comment77(self)
    def get_comment78(self):
        return get_comment78(self)
    def get_comment79(self):
        return get_comment79(self)
    def get_comment80(self):
        return get_comment80(self)
    def get_comment81(self):
        return get_comment81(self)
    def get_comment82(self):
        return get_comment82(self)
    def get_comment83(self):
        return get_comment83(self)
    def get_comment84(self):
        return get_comment84(self)
    def get_comment85(self):
        return get_comment85(self)
    def get_comment86(self):
        return get_comment86(self)
    def get_comment87(self):
        return get_comment87(self)
    def get_comment88(self):
        return get_comment88(self)
    def get_comment89(self):
        return get_comment89(self)
    def get_comment90(self):
        return get_comment90(self)
    def get_comment91(self):
        return get_comment91(self)
    def get_comment92(self):
        return get_comment92(self)
    def get_comment93(self):
        return get_comment93(self)
    def get_comment94(self):
        return get_comment94(self)
    def get_comment95(self):
        return get_comment95(self)
    def get_comment96(self):
        return get_comment96(self)
    def get_comment97(self):
        return get_comment97(self)
    def get_comment98(self):
        return get_comment98(self)
    def get_comment99(self):
        return get_comment99(self)
    def get_comment100(self):
        return get_comment100(self)
    def get_comment101(self):
        return get_comment101(self)
    def get_comment102(self):
        return get_comment102(self)
    def get_comment103(self):
        return get_comment103(self)

    def get_media_commenters(self, media_id):
        return get_media_commenters(self, media_id)

    def get_media_owner(self, media):
        return get_media_owner(self, media)

    def get_user_likers(self, user_id, media_count=10):
        return get_user_likers(self, user_id, media_count)

    def get_media_id_from_link(self, link):
        return get_media_id_from_link(self, link)

    def get_link_from_media_id(self, link):
        return get_link_from_media_id(self, link)

    def get_messages(self):
        return get_messages(self)

    def search_users(self, query):
        return search_users(self, query)

    def convert_to_user_id(self, usernames):
        return convert_to_user_id(self, usernames)

    def get_pending_thread_requests(self):
        return get_pending_thread_requests(self)

    # like

    def like(self, media_id, check_media=True):
        return like(self, media_id, check_media)

    def like_comment(self, comment_id):
        return like_comment(self, comment_id)

    def like_medias(self, media_ids, check_media=True):
        return like_medias(self, media_ids, check_media)

    def like_timeline(self, amount=None):
        return like_timeline(self, amount)

    def like_media_comments(self, media_id):
        return like_media_comments(self, media_id)

    def like_user(self, user_id, amount=None, filtration=True):
        return like_user(self, user_id, amount, filtration)

    def like_hashtag(self, hashtag, amount=None):
        return like_hashtag(self, hashtag, amount)

    def like_geotag(self, geotag, amount=None):
        return like_geotag(self, geotag, amount)

    def like_users(self, user_ids, nlikes=None, filtration=True):
        return like_users(self, user_ids, nlikes, filtration)

    def like_location_feed(self, place, amount):
        return like_location_feed(self, place, amount)

    def like_followers(self, user_id, nlikes=None, nfollows=None):
        return like_followers(self, user_id, nlikes, nfollows)

    def like_following(self, user_id, nlikes=None, nfollows=None):
        return like_following(self, user_id, nlikes, nfollows)

    # unlike

    def unlike(self, media_id):
        return unlike(self, media_id)

    def unlike_comment(self, comment_id):
        return unlike_comment(self, comment_id)

    def unlike_media_comments(self, media_id):
        return unlike_media_comments(self, media_id)

    def unlike_medias(self, media_ids):
        return unlike_medias(self, media_ids)

    def unlike_user(self, user):
        return unlike_user(self, user)

    # story
    def download_stories(self, username):
        return download_stories(self, username)

    def upload_story_photo(self, photo, upload_id=None):
        return upload_story_photo(self, photo, upload_id)

    def watch_users_reels(self, user_ids, max_users=100):
        return watch_users_reels(self, user_ids, max_users=max_users)														 
    # photo
    def download_photo(self, media_id, folder='photos', filename=None, save_description=False):
        return download_photo(self, media_id, folder, filename, save_description)

    def download_photos(self, medias, folder='photos', save_description=False):
        return download_photos(self, medias, folder, save_description)

    def upload_photo(self, photo, caption=None, upload_id=None, from_video=False, options={}):
        """Upload photo to Instagram

        @param photo         Path to photo file (String)
        @param caption       Media description (String)
        @param upload_id     Unique upload_id (String). When None, then generate automatically
        @param from_video    A flag that signals whether the photo is loaded from the video or by itself (Boolean, DEPRECATED: not used)
        @param options       Object with difference options, e.g. configure_timeout, rename (Dict)
                             Designed to reduce the number of function arguments!
                             This is the simplest request object.

        @return              Object with state of uploading to Instagram (or False)
        """
        return upload_photo(self, photo, caption, upload_id, from_video, options)


    # video

    def upload_video(self, video, caption='', thumbnail=None):
        return upload_video(self, video, caption, thumbnail)

    def upload_video(self, video, caption='', thumbnail=None, options={}):
        """Upload video to Instagram

        @param video      Path to video file (String)
        @param caption    Media description (String)
        @param thumbnail  Path to thumbnail for video (String). When None, then thumbnail is generate automatically
        @param options    Object with difference options, e.g. configure_timeout, rename_thumbnail, rename (Dict)
                          Designed to reduce the number of function arguments!

        @return           Object with state of uploading to Instagram (or False)
        """
        return upload_video(self, video, caption, thumbnail, options)

    def download_video(self, media_id, folder='videos', filename=None, save_description=False):
        return download_video(self, media_id, folder, filename, save_description)																							   

    # follow

    def follow(self, user_id):
        return follow(self, user_id)

    def follow_users(self, user_ids):
        return follow_users(self, user_ids)

    def follow_followers(self, user_id, nfollows=None):
        return follow_followers(self, user_id, nfollows)

    def follow_following(self, user_id, nfollows=None):
        return follow_following(self, user_id, nfollows)

    # unfollow

    def unfollow(self, user_id):
        return unfollow(self, user_id)

    def unfollow_users(self, user_ids):
        return unfollow_users(self, user_ids)

    def unfollow_non_followers(self, n_to_unfollows=None):
        return unfollow_non_followers(self, n_to_unfollows)

    def unfollow_non_followers_followed_by_bot(self, n_to_unfollows=None):
        return unfollow_non_followers_followed_by_bot(self, n_to_unfollows)																		  
    def unfollow_everyone(self):
        return unfollow_everyone(self)

    def approve_pending_follow_requests(self):
        return approve_pending_follow_requests(self)

    def reject_pending_follow_requests(self):
        return reject_pending_follow_requests(self)

    # direct

    def send_message(self, text, user_ids, thread_id=None):
        return send_message(self, text, user_ids, thread_id)

    def send_messages(self, text, user_ids):
        return send_messages(self, text, user_ids)

    def send_media(self, media_id, user_ids, text=None, thread_id=None):
        return send_media(self, media_id, user_ids, text, thread_id)

    def send_medias(self, media_id, user_ids, text=None):
        return send_medias(self, media_id, user_ids, text)

    def send_hashtag(self, hashtag, user_ids, text='', thread_id=None):
        return send_hashtag(self, hashtag, user_ids, text, thread_id)

    def send_profile(self, profile_user_id, user_ids, text='', thread_id=None):
        return send_profile(self, profile_user_id, user_ids, text, thread_id)

    def send_like(self, user_ids, thread_id=None):
        return send_like(self, user_ids, thread_id)

    def send_photo(self, user_ids, filepath, thread_id=None):
        return send_photo(self, user_ids, filepath, thread_id)

    def approve_pending_thread_requests(self):
        return approve_pending_thread_requests(self)

    # delete

    def delete_media(self, media_id):
        return delete_media(self, media_id)

    def delete_medias(self, medias):
        return delete_medias(self, medias)

    def delete_comment(self, media_id, comment_id):
        return delete_comment(self, media_id, comment_id)

    # archive

    def archive(self, media_id, undo=False):
        return archive(self, media_id, undo)

    def unarchive(self, media_id):
        return archive(self, media_id, True)

    def archive_medias(self, medias):
        return archive_medias(self, medias)

    def unarchive_medias(self, medias):
        return unarchive_medias(self, medias)

    # comment

    def comment(self, media_id, comment_text):
        return comment(self, media_id, comment_text)

    def reply_to_comment(self, media_id, comment_text, parent_comment_id):
        return reply_to_comment(self, media_id, comment_text, parent_comment_id)

    def comment_hashtag(self, hashtag, amount=None):
        return comment_hashtag(self, hashtag, amount)
		
    def comment_hashtag1(self, hashtag, amount=None):
        return comment_hashtag1(self, hashtag, amount)
    def comment_hashtag2(self, hashtag, amount=None):
        return comment_hashtag2(self, hashtag, amount)
    def comment_hashtag3(self, hashtag, amount=None):
        return comment_hashtag3(self, hashtag, amount)
    def comment_hashtag4(self, hashtag, amount=None):
        return comment_hashtag4(self, hashtag, amount)
    def comment_hashtag5(self, hashtag, amount=None):
        return comment_hashtag5(self, hashtag, amount)
    def comment_hashtag6(self, hashtag, amount=None):
        return comment_hashtag6(self, hashtag, amount)
    def comment_hashtag7(self, hashtag, amount=None):
        return comment_hashtag7(self, hashtag, amount)
    def comment_hashtag8(self, hashtag, amount=None):
        return comment_hashtag8(self, hashtag, amount)
    def comment_hashtag9(self, hashtag, amount=None):
        return comment_hashtag9(self, hashtag, amount)
    def comment_hashtag10(self, hashtag, amount=None):
        return comment_hashtag10(self, hashtag, amount)
    def comment_hashtag11(self, hashtag, amount=None):
        return comment_hashtag11(self, hashtag, amount)
    def comment_hashtag12(self, hashtag, amount=None):
        return comment_hashtag12(self, hashtag, amount)
    def comment_hashtag13(self, hashtag, amount=None):
        return comment_hashtag13(self, hashtag, amount)
    def comment_hashtag14(self, hashtag, amount=None):
        return comment_hashtag14(self, hashtag, amount)
    def comment_hashtag15(self, hashtag, amount=None):
        return comment_hashtag15(self, hashtag, amount)
    def comment_hashtag16(self, hashtag, amount=None):
        return comment_hashtag16(self, hashtag, amount)
    def comment_hashtag17(self, hashtag, amount=None):
        return comment_hashtag17(self, hashtag, amount)
    def comment_hashtag18(self, hashtag, amount=None):
        return comment_hashtag18(self, hashtag, amount)
    def comment_hashtag19(self, hashtag, amount=None):
        return comment_hashtag19(self, hashtag, amount)
    def comment_hashtag20(self, hashtag, amount=None):
        return comment_hashtag20(self, hashtag, amount)
    def comment_hashtag21(self, hashtag, amount=None):
        return comment_hashtag21(self, hashtag, amount)
    def comment_hashtag22(self, hashtag, amount=None):
        return comment_hashtag22(self, hashtag, amount)
    def comment_hashtag23(self, hashtag, amount=None):
        return comment_hashtag23(self, hashtag, amount)
    def comment_hashtag24(self, hashtag, amount=None):
        return comment_hashtag24(self, hashtag, amount)
    def comment_hashtag25(self, hashtag, amount=None):
        return comment_hashtag25(self, hashtag, amount)
    def comment_hashtag26(self, hashtag, amount=None):
        return comment_hashtag26(self, hashtag, amount)
    def comment_hashtag27(self, hashtag, amount=None):
        return comment_hashtag27(self, hashtag, amount)
    def comment_hashtag28(self, hashtag, amount=None):
        return comment_hashtag28(self, hashtag, amount)
    def comment_hashtag29(self, hashtag, amount=None):
        return comment_hashtag29(self, hashtag, amount)
    def comment_hashtag30(self, hashtag, amount=None):
        return comment_hashtag30(self, hashtag, amount)
    def comment_hashtag31(self, hashtag, amount=None):
        return comment_hashtag31(self, hashtag, amount)
    def comment_hashtag32(self, hashtag, amount=None):
        return comment_hashtag32(self, hashtag, amount)
    def comment_hashtag33(self, hashtag, amount=None):
        return comment_hashtag33(self, hashtag, amount)
    def comment_hashtag34(self, hashtag, amount=None):
        return comment_hashtag34(self, hashtag, amount)
    def comment_hashtag35(self, hashtag, amount=None):
        return comment_hashtag35(self, hashtag, amount)
    def comment_hashtag36(self, hashtag, amount=None):
        return comment_hashtag36(self, hashtag, amount)
    def comment_hashtag37(self, hashtag, amount=None):
        return comment_hashtag37(self, hashtag, amount)
    def comment_hashtag38(self, hashtag, amount=None):
        return comment_hashtag38(self, hashtag, amount)
    def comment_hashtag39(self, hashtag, amount=None):
        return comment_hashtag39(self, hashtag, amount)
    def comment_hashtag40(self, hashtag, amount=None):
        return comment_hashtag40(self, hashtag, amount)
    def comment_hashtag41(self, hashtag, amount=None):
        return comment_hashtag41(self, hashtag, amount)
    def comment_hashtag42(self, hashtag, amount=None):
        return comment_hashtag42(self, hashtag, amount)
    def comment_hashtag43(self, hashtag, amount=None):
        return comment_hashtag43(self, hashtag, amount)
    def comment_hashtag44(self, hashtag, amount=None):
        return comment_hashtag44(self, hashtag, amount)
    def comment_hashtag45(self, hashtag, amount=None):
        return comment_hashtag45(self, hashtag, amount)
    def comment_hashtag46(self, hashtag, amount=None):
        return comment_hashtag46(self, hashtag, amount)
    def comment_hashtag47(self, hashtag, amount=None):
        return comment_hashtag47(self, hashtag, amount)
    def comment_hashtag48(self, hashtag, amount=None):
        return comment_hashtag48(self, hashtag, amount)
    def comment_hashtag49(self, hashtag, amount=None):
        return comment_hashtag49(self, hashtag, amount)
    def comment_hashtag50(self, hashtag, amount=None):
        return comment_hashtag50(self, hashtag, amount)
    def comment_hashtag51(self, hashtag, amount=None):
        return comment_hashtag51(self, hashtag, amount)
    def comment_hashtag52(self, hashtag, amount=None):
        return comment_hashtag52(self, hashtag, amount)
    def comment_hashtag53(self, hashtag, amount=None):
        return comment_hashtag53(self, hashtag, amount)
    def comment_hashtag54(self, hashtag, amount=None):
        return comment_hashtag54(self, hashtag, amount)
    def comment_hashtag55(self, hashtag, amount=None):
        return comment_hashtag55(self, hashtag, amount)
    def comment_hashtag56(self, hashtag, amount=None):
        return comment_hashtag56(self, hashtag, amount)
    def comment_hashtag57(self, hashtag, amount=None):
        return comment_hashtag57(self, hashtag, amount)
    def comment_hashtag58(self, hashtag, amount=None):
        return comment_hashtag58(self, hashtag, amount)
    def comment_hashtag59(self, hashtag, amount=None):
        return comment_hashtag59(self, hashtag, amount)
    def comment_hashtag60(self, hashtag, amount=None):
        return comment_hashtag60(self, hashtag, amount)
    def comment_hashtag61(self, hashtag, amount=None):
        return comment_hashtag61(self, hashtag, amount)
    def comment_hashtag62(self, hashtag, amount=None):
        return comment_hashtag62(self, hashtag, amount)
    def comment_hashtag63(self, hashtag, amount=None):
        return comment_hashtag63(self, hashtag, amount)
    def comment_hashtag64(self, hashtag, amount=None):
        return comment_hashtag64(self, hashtag, amount)
    def comment_hashtag65(self, hashtag, amount=None):
        return comment_hashtag65(self, hashtag, amount)
    def comment_hashtag66(self, hashtag, amount=None):
        return comment_hashtag66(self, hashtag, amount)
    def comment_hashtag67(self, hashtag, amount=None):
        return comment_hashtag67(self, hashtag, amount)
    def comment_hashtag68(self, hashtag, amount=None):
        return comment_hashtag68(self, hashtag, amount)
    def comment_hashtag69(self, hashtag, amount=None):
        return comment_hashtag69(self, hashtag, amount)
    def comment_hashtag70(self, hashtag, amount=None):
        return comment_hashtag70(self, hashtag, amount)
    def comment_hashtag71(self, hashtag, amount=None):
        return comment_hashtag71(self, hashtag, amount)
    def comment_hashtag72(self, hashtag, amount=None):
        return comment_hashtag72(self, hashtag, amount)
    def comment_hashtag73(self, hashtag, amount=None):
        return comment_hashtag73(self, hashtag, amount)
    def comment_hashtag74(self, hashtag, amount=None):
        return comment_hashtag74(self, hashtag, amount)
    def comment_hashtag75(self, hashtag, amount=None):
        return comment_hashtag75(self, hashtag, amount)
    def comment_hashtag76(self, hashtag, amount=None):
        return comment_hashtag76(self, hashtag, amount)
    def comment_hashtag77(self, hashtag, amount=None):
        return comment_hashtag77(self, hashtag, amount)
    def comment_hashtag78(self, hashtag, amount=None):
        return comment_hashtag78(self, hashtag, amount)
    def comment_hashtag79(self, hashtag, amount=None):
        return comment_hashtag79(self, hashtag, amount)
    def comment_hashtag80(self, hashtag, amount=None):
        return comment_hashtag80(self, hashtag, amount)
    def comment_hashtag81(self, hashtag, amount=None):
        return comment_hashtag81(self, hashtag, amount)
    def comment_hashtag82(self, hashtag, amount=None):
        return comment_hashtag82(self, hashtag, amount)
    def comment_hashtag83(self, hashtag, amount=None):
        return comment_hashtag83(self, hashtag, amount)
    def comment_hashtag84(self, hashtag, amount=None):
        return comment_hashtag84(self, hashtag, amount)
    def comment_hashtag85(self, hashtag, amount=None):
        return comment_hashtag85(self, hashtag, amount)
    def comment_hashtag86(self, hashtag, amount=None):
        return comment_hashtag86(self, hashtag, amount)
    def comment_hashtag87(self, hashtag, amount=None):
        return comment_hashtag87(self, hashtag, amount)
    def comment_hashtag88(self, hashtag, amount=None):
        return comment_hashtag88(self, hashtag, amount)
    def comment_hashtag89(self, hashtag, amount=None):
        return comment_hashtag89(self, hashtag, amount)
    def comment_hashtag90(self, hashtag, amount=None):
        return comment_hashtag90(self, hashtag, amount)
    def comment_hashtag91(self, hashtag, amount=None):
        return comment_hashtag91(self, hashtag, amount)
    def comment_hashtag92(self, hashtag, amount=None):
        return comment_hashtag92(self, hashtag, amount)
    def comment_hashtag93(self, hashtag, amount=None):
        return comment_hashtag93(self, hashtag, amount)
    def comment_hashtag94(self, hashtag, amount=None):
        return comment_hashtag94(self, hashtag, amount)
    def comment_hashtag95(self, hashtag, amount=None):
        return comment_hashtag95(self, hashtag, amount)
    def comment_hashtag96(self, hashtag, amount=None):
        return comment_hashtag96(self, hashtag, amount)
    def comment_hashtag97(self, hashtag, amount=None):
        return comment_hashtag97(self, hashtag, amount)
    def comment_hashtag98(self, hashtag, amount=None):
        return comment_hashtag98(self, hashtag, amount)
    def comment_hashtag99(self, hashtag, amount=None):
        return comment_hashtag99(self, hashtag, amount)
    def comment_hashtag100(self, hashtag, amount=None):
        return comment_hashtag100(self, hashtag, amount)
    def comment_hashtag101(self, hashtag, amount=None):
        return comment_hashtag101(self, hashtag, amount)
    def comment_hashtag102(self, hashtag, amount=None):
        return comment_hashtag102(self, hashtag, amount)
    def comment_hashtag103(self, hashtag, amount=None):
        return comment_hashtag103(self, hashtag, amount)

    def comment_medias(self, medias):
        return comment_medias(self, medias)
		
    def comment_medias1(self, medias):
        return comment_medias1(self, medias)
    def comment_medias2(self, medias):
        return comment_medias2(self, medias)
    def comment_medias3(self, medias):
        return comment_medias3(self, medias)
    def comment_medias4(self, medias):
        return comment_medias4(self, medias)
    def comment_medias5(self, medias):
        return comment_medias5(self, medias)
    def comment_medias6(self, medias):
        return comment_medias6(self, medias)
    def comment_medias7(self, medias):
        return comment_medias7(self, medias)
    def comment_medias8(self, medias):
        return comment_medias8(self, medias)
    def comment_medias9(self, medias):
        return comment_medias9(self, medias)
    def comment_medias10(self, medias):
        return comment_medias10(self, medias)
    def comment_medias11(self, medias):
        return comment_medias11(self, medias)
    def comment_medias12(self, medias):
        return comment_medias12(self, medias)
    def comment_medias13(self, medias):
        return comment_medias13(self, medias)
    def comment_medias14(self, medias):
        return comment_medias14(self, medias)
    def comment_medias15(self, medias):
        return comment_medias15(self, medias)
    def comment_medias16(self, medias):
        return comment_medias16(self, medias)
    def comment_medias17(self, medias):
        return comment_medias17(self, medias)
    def comment_medias18(self, medias):
        return comment_medias18(self, medias)
    def comment_medias19(self, medias):
        return comment_medias19(self, medias)
    def comment_medias20(self, medias):
        return comment_medias20(self, medias)
    def comment_medias21(self, medias):
        return comment_medias21(self, medias)
    def comment_medias22(self, medias):
        return comment_medias22(self, medias)
    def comment_medias23(self, medias):
        return comment_medias23(self, medias)
    def comment_medias24(self, medias):
        return comment_medias24(self, medias)
    def comment_medias25(self, medias):
        return comment_medias25(self, medias)
    def comment_medias26(self, medias):
        return comment_medias26(self, medias)
    def comment_medias27(self, medias):
        return comment_medias27(self, medias)
    def comment_medias28(self, medias):
        return comment_medias28(self, medias)
    def comment_medias29(self, medias):
        return comment_medias29(self, medias)
    def comment_medias30(self, medias):
        return comment_medias30(self, medias)
    def comment_medias31(self, medias):
        return comment_medias31(self, medias)
    def comment_medias32(self, medias):
        return comment_medias32(self, medias)
    def comment_medias33(self, medias):
        return comment_medias33(self, medias)
    def comment_medias34(self, medias):
        return comment_medias34(self, medias)
    def comment_medias35(self, medias):
        return comment_medias35(self, medias)
    def comment_medias36(self, medias):
        return comment_medias36(self, medias)
    def comment_medias37(self, medias):
        return comment_medias37(self, medias)
    def comment_medias38(self, medias):
        return comment_medias38(self, medias)
    def comment_medias39(self, medias):
        return comment_medias39(self, medias)
    def comment_medias40(self, medias):
        return comment_medias40(self, medias)
    def comment_medias41(self, medias):
        return comment_medias41(self, medias)
    def comment_medias42(self, medias):
        return comment_medias42(self, medias)
    def comment_medias43(self, medias):
        return comment_medias43(self, medias)
    def comment_medias44(self, medias):
        return comment_medias44(self, medias)
    def comment_medias45(self, medias):
        return comment_medias45(self, medias)
    def comment_medias46(self, medias):
        return comment_medias46(self, medias)
    def comment_medias47(self, medias):
        return comment_medias47(self, medias)
    def comment_medias48(self, medias):
        return comment_medias48(self, medias)
    def comment_medias49(self, medias):
        return comment_medias49(self, medias)
    def comment_medias50(self, medias):
        return comment_medias50(self, medias)
    def comment_medias51(self, medias):
        return comment_medias51(self, medias)
    def comment_medias52(self, medias):
        return comment_medias52(self, medias)
    def comment_medias53(self, medias):
        return comment_medias53(self, medias)
    def comment_medias54(self, medias):
        return comment_medias54(self, medias)
    def comment_medias55(self, medias):
        return comment_medias55(self, medias)
    def comment_medias56(self, medias):
        return comment_medias56(self, medias)
    def comment_medias57(self, medias):
        return comment_medias57(self, medias)
    def comment_medias58(self, medias):
        return comment_medias58(self, medias)
    def comment_medias59(self, medias):
        return comment_medias59(self, medias)
    def comment_medias60(self, medias):
        return comment_medias60(self, medias)
    def comment_medias61(self, medias):
        return comment_medias61(self, medias)
    def comment_medias62(self, medias):
        return comment_medias62(self, medias)
    def comment_medias63(self, medias):
        return comment_medias63(self, medias)
    def comment_medias64(self, medias):
        return comment_medias64(self, medias)
    def comment_medias65(self, medias):
        return comment_medias65(self, medias)
    def comment_medias66(self, medias):
        return comment_medias66(self, medias)
    def comment_medias67(self, medias):
        return comment_medias67(self, medias)
    def comment_medias68(self, medias):
        return comment_medias68(self, medias)
    def comment_medias69(self, medias):
        return comment_medias69(self, medias)
    def comment_medias70(self, medias):
        return comment_medias70(self, medias)
    def comment_medias71(self, medias):
        return comment_medias71(self, medias)
    def comment_medias72(self, medias):
        return comment_medias72(self, medias)
    def comment_medias73(self, medias):
        return comment_medias73(self, medias)
    def comment_medias74(self, medias):
        return comment_medias74(self, medias)
    def comment_medias75(self, medias):
        return comment_medias75(self, medias)
    def comment_medias76(self, medias):
        return comment_medias76(self, medias)
    def comment_medias77(self, medias):
        return comment_medias77(self, medias)
    def comment_medias78(self, medias):
        return comment_medias78(self, medias)
    def comment_medias79(self, medias):
        return comment_medias79(self, medias)
    def comment_medias80(self, medias):
        return comment_medias80(self, medias)
    def comment_medias81(self, medias):
        return comment_medias81(self, medias)
    def comment_medias82(self, medias):
        return comment_medias82(self, medias)
    def comment_medias83(self, medias):
        return comment_medias83(self, medias)
    def comment_medias84(self, medias):
        return comment_medias84(self, medias)
    def comment_medias85(self, medias):
        return comment_medias85(self, medias)
    def comment_medias86(self, medias):
        return comment_medias86(self, medias)
    def comment_medias87(self, medias):
        return comment_medias87(self, medias)
    def comment_medias88(self, medias):
        return comment_medias88(self, medias)
    def comment_medias89(self, medias):
        return comment_medias89(self, medias)
    def comment_medias90(self, medias):
        return comment_medias90(self, medias)
    def comment_medias91(self, medias):
        return comment_medias91(self, medias)
    def comment_medias92(self, medias):
        return comment_medias92(self, medias)
    def comment_medias93(self, medias):
        return comment_medias93(self, medias)
    def comment_medias94(self, medias):
        return comment_medias94(self, medias)
    def comment_medias95(self, medias):
        return comment_medias95(self, medias)
    def comment_medias96(self, medias):
        return comment_medias96(self, medias)
    def comment_medias97(self, medias):
        return comment_medias97(self, medias)
    def comment_medias98(self, medias):
        return comment_medias98(self, medias)
    def comment_medias99(self, medias):
        return comment_medias99(self, medias)
    def comment_medias100(self, medias):
        return comment_medias100(self, medias)
    def comment_medias101(self, medias):
        return comment_medias101(self, medias)
    def comment_medias102(self, medias):
        return comment_medias102(self, medias)
    def comment_medias103(self, medias):
        return comment_medias103(self, medias)

    def comment_user(self, user_id, amount=None):
        return comment_user(self, user_id, amount)

    def comment_users(self, user_ids, ncomments=None):
        return comment_users(self, user_ids, ncomments)

    def comment_geotag(self, geotag):
        return comment_geotag(self, geotag)

    def is_commented(self, media_id):
        return is_commented(self, media_id)

    # block

    def block(self, user_id):
        return block(self, user_id)

    def unblock(self, user_id):
        return unblock(self, user_id)

    def block_users(self, user_ids):
        return block_users(self, user_ids)

    def unblock_users(self, user_ids):
        return unblock_users(self, user_ids)

    def block_bots(self):
        return block_bots(self)

    # filter

    def filter_medias(self, media_items, filtration=True, quiet=False, is_comment=False):
        return filter_medias(self, media_items, filtration, quiet, is_comment)

    def check_media(self, media):
        return check_media(self, media)

    def check_user(self, user, unfollowing=False):
        return check_user(self, user, unfollowing)

    def check_not_bot(self, user):
        return check_not_bot(self, user)

    # support

    def check_if_file_exists(self, file_path, quiet=False):
        return check_if_file_exists(file_path, quiet)

    def extract_urls(self, text):
        return extract_urls(text)

    def read_list_from_file(self, file_path):
        return read_list_from_file(file_path)

    def console_print(self, text, color=None):
        return console_print(self, text, color)

    # stats

    def save_user_stats(self, username, path=""):
        return save_user_stats(self, username, path=path)
