import yfinance as yf


tickers = ['BIDU', 'SIRI', 'SOHU', 'CAAS', 'VRA', 'WBA', 'GEG', 'GMAB', 'JBLU', 'NCTY', 'SEDG', 'UTSI', 'BABA', 'F', 'FL', 'GM', 'HMC', 'MOV', 'SONY', 'TCS', 'TM', 'TAP', 'UNFI', 'NOV', 'BEN', 'C', 'DB', 'OPY', 'CYD', 'SAVE', 'TWI', 'ZTO', 'XRX', 'CLW', 'NTR', 'PKX', 'X']
  # Add or replace with the companies you want

# Dictionary to store results
results = {}

# Loop through each ticker symbol
for ticker in tickers:
    # Download the stock's information
    stock = yf.Ticker(ticker)
    score = 0  # Initialize the score for each company

    try:
        # Calculate ROA for the last two years and current operating cash flow
        roa = stock.financials.loc['Net Income'] / stock.balance_sheet.loc['Total Assets']
        roa = roa.dropna()  # Remove any null values to avoid errors
        roa =  roa.sort_index(ascending=False)
        cfo = stock.cashflow.loc['Operating Cash Flow'].dropna().iloc[0]  # Most recent non-null CFO

        if len(roa) >= 2:
            current_roa = roa.iloc[0]  # Most recent ROA
            previous_roa = roa.iloc[1]  # ROA from the previous year

            # Check if current ROA is positive
            if current_roa > 0:
                score += 1  # Award a point for positive current ROA

            # Check if current-year ROA is higher than previous-year ROA
            if current_roa > previous_roa:
                score += 1  # Award an additional point
                
            if cfo > 0:
                score += 1  # Award a point for positive CFO

            # Award additional point if CFO is higher than current-year ROA
            if cfo > current_roa:
                score += 1

    except (KeyError, IndexError, TypeError):
        pass  # Skip if data is unavailable

    try:
        # Calculate the current ratio for the last two years
        current_ratio = stock.balance_sheet.loc['Current Assets'] / stock.balance_sheet.loc['Current Liabilities']
        current_ratio = current_ratio.dropna()
        current_ratio =  current_ratio.sort_index(ascending=False)

        if len(current_ratio) >= 2:
            current_current_ratio = current_ratio.iloc[0]  # Most recent current ratio
            previous_current_ratio = current_ratio.iloc[1]  # Previous year's current ratio

            # Check if current year's current ratio is higher than the previous year's
            if current_current_ratio > previous_current_ratio:
                score += 1  # Award a point for improvement in current ratio

    except (KeyError, IndexError, TypeError):
        pass  # Skip if data is unavailable

    try:
        # Calculate the long-term debt to total assets ratio for the last two years
        long_term_debt = stock.balance_sheet.loc['Long Term Debt']
        total_assets = stock.balance_sheet.loc['Total Assets']
        long_term_debt_to_assets = long_term_debt / total_assets
        long_term_debt_to_assets = long_term_debt_to_assets.dropna()
        long_term_debt_to_assets =  long_term_debt_to_assets.sort_index(ascending=False)

        if len(long_term_debt_to_assets) >= 2:
            current_long_term_debt_to_assets = long_term_debt_to_assets.iloc[0]  # Most recent ratio
            previous_long_term_debt_to_assets = long_term_debt_to_assets.iloc[1]  # Previous year's ratio

            # Check if current year's long-term debt to total assets ratio is lower than the previous year's
            if current_long_term_debt_to_assets < previous_long_term_debt_to_assets:
                score += 1  # Award a point for improvement in the debt-to-assets ratio

    except (KeyError, IndexError, TypeError):
        pass  # Skip if data is unavailable

    try:
        # Get the number of shares outstanding for the last two years
        shares_outstanding = stock.balance_sheet.loc['Ordinary Shares Number']
        shares_outstanding = shares_outstanding.dropna()
        shares_outstanding = shares_outstanding.sort_index(ascending=False)

        if len(shares_outstanding) >= 2:
            current_shares = shares_outstanding.iloc[0]  # Most recent number of shares
            previous_shares = shares_outstanding.iloc[1]  # Previous year's number of shares

            # Check if the current year's number of shares is the same or fewer than the previous year's
            if current_shares <= previous_shares:
                score += 1  # Award a point if shares are the same or fewer

    except (KeyError, IndexError, TypeError):
        pass  # Skip if data is unavailable

    try:
        # Calculate the gross margin ratio for the last two years
        gross_profit = stock.financials.loc['Gross Profit']
        total_revenue = stock.financials.loc['Total Revenue']
        gross_profit = gross_profit.dropna()
        total_revenue = total_revenue.dropna()
        gross_margin = gross_profit / total_revenue
        gross_margin = gross_margin.dropna()
        gross_margin =  gross_margin.sort_index(ascending=False)

        if len(gross_margin) >= 2:
            current_gross_margin = gross_margin.iloc[0]  # Most recent gross margin ratio
            previous_gross_margin = gross_margin.iloc[1]  # Previous year's gross margin ratio

            # Check if current year's gross margin ratio is higher than the previous year's
            if current_gross_margin > previous_gross_margin:
                score += 1  # Award a point for improvement in gross margin ratio
    except (KeyError, IndexError, TypeError):
        pass  # Skip if data is unavailable
    
    try:
        # Calculate the asset turnover ratio for the last two years
        total_revenue = stock.financials.loc['Total Revenue']
        total_assets = stock.balance_sheet.loc['Total Assets']
        asset_turnover = stock.financials.loc['Total Revenue'] / stock.balance_sheet.loc['Total Assets']
        asset_turnover = asset_turnover.dropna()
        asset_turnover =  asset_turnover.sort_index(ascending=False)
        if len(asset_turnover) >= 2:
            current_asset_turnover = asset_turnover.iloc[0]  # Most recent asset turnover ratio
            previous_asset_turnover = asset_turnover.iloc[1]  # Previous year's asset turnover ratio
            # Check if current year's asset turnover ratio is higher than the previous year's
            if current_asset_turnover > previous_asset_turnover:
                score += 1  # Award a point for improvement in asset turnover ratio

    except (KeyError, IndexError, TypeError):
        pass  # Skip if data is unavailable
    
    # Store the final score in results
    results[ticker] = score if score > 0 else "Data unavailable"
    
# Split companies by score groups
score_groups = {}

# Group companies by their score
for ticker, score in results.items():
    if score not in score_groups:
        score_groups[score] = []
    score_groups[score].append(ticker)

# Sort the score groups by score (from highest to lowest)
sorted_score_groups = sorted(score_groups.items(), key=lambda x: x[0], reverse=True)

# Display the sorted groups
for score, tickers in sorted_score_groups:
    print(f"Score {score}:")
    for ticker in tickers:
        print(f"  - {ticker}")
    print()
