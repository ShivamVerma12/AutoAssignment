def create_workspace(cnvrg, workspace_name, project_name):
    myproj = cnvrg.projects.get(project_name)
    workspace = myproj.workspaces.create(title=workspace_name,
                                         templates=["small", "worker.medium"],
                                         notebook_type='jupyterlab')


def verify_workspace(cnvrg, workspace_name, project_name):
    myproj = cnvrg.projects.get(project_name)
    workspace = myproj.workspaces.get(workspace_name)
    if workspace:
        return True
    else:
        return False
