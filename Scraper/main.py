
from src import Collector
import optparse

def parse_arguments():  
    parser = optparse.OptionParser()

    parser.add_option('-p', '--province',
        action="store", dest="province",
        help="province to scrape numbered 0 to 10 ", default=0)
    options, args = parser.parse_args()

    province_index = int(options.province)
    return province_index


if __name__ == "__main__":
    province_index = parse_arguments()
    Collector().start(province_index)
