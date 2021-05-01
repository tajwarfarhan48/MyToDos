class ToDo:
    """
    ALL TODOS WILL BE STORED AS INSTANCES OF THIS CLASS.

    THE 'ID' PROPERTY IS THE UNIQUE IDENTIFIER FOR EACH ID (BETWEEN 1 AND 999). THIS WILL BE USED TO FILTER A SPECIFIC ID IN THE PROGRAM.
    THE 'CONTENTS' PROPERTY CONTAINS THE USER-INPUTTED PART
    THE 'DONE' PROPERTY INDICATES WHETHER THE ACTION IS COMPLETE OR INCOMPLETE. 1 INDICATES THAT THE ACTION IS DONE, WHILE 0 INDICATES THAT IT IS INCOMPLETE.
    """
    def __init__(self, todo_id, contents, done):
        self.id = todo_id
        self.contents = contents
        self.done = done
