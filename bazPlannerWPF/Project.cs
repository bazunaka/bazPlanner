using System;
using System.Collections.Generic;
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
        

        public void InsertProject(string nameProject, string ownerProject, string dateProject)
        {
            //SQL Insert into table
        }

        static public void SelectProject()
        {
            command = new SQLiteCommand(connection)
            {
                CommandText = $"SELECT name_project FROM project WHERE owner_project=2" //переделать!
            };
            SQLiteDataReader reader = command.ExecuteReader();
            //List<string> listProject = new List<string>();
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
