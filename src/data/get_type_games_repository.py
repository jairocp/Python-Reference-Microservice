from bp import TypeGame
from .sentences_type_games_neo4j import GET_ALL_TYPE_GAMES
from .sentences_type_games_neo4j import GET_ALL_TYPE_GAMES_BY_USER

ID = "id"
NAME = "name"
URL_BACKGROUND = "urlBackground"
CODE = "code"
TYPE = "type"
NAME_LEVEL = "nameLevel"
LEVEL = "level"
PROGRESSION = "progression"


class GetAllTypeGamesRepository:

    def __init__(self, driver_neo4j):
        self.driver_neo4j = driver_neo4j

    def get_all_type_games(self, user_id):
        with self.driver_neo4j.session() as session:
            records = session.read_transaction(
                self._get_all_type_games_neo4j,
                user_id
            )

            type_games = []

            if(records):
                for record in records:
                    type_games.append(
                        TypeGame(
                            record[ID],
                            record[NAME],
                            record[URL_BACKGROUND],
                            record[CODE],
                            record[TYPE],
                            str(record[LEVEL]),
                            record[NAME_LEVEL]
                        )
                    )

            return type_games

    def get_type_games_by_user(self, user_id):
        with self.driver_neo4j.session() as session:
            records = session.read_transaction(
                self._get_type_games_by_user_neo4j,
                user_id
            )

            type_games = []

            if(records):
                for record in records:
                    type_games.append(
                        TypeGame(
                            record[ID],
                            record[NAME],
                            record[URL_BACKGROUND],
                            record[CODE],
                            record[TYPE],
                            str(record[LEVEL]),
                            record[NAME_LEVEL],
                            record[PROGRESSION]
                        )
                    )

            return type_games

    @staticmethod
    def _get_all_type_games_neo4j(tx, user_id):
        return tx.run(GET_ALL_TYPE_GAMES, userId=user_id)

    @staticmethod
    def _get_type_games_by_user_neo4j(tx, user_id):
        return tx.run(GET_ALL_TYPE_GAMES_BY_USER.format(user_id))
