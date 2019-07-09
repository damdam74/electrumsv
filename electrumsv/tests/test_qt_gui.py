from typing import Iterable
import unittest

from electrumsv.i18n import _
from electrumsv.bitcoin import COINBASE_MATURITY


class MockWhatever:
    pass


def get_confs_from_height(local_height: int, height: int) -> int:
    return max(local_height - height + 1, 0)


class HistoryListTests(unittest.TestCase):
    def test_get_tx_status(self) -> None:
        from electrumsv.gui.qt.history_list import TxStatus, get_tx_status

        wallet = MockWhatever()
        tx = MockWhatever()
        def _inputs() -> Iterable[MockWhatever]:
            return [ { "type": "notcoinbase" } ]
        tx.inputs = _inputs
        wallet.transactions = { "...": tx }
        local_height = 1000
        def _get_local_height() -> int:
            return local_height
        wallet.get_local_height = _get_local_height
        timestamp = 1 # Ignored

        height = -1 # Legacy unconfirmed parent.
        confs = 0
        status = get_tx_status(wallet, "...", height, confs, timestamp)
        self.assertEqual(TxStatus.UNCONFIRMED, status)

        height = 0
        confs = 0
        status = get_tx_status(wallet, "...", height, confs, timestamp)
        self.assertEqual(TxStatus.UNCONFIRMED, status)

        height = local_height + 1
        confs = get_confs_from_height(local_height, height)
        status = get_tx_status(wallet, "...", height, confs, timestamp)
        self.assertEqual(TxStatus.UNVERIFIED, status)

        height = local_height
        confs = get_confs_from_height(local_height, height)
        status = get_tx_status(wallet, "...", height, confs, timestamp)
        self.assertEqual(TxStatus.FINAL, status)

        height = local_height - 1
        confs = get_confs_from_height(local_height, height)
        status = get_tx_status(wallet, "...", height, confs, timestamp)
        self.assertEqual(TxStatus.FINAL, status)

    def test_get_tx_status_maturity(self) -> None:
        from electrumsv.gui.qt.history_list import TxStatus, get_tx_status

        wallet = MockWhatever()
        tx = MockWhatever()
        def _inputs() -> Iterable[MockWhatever]:
            return [ { "type": "coinbase" } ]
        tx.inputs = _inputs
        wallet.transactions = { "...": tx }
        local_height = 1000
        def _get_local_height() -> int:
            return local_height
        wallet.get_local_height = _get_local_height
        timestamp = confs = 1 # Ignored

        height = (local_height - COINBASE_MATURITY) + 1
        status = get_tx_status(wallet, "...", height, confs, timestamp)
        self.assertEqual(TxStatus.UNMATURED, status)

        height = (local_height - COINBASE_MATURITY)
        status = get_tx_status(wallet, "...", height, confs, timestamp)
        self.assertEqual(TxStatus.FINAL, status)

    def test_get_tx_desc(self) -> None:
        from electrumsv.gui.qt.history_list import TxStatus, TX_STATUS, get_tx_desc
        # Values with a text description should return that text description.
        for status_kind in [ TxStatus.UNCONFIRMED, TxStatus.MISSING ]:
            self.assertEqual(TX_STATUS[status_kind], get_tx_desc(status_kind, 1))
        # Otherwise the timestamp should be used.
        self.assertEqual("1970-01-01 13:00", get_tx_desc(TxStatus.FINAL, 1))
        self.assertEqual(_("unknown"), get_tx_desc(TxStatus.FINAL, False))