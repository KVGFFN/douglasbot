from bs4 import BeautifulSoup
import requests

class Helper():

    def getProductByFormat(url, format):
        # variables
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        product_detail__variant_names = soup.find_all("div", {"class": "product-detail__variant-name"})


        for product_detail__variant_name in product_detail__variant_names:
            if (product_detail__variant_name is not None):
                print(product_detail__variant_name.text)
                if (product_detail__variant_name.text == format):
                    print(f'Found {format} in {url}')
                    parent_product_name = product_detail__variant_name.find_parent("div", {"class": "product-detail__variant-row product-detail__variant-row--spread-content"})

                    child_product_detail_appfold = parent_product_name.find("div", {"class": "product-detail__variant-row--app-fold"})
                    child_stockstatus = child_product_detail_appfold.find("div", {"class": "variant-stock-status"})

                    span_status = child_stockstatus.find("span", {"class": "status_available_in_future"})
                    if (span_status is not None):
                        print("NOT AVAILABLE")
                        print(span_status.text)
                        break
                    else:
                        print("Is available")
                        break
                    
