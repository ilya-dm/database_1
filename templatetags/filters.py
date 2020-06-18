from django import template
register = template.Library()


# @register.filter
# def render_filter(catalog):
#     counter = 1
#     for i in catalog:
#         if counter % 2 == 0:
#             return """<tr> <td>
#
#             </td></tr>
#             """
#
#
#         counter += 1
