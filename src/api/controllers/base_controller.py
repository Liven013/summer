from fastapi import APIRouter

class MetaController(type):
    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)

        if not name.endswith("Controller"):
            raise TypeError("Controller classes must end with 'Controller'")
        
        if name != 'BaseController':
            if (
                (attrs.get('private') is None or not isinstance(attrs['private'], APIRouter))
                and (attrs.get('public') is None or not isinstance(attrs['public'], APIRouter)) 
                or (attrs.get('admin') is None or not isinstance(attrs['admin'], APIRouter))
            ):
                raise TypeError("Controller classes must have 'private', 'public' and 'admin' routers")
        elif not attrs.get('version'):
            raise TypeError("BaseController class must have 'version' attribute")
        
        return new_cls
    
class BaseController(metaclass=MetaController):
    version: int

    public: APIRouter | None = None
    private: APIRouter | None = None
    admin: APIRouter | None = None