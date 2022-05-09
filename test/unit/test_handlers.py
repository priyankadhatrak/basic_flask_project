import json
import unittest
from unittest.mock import patch
from flask import Response, render_template, request
from users import handlers
from users.logic import data_comments
from users.model import comments_info
from users.model.comments_info import Comments
import pytest
from flask_testing import TestCase
from mock import Mock, sentinel
from requests import codes, delete
from os import *


value_test= handlers.Comments(id,name,comment="")

@pytest.mark.run()
def test_index(mocker,fixture_client):
    fixture_client.get('/home')
    mocker.patch.object(data_comments, 'get_data', return_value= Response({'from': 'get_data'}))
    resp = fixture_client.get('/home')

    assert resp.status_code == 200
    result = json.loads(resp.data.decode())
    

@pytest.mark.run()
@pytest.mark.parametrize(( 'input','output'
        ),[
            (
            {"id":"","name":'sheetal', "comment":'sheetal here'},
             'Data Submitted Successfully.'),
            ({"id": "","name":"reeta", "comment":"reeta collection"},
              'Data Submitted Successfully.')
            ])
    
def test_post(mocker, fixture_client,input,output):
    fixture_client.post('/process')
    process_mock =mocker.patch.object(data_comments,'add_data')
    process_mock.return_value = output
    resp = fixture_client.post('/process',json=input)
    if resp.data.decode() != '':

        result_data = resp.data.decode()

        return result_data

    # result_data = handler_response.data.decode()

    assert resp.status_code == 200

@pytest.mark.parametrize(('id','input','output','status_code'
        ),[
            (
            21,{"id":"1","name":'sheetal', "comment":'sheetal here'},
             'Data Submitted Successfully.',200),
            (22,{"id": "12","name":"reeta", "comment":"reeta collection"},
              'Data Submitted Successfully.',200)
            ])
@pytest.mark.run()
def test_update(mocker,fixture_client,input,output,status_code,id):
    fixture_client.put('/update/<id>')
    update_mock =mocker.patch.object(data_comments,'update_data')
    update_mock.return_value = output
    resp = fixture_client.patch('/update/<id>',json=input)
    if resp.data.decode() != '':
       result_data = resp.data.decode()
       return result_data

    assert resp.status_code == status_code
    assert result_data == output.message
    assert update_mock.called
    assert update_mock.called_once_with(id)

@pytest.mark.run()
def test_delete(mocker):
    delete_mock = mocker.patch.object(data_comments,'delete_data')
    delete_mock.return_value = Response({'from': 'delete_data'})
    resp = data_comments.delete_data(id)
    assert resp.status_code == 200