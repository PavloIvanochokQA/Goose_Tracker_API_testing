

HOST = "https://goose-tracker-backend.p.goit.global"


class Endpoints:
    
    user_registration = f"{HOST}/user/register"
    user_authentication = f"{HOST}/user/login"
    logout = f"{HOST}/user/logout"
    refresh_tokens = f"{HOST}/user/refresh"
    get_user_info = f"{HOST}/user/info"
    update_user_info = f"{HOST}/user/update"
