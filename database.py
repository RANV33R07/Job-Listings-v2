import sqlalchemy
from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://2MV7kAJ8u835cqi.root:qOjWOWxOhLy0Zi86@gateway01.ap-southeast-1.prod.aws.tidbcloud.com/test?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/isrgrootx1.pem",
                       }})
