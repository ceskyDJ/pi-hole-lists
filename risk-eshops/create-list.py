import textwrap
from datetime import datetime, timezone

import regex as regex
import requests as requests
from lxml import etree


def is_domain_name(link: str) -> str:
    """
    Checks if the link is in domain name form

    :param link: Link to check
    :return: Is the link in domain name form (e.g. www.example.com)?
    """
    if 'regex' not in is_domain_name.__dict__:
        is_domain_name.regex = regex.compile(r'^[a-z0-9.\-]+$')

    search_domain_name_match = is_domain_name.regex.match(link)

    return search_domain_name_match is not None


def create_block_list() -> None:
    """Creates a block list from publicly available webpage of risk e-shops"""
    response = requests.get('https://www.coi.cz/pro-spotrebitele/rizikove-e-shopy/')
    parsed_html = etree.HTML(response.content)

    # Create block list (set of blocked domain names respectively)
    link_elements = parsed_html.xpath('//article[@class="information-row"]//p[@class="list_titles"]/span')
    domain_names = {link_element.text for link_element in link_elements if is_domain_name(link_element.text)}

    now = datetime.now(tz=timezone.utc)

    with open(f'out/risk-eshops.txt', 'w') as f:
        f.write(textwrap.dedent(f'''\
        # Title: Risk e-shops
        #
        # This is a block list for Pi-Hole created from a public list
        # of risk e-shops maintained by Czech Trade Inspection Authority
        # (CTIA or COI -- Ceska obchodni inspekce in Czech). This list
        # doesn't contain e-shops without own domain
        # (e.g. https://example.com/my-super-shop) due to possible false
        # positivity (there should be 100 valid e-shops on one domain
        # and 1 risk e-shop).
        #
        # Generated at: {now.strftime('%d %b %Y %H:%M:%S')} (UTC)
        # Number of unique domain names: {len(domain_names):,}
        #
        # Latest version of this file: https://pi-hole-lists.ceskydj.cz/risk-eshops
        # Project repository: https://github.com/ceskyDJ/pi-hole-lists
        # Source of domain names: https://www.coi.cz/pro-spotrebitele/rizikove-e-shopy/
        #
        # ===============================================================\n
        '''))
        f.writelines([f'0.0.0.0 {domain_name}\n' for domain_name in domain_names])


if __name__ == '__main__':
    create_block_list()
