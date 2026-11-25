from pydantic_settings import BaseSettings ,  SettingsConfigDict

class confingdata(BaseSettings):
    databasename : str
    port:int
    #str?
    databasepassword : str
    databaseusername : str
    databasehost : str
    seRect_key : str
    aLGORITHM : str
    Xxpier_token_time : int
    
    model_config = SettingsConfigDict(env_file=".env")

coonfig = confingdata()