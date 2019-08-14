# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from players.models import ATPPlayer
from matches.models import ATPMatch

class AtpPlayerScrapyPipeline(object):
    def process_item(self, item, spider):
        if 'atpplayer' not in getattr(spider, 'pipelines', []):
            return item
        try:
            player = ATPPlayer.objects.get(name=item["name"])
            print (player.name + " already exist")
            player.rank = item['rank']
            player.name = item['name']
            player.nicknames = item['nicknames']
            player.max_rank = item['max_rank']
            player.age = item['age']
            player.country = item['country']
            player.pts = item['pts']
            player.next_pts = item['next_pts']
            player.max_pts = item['max_pts']
            player.save()
            return item
        except ATPPlayer.DoesNotExist:
            pass
        item.save()
        return item

class AtpMatchScrapyPipeline(object):
    def process_item(self, item, spider):
        if 'atpmatch' not in getattr(spider, 'pipelines', []):
            return item
        try:
            match = ATPMatch.objects.get(home=item["home"], away=item['away'])
            print (match.home  + " already exist")
            match.rank = item['rank']
            match.round = item['round']
            match.date = item['date']
            match.home = item['home']
            match.away = item['away']
            match.location = item['location']
            match.tournament = item['tournament']
            match.winner = item['winner']
            match.loser = item['loser']
            match.status = item['status']
            match.comment = item['comment']
            match.home_r1 = item['home_r1']
            match.home_r2 = item['home_r2']
            match.home_r3 = item['home_r3']
            match.home_r4 = item['home_r4']
            match.home_r5 = item['home_r5']
            match.away_r1 = item['away_r1']
            match.away_r2 = item['away_r2']
            match.away_r3 = item['away_r3']
            match.away_r4 = item['away_r4']
            match.away_r5 = item['away_r5']
            match.home_winsets = item['home_winsets']
            match.home_winsets = item['home_winsets']
            match.save()
            return item
        except ATPMatch.DoesNotExist:
            pass
        item.save()
        return item
