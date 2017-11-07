import nycdb
import os


def test_extract_csvs_from_zip():
    test_csv_file = os.path.join(os.path.dirname(__file__), 'cats.zip')
    csv_content = nycdb.transform.extract_csvs_from_zip(test_csv_file)
    result = "name,superpower\nalice,eating\nfluffy,purring\nmeowses,sitting\npickles,looking out the window\n"
    assert csv_content == result


def test_to_csv(tmpdir):
    f = tmpdir.join('test.csv')
    f.write("name,borough,block,lot\nalice,queens,1,2\nbob,bronx,3,4")

    output_list = list(nycdb.transform.to_csv(f.strpath))
    assert output_list[0] == {'name': 'alice', 'borough': 'queens', 'block': '1', 'lot': '2'}
    assert output_list[1] == {'name': 'bob', 'borough': 'bronx', 'block': '3', 'lot': '4'}


def test_to_bbl():
    table = [ { 'borough': 'queens', 'block': '1', 'lot': '1' },{ 'borough': 'queens', 'block': '1', 'lot': '2' } ]
    out = list(nycdb.transform.with_bbl(table))
    assert out[0] == { 'borough': 'queens', 'block': '1', 'lot': '1', 'bbl': '4000010001' }
    assert out[1] == { 'borough': 'queens', 'block': '1', 'lot': '2', 'bbl': '4000010002' }