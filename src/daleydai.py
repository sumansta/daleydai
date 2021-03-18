import re
import json
import requests
import pandas as pd


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}


pd.set_option("display.max.columns", None)
pd.set_option("display.max.rows", None)
pd.set_option("display.precision", 10)


def request_api(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(response)
        raise Exception("Bad Request !!")


def get_broker_id():
    inputId = input("Daley Dai ko ID kati?    ")
    isInputValid = re.match(r"^[0-9]{1,2}$", inputId)
    if isInputValid == None:
        print("ID milena")
        get_broker_id()
    else:
        fetch_broker_data(inputId)


def fetch_broker_data(BROKER_ID):

    MAIN_URL = f"https://newweb.nepalstock.com/api/nots/nepse-data/floorsheet?&size=500&buyerBroker={BROKER_ID}&sort=contractId,desc"
    dataFrames = pd.DataFrame()
    jsonResponse = request_api(MAIN_URL)
    summaryData = pd.json_normalize(jsonResponse["floorsheets"])
    totalPages = summaryData["totalPages"].values[0]
    nextPage = 0
    while nextPage <= totalPages:
        print(f"Fetching page {nextPage + 1}")
        PAGED_URL = f"https://newweb.nepalstock.com/api/nots/nepse-data/floorsheet?page={nextPage}&size=500&buyerBroker={BROKER_ID}&sort=contractId,desc"
        pagedResponse = request_api(PAGED_URL)
        pagedDf = pd.json_normalize(pagedResponse["floorsheets"]["content"])
        dataFrames = pd.concat([pagedDf, dataFrames], sort=False)
        nextPage += 1

    unsortedDf = dataFrames.groupby("stockSymbol").agg(
        totalKittas=pd.NamedAgg(column="contractQuantity", aggfunc="sum"),
        totalAmount=pd.NamedAgg(column="contractAmount", aggfunc="sum"),
        totalTransactions=pd.NamedAgg(column="stockSymbol", aggfunc="count"),
        maxPrice=pd.NamedAgg(column="contractRate", aggfunc="max"),
        minPrice=pd.NamedAgg(column="contractRate", aggfunc="min"),
    )

    sortedDf = unsortedDf.sort_values("totalKittas", ascending=False)
    print(sortedDf)


def main():
    get_broker_id()


main()
