import os
import sqlite3

import numpy as np
import pandas as pd

conn = sqlite3.connect(os.path.expanduser('/Users/josh/Library/Messages/chat.db'))
c = conn.cursor()

# Collect all of the group chat info for a certain chat.
# cmd = f'SELECT ROWID, text, handle_id, \
#             datetime(date + strftime(\'%s\',\'2001-01-01\'), \'unixepoch\') as date_utc \
#             FROM message T1 \
#             INNER JOIN chat_message_join T2 \
#                 ON T2.chat_id=446 \
#                 AND T1.ROWID=T2.message_id \
#             ORDER BY T1.date'

cmd = f'SELECT chat.chat_identifier, count(chat.chat_identifier) AS message_count \
    FROM chat \
    JOIN chat_message_join ON chat. "ROWID" = chat_message_join.chat_id \
    JOIN message ON chat_message_join.message_id = message. "ROWID" \
    GROUP BY \
        chat.chat_identifier \
    ORDER BY \
        message_count DESC;'
c.execute(cmd)
#df = pd.DataFrame(c.fetchall(), columns = ['id', 'text', 'sender', 'time'])
#for i in np.stack(np.unique(df['sender'], return_counts = True)).T:
#    print(f'{i[0]:<4}:', i[1])
print(c.fetchone())
