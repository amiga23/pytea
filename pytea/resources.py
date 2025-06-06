resources = {
    u'/orgs': {
        u'post': {
            "parameters": {
                u'body': False
            }
        }
    },
    u'/orgs/{org}': {
        u'get': {
            'parameters': {
                u'org': True
            }
        },
        u'patch': {
            'parameters': {
                u'body': False,
                u'org': True
            }
        },
        u'delete': {
            'parameters': {
                u'org': True
            }
        }
    },
    u'/orgs/{org}/actions/secrets': {
        u'get': {
            'parameters': {
                u'body': False,
                u'org': True
            }
        }
    },
    u'/orgs/{org}/actions/secrets/{secretname}': {
        u'put': {
            'parameters': {
                u'org': True,
                u'secretname': True
            }
        },
        u'delete': {
            'parameters': {
                u'body': False,
                u'org': True,
                u'secretname': True
            }
        }
    },
    u'/orgs/{org}/hooks': {
        u'get': {
            'parameters': {}
        }
    },
    u'/orgs/{org}/hooks/': {
        u'post': {
            'parameters': {}
        }
    },
    u'/orgs/{org}/hooks/{id}': {
        u'get': {
            'parameters': {}
        },
        u'delete': {
            'parameters': {}
        },
        u'patch': {
            'parameters': {}
        }
    },
    u'/orgs/{org}/members': {
        u'get': {
            'parameters': {
                u'org': True
            }
        }
    },
    u'/orgs/{org}/members/{username}': {
        u'get': {
            'parameters': {
                u'username': True,
                u'org': True
            }
        },
        u'delete': {
            'parameters': {
                u'username': True,
                u'org': True
            }
        }
    },
    u'/orgs/{org}/public_members': {
        u'get': {
            'parameters': {
                u'org': True
            }
        }
    },
    u'/orgs/{org}/public_members/{username}': {
        u'put': {
            'parameters': {
                u'username': True,
                u'org': True
            }
        },
        u'get': {
            'parameters': {
                u'username': True,
                u'org': True
            }
        },
        u'delete': {
            'parameters': {
                u'username': True,
                u'org': True
            }
        }
    },
    u'/orgs/{org}/repos': {
        u'get': {
            'parameters': {
                u'org': True
            }
        }
    },
    u'/orgs/{org}/teams': {
        u'post': {
            'parameters': {
                u'body': False,
                u'org': True
            }
        },
        u'get': {
            'parameters': {
                u'org': True
            }
        }
    },
    u'/user/times': {
        u'get': {
            'parameters': {}
        }
    },
    u'/repos/{owner}/{repo}/issues/{index}/times': {
        u'post': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False,
                u'id': True
            }
        },
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True
            }
        }
    },
    u'/repos/{owner}/{repo}/statuses/{sha}': {
        u'post': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False,
                u'sha': True
            }
        },
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'sha': True
            }
        }
    },
    u'/users/search': {
        u'get': {
            'parameters': {
                u'q': False,
                u'limit': False
            }
        }
    },
    u'/repos/{owner}/{repo}/branches/{branch}': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'branch': True
            }
        }
    },
    u'/users/{username}/repos': {
        u'get': {
            'parameters': {
                u'username': True
            }
        }
    },
    u'/repos/{owner}/{repo}/issues/comments/{id}': {
        u'delete': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'id': True
            }
        },
        u'patch': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False,
                u'id': True
            }
        }
    },
    u'/admin/users/{username}/orgs': {
        u'post': {
            'parameters': {
                u'username': True
            }
        }
    },
    u'/user/gpg_keys': {
        u'post': {
            'parameters': {
                u'Form': False
            }
        },
        u'get': {
            'parameters': {}
        }
    },
    u'/repos/{owner}/{repo}/keys/{id}': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'id': True
            }
        },
        u'delete': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'id': True
            }
        }
    },
    u'/repos/{owner}/{repo}/keys': {
        u'post': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False
            }
        },
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True
            }
        }
    },
    u'/teams/{id}': {
        u'get': {
            'parameters': {
                u'id': True
            }
        },
        u'delete': {
            'parameters': {
                u'id': True
            }
        },
        u'patch': {
            'parameters': {
                u'body': False,
                u'id': True
            }
        }
    },
    u'/user/gpg_keys/{id}': {
        u'get': {
            'parameters': {
                u'id': True
            }
        },
        u'delete': {
            'parameters': {
                u'id': True
            }
        }
    },
    u'/repos/{owner}/{repo}': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True
            }
        },
        u'delete': {
            'parameters': {
                u'owner': True,
                u'repo': True
            }
        }
    },
    u'/repos/{owner}/{repo}/times': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True
            }
        }
    },
    u'/users/{username}/tokens': {
        u'post': {
            'parameters': {
                u'body': False
            }
        },
        u'get': {
            'parameters': {}
        }
    },
    u'/user/following/{username}': {
        u'put': {
            'parameters': {
                u'username': True
            }
        },
        u'delete': {
            'parameters': {
                u'username': True
            }
        }
    },
    u'/teams/{id}/repos': {
        u'get': {
            'parameters': {
                u'id': True
            }
        }
    },
    u'/markdown/raw': {
        u'post': {
            'parameters': {
                u'body': False
            }
        }
    },
    u'/users/{username}/followers': {
        u'get': {
            'parameters': {
                u'username': True
            }
        }
    },
    u'/repos/{owner}/{repo}/releases': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False
            }
        }
    },
    u'/teams/{id}/members/{username}': {
        u'put': {
            'parameters': {
                u'username': True,
                u'id': True
            }
        },
        u'delete': {
            'parameters': {
                u'username': True,
                u'id': True
            }
        }
    },
    u'/repos/{owner}/{repo}/milestones': {
        u'post': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False
            }
        },
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'id': True
            }
        }
    },
    u'/repos/{owner}/{repo}/collaborators': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True
            }
        }
    },
    u'/repos/{owner}/{repo}/releases/{id}': {
        u'delete': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'id': True
            }
        },
        u'patch': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False,
                u'id': True
            }
        }
    },
    u'/repos/{owner}/{repo}/subscription': {
        u'put': {
            'parameters': {
                u'owner': True,
                u'repo': True
            }
        },
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True
            }
        },
        u'delete': {
            'parameters': {
                u'owner': True,
                u'repo': True
            }
        }
    },
    u'/repos/{owner}/{repo}/issues/comments': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'string': False
            }
        }
    },
    u'/teams/{id}/members': {
        u'get': {
            'parameters': {
                u'id': True
            }
        }
    },
    u'/repos/{owner}/{repo}/raw/{filepath}': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'filepath': True
            }
        }
    },
    u'/repos/{owner}/{repo}/issue/{index}/labels/{id}': {
        u'delete': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'id': True,
                u'index': True
            }
        }
    },
    u'/repos/{owner}/{repo}/branches': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True
            }
        }
    },
    u'/users/{username}': {
        u'get': {
            'parameters': {
                u'username': True
            }
        }
    },
    u'/user/orgs': {
        u'get': {
            'parameters': {}
        }
    },
    u'/repos/{owner}/{repo}/hooks': {
        u'post': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False
            }
        },
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True
            }
        }
    },
    u'/repos/{owner}/{repo}/subscribers': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True
            }
        }
    },
    u'/admin/users': {
        u'post': {
            'parameters': {
                u'body': False
            }
        }
    },
    u'/users/{username}/following': {
        u'get': {
            'parameters': {
                u'username': True
            }
        }
    },
    u'/repos/{owner}/{repo}/mirror-sync': {
        u'post': {
            'parameters': {
                u'owner': True,
                u'repo': True
            }
        }
    },
    u'/repos/{owner}/{repo}/editorconfig/{filepath}': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'filepath': True
            }
        }
    },
    u'/user/following': {
        u'get': {
            'parameters': {}
        }
    },
    u'/admin/users/{username}/repos': {
        u'post': {
            'parameters': {
                u'username': True
            }
        }
    },
    u'/repos/{owner}/{repo}/issue/{index}/labels': {
        u'put': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False,
                u'index': True
            }
        },
        u'post': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False,
                u'index': True
            }
        },
        u'delete': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'index': True
            }
        }
    },
    u'/repos/{owner}/{repo}/pulls/{index}/merge': {
        u'post': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'index': True
            }
        },
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'index': True
            }
        }
    },
    u'/user/repos': {
        u'post': {
            'parameters': {
                u'body': False
            }
        },
        u'get': {
            'parameters': {}
        }
    },
    u'/users/{follower}/following/{followee}': {
        u'get': {
            'parameters': {
                u'follower': True,
                u'followee': True
            }
        }
    },
    u'/repos/{owner}/{repo}/collaborators/{collaborator}': {
        u'put': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False,
                u'collaborator': True
            }
        },
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'collaborator': True
            }
        },
        u'delete': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'collaborator': True
            }
        }
    },
    u'/user/keys': {
        u'post': {
            'parameters': {
                u'body': False
            }
        },
        u'get': {
            'parameters': {}
        }
    },
    u'/repos/{owner}/{repo}/times/{tracker}': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'user': True
            }
        }
    },
    u'/repos/search': {
        u'get': {
            'parameters': {
                u'exclusive': False,
                u'uid': False,
                u'q': False,
                u'limit': False,
                u'mode': False,
                u'page': False
            }
        }
    },
    u'/users/{username}/gpg_keys': {
        u'get': {
            'parameters': {
                u'username': True
            }
        }
    },
    u'/user/subscriptions': {
        u'get': {
            'parameters': {}
        }
    },
    u'/markdown': {
        u'post': {
            'parameters': {
                u'body': False
            }
        }
    },
    u'/repos/{owner}/{repo}/issue/{index}/comments': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'id': True,
                u'string': False
            }
        }
    },
    u'/user/emails': {
        u'post': {
            'parameters': {
                u'body': False
            }
        },
        u'get': {
            'parameters': {}
        },
        u'delete': {
            'parameters': {
                u'body': False
            }
        }
    },
    u'/repos/{owner}/{repo}/issues': {
        u'post': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False
            }
        },
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'state': False,
                u'page': False
            }
        }
    },
    u'/user/following/{followee}': {
        u'get': {
            'parameters': {
                u'followee': True
            }
        }
    },
    u'/user/{username}/orgs': {
        u'get': {
            'parameters': {
                u'username': False
            }
        }
    },
    u'/repos/migrate': {
        u'post': {
            'parameters': {
                u'body': False
            }
        }
    },
    u'/users/{username}/subscriptions': {
        u'get': {
            'parameters': {
                u'username': False
            }
        }
    },
    u'/user/starred/{owner}/{repo}': {
        u'put': {
            'parameters': {
                u'owner': True,
                u'repo': True
            }
        },
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True
            }
        },
        u'delete': {
            'parameters': {
                u'owner': True,
                u'repo': True
            }
        }
    },
    u'/repos/{owner}/{repo}/hooks/{id}': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'id': True
            }
        },
        u'patch': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False
            }
        }
    },
    u'/repos/{owner}/{repo}/archive/{filepath}': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'archive': True
            }
        }
    },
    u'/repos/{owner}/{repo}/stargazers': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True
            }
        }
    },
    u'/user/keys/{id}': {
        u'get': {
            'parameters': {
                u'id': True
            }
        },
        u'delete': {
            'parameters': {
                u'id': True
            }
        }
    },
    u'/user': {
        u'get': {
            'parameters': {}
        }
    },
    u'/admin/users/{username}': {
        u'delete': {
            'parameters': {
                u'username': True
            }
        },
        u'patch': {
            'parameters': {
                u'username': True,
                u'body': False
            }
        }
    },
    u'/repos/{owner}/{repo}/milestones/{id}': {
        u'get': {
            'parameters': {}
        },
        u'delete': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': True
            }
        },
        u'patch': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False
            }
        }
    },
    u'/admin/users/{username}/keys': {
        u'post': {
            'parameters': {
                u'username': True
            }
        }
    },
    u'/repos/{owner}/{repo}/commits/{ref}/statuses': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'ref': True
            }
        }
    },
    u'/users/{username}/keys': {
        u'get': {
            'parameters': {
                u'username': True
            }
        }
    },
    u'/repos/{owner}/{repo}/labels': {
        u'post': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False
            }
        },
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True
            }
        }
    },
    u'/repos/{owner}/{repo}/issues/{index}': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'index': True
            }
        },
        u'patch': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False,
                u'index': True
            }
        }
    },
    u'/repos/{owner}/{repo}/issues/{index}/labels': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'index': True
            }
        }
    },
    u'/repos/{owner}/{repo}/forks': {
        u'post': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False
            }
        },
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True
            }
        }
    },
    u'/repos/{owner}/{repo}/pulls': {
        u'post': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False
            }
        },
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True
            }
        }
    },
    u'/user/starred': {
        u'get': {
            'parameters': {}
        }
    },
    u'/repos/{owner}/{repo}/pulls/{index}': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'index': True
            }
        },
        u'patch': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False,
                u'index': True
            }
        }
    },
    u'/repos/{owner}/{repo}/labels/{id}': {
        u'get': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'id': True
            }
        },
        u'delete': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'id': True
            }
        },
        u'patch': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False,
                u'id': True
            }
        }
    },
    u'/repositories/{id}': {
        u'get': {
            'parameters': {
                u'id': True
            }
        }
    },
    u'/repos/{user}/{repo}/hooks/{id}': {
        u'delete': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'id': True
            }
        }
    },
    u'/repos/{owner}/{repo}/issues/{index}/comments': {
        u'post': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False,
                u'id': True
            }
        }
    },
    u'/admin/users/{username}/keys/{id}': {
        u'delete': {
            'parameters': {
                u'username': True,
                u'id': True
            }
        }
    },
    u'/users/{username}/starred': {
        u'get': {
            'parameters': {
                u'username': True
            }
        }
    },
    u'/user/followers': {
        u'get': {
            'parameters': {}
        }
    },
    u'/repos/{owner}/{repo}/issues/{index}/comments/{id}': {
        u'delete': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'id': True,
                u'index': True
            }
        },
        u'patch': {
            'parameters': {
                u'owner': True,
                u'repo': True,
                u'body': False,
                u'id': True,
                u'index': True
            }
        }
    },
    u'/teams/{id}/repos/{org}/{repo}': {
        u'put': {
            'parameters': {
                u'repo': True,
                u'org': True,
                u'id': True
            }
        },
        u'delete': {
            'parameters': {
                u'repo': True,
                u'org': True,
                u'id': True
            }
        }
    },
    u'/version': {
        u'get': {
            'parameters': {}
        }
    }
}
