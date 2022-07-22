using System;
using System.Windows;
using System.Data.SQLite;
using System.Diagnostics;
using bazPlanner.Forms;
using System.Collections.Generic;
using System.Data;

namespace bazPlanner.Models
{
    class Database
    {
        public static SQLiteConnection? connection;
        public static SQLiteCommand? command;
        //Create connection. 
        static public bool Connect()
        {
            try
            {
                connection = new SQLiteConnection("Data Source=test.db; Version=3; FailIfMissing=False");
                connection.Open();
                Debug.WriteLine("Connected!");
                return true;
            }
            catch (SQLiteException ex)
            {
                Debug.WriteLine($"Ошибка доступа к базе данных. Исключение: {ex.Message}");
                return false;
            }
            
        }
        
        //Select owner for auth.
        static public int SelectOwner(string OwnerName, string OwnerPass)
        {
            string nameLower = OwnerName.ToLower();
            string passLower = OwnerPass.ToLower(); 
            command = new SQLiteCommand(connection)
            {
                CommandText = $"SELECT * FROM Owners WHERE OwnerName = '{nameLower}' AND OwnerPass = '{passLower}'"
            };
            int cnt = command.ExecuteReader().StepCount;
            return cnt;
        }

        //Select owner for insert new task.
        static public string SelectOwner(string ProjectName)
        {
            string projectID = "";
            command = new SQLiteCommand(connection)
            {
                CommandText = $"SELECT Projects.ProjectID FROM Projects WHERE Projects.ProjectName = '{ProjectName}'"
            };
            SQLiteDataReader reader = command.ExecuteReader();
            if (reader.HasRows)
            {
                while (reader.Read())
                {
                    projectID = reader.GetValue(0).ToString();
                }                  
            }
            return projectID;
        }

        //Select projects.
        static public bool SelectProjects(string OwnerName)
        {
            command = new SQLiteCommand(connection)
            {
                CommandText = $"SELECT Projects.ProjectName FROM Projects INNER JOIN Owners ON Projects.ProjectOwner = Owners.OwnerID WHERE Owners.OwnerName = '{OwnerName}'"
            };
            SQLiteDataReader reader = command.ExecuteReader();
            if (reader.HasRows)
            {
                while (reader.Read())
                {
                    ((MainWindow)Application.Current.MainWindow).listProjects.Items.Add(reader[0].ToString());
                }
            }
            return true;
        }

        //Insert project in database.
        static public bool InsertProject(string projectName, string ownerProject)
        {
            string sqlFormattedDate = DateTime.Today.ToString("dd.MM.yyyy");
            command = new SQLiteCommand(connection)
            {
                CommandText = $"INSERT INTO Projects(ProjectName, ProjectOwner, ProjectDate) VALUES('{projectName}', " + 
                $"(SELECT Owners.OwnerID FROM Owners INNER JOIN Projects ON Projects.ProjectOwner = Owners.OwnerID WHERE Owners.OwnerName = '{ownerProject}'), '{sqlFormattedDate}')"
            };
            if (command.ExecuteNonQuery() == 1)
            {
                Debug.WriteLine("Success!");
            }
            else
            {
                Debug.WriteLine("Not Added!");
            }
            return true;
        }

        //Select priority.
        static public string[] SelectPriority()
        {
            List<string> list = new();
            command = new SQLiteCommand(connection)
            {
                CommandText = "SELECT PriorityName FROM Priorities"
            };
            SQLiteDataReader reader = command.ExecuteReader();
            if (reader.HasRows)
            {
                while(reader.Read())
                {
                    list.Add(reader.GetString(0));           
                }                
            }
            return list.ToArray();
        }

        //Insert task in database.
        static public bool InsertTask(string taskName, string projectID, string taskPriority, DateTime? taskStart, DateTime? taskEnd)
        {
            command = new SQLiteCommand(connection)
            {
                CommandText = $"INSERT INTO Tasks(TaskName, ProjectID, TaskPriority, TaskStart, TaskEnd, TaskProgress) VALUES('{taskName}', '{projectID}', '{taskPriority}'," +
                $"'{taskStart}', '{taskEnd}', 1)"
            };
            if (command.ExecuteNonQuery() == 1)
            {
                Debug.WriteLine("Success!");
            }
            else
            {
                Debug.WriteLine("Not Added!");
            }
            return true;
        }

        //Select task for DataGrid.
        static public void SelectTask()
        {
            command = new SQLiteCommand(connection)
            {
                //CommandText = $"SELECT TaskID, TaskName, TaskPriority FROM Tasks INNER JOIN Projects ON Projects.ProjectID = Tasks.ProjectID WHERE Projects.ProjectName = '{projectName}'"
                CommandText = "SELECT TaskID, TaskName FROM Tasks"

            };
            //SQLiteDataReader reader = command.ExecuteReader();
            DataSet _Bind = new DataSet();
            SQLiteDataAdapter da = new SQLiteDataAdapter(command);
            da.Fill(_Bind, "MyDataBinding");
            ((MainWindow)Application.Current.MainWindow).dataGrid.DataContext = _Bind;
        }
    }
}
