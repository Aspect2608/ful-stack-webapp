import sqlite3 , config
import alpaca_trade_api as tradeapi

def p_stocks():

    connection = sqlite3.connect(config.DB_FILE)
    connection.row_factory=sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT symbol, company FROM stock
    """)
    rows= cursor.fetchall()
    symbols=[row['symbol'] for row in rows]

    api = tradeapi.REST(config.API_KEY, config.SECRET_KEY, base_url=config.API_URL)
    assets = api.list_assets()

    for asset in assets:
        try:
            if asset.status == 'active' and asset.tradable and asset.symbol  not in symbols:
                print(f"Added a new stock{asset.symbol} {asset.name}")
                cursor.execute("INSERT INTO stock (symbol, company, exchange) VALUES (?, ?, ?)", (asset.symbol, asset.name, asset.exchange))
        except Exception as e:
            print(asset.symbol)
            print(e)

    connection.commit()

    cursor.execute("""
        delete from stock where id>10000
    """)

    connection.commit()