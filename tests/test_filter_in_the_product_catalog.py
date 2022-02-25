from pom.filter_in_catalog import ProductsFilters


def test_checking_the_filter_operation_by_price(web_browser):
    """Checks the prices of all filtered offers at a given price scope."""
    page = ProductsFilters(web_browser)
    min_cost = 2000
    max_cost = 3000

    page.underwear_tab.click()
    page.min_cost_input.send_keys(str(min_cost))
    page.max_cost_input.send_keys(str(max_cost))
    page.set_filter.scroll_to_element()
    page.set_filter.click()

    prices_of_all_offers = page.items_cost.get_text()
    prices = [int((price.replace(' ', '')).rstrip('₽')) for price in prices_of_all_offers]
    for price in prices:
        assert min_cost < price < max_cost


