#!/usr/bin/env python2
# -*- coding: utf8 -*-

class TaeminCafe(object):
    def __init__(self, taemin):
        self.taemin = taemin

    def on_pubmsg(self, serv, canal, message, key, value, **kwargs):
        if key not in ("all", "cafe"):
            return

        msg = " ".join(self.taemin.channels[canal].users())
        if key == "cafe":
            msg = "<<< CAFE !!! \\o/ %s \\o/ !!! CAFE >>>" % msg
        else:
            msg = "%s %s" % (msg, value)

        serv.privmsg(canal, msg)

