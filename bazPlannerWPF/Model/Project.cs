using System.Data.SQLite;
using System.Windows;
using static bazPlannerWPF.DBConnect;

namespace bazPlannerWPF
{
    public class Project
    {
        public string nameProject  = default;
        public string ownerProject = default;
        public string dateProject  = default;
        

        static public void InsertProject(string nameProject, string ownerProject)
        {
            command = new SQLiteCommand(connection)
            {
                CommandText = $"INSERT INTO project(name_project, owner_project, date_project) VALUES ('{nameProject}', " +
                $"(SELECT id_owner FROM owner WHERE name_owner = '{ownerProject}'), '15.07.2022')" //переделать! INSERT INTO tbl_name VALUES(expr, expr)
            };
            command.ExecuteNonQuery();
        }

        static public void SelectProject(string nameOwner)
        {
            command = new SQLiteCommand(connection)
            {
                CommandText = $"SELECT name_project FROM project, owner WHERE project.owner_project = owner.id_owner"
            };
            SQLiteDataReader reader = command.ExecuteReader();
            if (reader.HasRows)
            {
                while (reader.Read())
                {
                    ((MainWindow)Application.Current.MainWindow).listElements.Items.Add(reader[0].ToString());
                }
            }
        }
    }
}
