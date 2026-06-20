# Copyright 2026 bring.out doo Sarajevo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
{
    "name": "OAuth Exclusive Login",
    "version": "19.0.1.0.5",
    "summary": "Show only the OAuth/SSO login button, hide the password form",
    "description": "Forces the login form visible (v19 ships it d-none, revealed by JS) and hides everything except the OAuth provider buttons, so the login page offers SSO only — working even if the frontend JS that reveals the form fails.",
    "author": "bring.out doo Sarajevo",
    "website": "https://bring.out.ba",
    "license": "AGPL-3",
    "depends": ["auth_oauth"],
    "data": ["views/webclient_templates.xml"],
    "installable": True,
    "application": False,
}
