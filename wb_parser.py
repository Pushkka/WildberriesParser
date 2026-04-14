import csv
import json
import requests

#Получить баскет для картинок и карточки.
def get_basket_host(vol):
    if vol <= 143:
        return "basket-01.wbbasket.ru"
    elif vol <= 287:
        return "basket-02.wbbasket.ru"
    elif vol <= 431:
        return "basket-03.wbbasket.ru"
    elif vol <= 719:
        return "basket-04.wbbasket.ru"
    elif vol <= 1007:
        return "basket-05.wbbasket.ru"
    elif vol <= 1061:
        return "basket-06.wbbasket.ru"
    elif vol <= 1115:
        return "basket-07.wbbasket.ru"
    elif vol <= 1169:
        return "basket-08.wbbasket.ru"
    elif vol <= 1313:
        return "basket-09.wbbasket.ru"
    elif vol <= 1601:
        return "basket-10.wbbasket.ru"
    elif vol <= 1655:
        return "basket-11.wbbasket.ru"
    elif vol <= 1919:
        return "basket-12.wbbasket.ru"
    elif vol <= 2045:
        return "basket-13.wbbasket.ru"
    elif vol <= 2189:
        return "basket-14.wbbasket.ru"
    elif vol <= 2405:
        return "basket-15.wbbasket.ru"
    elif vol <= 2621:
        return "basket-16.wbbasket.ru"
    elif vol <= 2837:
        return "basket-17.wbbasket.ru"
    elif vol <= 3053:
        return "basket-18.wbbasket.ru"
    elif vol <= 3269:
        return "basket-19.wbbasket.ru"
    elif vol <= 3485:
        return "basket-20.wbbasket.ru"
    elif vol <= 3701:
        return "basket-21.wbbasket.ru"
    elif vol <= 3917:
        return "basket-22.wbbasket.ru"
    elif vol <= 4133:
        return "basket-23.wbbasket.ru"
    elif vol <= 4349:
        return "basket-24.wbbasket.ru"
    elif vol <= 4565:
        return "basket-25.wbbasket.ru"
    elif vol <= 4877:
        return "basket-26.wbbasket.ru"
    elif vol <= 5189:
        return "basket-27.wbbasket.ru"
    elif vol <= 5501:
        return "basket-28.wbbasket.ru"
    elif vol <= 5813:
        return "basket-29.wbbasket.ru"
    elif vol <= 6125:
        return "basket-30.wbbasket.ru"
    elif vol <= 6437:
        return "basket-31.wbbasket.ru"
    elif vol <= 6749:
        return "basket-32.wbbasket.ru"
    elif vol <= 7061:
        return "basket-33.wbbasket.ru"
    elif vol <= 7373:
        return "basket-34.wbbasket.ru"
    elif vol <= 7685:
        return "basket-35.wbbasket.ru"
    elif vol <= 7997:
        return "basket-36.wbbasket.ru"
    elif vol <= 8309:
        return "basket-37.wbbasket.ru"
    elif vol <= 8741:
        return "basket-38.wbbasket.ru"
    elif vol <= 9173:
        return "basket-39.wbbasket.ru"
    elif vol <= 9605:
        return "basket-40.wbbasket.ru"
    elif vol <= 10373:
        return "basket-41.wbbasket.ru"
    elif vol <= 11141:
        return "basket-42.wbbasket.ru"
    elif vol <= 11909:
        return "basket-43.wbbasket.ru"
    elif vol <= 12677:
        return "basket-44.wbbasket.ru"
    elif vol <= 13445:
        return "basket-45.wbbasket.ru"
    elif vol <= 14213:
        return "basket-46.wbbasket.ru"
    else:
        return "basket-01.wbbasket.ru"


def get_card_url(product_id):
    vol = product_id // 100000
    part = product_id // 1000
    host = get_basket_host(vol)
    return f"https://{host}/vol{vol}/part{part}/{product_id}/info/ru/card.json"


def get_image_urls(product_id, pics_count):
    vol = product_id // 10000
    part = product_id // 1000
    host = get_basket_host(vol)
    urls = []
    for i in range(1, pics_count + 1):
        urls.append(
            f"https://{host}/vol{vol}/part{part}/{product_id}/images/big/{i}.webp"
        )
    return urls


class WildberriesParser:
    BASE_URL = (
        "https://www.wildberries.ru/__internal/u-search/exactmatch/ru/common/v18/search"
    )

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "x-wbaas-token": "1.1000.b54048e79aff4d4cbf496b11c27554d4.MHwxNzguNzAuODYuOTZ8TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzE0NS4wLjAuMCBTYWZhcmkvNTM3LjM2IE9QUi8xMjkuMC4wLjB8MTc3NzM2NDc4NHxyZXVzYWJsZXwyfGV5Sm9ZWE5vSWpvaUluMD18MHwzfDE3NzY3NTk5ODR8MQ==.MEQCICpaqgvgPNWILrtj5fJmAQ72rhVcFH75w58wgAFMsuFZAiAuUzo4e8BZ708xn1fl0AkIEROV1NQa5d5USekdcdFfPA==",
            }
        )

    # Получение списка товаров.
    def search(self, query, page=1, limit=100):
        params = {
            "curr": "rub",
            "dest": "-1185367",
            "hide_dtype": 9,
            "limit": limit,
            "page": page,
            "hide_vflags": 4294967296,
            "inheritFilters": False,
            "lang": "ru",
            "query": query,
            "resultset": "catalog",
            "sort": "popular",
            "spp": 30,
        }

        response = self.session.get(self.BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        products = data.get("products", [])
        return products

    # Получение описания и характеристик.
    def fetch_card_data(self, product_id):
        url = get_card_url(product_id)

        response = self.session.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    # Партинг характеристик.
    @staticmethod
    def parse_options(options):
        if not options:
            return ""
        parts = []
        for opt in options:
            name = opt.get("name", "")
            value = opt.get("value", "")
            if name and value:
                parts.append(f"{name}: {value}")
        return "; ".join(parts)

    #Парсинг карточки товара.
    def parse_product(self, product):
        nm_id = product.get("id", "")
        supplier_id = product.get("supplierId", "")
        pics = product.get("pics", 0)

        sizes = product.get("sizes", [])
        size_names = "; ".join([str(s.get("name", "")) for s in sizes])

        price = 0
        if sizes:
            price = sizes[0].get("price", {}).get("product", 0) / 100

        image_urls = "; ".join(get_image_urls(nm_id, pics)) if pics > 0 else ""

        description = ""
        options = ""

        card_data = self.fetch_card_data(nm_id)
        if card_data:
            description = card_data.get("description", "").replace("\n", " ")
            options = self.parse_options(card_data.get("options", []))

        return {
            "product_link": f"https://www.wildberries.ru/catalog/{nm_id}/detail.aspx",
            "article": nm_id,
            "name": product.get("name", ""),
            "price": price,
            "description": description,
            "options": options,
            "image_urls": image_urls,
            "seller_name": product.get("supplier", ""),
            "seller_link": f"https://www.wildberries.ru/seller/{supplier_id}",
            "sizes": size_names,
            "stock": product.get("totalQuantity", 0),
            "rating": product.get("rating", 0),
            "feedbacks": product.get("feedbacks", 0),
        }

    #Заголовки для перевода.
    HEADERS_RU = {
        "product_link": "Ссылка на товар",
        "article": "Артикул",
        "name": "Название",
        "price": "Цена",
        "description": "Описание",
        "options": "Характеристики",
        "image_urls": "Ссылки на изображения",
        "seller_name": "Название селлера",
        "seller_link": "Ссылка на селлера",
        "sizes": "Размеры",
        "stock": "Остатки",
        "rating": "Рейтинг",
        "feedbacks": "Количество отзывов",
    }

    @staticmethod
    def save_to_csv(products, filename="products.csv"):
        if not products:
            return

        fieldnames = list(WildberriesParser.HEADERS_RU.keys())
        headers_ru = list(WildberriesParser.HEADERS_RU.values())

        with open(filename, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(headers_ru)
            for product in products:
                writer.writerow([product.get(field, "") for field in fieldnames])

        print(f"Сохранено {len(products)} продуктов в {filename}")

    @staticmethod
    def save_filtered_csv(products, filename="filtered_products.csv"):
        filtered = []
        for p in products:
            if (
                p["rating"] >= 4.5
                and p["price"] <= 10000
                and "Россия" in p["characteristics"]
            ):
                filtered.append(p)

        if not filtered:
            print(f"Нет продуктов, соответствующих фильтру")
            return

        fieldnames = list(WildberriesParser.HEADERS_RU.keys())
        headers_ru = list(WildberriesParser.HEADERS_RU.values())

        with open(filename, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(headers_ru)
            for product in filtered:
                writer.writerow([product.get(field, "") for field in fieldnames])

        print(f"Сохранено {len(filtered)} отфильтрованных продуктов в {filename}")


def main():
    parser = WildberriesParser()

    query = input("Введите запрос: ").strip()
    if not query:
        query = "пальто из натуральной шерсти"

    print(f"\nПоиск по запросу '{query}'...\n")

    products = parser.search(query, page=1, limit=100)
    if not products:
        print("Ничего не найдено.")
        return

    parsed = []
    for i, product in enumerate(products):
        print(f"Обработка {i + 1}/{len(products)}...")
        parsed.append(parser.parse_product(product))

    parser.save_to_csv(parsed)
    parser.save_filtered_csv(parsed)

    print(f"\nНайдено {len(parsed)} продуктов.")


if __name__ == "__main__":
    main()
