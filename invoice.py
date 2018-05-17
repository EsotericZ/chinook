from connect import run_query, run_command

q1 = '''
WITH first_track AS \
    (SELECT \
    ii.invoice_id invoice_id, \
    MIN(ii.track_id) first \
    FROM invoice_items ii \
    GROUP BY 1) \
\
SELECT \
    album_purchase, \
    COUNT(invoice_id) invoices, \
    CAST(COUNT(invoice_id) AS Float) / (SELECT COUNT(*) FROM invoice) percent \
FROM \
(SELECT \
    ft.*, \
    CASE \
    	WHEN( \
             SELECT t.track_id FROM tracks t \
             WHERE t.album_id = (SELECT t2.album_id FROM tracks t2 \
                                 WHERE t2.track_id = ft.first) \
        EXCEPT \
             SELECT ii2.track_id FROM invoice_items ii2 \
                  WHERE ii2.invoice_id = ft.invoice_id) IS NULL \
             AND \
                 (SELECT ii2.track_id FROM invoice_items ii2 \
                  WHERE ii2.invoice_id = ft.invoice_id \
        EXCEPT \
             SELECT t.track_id FROM tracks t \
             WHERE t.album_id = (SELECT t2.album_id FROM tracks t2 \
                                 WHERE t2.track_id = ft.first) IS NULL \
        THEN "Yes" \
        ELSE "No" \
    END AS "album_purchase" \
    FROM first_track ft \
    ) \
GROUP BY album_purchase; \
'''

print(run_query(q1))
