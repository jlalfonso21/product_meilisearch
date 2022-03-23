from odoo import models, fields


class MeiliSearchConfigWizard(models.TransientModel):
    _inherit = "res.config.settings"

    config_msearch_service_url = fields.Char(
        "Meili Search Service URL", config_parameter="msearch.service.url"
    )

    config_msearch_service_api_key = fields.Char(
        "Meili Search Service API KEY", config_parameter="msearch.service.apikey"
    )

    config_msearch_product_index = fields.Char(
        "Meili Search Service Product Index",
        config_parameter="msearch.service.product.index",
        default="products",
    )
