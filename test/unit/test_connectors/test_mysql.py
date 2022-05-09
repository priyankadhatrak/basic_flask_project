import pytest
from sqlalchemy import exc
from users.connectors import mysql

@pytest.mark.run()
def test_session_rollback(mocker):
        mock = mocker.patch.object(mysql, '_db_session')
        with pytest.raises(exc.SQLAlchemyError):
            with mysql.db_session():
                raise exc.SQLAlchemyError()
        session = mock.return_value
        assert session.rollback.called
        assert 200