from django.core.management.base import NoArgsCommand, CommandError
from django.db import connection
from app.models import Album, Band, Review
from django.db.models import Count, Avg
import decimal
from decimal import Decimal, ROUND_HALF_DOWN

class Command(NoArgsCommand):
           
    def handle_noargs(self, **options):
        
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(1)/COUNT(DISTINCT `album_id`) as `v` FROM `app_review`")
        avg_num_votes = decimal.Decimal(cursor.fetchone()[0])
        cursor.execute("SELECT SUM(`score`)/COUNT(1) as `v` FROM `app_review`")
        avg_rating = decimal.Decimal(cursor.fetchone()[0])
        magic = avg_num_votes * avg_rating
        for album in Album.objects.all().annotate(i_reviews=Count('review'), i_score=Avg('review__score')):
            print album.name
            if album.i_reviews > 0:
                score = ((avg_num_votes*avg_rating) + decimal.Decimal((album.i_reviews * album.i_score)))/(avg_num_votes + decimal.Decimal(album.i_reviews))
                score = decimal.Decimal(str(score)).quantize(decimal.Decimal('.001'), rounding=ROUND_HALF_DOWN)
                print score
                album.score = score
                album.save()
        
        return