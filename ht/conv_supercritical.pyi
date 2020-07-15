# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from typing import List
from typing import (
    Optional,
    Union,
)


def Nu_Bishop(
    Re: float,
    Pr: float,
    rho_w: Optional[float] = ...,
    rho_b: Optional[float] = ...,
    D: Optional[float] = ...,
    x: Optional[float] = ...
) -> float: ...


def Nu_Bringer_Smith(Re: float, Pr: float) -> float: ...


def Nu_Gorban(Re: float, Pr: float) -> float: ...


def Nu_Griem(Re: float, Pr: float, H: Optional[float] = ...) -> float: ...


def Nu_Gupta(
    Re: float,
    Pr: float,
    rho_w: Optional[int] = ...,
    rho_b: Optional[float] = ...,
    mu_w: Optional[float] = ...,
    mu_b: Optional[float] = ...
) -> float: ...


def Nu_Jackson(
    Re: float,
    Pr: float,
    rho_w: Optional[float] = ...,
    rho_b: Optional[float] = ...,
    Cp_avg: Optional[float] = ...,
    Cp_b: Optional[float] = ...,
    T_b: Optional[int] = ...,
    T_w: Optional[int] = ...,
    T_pc: Optional[int] = ...
) -> float: ...


def Nu_Kitoh(Re: float, Pr: float, H: Optional[float] = ..., G: Optional[int] = ..., q: Optional[float] = ...) -> float: ...


def Nu_Krasnoshchekov(
    Re: float,
    Pr: float,
    rho_w: Optional[float] = ...,
    rho_b: Optional[float] = ...,
    Cp_avg: Optional[float] = ...,
    Cp_b: Optional[float] = ...,
    T_b: Optional[float] = ...,
    T_w: Optional[float] = ...,
    T_pc: Optional[float] = ...
) -> float: ...


def Nu_Krasnoshchekov_Protopopov(
    Re: float,
    Pr: float,
    Cp_avg: Optional[int] = ...,
    Cp_b: Optional[float] = ...,
    k_w: Optional[float] = ...,
    k_b: Optional[float] = ...,
    mu_w: Optional[float] = ...,
    mu_b: Optional[float] = ...
) -> float: ...


def Nu_McAdams(Re: float, Pr: float) -> float: ...


def Nu_Mokry(Re: float, Pr: float, rho_w: Optional[int] = ..., rho_b: Optional[float] = ...) -> float: ...


def Nu_Ornatsky(Re: float, Pr_b: float, Pr_w: float, rho_w: Optional[int] = ..., rho_b: Optional[float] = ...) -> float: ...


def Nu_Petukhov(
    Re: float,
    Pr: float,
    rho_w: Optional[float] = ...,
    rho_b: Optional[float] = ...,
    mu_w: Optional[float] = ...,
    mu_b: Optional[float] = ...
) -> float: ...


def Nu_Shitsman(Re: float, Pr_b: float, Pr_w: float) -> float: ...


def Nu_Swenson(Re: float, Pr: float, rho_w: Optional[int] = ..., rho_b: Optional[float] = ...) -> float: ...


def Nu_Xu(
    Re: float,
    Pr: float,
    rho_w: Optional[int] = ...,
    rho_b: Optional[float] = ...,
    mu_w: Optional[float] = ...,
    mu_b: Optional[float] = ...
) -> float: ...


def Nu_Yamagata(
    Re: float,
    Pr: float,
    Pr_pc: Optional[float] = ...,
    Cp_avg: Optional[float] = ...,
    Cp_b: Optional[float] = ...,
    T_b: Optional[int] = ...,
    T_w: Optional[int] = ...,
    T_pc: Optional[float] = ...
) -> float: ...


def Nu_Zhu(
    Re: float,
    Pr: float,
    rho_w: Optional[int] = ...,
    rho_b: Optional[float] = ...,
    k_w: Optional[float] = ...,
    k_b: Optional[float] = ...
) -> float: ...

__all__: List[str]