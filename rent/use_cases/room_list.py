
#  RespoRespoResp

from rent.responses import ResponseSuccess
def room_list_use_case(repo, request):
    rooms= repo.list()
    return ResponseSuccess(rooms)