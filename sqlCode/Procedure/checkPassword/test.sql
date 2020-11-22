call loginWithUsernamePassword('nine','1234',@response);

select @response;
-- encrypted user
--------------------------------------------------------------------------------

call loginWithUsernamePassword('5678','12345',@response);

select @response;
-- non encrypted user