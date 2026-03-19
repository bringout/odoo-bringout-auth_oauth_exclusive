# Copyright 2026 bring.out doo Sarajevo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
{
    "name": "OAuth Exclusive Login",
    "version": "16.0.1.0.0",
    "summary": "Hide password login, redirect to OAuth provider",
    "description": "Hides the password form on the login page and auto-redirects to the configured OAuth/OIDC provider.",
    "author": "bring.out doo Sarajevo",
    "website": "https://bring.out.ba",
    "license": "AGPL-3",
    "depends": ["auth_oauth"],
    "data": ["views/webclient_templates.xml"],
    "installable": True,
    "application": False,
}
