import asyncio
import asyncpg
import db_config

dbuser = db_config.dbuser
dbpassword = db_config.dbpassword
dbdatabase = db_config.dbdatabase
dbhost = db_config.dbhost

async def get_xp(user_id):
    try:
        conn = await asyncpg.connect(user=dbuser, password=dbpassword, database=dbdatabase, host=dbhost)
        xp = await conn.fetch('''SELECT xp FROM public.usuarios WHERE id = {}'''.format(user_id))    
        xpr = xp[0]
        xp = xpr['xp']        
        await conn.close()
        return xp
    except:KO
        await conn.close()
        return 0