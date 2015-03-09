package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"runtime"
	"sort"
	"sync"
)

const GITHUB_USERNAME = "django"
const GITHUB_REPO = "django"
const CONTRIBUTORS_URL = "https://api.github.com/repos/%s/%s/contributors"
const REPOS_URL = "https://api.github.com/users/%s/repos"

type ContribPair struct {
	Key   string
	Value int32
}

type Pairs []ContribPair

func (p Pairs) Len() int {
	return len(p)
}

func (p Pairs) Swap(x, y int) {
	p[x], p[y] = p[y], p[x]
}

func (p Pairs) Less(x, y int) bool {
	return p[x].Value > p[y].Value
}

func SortContribs(p Pairs) Pairs {
	sort.Sort(p)
	return p
}

type Owner struct {
	Login               string `json:"login"`
	Id                  int32  `json:"id"`
	Avatar_url          string `json:"avatar_url"`
	Gravatar_id         string `json:"gravatar_id"`
	Url                 string `json:"url"`
	Html_url            string `json:"html_url"`
	Followers_url       string `json:"followers_url"`
	Following_url       string `json:"following_url"`
	Gists_url           string `json:"gists_url"`
	Starred_url         string `json:"starred_url"`
	Subscriptions_url   string `json:"subscriptions_url"`
	Organizations_url   string `json:"organizations_url"`
	Repos_url           string `json:"repos_url"`
	Events_url          string `json:"events_url"`
	Received_events_url string `json:"received_events_url"`
	Owner_type          string `json:"type"`
	Site_admin          bool   `json:"site_admin"`
}

type Repo struct {
	id                int32  `json:"id"`
	Name              string `json:"name"`
	Full_name         string `json:"full_name"`
	Owner             Owner  `json:"owner"`
	Private           bool   `json:"private"`
	Html_url          string `json:"html_url"`
	Description       string `json:"description"`
	Fork              bool   `json:"fork"`
	Url               string `json:"url"`
	Forks_url         string `json:"forks_url"`
	Keys_url          string `json:"keys_url"`
	Collaborators_url string `json:"collaborators_url"`
	Teams_url         string `json:"teams_url"`
	Hooks_url         string `json:"hooks_url"`
	Issue_events_url  string `json:"issue_events_url"`
	Events_url        string `json:"events_url"`
	Assignees_url     string `json:"assignees_url"`
	Branches_url      string `json:"branches_url"`
	Tags_url          string `json:"tags_url"`
	Blobs_url         string `json:"blobs_url"`
	Git_tags_url      string `json:"git_tags_url"`
	Git_refs_url      string `json:"git_refs_url"`
	Trees_url         string `json:"trees_url"`
	Statuses_url      string `json:"statuses_url"`
	Languages_url     string `json:"languages_url"`
	Stargazers_url    string `json:"stargazers_url"`
	Contributors_url  string `json:"contributors_url"`
	Subscribers_url   string `json:"subscribers_url"`
	Subscription_url  string `json:"subscription_url"`
	Commits_url       string `json:"commits_url"`
	Git_commits_url   string `json:"git_commits_url"`
	Comments_url      string `json:"comments_url"`
	Issue_comment_url string `json:"issue_comment_url"`
	Contents_url      string `json:"contents_url"`
	Compare_url       string `json:"compare_url"`
	Merges_url        string `json:"merges_url"`
	Archive_url       string `json:"archive_url"`
	Downloads_url     string `json:"downloads_url"`
	Issues_url        string `json:"issues_url"`
	Pulls_url         string `json:"pulls_url"`
	Milestones_url    string `json:"milestones_url"`
	Notifications_url string `json:"notifications_url"`
	Labels_url        string `json:"labels_url"`
	Releases_url      string `json:"releases_url"`
	Created_at        string `json:"created_at"`
	Updated_at        string `json:"updated_at"`
	Pushed_at         string `json:"pushed_at"`
	Git_url           string `json:"git_url"`
	Ssh_url           string `json:"ssh_url"`
	Clone_url         string `json:"clone_url"`
	Svn_url           string `json:"svn_url"`
	Homepage          string `json:"homepage"`
	Size              int32  `json:"size"`
	Stargazers_count  int32  `json:"stargazers_count"`
	Watchers_count    int32  `json:"watchers_count"`
	Language          string `json:"language"`
	Has_issues        bool   `json:"has_issues"`
	Has_downloads     bool   `json:"has_downloads"`
	Has_wiki          bool   `json:"has_wiki"`
	Has_pages         bool   `json:"has_pages"`
	Forks_count       int32  `json:"forks_count"`
	Mirror_url        string `json:"mirror_url"`
	Open_issues_count int32  `json:"open_issues_count"`
	Forks             int32  `json:"forks"`
	Open_issues       int32  `json:"open_issues"`
	Watchers          int32  `json:"watchers"`
	Default_branch    string `json:"default_branch"`
}

type Contributor struct {
	Login               string `json:"login"`
	Id                  int32  `json:"id"`
	Avatar_url          string `json:"avatar_url"`
	Gravatar_id         string `json:"gravatar_id"`
	Url                 string `json:"url"`
	Html_url            string `json:"html_url"`
	Followers_url       string `json:"followers_url"`
	Following_url       string `json:"following_url"`
	Gists_url           string `json:"gists_url"`
	Starred_url         string `json:"starred_url"`
	Subscriptions_url   string `json:"subscriptions_url"`
	Organizations_url   string `json:"organizations_url"`
	Repos_url           string `json:"repos_url"`
	Events_url          string `json:"events_url"`
	Received_events_url string `json:"received_events_url"`
	Type                string `json:"type"`
	Site_admin          bool   `json:"site_admin"`
	Contributions       int32  `json:"contributions"`
}

func HandleError(err error) {
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}

func main() {
	runtime.GOMAXPROCS(runtime.NumCPU())

	cwg := sync.WaitGroup{}

	// Fetch all contributors to project
	// Spin up goroutine for each to get stargazers
	// Combine into map

	// Request contributors
	resp, err := http.Get(fmt.Sprintf(CONTRIBUTORS_URL, GITHUB_USERNAME, GITHUB_REPO))
	HandleError(err)

	// Read contributor data
	defer resp.Body.Close()
	data, err := ioutil.ReadAll(resp.Body)
	HandleError(err)

	// Create contributor objects
	var contr []Contributor
	json_err := json.Unmarshal(data, &contr)
	HandleError(json_err)

	// Define channel to hold contribs
	contribs := make(chan ContribPair, len(contr))

	// Process each contributor concurrently finding total stargazers
	for _, c := range contr {
		cwg.Add(1)
		go func(c Contributor) {
			defer cwg.Done()
			rwg := sync.WaitGroup{}

			// Make request
			resp, err := http.Get(fmt.Sprintf(REPOS_URL, c.Login))
			HandleError(err)

			// Read response data
			defer resp.Body.Close()
			data, err := ioutil.ReadAll(resp.Body)
			HandleError(err)

			// Convert JSON to Objects
			var repos []Repo
			json_err := json.Unmarshal(data, &repos)
			HandleError(json_err)

			// Define channel
			reps := make(chan int32, len(repos))
			owner := repos[0].Owner.Login

			// Process each repo concurrently
			for _, repo := range repos {
				rwg.Add(1)
				go func(repo Repo) {
					defer rwg.Done()
					reps <- repo.Stargazers_count
				}(repo)
			}

			// Close our channel and WaitGroup at the end
			rwg.Wait()
			close(reps)

			// Total the values
			var total int32
			for v := range reps {
				total += v
			}

			contribs <- ContribPair{Key: owner, Value: total}
		}(c)
	}

	// Close our channel and WaitGroup at the end
	cwg.Wait()
	close(contribs)

	var p Pairs

	for c := range contribs {
		p = append(p, c)
	}

	sorted := SortContribs(p)

	fmt.Printf("Contributors to %s/%s With the Most Personal Starred Repos\n\n", GITHUB_USERNAME, GITHUB_REPO)
	for i, v := range sorted {
		fmt.Printf("%d. %s has %d stars across all their repos\n", i, v.Key, v.Value)
	}
}
