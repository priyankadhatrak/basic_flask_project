from flask import Response
from users.model.comments_info import Comments
import pytest

@pytest.mark.parametrize(( 'input','output'
        ),[
            (
            {"id":"","name":'sheetal', "comment":'sheetal here'},
             'Data Submitted Successfully.')
            ])
@pytest.mark.run()
def test_add(mocker,fixture_client,output,input):
    mocker.patch.object( Comments,'add', return_value=Response({'from': 'add'}))
    add_mock = mocker.patch.object(Comments,'add')
    add_mock.return_value = output
    resp = fixture_client.post(json=input)
    
    if resp.data.decode() != '':
        result_data = resp.data.decode()
        return result_data ==200
    assert resp.response == result_data
        
@pytest.mark.run()
def test_save(mocker):
    mocker.patch.object( Comments,'save', return_value=Response({'from': 'save'}))
    save_mock=mocker.patch.object(Comments,'save')
    save_mock.return_value= Response()
    resp = Comments.save()
    assert resp.status_code == 200

@pytest.mark.run()
def test_delete(mocker):
    mocker.patch.object( Comments,'delete', return_value=Response({'from': 'delete'}))
    delete_mock=mocker.patch.object(Comments,'delete')
    delete_mock.return_value= Response()
    resp = Comments.delete(data1=id)
    assert resp.status_code == 200


@pytest.mark.run()
def test_allQuery(mocker):
    mocker.patch.object( Comments,'allQuery', return_value=Response({'from': 'allQuery'}))
    result = Comments.allQuery()
    assert result.status_code==200

@pytest.mark.run()
def test_singleQuery(mocker):
    mocker.patch.object( Comments,'singleQuery', return_value=Response({'from': 'singleQuery'}))
    single_mock=mocker.patch.object(Comments,'singleQuery')
    single_mock.return_value= Response()
    result = Comments.singleQuery(id=id)
    assert result.status_code == 200
