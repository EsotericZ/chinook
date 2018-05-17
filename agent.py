from connect import run_query
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

q1 = ("SELECT \
    e.EmployeeId, \
    e.FirstName || ' ' || e.LastName Agent, \
    COUNT(i.InvoiceId) 'Total $ Assigned', \
    SUM(i.total) 'Total Spent', \
    e.Country Country \
    FROM Employees e \
    INNER JOIN customers c ON c.SupportRepId = e.EmployeeId \
    INNER JOIN invoices i ON i.CustomerId = c.CustomerId \
    GROUP BY 1 ORDER BY 4 DESC \
    ")
agent = run_query(q1)

ax = agent[['Total $ Assigned']].plot(kind='bar', title='Total Assigned $ per Agent', figsize=(5,5))
ax.set_xlabel('Agent')
ax.set_ylabel('Total $ Assigned')
ax.set_xticklabels(agent.Agent)
plt.show()

# RESULTS
# The three sales reps do about the same in terms of sales, and they all live in the great white north!
