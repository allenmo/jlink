import sqlite3

class ledDb(object):
    def __init__(self):
        self.con = sqlite3.connect("led.db")
        self.con.isolation_level = None
        self.cur = self.con.cursor()
        self.createTable()

    def createTable(self):
        self.con.execute("CREATE TABLE IF NOT EXISTS `check_led` (\
        `id` integer NOT NULL PRIMARY KEY AUTOINCREMENT,\
        `name` varchar(20) DEFAULT NULL,\
        `x` integer DEFAULT NULL,\
        `y` int(11) DEFAULT NULL,\
        `R1` int(11) DEFAULT NULL,\
        `R2` int(11) DEFAULT NULL,\
        `L1` int(11) DEFAULT NULL,\
        `U1` int(11) DEFAULT NULL,\
        `L2` int(11) DEFAULT NULL,\
        `U2` int(11) DEFAULT NULL,\
        `L3` int(11) DEFAULT NULL,\
        `U3` int(11) DEFAULT NULL,\
        `color_space` varchar(10) NOT NULL,\
        `mode` varchar(20) NOT NULL\
        )")
        self.con.commit()

    def insertOneLedInfo(self, name='',x=0,y=0,r1=0,r2=0,L1=0,U1=0,L2=0,U2=0,L3=0,U3=0,color_space='RGB',mode='CIRCLE'):
        sql = "insert into check_led(name,x,y,R1,R2,L1,U1,L2,U2,L3,U3,color_space,mode) values('%s',%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,'%s','%s')" %(name,x,y,r1,r2,L1,U1,L2,U2,L3,U3,color_space,mode)
        self.cur.execute(sql)
        self.con.commit()
        print 'row insert:', self.cur.rowcount

    def selectAllLed(self):
        self.cur.execute("select * from check_led")
        res = self.cur.fetchall()
        # print 'row:', len(res)
        return res

    def getDesc(self):
        return self.cur.description

    def printAllLed(self):
        res = self.selectAllLed()
        for line in res:
            for f in line:
                print f,
            print
        print '-'*60

    def selectOneLed(self):
        self.cur.execute("select * from  check_led")
        res = self.cur.fetchone()
        return res

    def printOneLed(self):
        res = selectOneLed()
        print 'row:', len(res)
        for f in res:
            print f,
        print
        print '-'*60

    def selectOneLedNearXY(self, x, y, r=6):
        self.cur.execute("select * from check_led where x>%d and x<%d and y>%d and y<%d" %(x-r,x+r,y-r,y+r))
        res = self.cur.fetchone()
        return res

    def selectOneLedNearIn2Points(self, x1, y1, x2, y2):
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        self.cur.execute("select * from check_led where x>%d and x<%d and y>%d and y<%d" %(x1, x2, y1, y2))
        res = self.cur.fetchone()
        return res

    def deleteOneLedById(self, id):
        self.cur.execute("delete from check_led where id = %d" %id)
        self.con.commit()
        return self.cur.rowcount

    def close(self):
        self.cur.close()
        self.con.close()

if __name__ == "__main__":
    db = ledDb()
    db.insertOneLedInfo()
    db.printAllLed()
    db.close()
