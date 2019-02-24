#!/usr/bin/python3

import sys
import psycopg2

conn = psycopg2.connect("service=cb")
cur = conn.cursor()

#40CW  23-Feb-19 20:33 0001  YU4SSR         599  599  466           YU   46  3

for line in sys.stdin:
    if line[1:3] == '40':
        qrg = 7
    else:
        raise Exception('unknown band', line[1:3])

    if line[23] != '0':
        Exception('serial does not start with 0')

    cur.execute("INSERT INTO LOG (start, call, qrg, rsttx, rstrx, comment, mypwr) " +
                "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (line[7:22], line[29:39].rstrip(), qrg, line[44:47]+line[24:27], line[49:52]+line[54:64].rstrip(), sys.argv[1], sys.argv[2]))

conn.commit()