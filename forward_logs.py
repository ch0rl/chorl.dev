import queue
import socketserver
import json
import sys
import os
import psycopg2


print(os.getenv("DB_HOST", "host.docker.internal"),
      os.getenv("DB_NAME", "chorl-dev"),
      os.getenv("DB_USER", "postgres"),
      os.getenv("DB_PASS", ""), sep="\n", file=sys.stderr)


class Handler(socketserver.BaseRequestHandler):
    db_host = os.getenv("DB_HOST", "host.docker.internal")
    db_name = os.getenv("DB_NAME", "chorl-dev")
    db_user = os.getenv("DB_USER", "postgres")
    db_pass = os.getenv("DB_PASS", "")

    queue = []

    def to_db(self, data):
        Handler.queue.append(data)

    def handle(self):
        print(self.request[0], file=sys.stderr)
        try:
            data = json.loads(self.request[0].split(b"nginx: ")[1])
        except BaseException as e:
            print(e, file=sys.stderr)
            return
        else:
            self.to_db(data)

    def setup(self):
        if len(Handler.queue) >= 20:
            conn = psycopg2.connect(
                f"dbname={Handler.db_name} user={Handler.db_user} host={Handler.db_host} password={Handler.db_pass}")
            cur = conn.cursor()
            for i in Handler.queue:
                cur.execute("insert into access_log ("
                            "path, ip, stamp, user_agent, id_got, id_set, status, forwarded_for, referrer) values ("
                            "%(path)s, %(ip)s, %(time)s, %(user_agent)s, %(user_id_got)s, %(user_id_set)s, "
                            "%(status)s, %(x_forwarded_for)s, %(http_referrer)s);", i)
            conn.commit()
            cur.close()
            conn.close()


print("logging forwarding starting", file=sys.stderr)
with socketserver.ThreadingUnixDatagramServer("/var/log/chorl.dev_log.sock", Handler) as server:
    # Change perms
    os.chmod("/var/log/chorl.dev_log.sock", 0o777)

    print("listen forever :3", file=sys.stderr)
    server.serve_forever()
