from django.db import connection
from addressbase.management.base_command import BaseAddressBaseCommand
from addressbase.models import Blacklist


"""
Use AddressBase and ONSAD to create a list of
postcodes which contain UPRNs in >1 local authorities
"""
class Command(BaseAddressBaseCommand):

    def get_bad_postcodes(self):
        # get a list of postcodes containing UPRNs in >1 local authorities
        self.cursor.execute("""
            SELECT DISTINCT(postcode)
            FROM addressbase_address as AB
            JOIN addressbase_onsad ONSAD
            ON AB.uprn = ONSAD.uprn
            GROUP BY postcode
            HAVING COUNT(DISTINCT(LAD))>1;
        """)
        postcodes = self.cursor.fetchall()
        return [postcode[0] for postcode in postcodes]

    def get_councils(self, postcode):
        # get a list of local auths containing 1 or more UPRNs in postcode
        self.cursor.execute("""
            SELECT DISTINCT(LAD)
            FROM addressbase_address as AB
            JOIN addressbase_onsad ONSAD
            ON AB.uprn = ONSAD.uprn
            WHERE AB.postcode=%s;
        """, [postcode])
        councils = self.cursor.fetchall()
        return [council[0] for council in councils]

    def handle(self, *args, **kwargs):
        self.perform_checks()

        self.cursor = connection.cursor()
        print("clearing existing data..")
        self.cursor.execute("TRUNCATE TABLE addressbase_blacklist;")

        print("blacklisting postcodes..")
        postcodes = self.get_bad_postcodes()

        for postcode in postcodes:
            councils = self.get_councils(postcode)
            for council in councils:
                Blacklist.objects.create(postcode=postcode, lad=council)

        self.cursor.execute("""
            UPDATE addressbase_blacklist
            SET postcode=REPLACE(postcode, ' ', '')
        """)

        print("...done")