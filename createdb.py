import refs.DB
cursor = refs.DB.lazy_connect()
input = [line for line in file('refs/schema.sql') if not line.startswith('--')]
input = '\n'.join(input)
for s in input.split(';'):
    s = s.strip()
    if not s: continue
    cursor.execute(s)
