"""
    Bot functions to generate and post a comments.

    Instructions to file with comments:
        one line - one comment.

    Example:
        lol
        kek

"""
from tqdm import tqdm


def comment(self, media_id, comment_text):
    if self.is_commented(media_id):
        return True
    if not self.reached_limit('comments'):
        if self.blocked_actions['comments']:
            self.logger.warning('YOUR `COMMENT` ACTION IS BLOCKED')
            if self.blocked_actions_protection:
                from datetime import timedelta
                next_reset = (self.start_time.date() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
                self.logger.warning('blocked_actions_protection ACTIVE. Skipping `comment` action till, at least, {}.'.format(next_reset))
                return False
        self.delay('comment')
        _r = self.api.comment(media_id, comment_text)
        if _r == 'feedback_required':
            self.logger.error("`Comment` action has been BLOCKED...!!!")
            return False
        if _r:
            self.total['comments'] += 1
            return True
    else:
        self.logger.info("Out of comments for today.")
    return False


def reply_to_comment(self, media_id, comment_text, parent_comment_id):
    if not self.is_commented(media_id):
        self.logger.info("Media is not commented yet, nothing to answer to...")
        return False
    if not self.reached_limit('comments'):
        if self.blocked_actions['comments']:
            self.logger.warning('YOUR `COMMENT` ACTION IS BLOCKED')
            if self.blocked_actions_protection:
                self.logger.warning('blocked_actions_protection ACTIVE. Skipping `comment` action.')
                return False
        self.delay('comment')
        if comment_text[0] != '@':
            self.logger.error("A reply must start with mention, so '@' must be the 1st char, followed by the username you're replying to")
            return False
        if comment_text.split(' ')[0][1:] == self.get_username_from_user_id(self.user_id):
            self.logger.error("You can't reply to yourself")
            return False
        _r = self.api.reply_to_comment(media_id, comment_text, parent_comment_id)
        if _r == 'feedback_required':
            self.logger.error("`Comment` action has been BLOCKED...!!!")
            return False
        if _r:
            self.logger.info('Replied to comment {} of media {}'.format(parent_comment_id, media_id))
            self.total['comments'] += 1
            return True
    else:
        self.logger.info("Out of comments for today.")
    return False


def comment_medias(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.check_media(media):
            continue									   
        if not self.is_commented(media):
            text = self.get_comment()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias1(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.check_media(media):
            continue
        if not self.is_commented(media):
            text = self.get_comment1()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias2(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.check_media(media):
            continue
        if not self.is_commented(media):
            text = self.get_comment2()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias3(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.check_media(media):
            continue
        if not self.is_commented(media):
            text = self.get_comment3()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias4(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.check_media(media):
            continue
        if not self.is_commented(media):
            text = self.get_comment4()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias5(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.check_media(media):
            continue
        if not self.is_commented(media):
            text = self.get_comment5()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias6(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.check_media(media):
            continue
        if not self.is_commented(media):
            text = self.get_comment6()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias7(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.check_media(media):
            continue
        if not self.is_commented(media):
            text = self.get_comment7()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias8(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.check_media(media):
            continue
        if not self.is_commented(media):
            text = self.get_comment8()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias9(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment9()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias10(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment10()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias11(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment11()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias12(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment12()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias13(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment13()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias14(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment14()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias15(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment15()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias16(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment16()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias17(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment17()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias18(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment18()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias19(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment19()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias20(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment20()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias21(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment21()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias22(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment22()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias23(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment23()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias24(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment24()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias25(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment25()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias26(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment26()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias27(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment27()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias28(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment28()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias29(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment29()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias30(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment30()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias31(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment31()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias32(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment32()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias33(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment33()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias34(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment34()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias35(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment35()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias36(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment36()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias37(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment37()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias38(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment38()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias39(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment39()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias40(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment40()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias41(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment41()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias42(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment42()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias43(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment43()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias44(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment44()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias45(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment45()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias46(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment46()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias47(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment47()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias48(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment48()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias49(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment49()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias50(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment50()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias51(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment51()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias52(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment52()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias53(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment53()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias54(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment54()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias55(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment55()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias56(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment56()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias57(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment57()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias58(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment58()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias59(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment59()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias60(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment60()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias61(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment61()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias62(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment62()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias63(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment63()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias64(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment64()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias65(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment65()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias66(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment66()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias67(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment67()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias68(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment68()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias69(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment69()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias70(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment70()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias71(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment71()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias72(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment72()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias73(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment73()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias74(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment74()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias75(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment75()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias76(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment76()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias77(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment77()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias78(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment78()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias79(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment79()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias80(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment80()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias81(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment81()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias82(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment82()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias83(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment83()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias84(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment84()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias85(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment85()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias86(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment86()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias87(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment87()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias88(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment88()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias89(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment89()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias90(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment90()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias91(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment91()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias92(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment92()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias93(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment93()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias94(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment94()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias95(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment95()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias96(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment96()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias97(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment97()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias98(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment98()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias99(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment99()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias100(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment100()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias101(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment101()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias102(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment102()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items
def comment_medias103(self, medias):
    broken_items = []
    self.logger.info("Going to comment %d medias." % (len(medias)))
    for media in tqdm(medias):
        if not self.is_commented(media):
            text = self.get_comment103()
            self.logger.info("Commented with text: %s" % text)
            if not self.comment(media, text):
                self.delay('comment')
                broken_items = medias[medias.index(media):]
                break
    self.logger.info("DONE: Total commented on %d medias. " %
                     self.total['comments'])
    return broken_items


def comment_hashtag(self, hashtag, amount=None):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount)
    return self.comment_medias(medias)

def comment_hashtag1(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias1(medias)
def comment_hashtag2(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias2(medias)
def comment_hashtag3(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias3(medias)
def comment_hashtag4(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias4(medias)
def comment_hashtag5(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias5(medias)
def comment_hashtag6(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias6(medias)
def comment_hashtag7(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias7(medias)
def comment_hashtag8(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias8(medias)
def comment_hashtag9(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias9(medias)
def comment_hashtag10(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias10(medias)
def comment_hashtag11(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias11(medias)
def comment_hashtag12(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias12(medias)
def comment_hashtag13(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias13(medias)
def comment_hashtag14(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias14(medias)
def comment_hashtag15(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias15(medias)
def comment_hashtag16(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias16(medias)
def comment_hashtag17(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias17(medias)
def comment_hashtag18(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias18(medias)
def comment_hashtag19(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias19(medias)
def comment_hashtag20(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias20(medias)
def comment_hashtag21(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias21(medias)
def comment_hashtag22(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias22(medias)
def comment_hashtag23(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias23(medias)
def comment_hashtag24(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias24(medias)
def comment_hashtag25(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias25(medias)
def comment_hashtag26(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias26(medias)
def comment_hashtag27(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias27(medias)
def comment_hashtag28(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias28(medias)
def comment_hashtag29(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias29(medias)
def comment_hashtag30(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias30(medias)
def comment_hashtag31(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias31(medias)
def comment_hashtag32(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias32(medias)
def comment_hashtag33(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias33(medias)
def comment_hashtag34(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias34(medias)
def comment_hashtag35(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias35(medias)
def comment_hashtag36(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias36(medias)
def comment_hashtag37(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias37(medias)
def comment_hashtag38(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias38(medias)
def comment_hashtag39(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias39(medias)
def comment_hashtag40(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias40(medias)
def comment_hashtag41(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias41(medias)
def comment_hashtag42(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias42(medias)
def comment_hashtag43(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias43(medias)
def comment_hashtag44(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias44(medias)
def comment_hashtag45(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias45(medias)
def comment_hashtag46(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias46(medias)
def comment_hashtag47(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias47(medias)
def comment_hashtag48(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias48(medias)
def comment_hashtag49(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias49(medias)
def comment_hashtag50(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias50(medias)
def comment_hashtag51(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias51(medias)
def comment_hashtag52(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias52(medias)
def comment_hashtag53(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias53(medias)
def comment_hashtag54(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias54(medias)
def comment_hashtag55(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias55(medias)
def comment_hashtag56(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias56(medias)
def comment_hashtag57(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias57(medias)
def comment_hashtag58(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias58(medias)
def comment_hashtag59(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias59(medias)
def comment_hashtag60(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias60(medias)
def comment_hashtag61(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias61(medias)
def comment_hashtag62(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias62(medias)
def comment_hashtag63(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias63(medias)
def comment_hashtag64(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias64(medias)
def comment_hashtag65(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias65(medias)
def comment_hashtag66(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias66(medias)
def comment_hashtag67(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias67(medias)
def comment_hashtag68(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias68(medias)
def comment_hashtag69(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias69(medias)
def comment_hashtag70(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias70(medias)
def comment_hashtag71(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias71(medias)
def comment_hashtag72(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias72(medias)
def comment_hashtag73(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias73(medias)
def comment_hashtag74(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias74(medias)
def comment_hashtag75(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias75(medias)
def comment_hashtag76(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias76(medias)
def comment_hashtag77(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias77(medias)
def comment_hashtag78(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias78(medias)
def comment_hashtag79(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias79(medias)
def comment_hashtag80(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias80(medias)
def comment_hashtag81(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias81(medias)
def comment_hashtag82(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias82(medias)
def comment_hashtag83(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias83(medias)
def comment_hashtag84(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias84(medias)
def comment_hashtag85(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias85(medias)
def comment_hashtag86(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias86(medias)
def comment_hashtag87(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias87(medias)
def comment_hashtag88(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias88(medias)
def comment_hashtag89(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias89(medias)
def comment_hashtag90(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias90(medias)
def comment_hashtag91(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias91(medias)
def comment_hashtag92(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias92(medias)
def comment_hashtag93(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias93(medias)
def comment_hashtag94(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias94(medias)
def comment_hashtag95(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias95(medias)
def comment_hashtag96(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias96(medias)
def comment_hashtag97(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias97(medias)
def comment_hashtag98(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias98(medias)
def comment_hashtag99(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias99(medias)
def comment_hashtag100(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias100(medias)
def comment_hashtag101(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias101(medias)
def comment_hashtag102(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias102(medias)
def comment_hashtag103(self, hashtag, amount=1):
    self.logger.info("Going to comment medias by %s hashtag" % hashtag)
    medias = self.get_total_hashtag_medias(hashtag, amount=1)
    return self.comment_medias103(medias)



def comment_user(self, user_id, amount=None):
    """ Comments last user_id's medias """
    if not self.check_user(user_id):
        return False
    self.logger.info("Going to comment user_%s's feed:" % user_id)
    user_id = self.convert_to_user_id(user_id)
    medias = self.get_user_medias(user_id, is_comment=True)
    if not medias:
        self.logger.info(
            "None medias received: account is closed or medias have been filtered.")
        return False
    return self.comment_medias(medias[:amount])


def comment_users(self, user_ids, ncomments=None):
    for user_id in user_ids:
        if self.reached_limit('comments'):
            self.logger.info("Out of comments for today.")
            return
        self.comment_user(user_id, amount=ncomments)


def comment_geotag(self, geotag):
    # TODO: comment every media from geotag
    pass


def is_commented(self, media_id):
    return self.user_id in self.get_media_commenters(media_id)
