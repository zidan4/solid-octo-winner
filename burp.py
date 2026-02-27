class BHPFuzzer(IIntruderPayloadGenerator):
  def __init__(self, extender, attack):
    self._extender = extender
    self._helpers = extender._helpers
    self._attack = attack
    
    self.max_payloads = 10
    self.num_iterations = 0
    return
    
  def hasMorePayloads(self):
    if self.num_iterations == self.max_payloads:
      return False
    else:
      return True
      
  def getNextPayload(self,current_payload):
    # convert into a string
    payload = "".join(chr(x) for x in current_payload)
    # call our simple mutator to fuzz the POST
    payload = self.mutate_payload(payload)
    # increase the number of fuzzing attempts
    self.num_iterations += 1
    return payload
    
  def reset(self):
    self.num_iterations = 0
    return
