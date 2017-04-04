from data_collection.morph_importer import BaseMorphApiImporter

class Command(BaseMorphApiImporter):

    srid = 4326
    districts_srid  = 4326
    council_id = 'E07000114'
    elections = ['local.kent.2017-05-04']
    scraper_name = 'wdiv-scrapers/DC-PollingStations-Thanet'
    geom_type = 'geojson'

    def district_record_to_dict(self, record):
        poly = self.extract_geometry(record, self.geom_type, self.get_srid('districts'))
        return {
            'internal_council_id': record['Code'],
            'name': record['Name'] + ' - ' + record['Code'],
            'area': poly,
            'polling_station_id': record['Code'],
        }

    def station_record_to_dict(self, record):
        location = self.extract_geometry(record, self.geom_type, self.get_srid('stations'))
        return {
            'internal_council_id': record['DISTRICT'],
            'postcode': record['POSTCODE'],
            'address': record['ADDRESS'],
            'location': location,
        }
