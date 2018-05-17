from connect import run_query, run_command

c = ("CREATE VIEW sort AS \
     SELECT \
     Number Country, \
     SUM(Customers) Customers, \
     SUM(Total_Sales) 'Tot_Sales', \
     SUM(Total_Orders) 'Tot_Orders' \
     FROM \
        (SELECT \
        c.Country, \
        COUNT(DISTINCT c.CustomerId) Customers, \
        (CASE \
            WHEN COUNT(DISTINCT c.CustomerId) == 1 THEN 'Other' \
            ELSE c.Country \
        END) Number, \
        SUM(i.Total) 'Total_Sales', \
        SUM(ii.Quantity) 'Total_Orders' \
        FROM Customers c \
        INNER JOIN invoices i ON i.CustomerId = c.CustomerId \
        INNER JOIN invoice_items ii ON ii.InvoiceId = i.InvoiceId \
        GROUP BY 1 \
        ) \
    GROUP BY 1 \
    ORDER BY 2 DESC \
    ")
# run_command(c)

q1 = ("SELECT \
     Country, \
     Customers, \
     Tot_Sales 'Total Sales', \
     CAST(Tot_Sales as Float)/CAST(Customers as Float) 'Avg Value/Sale', \
     CAST(Tot_Orders as Float)/CAST(Customers as Float) 'Avg Value/Order' \
     FROM \
        (SELECT \
        *, \
        CASE \
            WHEN Country = 'Other' THEN 1 \
            ELSE 0 \
        END sort2 \
        FROM \
        sort \
        ORDER BY sort2 ASC \
        ) \
     ")

results = run_query(q1)
print(results)
