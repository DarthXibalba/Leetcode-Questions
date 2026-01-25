from typing import Callable, Iterable, Tuple, Any

def run_cases(
    *,
    func: Callable[..., Any],
    cases: Iterable[Tuple[Any, Any]],
    name: str | None = None,
) -> None:
    """
    Run a sequence of test cases against a pure function.


    Each case is a tuple:
    (input, expected)


    - func: the solution function under test
    - cases: iterable of (input, expected) pairs
    - name: optional label for clearer assertion messages


    The input is passed directly to func.
    The return value is compared to expected using ==.
    """


    for idx, (inp, expected) in enumerate(cases):
        try:
            actual = func(inp)
        except Exception as exc:
            case_name = f"{name} (case {idx})" if name else f"case {idx}"
            raise AssertionError(
                f"{case_name}: function raised an exception\n"
                f"input={inp!r}\n"
                f"exception={exc!r}"
            ) from exc


        if actual != expected:
            case_name = f"{name} (case {idx})" if name else f"case {idx}"
            raise AssertionError(
                f"{case_name}: incorrect result\n"
                f"input={inp!r}\n"
                f"expected={expected!r}\n"
                f"actual={actual!r}"
)