import unittest
from chain.block import Block
from transaction.transaction import CommitRandomTransaction, RevealRandomTransaction
from crypto.enc_random import enc_part_random
from Crypto.Hash import SHA256

class TestTransaction(unittest.TestCase):

    def test_pack_parse_commit_transaction(self):
        original = CommitRandomTransaction()
        data, _ = enc_part_random(SHA256.new(b"era_hash").digest())
        original.rand = data

        raw = original.pack()
        restored = CommitRandomTransaction()
        restored.parse(raw)

        self.assertEqual(original.get_hash().digest(), restored.get_hash().digest())

    def test_pack_parse_reveal_transaction(self):
        original = RevealRandomTransaction()
        original.commit_hash = SHA256.new(b"previous_transaction").digest()
        original.key = b'i\xe4O\xf2\xb9\xdd\x80\x8e"\x8f\xfa\xa5\x82\xa9\xa6\x80\xb7\xd6\xc7\x0f\x84\x9b\x97.\x05\xe1nj9G(\xe5\xef\xf2\xbeM\xf3\x96\t\xca\xaa\x17\xd5\xa8^%\x00N\x8fm\xb4\xc3\x12~\xdf\xd9+\x89\xe5\x17+\xadN\x86>\x8ek\x87Fq\xea_\x9c\xcdD\x97\xd6\xb9\xadb\xc3)h\xb9b\x82m_\xf5\x97+-&\xfd\xa22:\x08_%\xda\xb1\xaa\x89\x1f\x8a3\x18=O\x8dzMi\x16\xc1\x81\xd8H\x12\xa3\x9e\x9b\n\xa3m\x16x'

        raw = original.pack()
        restored = CommitRandomTransaction()
        restored.parse(raw)

        self.assertEqual(original.get_hash().digest(), restored.get_hash().digest())        
