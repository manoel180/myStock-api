# app.include_router(user_router)
URLS = [
    #Users
    'routers.user.find_all.user_router',
    'routers.user.save.router',
    'routers.user.update.user_router',
    'routers.user.delete.user_router',

    #Auth
    'routers.auth.login.auth_router',

    #Category
    'routers.category.find_all.router',
    'routers.category.save.router',
    'routers.category.update.router',
    'routers.category.delete.router',

    #Product
    'routers.product.find_all.router',
    'routers.product.save.router',
    'routers.product.update.router',
    'routers.product.delete.router',
    'routers.product.get_id.router',
    
    #ws
    'routers.websocket.websocket.router'
]