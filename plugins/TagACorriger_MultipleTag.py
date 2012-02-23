#-*- coding: utf-8 -*-

###########################################################################
##                                                                       ##
## Copyrights Frédéric Rodrigo 2011                                      ##
##                                                                       ##
## This program is free software: you can redistribute it and/or modify  ##
## it under the terms of the GNU General Public License as published by  ##
## the Free Software Foundation, either version 3 of the License, or     ##
## (at your option) any later version.                                   ##
##                                                                       ##
## This program is distributed in the hope that it will be useful,       ##
## but WITHOUT ANY WARRANTY; without even the implied warranty of        ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         ##
## GNU General Public License for more details.                          ##
##                                                                       ##
## You should have received a copy of the GNU General Public License     ##
## along with this program.  If not, see <http://www.gnu.org/licenses/>. ##
##                                                                       ##
###########################################################################

from plugins.Plugin import Plugin


class TagACorriger_MultipleTag(Plugin):

    def init(self, logger):
        Plugin.init(self, logger)
        self.errors[3034] = { "item": 3034, "desc": {"en": u"Watch multiple tags"} }

    def way(self, data, tags, nds):
        err = []
        if "highway" in tags and "fee" in tags:
            err.append((3034, 1, {"fr": u"Use tags \"toll\" in place of \"fee\""}))

        return err