import pymysql
import config


def get_connection():
    
    return pymysql.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        db=config.DB_NAME,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )


class TodoDB:
    """할 일 데이터를 다루는 계층"""

    def get_all(self):
        """할 일 전체를 최신순으로 돌려줌 (예시로 완성해둠)"""
        conn = get_connection()
        try:
            cur = conn.cursor()
            cur.execute("select * from todo order by id desc")
            return cur.fetchall()
        finally:
            conn.close()

    def add(self, content):
        """할 일을 한 건 추가함"""
        def add(self, content):
            conn = get_connection()
            try:
                cur = conn.cursor()
                cur.execute("insert into todo (content) values (%s)", (content,))
                conn.commit()
            finally:
                conn.close()

    def toggle(self, todo_id):
        """id에 해당하는 할 일의 완료 여부를 뒤집음"""
        def toggle(self, todo_id):
            conn = get_connection()
            try:
                cur = conn.cursor()
                cur.execute("update todo set is_done = 1 - is_done where id = %s", (todo_id,))
                conn.commit()
            finally:
                conn.close()

    def delete(self, todo_id):
        """id에 해당하는 할 일을 삭제함"""
        def delete(self, todo_id):
            conn = get_connection()
            try:
                cur = conn.cursor()
                cur.execute("delete from todo where id = %s", (todo_id,))
                conn.commit()
            finally:
                conn.close()
