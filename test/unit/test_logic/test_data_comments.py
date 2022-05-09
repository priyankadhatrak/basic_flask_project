import json
from flask import Response
from users.logic import data_comments
import pytest 

@pytest.mark.run()
def test_get_data(mocker):
    mocker.patch.object( data_comments,'get_data', return_value=Response({'from': 'get_data'}))
    result = data_comments.get_data()
    assert result

@pytest.mark.run()
@pytest.mark.parametrize(( 'input','output'),
            [
            (
            {"id":"","name":'sheetal', "comment":'sheetal here'},
             'Data Submitted Successfully.'),
            ({"id": "","name":"reeta", "comment":"reeta collection"},
              'Data Submitted Successfully.')
            ])
def test_add_data(mocker, input,output):
    add_data_mock = mocker.patch.object(data_comments,'add_data')
    res = data_comments.add_data(signature=input)
    add_data_mock.return_value = output
    assert res

@pytest.mark.run()
@pytest.mark.parametrize(('id','input','output'
        ),[
            (
            21,{"id":"1","name":'sheetal', "comment":'sheetal here'},
             'Data Submitted Successfully.'),
            (22,{"id": "12","name":"reeta", "comment":"reeta collection"},
              'Data Submitted Successfully.')
            ])
def test_update_data(mocker,input,output,id):
    update_data_mock = mocker.patch.object(data_comments, 'update_data')
    update_data_mock.return_value = output
    res = data_comments.update_data(input)
    assert res
    assert update_data_mock.called_once_with(id)
    
@pytest.mark.run()
def test_delete_data(mocker):
    delete_data_mock = mocker.patch.object(data_comments,'delete_data')
    delete_data_mock.return_value= Response()
    res = data_comments.delete_data(id)
    assert res.status_code == 200