using System.Data.SQLite;
using System.Windows;
using static bazPlannerWPF.DBConnect;

namespace bazPlannerWPF
{
    public class Project
    {
        public string nameProject;
        public string ownerProject;
        public string dateProject;
        

        static public void InsertProject()
        {
            command = new SQLiteCommand(connection)
            {
                CommandText = $"INSERT INTO project(name_project, owner_project, date_project) VALUES ('asdsad', 2, '12.07.2022')" //переделать! INSERT INTO tbl_name VALUES(expr, expr)
            };
            command.ExecuteNonQuery();
        }

        static public void SelectProject()
        {
            command = new SQLiteCommand(connection)
            {
                CommandText = $"SELECT name_project FROM project WHERE owner_project=2" //переделать!
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
