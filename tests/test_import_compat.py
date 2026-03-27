#!/usr/bin/env python3

import os
import subprocess
import sys
import unittest


class TestImportCompatibility(unittest.TestCase):
    def test_import_creates_current_event_loop_when_missing(self):
        repo_root = os.path.dirname(os.path.dirname(__file__))
        env = dict(os.environ)
        env["PYTHONPATH"] = repo_root + os.pathsep + env.get("PYTHONPATH", "")

        proc = subprocess.run(
            [
                sys.executable,
                "-c",
                (
                    "import asyncio; "
                    "asyncio.set_event_loop(None); "
                    "import farc; "
                    "assert farc.Framework._event_loop is asyncio.get_event_loop()"
                ),
            ],
            env=env,
            capture_output=True,
            text=True,
        )

        self.assertEqual(proc.returncode, 0, msg=proc.stderr)


if __name__ == '__main__':
    unittest.main()
