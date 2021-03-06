from data_importers.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "E07000076"
    addresses_name = (
        "parl.2019-12-12/Version 1/Democracy_Club__12December2019tendring.tsv"
    )
    stations_name = (
        "parl.2019-12-12/Version 1/Democracy_Club__12December2019tendring.tsv"
    )
    elections = ["parl.2019-12-12"]
    csv_delimiter = "\t"
    allow_station_point_from_postcode = False

    def address_record_to_dict(self, record):
        rec = super().address_record_to_dict(record)
        uprn = record.property_urn.strip().lstrip("0")

        if uprn in [
            "10007931054",
            "10007941736",
            "100091273215",
            "100091463517",
        ]:
            return None

        if uprn == "10007936637":
            rec["postcode"] = "CO15 1TT"

        if uprn in [
            "10007940599",  # CO168TA -> CO148TA : 106 Kirby Road, Walton-on-the-Naze, Essex
            "10007941701",  # CO169DT -> CO169BX : The Annexe, 5 Bentley Road, Weeley, Clacton-on-Sea, Essex
            "10007944266",  # CO151PT -> CO151QA : Flat 1 Moon and Starfish, 1 Marine Parade East, Clacton-on-Sea, Essex
            "10007944355",  # CO151PT -> CO151QA : Flat 2 Moon and Starfish, 1 Marine Parade East, Clacton-on-Sea, Essex
            "100090634962",  # CO123PJ -> CO123PF : 302A Main Road, Harwich, Essex
            "100090635741",  # CO154LJ -> CO123UB : 11 Nightingale Way, Clacton-on-Sea, Essex
            "100091272552",  # CO130AG -> CO130DT : 30 Walton Road, Frinton-on-Sea, Essex
            "100091460461",  # CO112UJ -> CO112TA : Spinnels Farm, Spinnels Lane, Wix, Manningtree, Essex
            "100091462057",  # CO130PA -> CO130PB : Melrose, Frinton Road, Kirby Cross, Frinton-on-Sea, Essex
            "100091463517",  # CO168ET -> CO151UG : 2 Beach Road, Lee-Over-Sands, Clacton-on-Sea, Essex
            "100091464541",  # CO153AZ -> CO153AT : 135, Old Road, Clacton-on-Sea, Essex
            "10024056898",  # CO78RF -> CO78RE : 2 The Saltings, Bentley Country Park, Flag Hill, Great Bentley, Colchester, Essex
            "10024056899",  # CO78RF -> CO78RE : 9 The Saltings, Bentley Country Park, Flag Hill, Great Bentley, Colchester, Essex
            "10024056900",  # CO78RF -> CO78RE : 15 The Saltings, Bentley Country Park, Flag Hill, Great Bentley, Colchester, Essex
            "10024056901",  # CO78RF -> CO78RE : 19 The Saltings, Bentley Country Park, Flag Hill, Great Bentley, Colchester, Essex
            "10024056902",  # CO78RF -> CO78RE : 10 Riverside, Bentley Country Park, Flag Hill, Great Bentley, Colchester, Essex
            "10024056903",  # CO78RF -> CO78RE : 24 Riverside, Bentley Country Park, Flag Hill, Great Bentley, Colchester, Essex
            "10024059148",  # CO78RF -> CO78RE : 17 Riverside, Bentley Country Park, Flag Hill, Great Bentley, Colchester, Essex
            "10024059227",  # CO78RF -> CO78RE : 7 Kingfisher Lake, Bentley Country Park, Flag Hill, Great Bentley, Colchester, Essex
            "10024059229",  # CO78RF -> CO78RE : 4 The Saltings, Bentley Country Park, Flag Hill, Great Bentley, Colchester, Essex
            "10024060309",  # CO78RF -> CO78RE : 1 Kingfisher Lake, Bentley Country Park, Flag Hill, Great Bentley, Colchester, Essex
            "10024060310",  # CO78RF -> CO78RE : 2 Kingfisher Lake, Bentley Country Park, Flag Hill, Great Bentley, Colchester, Essex
            "10024060311",  # CO78RF -> CO78RE : 15 Kingfisher Lake, Bentley Country Park, Flag Hill, Great Bentley, Colchester, Essex
            "10024060312",  # CO78RF -> CO78RE : 21 The Saltings, Bentley Country Park, Flag Hill, Great Bentley, Colchester, Essex
            "10024060345",  # CO78RF -> CO78RE : 19 Riverside, Bentley Country Park, Flag Hill, Great Bentley, Colchester, Essex
            "10024060445",  # CO78RF -> CO78RE : 7 Whitebeam, Bentley Country Park, Flag Hill, Great Bentley, Colchester, Essex
            "10090655999",  # CO78RF -> CO78RE : 1 Whitebeam, Bentley Country Park, Flag Hill, Great Bentley, Colchester, Essex
            "10090657509",  # CO78RF -> CO78RE : 21 Riverside, Bentley Country Park, Flag Hill, Great Bentley, Colchester, Essex
            "10090657800",  # CO78RF -> CO78RE : 3 Kingfisher Lake, Bentley Country Park, Flag Hill, Great Bentley, Colchester, Essex
            "10094246358",  # CO168SG -> CO168TA : 422 Seawick Holiday Park, Beach Road, St Osyth, Clacton-on-Sea, Essex
            "10094246534",  # CO156LY -> CO154BE : 406 Valley Farm Holiday Park, Valley Road, Clacton-on-Sea, Essex
            "200001487728",  # CO77DW -> CO77DJ : Brendon, Colchester Road, Frating, Colchester, Essex
            "10090659423",  # CO78RF -> CO78RE : 4 Lakelands, Bentley Country Park, Flag Hill, Great Bentley, Colchester, Essex
            "10090658018",  # CO78RF -> CO78RE : 9 Whitebeam, Bentley Country Park, Flag Hill, Great Bentley, Colchester, Essex
            "10090656284",  # CO78RF -> CO78RE : 11 Lake View, Bentley County Park, Flag Hill, Great Bentley, Colchester, Essex
            "100091271615",  # CO77NB -> CO78NB : Shangrila, Weeley Road, Aingers Green, Great Bentley, Colchester, Essex
            "10007931091",  # CO154BS -> CO154BT : 72A St Johns Road, Clacton-on-Sea, Essex
            "100090599546",  # CO156QE -> CO156QF : The Carnarvon Nursing Home, 22-24 Carnarvon Road, Clacton-on-Sea, Essex
            "100090613536",  # CO168JL -> CO168NW : 262 Point Clear Road, St Osyth, Clacton-on-Sea, Essex
            "10007941693",  # CO168JL -> CO168NW : The Annexe, 262 Point Clear Road, St Osyth, Clacton-on-Sea, Essex
        ]:
            rec["accept_suggestion"] = True

        if uprn in [
            "100091463343",  # CO123LD -> CO151PP : 18 Orwell Road, Harwich, Essex
            "100090623245",  # CO70AG -> CO111AH : 25A High Street, Brightlingsea, Colchester, Essex
        ]:
            rec["accept_suggestion"] = False

        return rec
