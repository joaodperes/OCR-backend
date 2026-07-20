from .operations import OpCode


class Router:

    def dispatch(self, opcode, payload):

        print()

        print("====================================")
        print("Incoming Operation")
        print("------------------------------------")
        print("Opcode :", opcode)
        print("Payload:", payload)
        print("====================================")

        return {
            "returnCode": 0
        }


router = Router()