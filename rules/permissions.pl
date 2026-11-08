allowed(read_public).
allowed(write_draft).
permitted(Action) :- allowed(Action).
