class DataViews:
    """ This class is for give format to data coming from DB"""

    def data_flats(self, flats):
        list_of_flats = []
        for info in flats:
            fat_dict = {
                "address": info[1],
                "latitude": info[2],
                "longitude": info[3],
                "cp": info[4],
                "city": info[5],
                "year_const": info[6],
                "total_price": info[7],
                "total_area": info[8],
                "price_m2": info[9],
                "elevator": info[10],
                "valuation_date": info[11],
                "year_renovation": info[12],
                "img_url": info[13]
            }
            list_of_flats.append(fat_dict)

        return list_of_flats
