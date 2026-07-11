# Copyright (c) 2026, Jhon Biancent and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LibraryTransaction(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		article: DF.Link
		date: DF.Date
		library_member: DF.Link
		type: DF.Literal["Issue", "Return"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Library Transaction"
