from django.contrib.gis.db import models
from django.db import connection
from uk_geo_utils.models import (
    AbstractAddress,
    AbstractAddressManager,
    AbstractOnsudManager,
)


class AddressManager(AbstractAddressManager):
    def postcodes_for_district(self, district):
        qs = self.filter(location__within=district.area)
        qs = qs.values_list("postcode", flat=True).distinct()
        return list(qs)

    def points_for_postcode(self, postcode):
        qs = self.filter(postcode=postcode)
        qs = qs.values_list("location", flat=True)
        return list(qs)


class Address(AbstractAddress):
    objects = AddressManager()


class UprnToCouncil(models.Model):
    class Meta:
        indexes = [
            models.Index(
                fields=[
                    "lad",
                ],
                name="lookup_lad_idx",
            )
        ]

    objects = AbstractOnsudManager()
    lad = models.CharField(blank=True, max_length=9)
    uprn = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        primary_key=True,
        max_length=12,
        db_column="uprn",
    )
    polling_station_id = models.CharField(blank=True, max_length=255)


def get_uprn_hash_table(council_id):
    # get all the UPRNs in target local auth
    # NB we miss ~25 over the country because lighthouses etc.
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT
            a.uprn,
            a.address,
            REPLACE(a.postcode, ' ', ''),
            a.location
        FROM addressbase_address a
        JOIN addressbase_uprntocouncil u ON a.uprn=u.uprn
        WHERE u.lad=%s;
        """,
        [council_id],
    )
    # return result a hash table keyed by UPRN
    return {
        row[0]: {"address": row[1], "postcode": row[2], "location": row[3]}
        for row in cursor.fetchall()
    }
