from connect import run_query
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

q1 = ("SELECT SUM(qty) FROM (SELECT \
        i.BillingCountry, \
        SUM(ii.Quantity) qty, \
        g.name \
    FROM invoices i \
    INNER JOIN invoice_items ii ON i.InvoiceId = ii.invoiceId \
    INNER JOIN tracks t ON t.TrackId = ii.TrackId \
    INNER JOIN genres g ON g.GenreId = t.GenreId \
    WHERE i.BillingCountry = 'USA' \
    GROUP BY 3 ORDER BY 2 DESC \
    )")
# print(run_query(q1))
# Total Tracks Sold = 494

q2 = ("SELECT \
        g.name Genre, \
        SUM(ii.Quantity) Quantity, \
        ((CAST(SUM(ii.Quantity) as Float)/494)*100) Percent \
    FROM invoices i \
    INNER JOIN invoice_items ii ON i.InvoiceId = ii.invoiceId \
    INNER JOIN tracks t ON t.TrackId = ii.TrackId \
    INNER JOIN genres g ON g.GenreId = t.GenreId \
    WHERE i.BillingCountry = 'USA' \
    GROUP BY 1 ORDER BY 2 DESC \
    ")
tops = run_query(q2)[:10]
# print(tops)

ax = tops[['Percent']].plot(kind='bar', title='Top 5 Genres Sold in US by Percentage', figsize=(5,5))
ax.set_xlabel('Genre')
ax.set_ylabel('Percentage of Sales')
ax.set_xticklabels(tops.Genre)
plt.show()

# RESULTS
# The shop should stock the Punk, Blues and Pop artist first as the genres are sold at a higher percentage in the US
