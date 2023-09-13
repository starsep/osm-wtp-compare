import unittest

import httpx

from distance import geoDistance, GeoPoint
from logger import log_duration
from warsaw.wtpScraper import mapWtpStop, cachedParseWebsite, manualHtmlParsing


class OSMWTPCompareTests(unittest.TestCase):
    def test_mapWtpStop(self):
        self.assertEqual(mapWtpStop("100081", "Test 81"), ("100001", "Test 01"))


class GeoDistanceTests(unittest.TestCase):
    def test_geoDistance(self):
        self.assertAlmostEqual(
            geoDistance(
                GeoPoint(lat=52.137859, lon=21.234539),
                GeoPoint(lat=52.136611, lon=21.234386),
            ),
            139,
        )
        self.assertAlmostEqual(
            geoDistance(
                GeoPoint(lat=52.217726, lon=21.242986),
                GeoPoint(lat=52.198978, lon=21.168815),
            ),
            5482,
            delta=20,
        )


class ParseHTMLResultTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with httpx.Client() as client:
            cls.htmlContent = client.get(
                url="https://www.wtp.waw.pl/rozklady-jazdy/?wtp_md=3&wtp_ln=512&wtp_dr=A"
            ).text

    def test_m(self):
        # warmup
        for i in range(20):
            cachedParseWebsite(self.htmlContent, "", None)
        for i in range(20):
            manualHtmlParsing(self.htmlContent, "", None)

        with log_duration("bs4"):
            bs4Result = cachedParseWebsite(self.htmlContent, "", None)
        with log_duration("manual"):
            manualResult = manualHtmlParsing(self.htmlContent, "", None)
        self.assertEqual(bs4Result, manualResult)
