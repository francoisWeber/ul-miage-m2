# jupyterhub_config.py

c = get_config()

# Use PAMAuthenticator to authenticate system users
from jupyterhub.auth import PAMAuthenticator

c.JupyterHub.authenticator_class = PAMAuthenticator

c.LocalAuthenticator.create_system_users = True

# Set the JupyterHub IP and port
c.JupyterHub.bind_url = "http://:8000"

# Specify the JupyterHub cookie secret file
c.JupyterHub.cookie_secret_file = "/srv/jupyterhub/jupyterhub_cookie_secret"

# Set the database file for JupyterHub
c.JupyterHub.db_url = "sqlite:////srv/jupyterhub/jupyterhub.sqlite"

# Configuration for the JupyterHub spawner
c.Spawner.default_url = "/lab"

# Admin users (replace with actual system user names)
c.Authenticator.admin_users = {"admin_user", "francois.weber"}

# Allowed users (replace with actual system user names)
c.Authenticator.whitelist = {"user1", "user2", "francois.weber"}
