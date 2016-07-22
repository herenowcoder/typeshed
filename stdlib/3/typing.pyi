# Stubs for typing

from abc import abstractmethod, ABCMeta

# Definitions of special type checking related constructs.  Their definition
# are not used, so their value does not matter.

cast = object()
overload = object()
Any = object()
TypeVar = object()
Generic = object()
Tuple = object()
Callable = object()
Type = object()
builtinclass = object()
_promote = object()
NamedTuple = object()
no_type_check = object()

# Type aliases and type constructors

class TypeAlias:
    # Class for defining generic aliases for library types.
    def __init__(self, target_type: type) -> None: ...
    def __getitem__(self, typeargs: Any) -> Any: ...

Union = TypeAlias(object)
Optional = TypeAlias(object)
List = TypeAlias(object)
Dict = TypeAlias(object)
DefaultDict = TypeAlias(object)
Set = TypeAlias(object)

# Predefined type variables.
AnyStr = TypeVar('AnyStr', str, bytes)

# Abstract base classes.

# These type variables are used by the container types.
_T = TypeVar('_T')
_S = TypeVar('_S')
_KT = TypeVar('_KT')  # Key type.
_VT = TypeVar('_VT')  # Value type.
_T_co = TypeVar('_T_co', covariant=True)  # Any type covariant containers.
_V_co = TypeVar('_V_co', covariant=True)  # Any type covariant containers.
_KT_co = TypeVar('_KT_co', covariant=True)  # Key type covariant containers.
_VT_co = TypeVar('_VT_co', covariant=True)  # Value type covariant containers.
_T_contra = TypeVar('_T_contra', contravariant=True)  # Ditto contravariant.

class SupportsInt(metaclass=ABCMeta):
    @abstractmethod
    def __int__(self) -> int: ...

class SupportsFloat(metaclass=ABCMeta):
    @abstractmethod
    def __float__(self) -> float: ...

class SupportsComplex(metaclass=ABCMeta):
    @abstractmethod
    def __complex__(self) -> complex: pass

class SupportsBytes(metaclass=ABCMeta):
    @abstractmethod
    def __bytes__(self) -> bytes: pass

class SupportsAbs(Generic[_T]):
    @abstractmethod
    def __abs__(self) -> _T: ...

class SupportsRound(Generic[_T]):
    @abstractmethod
    def __round__(self, ndigits: int = ...) -> _T: ...

class Reversible(Generic[_T_co]):
    @abstractmethod
    def __reversed__(self) -> Iterator[_T_co]: ...

class Sized(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self) -> int: ...

class Hashable(metaclass=ABCMeta):
    # TODO: This is special, in that a subclass of a hashable class may not be hashable
    #   (for example, list vs. object). It's not obvious how to represent this. This class
    #   is currently mostly useless for static checking.
    @abstractmethod
    def __hash__(self) -> int: ...

class Iterable(Generic[_T_co]):
    @abstractmethod
    def __iter__(self) -> Iterator[_T_co]: ...

class Iterator(Iterable[_T_co], Generic[_T_co]):
    @abstractmethod
    def __next__(self) -> _T_co: ...
    def __iter__(self) -> 'Iterator[_T_co]': ...

class Generator(Iterator[_T_co], Generic[_T_co, _T_contra, _V_co]):
    @abstractmethod
    def __next__(self) -> _T_co:...

    @abstractmethod
    def send(self, value: _T_contra) -> _T_co:...

    @abstractmethod
    def throw(self, typ: BaseException, val: Any = None, tb: Any = None) -> None:...

    @abstractmethod
    def close(self) -> None:...

    @abstractmethod
    def __iter__(self) -> 'Generator[_T_co, _T_contra, _V_co]': ...

class Awaitable(Generic[_T_co]):
    @abstractmethod
    def __await__(self) -> Generator[Any, None, _T_co]:...

# NOTE: This type does not exist in typing.py or PEP 484.
class AwaitableGenerator(Generator[_T_co, _T_contra, _V_co], Awaitable[_T_co],
                         Generic[_T_co, _T_contra, _V_co]):
    pass

class AsyncIterable(Generic[_T_co]):
    @abstractmethod
    def __anext__(self) -> Awaitable[_T_co]:...

class AsyncIterator(AsyncIterable[_T_co],
                    Generic[_T_co]):
    @abstractmethod
    def __anext__(self) -> Awaitable[_T_co]:...
    def __aiter__(self) -> 'AsyncIterator[_T_co]':...

class Container(Generic[_T_co]):
    @abstractmethod
    def __contains__(self, x: object) -> bool: ...

class Sequence(Iterable[_T_co], Container[_T_co], Sized, Reversible[_T_co], Generic[_T_co]):
    @overload
    @abstractmethod
    def __getitem__(self, i: int) -> _T_co: ...
    @overload
    @abstractmethod
    def __getitem__(self, s: slice) -> Sequence[_T_co]: ...
    # Mixin methods
    def index(self, x: Any) -> int: ...
    def count(self, x: Any) -> int: ...
    def __contains__(self, x: object) -> bool: ...
    def __iter__(self) -> Iterator[_T_co]: ...
    def __reversed__(self) -> Iterator[_T_co]: ...

class MutableSequence(Sequence[_T], Generic[_T]):
    @abstractmethod
    def insert(self, index: int, object: _T) -> None: ...
    @overload
    @abstractmethod
    def __setitem__(self, i: int, o: _T) -> None: ...
    @overload
    @abstractmethod
    def __setitem__(self, s: slice, o: Sequence[_T]) -> None: ...
    @overload
    @abstractmethod
    def __delitem__(self, i: int) -> None: ...
    @overload
    @abstractmethod
    def __delitem__(self, i: slice) -> None: ...
    # Mixin methods
    def append(self, object: _T) -> None: ...
    def extend(self, iterable: Iterable[_T]) -> None: ...
    def reverse(self) -> None: ...
    def pop(self, index: int = ...) -> _T: ...
    def remove(self, object: _T) -> None: ...
    def __iadd__(self, x: Iterable[_T]) -> MutableSequence[_T]: ...

class AbstractSet(Iterable[_T_co], Container[_T_co], Sized, Generic[_T_co]):
    @abstractmethod
    def __contains__(self, x: object) -> bool: ...
    # Mixin methods
    def __le__(self, s: AbstractSet[Any]) -> bool: ...
    def __lt__(self, s: AbstractSet[Any]) -> bool: ...
    def __gt__(self, s: AbstractSet[Any]) -> bool: ...
    def __ge__(self, s: AbstractSet[Any]) -> bool: ...
    def __and__(self, s: AbstractSet[Any]) -> AbstractSet[_T_co]: ...
    def __or__(self, s: AbstractSet[_T]) -> AbstractSet[Union[_T_co, _T]]: ...
    def __sub__(self, s: AbstractSet[Any]) -> AbstractSet[_T_co]: ...
    def __xor__(self, s: AbstractSet[_T]) -> AbstractSet[Union[_T_co, _T]]: ...
    # TODO: Argument can be a more general ABC?
    def isdisjoint(self, s: AbstractSet[Any]) -> bool: ...

class MutableSet(AbstractSet[_T], Generic[_T]):
    @abstractmethod
    def add(self, x: _T) -> None: ...
    @abstractmethod
    def discard(self, x: _T) -> None: ...
    # Mixin methods
    def clear(self) -> None: ...
    def pop(self) -> _T: ...
    def remove(self, element: _T) -> None: ...
    def __ior__(self, s: AbstractSet[_S]) -> MutableSet[Union[_T, _S]]: ...
    def __iand__(self, s: AbstractSet[Any]) -> MutableSet[_T]: ...
    def __ixor__(self, s: AbstractSet[_S]) -> MutableSet[Union[_T, _S]]: ...
    def __isub__(self, s: AbstractSet[Any]) -> MutableSet[_T]: ...

class MappingView(Sized):
    def __len__(self) -> int: ...

class ItemsView(AbstractSet[Tuple[_KT_co, _VT_co]], MappingView, Generic[_KT_co, _VT_co]):
    def __contains__(self, o: object) -> bool: ...
    def __iter__(self) -> Iterator[Tuple[_KT_co, _VT_co]]: ...

class KeysView(AbstractSet[_KT_co], MappingView, Generic[_KT_co]):
    def __contains__(self, o: object) -> bool: ...
    def __iter__(self) -> Iterator[_KT_co]: ...

class ValuesView(MappingView, Iterable[_VT_co], Generic[_VT_co]):
    def __contains__(self, o: object) -> bool: ...
    def __iter__(self) -> Iterator[_VT_co]: ...

# TODO: ContextManager (only if contextlib.AbstractContextManager exists)

class Mapping(Iterable[_KT], Container[_KT], Sized, Generic[_KT, _VT]):
    # TODO: Value type should be covariant, but currently we can't give a good signature for
    #   get if this is the case.
    @abstractmethod
    def __getitem__(self, k: _KT) -> _VT: ...
    # Mixin methods
    def get(self, k: _KT, default: _VT = ...) -> _VT: ...
    def items(self) -> AbstractSet[Tuple[_KT, _VT]]: ...
    def keys(self) -> AbstractSet[_KT]: ...
    def values(self) -> ValuesView[_VT]: ...
    def __contains__(self, o: object) -> bool: ...

class MutableMapping(Mapping[_KT, _VT], Generic[_KT, _VT]):
    @abstractmethod
    def __setitem__(self, k: _KT, v: _VT) -> None: ...
    @abstractmethod
    def __delitem__(self, v: _KT) -> None: ...

    def clear(self) -> None: ...
    def pop(self, k: _KT, default: _VT = ...) -> _VT: ...
    def popitem(self) -> Tuple[_KT, _VT]: ...
    def setdefault(self, k: _KT, default: _VT = ...) -> _VT: ...
    # 'update' used to take a Union, but using overloading is better.
    # The second overloaded type here is a bit too general, because
    # Mapping[Tuple[_KT, _VT], W] is a subclass of Iterable[Tuple[_KT, _VT]],
    # but will always have the behavior of the first overloaded type
    # at runtime, leading to keys of a mix of types _KT and Tuple[_KT, _VT].
    # We don't currently have any way of forcing all Mappings to use
    # the first overload, but by using overloading rather than a Union,
    # mypy will commit to using the first overload when the argument is
    # known to be a Mapping with unknown type parameters, which is closer
    # to the behavior we want. See mypy issue #1430.
    @overload
    def update(self, m: Mapping[_KT, _VT]) -> None: ...
    @overload
    def update(self, m: Iterable[Tuple[_KT, _VT]]) -> None: ...

Text = str

TYPE_CHECKING = True

class IO(Iterable[AnyStr], Generic[AnyStr]):
    # TODO detach
    # TODO use abstract properties
    @property
    def mode(self) -> str: ...
    @property
    def name(self) -> str: ...
    @abstractmethod
    def close(self) -> None: ...
    @property
    def closed(self) -> bool: ...
    @abstractmethod
    def fileno(self) -> int: ...
    @abstractmethod
    def flush(self) -> None: ...
    @abstractmethod
    def isatty(self) -> bool: ...
    # TODO what if n is None?
    @abstractmethod
    def read(self, n: int = ...) -> AnyStr: ...
    @abstractmethod
    def readable(self) -> bool: ...
    @abstractmethod
    def readline(self, limit: int = ...) -> AnyStr: ...
    @abstractmethod
    def readlines(self, hint: int = ...) -> list[AnyStr]: ...
    @abstractmethod
    def seek(self, offset: int, whence: int = ...) -> int: ...
    @abstractmethod
    def seekable(self) -> bool: ...
    @abstractmethod
    def tell(self) -> int: ...
    # TODO None should not be compatible with int
    @abstractmethod
    def truncate(self, size: int = ...) -> int: ...
    @abstractmethod
    def writable(self) -> bool: ...
    # TODO buffer objects
    @abstractmethod
    def write(self, s: AnyStr) -> int: ...
    @abstractmethod
    def writelines(self, lines: Iterable[AnyStr]) -> None: ...

    @abstractmethod
    def __iter__(self) -> Iterator[AnyStr]: ...
    @abstractmethod
    def __enter__(self) -> 'IO[AnyStr]': ...
    @abstractmethod
    def __exit__(self, t: type = None, value: BaseException = None, traceback: Any = None) -> bool: ...

class BinaryIO(IO[bytes]):
    # TODO readinto
    # TODO read1?
    # TODO peek?
    @overload
    @abstractmethod
    def write(self, s: bytes) -> int: ...
    @overload
    @abstractmethod
    def write(self, s: bytearray) -> int: ...

    @abstractmethod
    def __enter__(self) -> BinaryIO: ...

class TextIO(IO[str]):
    # TODO use abstractproperty
    @property
    def buffer(self) -> BinaryIO: ...
    @property
    def encoding(self) -> str: ...
    @property
    def errors(self) -> str: ...
    @property
    def line_buffering(self) -> int: ...  # int on PyPy, bool on CPython
    @property
    def newlines(self) -> Any: ... # None, str or tuple
    @abstractmethod
    def __enter__(self) -> TextIO: ...

class ByteString(Sequence[int]): ...

class Match(Generic[AnyStr]):
    pos = 0
    endpos = 0
    lastindex = 0
    lastgroup = ...  # type: AnyStr
    string = ...  # type: AnyStr

    # The regular expression object whose match() or search() method produced
    # this match instance.
    re = ...  # type: 'Pattern[AnyStr]'

    def expand(self, template: AnyStr) -> AnyStr: ...

    @overload
    def group(self, group1: int = ...) -> AnyStr: ...
    @overload
    def group(self, group1: str) -> AnyStr: ...
    @overload
    def group(self, group1: int, group2: int,
              *groups: int) -> Sequence[AnyStr]: ...
    @overload
    def group(self, group1: str, group2: str,
              *groups: str) -> Sequence[AnyStr]: ...

    def groups(self, default: AnyStr = ...) -> Sequence[AnyStr]: ...
    def groupdict(self, default: AnyStr = ...) -> dict[str, AnyStr]: ...
    def start(self, group: Union[int, str] = ...) -> int: ...
    def end(self, group: Union[int, str] = ...) -> int: ...
    def span(self, group: Union[int, str] = ...) -> Tuple[int, int]: ...

class Pattern(Generic[AnyStr]):
    flags = 0
    groupindex = 0
    groups = 0
    pattern = ...  # type: AnyStr

    def search(self, string: AnyStr, pos: int = ...,
               endpos: int = ...) -> Match[AnyStr]: ...
    def match(self, string: AnyStr, pos: int = ...,
              endpos: int = ...) -> Match[AnyStr]: ...
    def split(self, string: AnyStr, maxsplit: int = ...) -> list[AnyStr]: ...
    def findall(self, string: AnyStr, pos: int = ...,
                endpos: int = ...) -> list[Any]: ...
    def finditer(self, string: AnyStr, pos: int = ...,
                 endpos: int = ...) -> Iterator[Match[AnyStr]]: ...

    @overload
    def sub(self, repl: AnyStr, string: AnyStr,
            count: int = ...) -> AnyStr: ...
    @overload
    def sub(self, repl: Callable[[Match[AnyStr]], AnyStr], string: AnyStr,
            count: int = ...) -> AnyStr: ...

    @overload
    def subn(self, repl: AnyStr, string: AnyStr,
             count: int = ...) -> Tuple[AnyStr, int]: ...
    @overload
    def subn(self, repl: Callable[[Match[AnyStr]], AnyStr], string: AnyStr,
             count: int = ...) -> Tuple[AnyStr, int]: ...
