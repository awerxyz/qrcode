import pytest
from utils import generate_qr_code

def test_generate_qr_code_default_options():
    data = "Test Data"
    options = {}
    
    tk_image = generate_qr_code(data, options)
    
    assert tk_image is not None
    assert isinstance(tk_image, type(tk.PhotoImage()))

def test_generate_qr_code_custom_options():
    data = "Custom Test Data"
    options = {
        "fill_color": "red",
        "back_color": "yellow",
        "box_size": 10,
        "quiet_zone": 2
    }
    
    tk_image = generate_qr_code(data, options)
    
    assert tk_image is not None
    assert isinstance(tk_image, type(tk.PhotoImage()))

def test_generate_qr_code_missing_options():
    data = "Test Data"
    options = {
        "fill_color": "red",
        "box_size": 10
    }
    
    tk_image = generate_qr_code(data, options)
    
    assert tk_image is not None
    assert isinstance(tk_image, type(tk.PhotoImage()))

def test_generate_qr_code_invalid_options():
    data = "Test Data"
    options = {
        "fill_color": "invalid_color",
        "back_color": "invalid_color",
        "box_size": "invalid_size",
        "quiet_zone": "invalid_zone"
    }
    
    with pytest.raises(ValueError):
        generate_qr_code(data, options)
