import create_db,drop_db,populate_stocks,populate_prices

def setStage(isCreated):
    if isCreated:
        drop_db.delete_db()
        create_db.make_db()
        populate_stocks.p_stocks()
        populate_prices.p_prices()

    else:
        print("everything is already set")

    return 

setStage(True)