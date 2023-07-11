#import des bibliothèques nécessaires pour le module finance yahoo, le module horaire et les tables avec pandas
import yfinance as yf
import time
import pandas as pd

#definition du stock
def get_stock_price(stock):
    ticker = yf.Ticker(stock)
    if 'regularMarketPreviousClose' in ticker.info:
        return ticker.info['regularMarketPreviousClose']
    else:
        return None
def print_stock_prices():
    stocks = ['TTE.PA', 'SAN.PA', 'ORA.PA', 'ENGI.PA', 'VIE.PA', 'DG.PA', 'OR.PA', 'AI.PA', 'BN.PA', 'EN.PA', 'EL.PA', 'SW.PA', 'GLE.PA', 'CS.PA', 'BNP.PA', 'VIV.PA', 'ACA.PA', 'SU.PA', 'RNO.PA']
    owned_stocks = {'ORA.PA': 2, 'ENGI.PA': 1, 'TTE.PA': 1}  # Ajoutez ici vos actions possédées
    data = []
    for stock in stocks:
        ticker = yf.Ticker(stock)
        history = ticker.history(period="1we")
        month_low = history['Low'].min()
        month_avg = history['Close'].mean()
        month_mid = history['Close'].mean()
        current_price = get_stock_price(stock)
        trend = 'haussière' if current_price > month_avg else 'baissière'
        owned = owned_stocks.get(stock, 0)  # Obtenez le nombre d'actions possédées, 0 si non possédées
        buy_sell_signal = 'vente' if current_price > month_avg else 'achat'
        data.append([ticker.info["longName"] if "longName" in ticker.info else stock, current_price, month_mid, current_price - month_low, trend, owned, buy_sell_signal])
    df = pd.DataFrame(data, columns=["Nom", "Prix actuel", "Prix moyen du mois", "+ bas du mois", "Tendance", "Actions possédées", "Tendance d'achat"])
  #definition du code js retranscrit dans le fichier actions.html
    js ="""
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.22/js/jquery.dataTables.min.js"></script>
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.22/css/jquery.dataTables.min.css">
    <script>
    $(document).ready(function() {
        $('#monTableauId').DataTable({
        "pageLength": 100,
        "createdRow": function( row, data, dataIndex ){
            }
        });
    });
    </script>
    """
  #idem pour le css
    css = """
    <style>
        .monTableau {
            border-collapse: collapse;
            width: 100%;
        }
        .monTableau td, .monTableau th {
            border: 1px solid #ddd;
            padding: 8px;
        }
        .monTableau tr:nth-child(even){background-color: #f2f2f2;}
        .monTableau th {
            padding-top: 12px;
            padding-bottom: 12px;
            text-align: left;
            background-color: #4CAF50;
            color: white;
        }
        .achat {
        background-color: green;
        color: white;
        }

        .vente {
        background-color: red;
        color: white;
        }
    </style>
    """
    js_correction = """
    <script>
    $(document).ready(function() {
        $("td:contains('achat')").addClass("achat");
        $("td:contains('vente')").addClass("vente");
    });
    </script>
    """
  #rappel de df dans une variable html pour pouvoir l'ecrire dans actions.html
    html = df.to_html(classes='monTableau', table_id='monTableauId')
    with open('actions.html', 'w') as f:
        f.write('<title>Portefeuille d\'actions</title>')
        f.write(js)
        f.write(css)
        f.write(html) 
        f.write(js_correction)
  #affichage du stock
print_stock_prices()
  #ouverture de actions.html sur page web
import webbrowser
webbrowser.open('file:///users/gouj/Desktop/Dev%20IA/actions.html')
#remplacer gouj par nom d'utilisateur, même chose pour le chemin de fichier
