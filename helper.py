from bs4 import BeautifulSoup
import requests

class Helper():

    def getProductByFormat(url, format):
        print("-- checking product status --")
        # variables
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        product_detail__variant_names = soup.find_all("div", {"class": "product-detail__variant-name"})


        for product_detail__variant_name in product_detail__variant_names:
            if (product_detail__variant_name is not None):
                if (product_detail__variant_name.text == format):
                    parent_product_name = product_detail__variant_name.find_parent("div", {"class": "product-detail__variant-row product-detail__variant-row--spread-content"})

                    child_product_detail_appfold = parent_product_name.find("div", {"class": "product-detail__variant-row--app-fold"})
                    child_stockstatus = child_product_detail_appfold.find("div", {"class": "variant-stock-status"})

                    span_status = child_stockstatus.find("span", {"class": "status_available_in_future"})
                    if (span_status is not None):
                        print(f"{format} isn't available yet :cry:" )
                        break
                    else:
                        print(f":warning: {format} AVAILABLE :warning: @everyone")
                        print(url)
                        break
                    
