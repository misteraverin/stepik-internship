-- example dynamic request script which demonstrates changing
-- the request path for each request
-------------------------------------------------------------
-- NOTE: each wrk thread has an independent Lua scripting
-- context and thus there will be one counter per thread

counter = 0

request = function()
   path = "/api/steps/lesson=" .. counter
   counter = counter + 1
   return wrk.format(nil, path)
end
