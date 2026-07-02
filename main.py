from http.server import HTTPServer

from config import HOST, PORT
from database.database import database
from gameserver.session_manager import session_manager
from web.handler import Handler


def main():

    database.connect()

    session_manager.create_session()
    
    from gameserver.packet_factory import PacketFactory

    session = session_manager.get_current()

    packet = PacketFactory.session_info(session)

    print(packet)

    from gameserver.game_loop import game_loop

    game_loop.start()

    print(f"Listening on {HOST}:{PORT}")

    HTTPServer((HOST, PORT), Handler).serve_forever()

if __name__ == "__main__":
    main()