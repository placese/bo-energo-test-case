import pytest

from logic.equations_handler import (
        RootsOfQuadraticEquation,
        solve_quadratic_equation,
    )


@pytest.mark.asyncio
async def test_solve_quadratic_equation():
    """Тест-кейс с простыми параметрами
    Test-case with simple parameters
    """
    expected_result = RootsOfQuadraticEquation(x1=0.0, x2=-1.0)
    result = await solve_quadratic_equation(a=1, b=1)
    assert expected_result.x1 == result.x1
    assert expected_result.x2 == result.x2
    assert result == expected_result

@pytest.mark.asyncio
async def test_solve_quadratic_equation_with_negative_discriminant():
    """Тест-кейс с отрицательным дискриминантом
    Test-case with negative discriminant
    """
    expected_result = RootsOfQuadraticEquation()
    result = await solve_quadratic_equation(a=1, c=3)
    assert result == expected_result

@pytest.mark.asyncio
async def test_solve_quadratic_equation_with_zero_discriminant():
    """Тест-кейс с нулевым дискриминантом
    Test-case with zero discriminant
    """
    expected_result = RootsOfQuadraticEquation(x1=-1, x2=-1.0)
    result = await solve_quadratic_equation(a=2, b=4, c=2)
    assert result == expected_result

@pytest.mark.asyncio
async def test_solve_quadratic_equation_with_all_parameters():
    """Тест-кейс с ненулевыми параметрами a, b, c
    Test-case with non-zero a, b, c parameters 
    """
    expected_result = RootsOfQuadraticEquation(x1=2.5485837703548637,
                                               x2=0.7847495629784698)
    result = await solve_quadratic_equation(a=1.5, b=-5, c=3)
    assert result == expected_result
    
@pytest.mark.asyncio
async def test_solve_quadratic_equation_with_two_parameters():
    """Тест-кейс с ненулевыми параметрами a, c и a, b
    Test-case with non-zero a, c and a, b parameters 
    """
    expected_result = RootsOfQuadraticEquation(x1=1.224744871391589,
                                               x2=-1.224744871391589)
    result = await solve_quadratic_equation(a=2, c=-3)
    assert result == expected_result
    expected_result = RootsOfQuadraticEquation(x1=0.23463687150837992,
                                               x2=0)
    result = await solve_quadratic_equation(a=17.9, b=-4.2)
    assert result == expected_result

@pytest.mark.asyncio
async def test_solve_quadratic_equation_with_nullable_a():
    """Тест-кейс с нулевым параметром а
    Test-case with nullable parameter a
    """
    with pytest.raises(Exception):
        await solve_quadratic_equation(a=0)
    
