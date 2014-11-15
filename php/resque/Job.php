<?php

class Job
{
    public function perform()
    {
        try {
            $url = sprintf('https://api.github.com/users/%s/repos', $this->args['username']);
            $client = new Guzzle\Http\Client();

            // Make the request
            $request = $client->get($url);
            $response = $request->send();

            // Print the number of a repositories for the user
            echo count($response->json());
        } catch (\Exception $e) {
            echo $e->getMessage();
        }
    }
}
