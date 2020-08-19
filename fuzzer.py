# from ast_api import AST_API
# from models.UnitTestDataContainer import UnitTestDataContainer
from misc import FUZZ_DIR


class ZyFuzzer(object):
	def __init__(self, _cls_unit_model):
		super(ZyFuzzer, self).__init__()
		self.cls_unit_model = _cls_unit_model
		self.out_path = FUZZ_DIR

		# maybe new enviroment?

	def mutate(self):
		# radamsa, bleb bindings?
		pass

	def code_transform(self):
		# calls to ast_api, then mutate call?
		pass
		


